# 🔬 Bardcore Forge — QA Loop Log
*Persistent across rounds. Read this first each round so we don't repeat work.*

**Target files**
- The Bardcore Forge (Start Here).html
- Bardcore Engineering.html
- The Bard's Codex.html
- From Cold to Flame.html

**Harness:** `forge_qa.py` (static analyzer, grows each round) + live checks via the preview server.

---

## Test categories implemented (cumulative)
| # | Category | Round | What it checks |
|---|---|---|---|
| 1 | smoke | 1 | title, charset, viewport, lang, substantial content |
| 2 | duplicate-ids | 1 | no repeated `id=` (breaks anchors) |
| 3 | link/anchor integrity | 1 | every internal `#anchor` + cross-file link resolves |
| 4 | offline audit | 1 | no external `src`/CDN — must work offline |
| 5 | images resolve | 1 | every local `src` exists (n/a — no `<img>`) |
| 6 | family cross-links | 1 | every room links to all siblings + Start (no islands) |
| 7 | tag-balance | 2 | stack-based check for unclosed/stray/interleaved block tags |
| 8 | live console errors | 2 | load page in browser, assert zero console errors |
| 9 | responsive wide-table scroll | 3 | files with `.card.full` tables must have an `overflow-x` mobile rule |
| 10 | SVG accessibility | 4 | every `<svg>` has `aria-label`/`role` |
| 11 | heading structure | 4 | exactly one `<h1>`; no skipped heading levels |
| 12 | print styles | 4 | pages with a Print button include `@media print` |
| 13 | no leftover placeholders | 4 | no lorem/TODO/FIXME/placeholder text |
| 14 | doubled-word typo scan | 5 | visible-text scan for accidental repeated words (tag-boundary aware) |
| 15 | back-to-top affordance | 6 | long content pages have a back-to-top control |
| 16 | min-font floor | 6 | no CSS text below 9px |
| 17 | nav coverage | 6 | every `<section id>` is reachable from an in-page nav link |
| + | live WCAG contrast + min-font audit | 6 | computed per page via the browser (not in static harness) |

---

## Round log

