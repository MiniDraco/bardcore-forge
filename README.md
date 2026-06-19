# 🔨🔥 The Bardcore Forge

**From the first spark to a finished track.** A small, self-contained set of guides that teach writing lyrics & poetry and turning them into songs with [Suno](https://suno.com) — no music theory required. The AI makes the music; you bring the words and the shape.

Everything is **plain HTML, offline-safe, no dependencies** — open a file in any browser.

## 🚪 Start here
Open **`The Bardcore Forge (Start Here).html`** — it's the front door and routes you to the right guide.

| Guide | File | For |
|---|---|---|
| 🔥 **From Cold to Flame** | `From Cold to Flame.html` | The beginner course. Start from zero: find your material → build verses & choruses → hand it to Suno. |
| 📜 **The Bard's Codex** | `The Bard's Codex.html` | The full craft reference — music & poetry on illustrated panels (circle of fifths, modes, song structure, rhyme, form, genre recipes, the Emotional Console). |
| ⚒️ **Bardcore Engineering** | `Bardcore Engineering.html` | The Suno guide — keys/modes/tempo/meter/meta-tags + a practical Operator's Manual (the field law, what actually works vs placebo, vocal stacking, phonetic respelling). |

The three are cross-linked; every page has a door to every other page.

## 🧪 Quality
The HTML is checked by a small static analyzer, [`forge_qa.py`](forge_qa.py) — 17 test categories (link/anchor integrity, tag balance, offline-safety, accessibility, contrast, usability, and more). Run it from this folder:

```
python forge_qa.py
```

Test history and findings live in [`FORGE_QA_LOG.md`](FORGE_QA_LOG.md).

## A note on the Suno tips
The Suno-specific tags/tricks (in `Bardcore Engineering.html` and the attached `suno tags list.md` / `suno-maximalist-tricks.md`) are **community-sourced** and tied to a fast-changing platform. Treat them as **"try, don't depend"** — verify against the live app.

## License
MIT — see [LICENSE](LICENSE). Use it, remix it, share it. If it helps someone turn what they feel into a song, that's the whole point. 🔥
