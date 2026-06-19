#!/usr/bin/env python3
"""Bardcore Forge QA harness — static analysis of the Forge HTML files.
Grows each QA round. Run:  python forge_qa.py
Exit code = number of FAILs (0 = all green)."""
import os, sys, re
from html.parser import HTMLParser
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = [
    "The Bardcore Forge (Start Here).html",
    "Bardcore Engineering.html",
    "The Bard's Codex.html",
    "From Cold to Flame.html",
]

class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []                # list (to catch duplicates)
        self.links = []              # <a href>
        self.srcs = []               # any src
        self.ext = []                # external resources (offline-breakers)
        self.svgs = []               # bool: has aria-label/role
        self.headings = []           # (level, text)
        self.has_title = False; self.in_title = False; self.title = ""
        self.html_lang = None; self.has_viewport = False; self.has_charset = False
        self.tags = {}
        self._cur_h = None
        self.text_len = 0
        self.SAFE = {"div", "section", "footer", "header", "table", "thead", "tbody",
                     "pre", "svg", "style", "ul", "ol", "html", "head", "body", "title"}
        self.stack = []
        self.balance_issues = []
        self.in_style = False; self.in_script = False
        self.vtext = ""
        self.section_ids = []

    def handle_starttag(self, tag, attrs):
        self.vtext += " | "   # tag boundary → prevents phantom cross-element doubled words
        d = dict(attrs)
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if "id" in d: self.ids.append(d["id"])
        if tag == "section" and "id" in d: self.section_ids.append(d["id"])
        if tag == "a" and "href" in d: self.links.append(d["href"])
        if "src" in d:
            self.srcs.append(d["src"])
            if d["src"].startswith(("http://", "https://", "//")):
                self.ext.append((tag, d["src"]))
        if tag == "link" and d.get("rel") == "stylesheet" and d.get("href", "").startswith(("http", "//")):
            self.ext.append((tag, d["href"]))
        if tag == "script" and d.get("src", "").startswith(("http", "//")):
            self.ext.append((tag, d["src"]))
        if tag == "title": self.in_title = True; self.has_title = True
        if tag == "html": self.html_lang = d.get("lang")
        if tag == "meta":
            if d.get("name") == "viewport": self.has_viewport = True
            if "charset" in d: self.has_charset = True
        if tag == "svg": self.svgs.append(("aria-label" in d) or ("role" in d))
        if tag in ("h1", "h2", "h3"):
            self._cur_h = (int(tag[1]), "")
        if tag in self.SAFE:
            self.stack.append(tag)
        if tag == "style": self.in_style = True
        if tag == "script": self.in_script = True

    def handle_endtag(self, tag):
        self.vtext += " | "
        if tag == "title": self.in_title = False
        if tag == "style": self.in_style = False
        if tag == "script": self.in_script = False
        if tag in ("h1", "h2", "h3") and self._cur_h:
            self.headings.append(self._cur_h); self._cur_h = None
        if tag in self.SAFE:
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            elif tag in self.stack:
                self.balance_issues.append(f"interleaved </{tag}>")
                while self.stack and self.stack.pop() != tag:
                    pass
            else:
                self.balance_issues.append(f"stray </{tag}>")

    def handle_data(self, data):
        if self.in_title: self.title += data
        if self._cur_h: self._cur_h = (self._cur_h[0], self._cur_h[1] + data)
        self.text_len += len(data.strip())
        if not self.in_style and not self.in_script:
            self.vtext += " " + data


def parse(path):
    s = Scan()
    with open(path, encoding="utf-8") as f:
        s.raw = f.read()
    s.feed(s.raw)
    return s


def split_href(href):
    if "#" in href:
        a, b = href.split("#", 1); return a, b
    return href, None