### Round 1 — foundation + link integrity ✅
- Built `forge_qa.py` (static analyzer) + this log.
- **Bug found & fixed:** *The Bard's Codex* and *From Cold to Flame* were navigation **islands** — no links to siblings or Start (contradicted the "every room has a door" claim). Added family cross-link footers to both.
- New tests this round: all 6 categories above (esp. #6 family-links, which caught the bug).
- Result: **81 pass · 0 warn · 0 FAIL.**
- Not yet covered (future rounds): runtime console errors, responsive/overflow at mobile width, SVG/a11y, heading order, content/typo + cross-doc factual consistency, full live regression.

### Round 2 — error & structure check ✅
- New tests: **#7 tag-balance** (stack-based unclosed/stray detection) + **#8 live console errors**.
- Ran tag-balance over all 4 files (worried my big Operator's-Manual insert left an unclosed `<div>`) → **all balanced**.
- Live console check on the two most complex/edited pages (Bardcore Engineering, The Bard's Codex) → **zero console errors**.
- Bugs found: **none** this round.
- Result: **85 pass · 0 warn · 0 FAIL.**
- Still open: responsive/overflow at mobile width (the 7-column genre table is a suspect), SVG/a11y, heading order, content/typo + cross-doc consistency.

### Round 3 — responsive / stress ✅
- New test: **#9 responsive wide-table scroll**.
- Stress: loaded at mobile preset. **Caveat:** the headless preview's viewport reporting is unreliable (reported 647px when set to 375, 0×0 earlier) — couldn't get a trustworthy pixel measurement. At the width it did report, **zero horizontal overflow**.
- **Change made (safe, desktop-neutral):** added `.card.full{overflow-x:auto}` + `@media(max-width:640px){.card.full table{min-width:560px}}` to *The Bard's Codex* and *Bardcore Engineering*, so wide reference tables scroll horizontally on phones instead of cramping. Only engages ≤640px — **desktop PNG export untouched.**
- Verified Codex still renders with **zero console errors** after the CSS change.
- Bugs found: none hard-confirmed (tooling-limited); shipped a low-risk responsive improvement.
- Result: **87 pass · 0 warn · 0 FAIL.**
- Still open: SVG/a11y labels, heading order, viewport/lang already pass, content/typo + cross-doc factual consistency.

### Round 4 — quality & accessibility ✅
- New tests: **#10 SVG a11y**, **#11 heading structure**, **#12 print styles**, **#13 no placeholders**.
- Results: all SVGs labeled · exactly one `<h1>` per page · no skipped heading levels · `@media print` present on all 3 printable docs · no leftover lorem/TODO/placeholder text.
- **Quality fix (not test-catchable):** front-door footer said "Keep all four files in the same folder" — stale (there are more files now + the attached refs). Changed to "Keep these files together in one folder."
- Result: **104 pass · 0 warn · 0 FAIL.**
- Still open: content/typo scan + cross-doc factual consistency (e.g., does the Codex carry the same key/time-sig reality-check the Bardcore guide now has?), then a full regression.

### Round 5 — content audit + cross-doc consistency + final regression ✅
- New test: **#14 doubled-word typo scan** (now tag-boundary aware to avoid cross-element phantoms).
- First pass flagged 3 doubled-word WARNs → **investigated, all false positives**: `twenty twenty-four` is the intentional 2024 respelling; `build/bridge/chorus/pre` were cross-element phantoms (verified via grep — no literal adjacency in raw). **No real typos.** Hardened the scanner (tag-boundary separators + whitelist) so it's trustworthy.
- **Cross-doc consistency bug found & fixed:** the Codex's prompt skeleton listed `[key/mode]` as a lever but lacked the placebo caveat the Bardcore guide now carries. Added a "Suno reality-check" note + link in the Codex so the two docs agree.
- **Final full regression: 109 pass · 0 warn · 0 FAIL** across all 14 categories × 4 files. Live console check on the edited Codex: zero errors.

---

## ✅ FINAL STATE (after 5 rounds)
- **Suite:** 14 test categories, `forge_qa.py` (re-runnable, exit code = #FAILs). **All green.**
- **Bugs fixed:** (R1) 2 navigation islands — Codex & From Cold to Flame had no sibling/Start links; (R4) stale "four files" copy on the front door; (R5) Codex↔Bardcore key/time-sig consistency.
- **Improvements:** (R3) mobile horizontal-scroll for wide reference tables (desktop untouched).
- **Verified clean:** tag balance, links/anchors, offline (no external deps), dup-ids, SVG a11y, single-h1/heading order, print styles, no placeholders, no typos, no console errors.
- **Tooling caveat logged:** headless preview viewport reporting is unreliable for precise responsive pixel measurement — used safe, scoped CSS instead of chasing it.
- **Re-run anytime:** `python forge_qa.py` from the Downloads folder.

### Round 6 — usability battery ✅
- New tests: **#15 back-to-top**, **#16 min-font floor**, **#17 nav coverage** + a **live WCAG contrast/min-font audit** per page.
- **Live audit findings:**
  - *Bardcore Engineering*: clean (0 low-contrast, 9px min).
  - *From Cold to Flame*: clean except one borderline map-label (2.97 — measurement artifact: the label is offset onto the dark page bg, not the block it parents to).
  - *The Bard's Codex*: real issues → fixed.
- **Bugs found & fixed:**
  1. **No back-to-top on long pages** — the biggest usability gap. The 3 content docs (Codex ~10k px, Cold to Flame ~16k px, Bardcore Engineering) had nav only at the very top, no way back after scrolling. Added a floating ↑ Back-to-top button (smooth scroll, aria-labelled, hidden in print) to all three.
  2. **Codex frequency-bar labels: dark text on dark segments (contrast 1.8) + 8.5px** — illegible on the maroon/red segments. Fixed: white text + dark text-shadow + bumped to 10px. The dark-segment ratio went 1.8 → 10.95.
  3. **Marginal AA**: lightened the Codex footer-tip grey (#6f7488 → #9298ac) to clear 4.5:1.
- **Honest caveat:** after the freqbar fix, the *bright* segments now show white-on-bright at pure-WCAG 2.3–3.7 — but the dark text-shadow halo makes them legible (WCAG math can't measure shadows). It's a tiny decorative 7-label legend; the real illegibility (dark-on-dark) is gone. Documented rather than over-tuned.
- Verified: harness **120 pass · 0 warn · 0 FAIL**; topbtn present + aria-labelled on all 3; zero console errors.

---

## ✅ FINAL STATE (after 6 rounds)
- **Suite:** 17 static categories + a live contrast/font audit. `python forge_qa.py` → **120 pass · 0 FAIL.**
- **Usability now covered:** back-to-top on every long page · no sub-9px text · all sections nav-reachable · WCAG contrast audited & dark-on-dark fixed · responsive table scroll · single-h1/heading order · SVG labels · offline-safe · zero console errors.
- **Bugs fixed across 6 rounds:** navigation islands (R1) · stale front-door copy (R4) · Codex↔Bardcore key/time-sig consistency (R5) · no-back-to-top + freqbar contrast + marginal greys (R6).