def run():
    R = []  # (level, file, msg)
    def add(level, file, msg): R.append((level, file, msg))

    scans = {}
    for fn in FILES:
        p = os.path.join(HERE, fn)
        if not os.path.exists(p):
            add("FAIL", fn, "FILE MISSING"); continue
        try:
            scans[fn] = parse(p)
        except Exception as e:
            add("FAIL", fn, f"parse error: {e}")

    # ---- CATEGORY: smoke (R1) ----
    for fn, s in scans.items():
        add("PASS" if s.has_title else "FAIL", fn, f"smoke: <title> present ('{s.title.strip()[:36]}')")
        add("PASS" if s.has_charset else "WARN", fn, "smoke: charset meta")
        add("PASS" if s.has_viewport else "WARN", fn, "smoke: viewport meta")
        add("PASS" if s.html_lang else "WARN", fn, f"smoke: <html lang> = {s.html_lang}")
        add("PASS" if s.text_len > 1500 else "FAIL", fn, f"smoke: has substantial content ({s.text_len} chars)")

    # ---- CATEGORY: duplicate ids (R1) ----
    for fn, s in scans.items():
        seen, dups = set(), set()
        for i in s.ids:
            if i in seen: dups.add(i)
            seen.add(i)
        add("PASS" if not dups else "FAIL", fn, f"dup-ids: {'none' if not dups else sorted(dups)}")

    # ---- CATEGORY: link & anchor integrity (R1) ----
    for fn, s in scans.items():
        for href in s.links:
            if href.startswith(("http://", "https://", "mailto:")):  # external hyperlink, fine
                continue
            if href.strip() in ("", "#"):
                add("WARN", fn, f"empty/# href"); continue
            filepart, frag = split_href(href)
            if filepart == "":  # same-page anchor
                ok = frag in s.ids
                add("PASS" if ok else "FAIL", fn, f"anchor #{frag}: {'ok' if ok else 'TARGET MISSING'}")
            else:
                target = unquote(filepart)
                exists = os.path.exists(os.path.join(HERE, target))
                add("PASS" if exists else "FAIL", fn, f"link->{target}: {'ok' if exists else 'FILE MISSING'}")
                if exists and frag and target in scans:
                    ok = frag in scans[target].ids
                    add("PASS" if ok else "FAIL", fn, f"xanchor {target}#{frag}: {'ok' if ok else 'MISSING'}")

    # ---- CATEGORY: offline / external-resource audit (R1) ----
    for fn, s in scans.items():
        if s.ext:
            for t, u in s.ext: add("FAIL", fn, f"offline: external <{t}> {u[:48]} breaks offline use")
        else:
            add("PASS", fn, "offline: no external resources")

    # ---- CATEGORY: images resolve (R1) ----
    for fn, s in scans.items():
        bad = [src for src in s.srcs if not src.startswith(("http", "data:", "//"))
               and not os.path.exists(os.path.join(HERE, unquote(src)))]
        add("PASS" if not bad else "FAIL", fn, f"images: {'all resolve / none' if not bad else bad}")

    # ---- CATEGORY: family cross-link integrity (R1) ----
    # every room should have a door to every other room (no islands)
    family = set(FILES)
    for fn, s in scans.items():
        linked = set()
        for href in s.links:
            fp, _ = split_href(href)
            t = unquote(fp)
            if t in family and t != fn:
                linked.add(t)
        missing = (family - {fn}) - linked
        add("PASS" if not missing else "FAIL", fn,
            f"family-links: {'all siblings linked' if not missing else 'NO LINK to '+str(sorted(missing))}")

    # ---- CATEGORY: tag balance / unclosed blocks (R2) ----
    for fn, s in scans.items():
        problems = list(s.balance_issues)
        if s.stack:
            problems.append(f"unclosed at EOF: {s.stack}")
        add("PASS" if not problems else "FAIL", fn, f"tag-balance: {'ok' if not problems else problems}")

    # ---- CATEGORY: responsive wide-table scroll (R3) ----
    for fn, s in scans.items():
        raw = getattr(s, "raw", "")
        if 'class="card full"' in raw:  # has a full-width (wide) table card
            ok = "overflow-x" in raw
            add("PASS" if ok else "FAIL", fn,
                f"responsive: wide-table card has overflow-x scroll {'ok' if ok else 'MISSING'}")

    # ---- CATEGORY: SVG accessibility (R4) ----
    for fn, s in scans.items():
        if s.svgs:
            add("PASS" if all(s.svgs) else "FAIL", fn,
                f"a11y: SVGs have aria-label/role ({sum(s.svgs)}/{len(s.svgs)})")

    # ---- CATEGORY: heading structure (R4) ----
    for fn, s in scans.items():
        h1s = [h for h in s.headings if h[0] == 1]
        add("PASS" if len(h1s) == 1 else "FAIL", fn, f"a11y: exactly one <h1> (found {len(h1s)})")
        jumps, prev = [], 0
        for lvl, _ in s.headings:
            if prev and lvl > prev + 1:
                jumps.append(f"h{prev}->h{lvl}")
            prev = lvl
        add("PASS" if not jumps else "WARN", fn, f"a11y: heading order {'ok' if not jumps else 'skips '+str(jumps)}")

    # ---- CATEGORY: print styles present (R4) ----
    for fn, s in scans.items():
        raw = getattr(s, "raw", "")
        if "window.print" in raw or "printbtn" in raw:
            ok = "@media print" in raw
            add("PASS" if ok else "WARN", fn, f"print: @media print rules {'ok' if ok else 'MISSING'}")

    # ---- CATEGORY: no leftover placeholders (R4) ----
    markers = ["lorem ipsum", "todo:", "fixme", "placeholder text", "xxxxx"]
    for fn, s in scans.items():
        raw = getattr(s, "raw", "").lower()
        hits = [m for m in markers if m in raw]
        add("PASS" if not hits else "FAIL", fn, f"content: no leftover placeholders {'ok' if not hits else hits}")

    # ---- CATEGORY: doubled-word typo scan (R5) ----
    legit = {"that", "had", "is", "no", "very", "so", "ha", "na", "la", "oh", "uh", "go", "blah", "twenty"}
    for fn, s in scans.items():
        txt = re.sub(r"\s+", " ", getattr(s, "vtext", ""))
        dubs = [d for d in re.findall(r"\b([A-Za-z]{2,})\s+\1\b", txt, flags=re.I)
                if d.lower() not in legit]
        uniq = sorted(set(d.lower() for d in dubs))
        add("PASS" if not uniq else "WARN", fn, f"content: doubled words {'none' if not uniq else uniq[:10]}")

    # ---- CATEGORY: back-to-top affordance (R6, usability) ----
    for fn, s in scans.items():
        raw = getattr(s, "raw", "")
        if 'class="printbtn"' in raw:  # a long, scrollable content doc
            ok = "topbtn" in raw or "scrollTo" in raw
            add("PASS" if ok else "FAIL", fn, f"usability: back-to-top control {'present' if ok else 'MISSING on long page'}")

    # ---- CATEGORY: minimum font floor (R6, usability) ----
    for fn, s in scans.items():
        raw = getattr(s, "raw", "")
        sizes = [float(m) for m in re.findall(r"font-size:\s*([0-9.]+)px", raw)]
        tiny = sorted(set(x for x in sizes if x < 9))
        floor = min(sizes) if sizes else None
        add("PASS" if not tiny else "WARN", fn,
            f"usability: no sub-9px text {'ok (min '+str(floor)+'px)' if not tiny else 'TINY '+str(tiny)}")

    # ---- CATEGORY: nav coverage (R6, usability) ----
    for fn, s in scans.items():
        anchors = {h[1:] for h in s.links if h.startswith("#") and len(h) > 1}
        uncovered = [sid for sid in s.section_ids if sid not in anchors]
        add("PASS" if not uncovered else "WARN", fn,
            f"usability: every <section> reachable from nav {'ok' if not uncovered else 'UNCOVERED '+str(uncovered)}")

    return R


if __name__ == "__main__":
    R = run()
    fails = [r for r in R if r[0] == "FAIL"]
    warns = [r for r in R if r[0] == "WARN"]
    passes = [r for r in R if r[0] == "PASS"]
    cur = None
    for level, fn, msg in R:
        if fn != cur:
            print(f"\n=== {fn} ==="); cur = fn
        mark = {"PASS": "  ok ", "WARN": " warn", "FAIL": "FAIL!"}[level]
        if level != "PASS":
            print(f"  [{mark}] {msg}")
    print("\n" + "=" * 48)
    print(f"SUMMARY: {len(passes)} pass · {len(warns)} warn · {len(fails)} FAIL")
    if fails:
        print("\nFAILURES:")
        for _, fn, msg in fails: print(f"  - [{fn}] {msg}")
    sys.exit(len(fails))
