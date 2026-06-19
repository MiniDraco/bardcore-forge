# The Maximalist Suno Trick Bible — Expanded Edition
*Non-standard tips, hacks, exploits, word-bypasses, genre blueprints, and troubleshooting. Current to the v5 / v5.5 era (mid-2026).*

> **Read this first.** Suno changes constantly and a large fraction of "community lore" is half-true, version-specific, or placebo. Items tagged **⚠️** are folklore / inconsistent — *try them, don't depend on them.* Everything works better when you treat each generation as a **probability nudge, not a command.** Suno doesn't parse language; it pattern-matches sound from spelling and tags. When a trick "stops working," it's almost always because the model rev changed, not because you did it wrong. Keep your own log of what lands for *your* genre.

---

## TABLE OF CONTENTS
1. The mental model
2. The two-field system & field-bleed exploits
3. The 5-part style-prompt formula
4. Field limits & character budgets
5. Generation modes, sliders & "Max"
6. The complete tag taxonomy (genre / mood / energy / texture / vocal / instrument)
7. Structure & meta-tags (exhaustive) + tag placement theory
8. BPM & tempo map
9. Emotionally-aware "TTS": making vocals act
10. The vocal triple-stack (character + delivery + effects)
11. Accent, dialect & multilingual control
12. The Word-Bypass Dictionary (force exact pronunciation)
13. Performance formatting (the typography layer)
14. Sound design, SFX, adlibs & ambience
15. Structure & arrangement power-moves
16. "Sound like any artist" — the deconstruction method
17. Consistency: Personas, Voices, Custom Models, My Taste
18. Editing existing tracks: Covers, Remix, Remaster, Extend, Replace
19. Studio, stems & DAW workflow
20. Negative prompting & exclusion
21. Instrumentals & no-vocal tracks
22. Song length & arrangement length control
23. Album / project / multi-track consistency
24. Credit-saving & iteration discipline
25. Genre Blueprint Library (copy-paste formulas)
26. Genre-blending recipes
27. Deliberately weird / experimental
28. Troubleshooting matrix (symptom → fix)
29. Myths, gotchas & things that don't work
30. Commercial / copyright notes
31. Master cheat strip
32. Glossary

---

## 1. The mental model that makes everything else work

- **Suno sings by spelling, not meaning.** No dictionary, no IPA, no grammar parser. It predicts "what do words/tags that look like this usually sound like." Every trick here exploits that.
- **Two brains, two boxes.** The **Style / Description** field controls *sound* (genre, instruments, production, voice character, tempo). The **Lyrics** field controls *words + performance directions*. They bleed into each other, and abusing that bleed is where most hacks live.
- **Brackets `[ ]` = stage directions** (read as instructions, not sung). **Parentheses `( )` = usually sung** (backing vocals, echoes, adlibs).
- **It's a weighted slot machine.** You shift odds, you don't force outcomes. Re-roll cheaply, lock what works, refine late.
- **Tag order is weight order.** The *first* genre/tag carries the most pull. Front-load what matters.
- **Local vs global signal.** A tag at the very top of the lyrics is a *broad* instruction for the whole song. The same tag right before a chorus/drop/bridge is a *local* instruction for that moment.
- **Mood must match across fields.** Aggressive style + gentle love lyrics = unpredictable mush. Align the emotional tone of Style and Lyrics or create contrast *deliberately* with structure.
- **Pronunciation/timing freezes at generation.** You can't fix a mispronounced word after the fact — only regenerate or section-replace. Front-load every phonetic fix.

---

## 2. The two-field system & field-bleed exploits

- **Prompt-in-the-lyrics-box ⚠️.** Put a *style description* (not lyrics) into the Lyrics field and, in an edit/extend/custom flow, instruct it to treat it as a brief — e.g. a leading bracket `[interpret as style: dark synthwave, 90 BPM, breathy female vocal]`. On some versions this leaks into the conditioning and biases the sound. Inconsistent — test, don't trust.
- **Style-box overflow → lyrics brackets.** When the Style field is full or keeps ignoring a descriptor, sneak it into the lyrics as a leading bracket tag. Vocal/performance cues often land *harder* from the lyrics field than the style field.
- **Double-declare stubborn traits.** If a sax solo, an accent, or a specific texture keeps getting dropped, state it in *both* boxes. Redundancy raises odds.
- **Genre in Style, production in Lyrics.** "indie folk" in Style; `[fingerpicked acoustic guitar, room reverb, vinyl crackle]` as an intro bracket. Splitting the load reduces tag-soup dilution.
- **Near-blank Style box** when you want words + delivery to dominate the arrangement (spoken-word, narrative, rap-forward). Load everything into bracketed lyric tags instead.
- **Mood handshake.** Put the *same* mood word in both fields ("melancholic" in Style, `[melancholic, restrained]` atop the first verse) to lock emotional tone.

---

## 3. The 5-part style-prompt formula

A strong Style prompt is a comma-separated stack. You don't need all five every time, but specificity = consistency. Aim for **8–15 tags**; under 5 is too vague, over 20 dilutes.

1. **Genre & subgenre** (1–2 tags, dominant first). "rock" → "90s grunge, alternative rock." Subgenres beat broad labels.
2. **Mood & energy.** melancholic / euphoric / brooding / nostalgic / dreamy / aggressive / intimate / triumphant / haunting + an energy word (laid-back, building, explosive).
3. **Vocal direction** = character + delivery + effects (see §10).
4. **Instrumentation** — name 2–4 instruments *with character*: "Rhodes electric piano," not "keyboard"; "808 sub-bass," not "bass."
5. **Production & tempo** — mix aesthetic + BPM: "lo-fi tape warmth, 95 BPM" / "polished radio-ready mix, 118 BPM."

**Worked example:**
```
synth-pop, 80s-inspired, euphoric and nostalgic, powerful female vocals with layered
harmonies, analog synth pads, punchy drum machine, shimmering arpeggios, Moog bass,
polished radio-ready production, 118 BPM
```

---

## 4. Field limits & character budgets

- **Style field:** ~200 characters on older versions, ~**1,000 characters on v5.5.** Spend it on specifics, not filler adjectives.
- **Lyrics field:** ~**3,000 characters** (varies). Long lyric walls make Suno rush delivery — keep sections tight.
- **Tag economy:** every weak tag steals weight from a strong one. 5 precise tags beat 15 vague ones.
- **Section length controls vocal density:** verses 4–8 lines, choruses 2–4 lines. More lines per section = faster, more crammed delivery.

---

## 5. Generation modes, sliders & "Max"

- **Max Mode / highest-quality toggle ⚠️.** Newer UIs expose a "max" or top-fidelity option (exact name shifts by tier/version — confirm in *your* UI). Generally = longer context, fuller arrangement, cleaner high end, more credits. Use for final renders, not idea-hunting.
- **Creative Sliders are weighted bias, not on/off:**
  - **Weirdness / Strangeness:** low = safe, on-genre. Above ~60 it reaches for microtonal scales, odd percussion, unconventional transitions. Great for IDM/experimental, risky for clean pop.
  - **Style Influence / Style Consistency:** how hard it clamps to your prompt. ~45–50 is the reported sweet spot for "creative but coherent." Crank for faithful genre repro; drop to be surprised.
  - **Audio Influence** (when seeding from an uploaded clip): how strongly the reference audio steers the result.
- **Simple vs Custom Mode.** Custom Mode exposes lyrics, structure tags, instrumental toggle, and full control. Live there.
- **Re-roll before you refine.** Cheap re-rolls of the *same* prompt explore the space; only tune tags once a roll is ~80% there.
- **Test clips.** Generate 20–30s to test a voice, accent, name, or hook before committing to a full render.

---

## 6. The complete tag taxonomy

Tags in the **Style field** go *without* brackets (comma-separated). Tags in the **Lyrics field** go *in* brackets, on their own line. Many work in both; placement changes whether it's a global sound cue or a local performance cue.

### Genre / subgenre (specific beats broad)
indie rock · garage rock · post-punk · shoegaze · 90s grunge · arena rock · math rock · synth-pop · new wave · synthwave · darkwave · hyperpop · bedroom pop · dream pop · deep house · tech house · minimal techno · acid · trance · drum and bass · jungle · breakbeat · dubstep · trap · drill · phonk · boom bap · 90s east coast hip-hop · jazz rap · cloud rap · neo-soul · alternative R&B · funk · disco · gospel · blues · delta blues · bossa nova · samba · reggaeton · dembow · afrobeat · amapiano · dancehall · cumbia · K-pop · city pop · ambient · drone · IDM · lo-fi hip-hop · cinematic orchestral · trailer score · folk · indie folk · bluegrass · country · outlaw country · metal · doom · black metal · djent · punk · hardcore · ska

### Mood
melancholic · euphoric · brooding · nostalgic · dreamy · aggressive · intimate · triumphant · haunting · romantic · mysterious · peaceful · dark · uplifting · playful · cinematic · menacing · bittersweet · hopeful · defeated · ecstatic · anxious · serene

### Energy / dynamics
laid-back · chill · mid-tempo · driving · high-energy · explosive · building intensity · slow burn · frantic · hypnotic · pulsing · anthemic · stripped-back · sparse · massive · wall-of-sound

### Texture / production
lo-fi tape hiss · vinyl crackle · warm analog · tape saturation · polished radio-ready mix · crisp digital clarity · reverb-drenched · dry and close-mic · stadium reverb · bedroom-recording feel · spacious and wide · compressed and loud · gritty · clean · cavernous · intimate close-mic · 48kHz hi-fi · underwater/filtered · bit-crushed

### Vocal character (who)
raspy female vocals · smooth baritone · young male tenor · deep female alto · airy soprano · gravelly · childlike · operatic · husky · nasal twang · androgynous

### Vocal delivery (how)
breathy · powerful belt · whispered · spoken word · melodic rap · conversational rap · drawl · falsetto · head voice · chest voice · aggressive growl · screamed · crooning · vibrato-heavy · staccato · legato · vocal runs · melisma

### Vocal effects (mix)
reverb-drenched · dry and punchy · doubled harmonies · layered harmonies · lo-fi filtered · auto-tuned · vocoder · telephone EQ · pitched-down · pitched-up chipmunk · heavily processed · close-mic intimate

### Instruments — by family
**Keys:** Rhodes electric piano · grand piano with sustain · honky-tonk upright · Wurlitzer · clavinet · harpsichord · organ · Hammond B3
**Strings (plucked/bowed):** clean jangly Telecaster · overdriven crunch guitar · nylon fingerpicking · 12-string acoustic · slide guitar · banjo · mandolin · upright bass · fingerstyle bass · fuzz bass · slap bass · lush string section · solo cello · pizzicato strings
**Drums/percussion:** 808 trap drums · punchy live kit · brushed jazz drums · programmed drum machine · gated-reverb 80s drums · four-on-the-floor kick · breakbeat · shakers · congas · timpani rolls · handclaps · finger snaps
**Wind/brass:** saxophone · muted trumpet · French horns · flugelhorn · flute · clarinet · harmonica · brass section
**Synths:** analog pad · Moog bass · arpeggiator lead · warm polysynth · supersaw · FM bells · sub-bass · acid 303 line
**Orchestral/cinematic:** full symphony orchestra · soaring strings · choir swell · epic percussion · sound-design risers

---

## 7. Structure & meta-tags (exhaustive) + placement theory

**Sectioning tags (lyrics field, own line each):**
`[Intro] [Verse] [Verse 1] [Pre-Chorus] [Chorus] [Post-Chorus] [Hook] [Refrain] [Bridge] [Breakdown] [Drop] [Build] [Buildup] [Interlude] [Instrumental] [Break] [Solo] [Outro] [End] [Fade Out]`

**Behavior notes:**
- **`[Chorus]`** gets the most melodic energy/emphasis automatically.
- **Numbered verses** (`[Verse 1]`, `[Verse 2]`) get *different* melodies; reuse `[Chorus]` to repeat the hook melody.
- **`[Pre-Chorus]`** builds tension; **`[Post-Chorus]`** extends energy after the hook (common in modern pop).
- **`[End]` / `[Fade Out]`** stops the dreaded long instrumental tail and extra repeats — this alone saves credits.
- **`[Instrumental]` / `[Break]`** = no vocals; use for breathing room and to slow vocal density.

**Modifier-loaded section tags** (hit rate varies, but nudges):
`[Chorus: huge, anthemic]` · `[Verse: half-time, sparse]` · `[Bridge: key change, builds]` · `[Final Chorus: full choir, louder]`

**Instrument-only sections:** `[Guitar Solo] [Piano Interlude] [Drum Break] [Sax Solo] [Bass Drop]`. For full instrumentals leave lyrics empty but *still* mark sections so it builds structure instead of noodling.

**Dynamics/arrangement events:** `[Quiet] [Soft] [Building] [Loud] [Explosive] [Climax] [Half-time] [Double-time] [Beat switch] [Tempo change] [Key change] [Modulate up a step] [Stripped back] [Full band enters] [Time signature change]`

**Placement theory (important):**
- **Top-of-lyrics tag = global signal.** Before your first line, set *one* mood + *one* energy direction + *1–3* key sound cues. Don't dump 12 tags there.
- **Tag directly before a section = local signal.** Put the hard turn ("[Beat switch]", "[half-time]") immediately before the bar it should affect.
- **One instruction per bracket.** Long bracket sentences get ignored or mangled. Keep tags 1–3 words.

---

## 8. BPM & tempo map (anchor every prompt)

| Genre | Range | Sweet spot |
|---|---|---|
| Lo-fi / chill | 60–85 | 72 |
| R&B / soul / neo-soul | 65–85 | 78 |
| Hip-hop | 80–100 | 88 |
| Reggaeton | 88–100 | 95 |
| Indie folk | 85–110 | 95 |
| Pop | 100–130 | 118 |
| Rock | 110–140 | 128 |
| House | 120–130 | 124 |
| Techno | 125–150 | 135 |
| Trap | 130–170 | 140 |
| Drum & bass | 160–180 | 174 |
| Punk | 150–200 | 170 |

A specific BPM anchors the groove and *prevents genre drift* (folk prompts stop sprouting trap hats). Always include one.

---

## 9. Emotionally-aware "TTS": making vocals act

The cluster that turns a flat read into a *performance*. The reliable move: **emotion tag + delivery tag + typography**, compounding.

**Emotion / affect tags (bracketed, before the line):**
`[whispered] [breathy] [intimate] [tender] [vulnerable] [pleading] [desperate] [angry] [seething] [shouting] [screaming] [crying] [sobbing] [trembling voice] [voice cracks] [laughing] [giggling] [sighing] [exhausted] [confident] [smug] [playful] [mocking] [deadpan] [reverent] [hopeful] [defeated]`

**Delivery / technique tags:**
`[spoken word] [spoken] [narration] [rap] [sung] [belted] [falsetto] [head voice] [chest voice] [vibrato] [staccato] [legato] [melisma] [vocal run] [ad-lib] [call and response] [harmonized] [in unison]`

**Choir / ensemble:**
`[choir] [gospel choir] [SATB choir] [backing vocals] [group vocals] [crowd chant] [duet] [trade-off verses] [male and female duet]`

**The "acting" stack — layer them:**
```
[verse]
[whispered, trembling]
I keep your number... I never call
[building, voice cracks]
And every NIGHT it gets a little harder
[belted, desperate]
to PRETEND that I'm fine at all
```

- **Tag sets intent; typography executes it.** Caps for the loud word, ellipses for the broken pause, stretched vowels for the ache.
- **Clearest enunciation** (best intelligibility): `[spoken word]` > `[staccato]` > `[operatic]` > `[crisp]`. Use when words *must* land.
- **Punctuation as emotion:** `...` → softer/sadder; `!` → harder; `—` → clipped break.
- **Duet engineering:** label speakers — `[Male:]` / `[Female:]` or `[Singer 1:]` / `[Singer 2:]` before lines — to force alternation and stop voice-blurring.

---

## 10. The vocal triple-stack (character + delivery + effects)

"Male vocals" gives Suno almost nothing. Always specify **all three layers**:
- **Character (who):** raspy female tenor / smooth baritone / airy soprano / gravelly old-man.
- **Delivery (how):** breathy / belted / whispered / conversational rap / drawl.
- **Effects (mix):** reverb-drenched / dry close-mic / doubled / auto-tuned / telephone EQ.

**Genre-matched default voices** (start here, then bend):
| Genre | Natural voice |
|---|---|
| Lo-fi | pitched-down sample, filtered, distant |
| Trap | melodic rap, auto-tuned, adlibs |
| Indie folk | soft, breathy, close-mic, intimate |
| Metal | aggressive growl, screamed, powerful |
| R&B | smooth, silky, runs, falsetto |
| Pop | clear, bright, belted chorus |
| Country | drawl, twang, storytelling delivery |

**Inline dynamics:** drop `(whispered, intimate)` over a verse and `(belted, powerful)` over the chorus for section-specific control.

---

## 11. Accent, dialect & multilingual control

- **Language is inferred from the lyrics.** Write the verse in the target language and Suno sings it in that language. Optionally reinforce in Style: "Japanese city pop, female vocals."
- **Best-supported languages:** English, Spanish, Portuguese, French, Japanese, Korean, Mandarin. Lesser-represented languages come out accented or imprecise — phonetic-respell heavily and test small.
- **Accent steering ⚠️:** describe the accent in Style ("sharp NYC accent," "southern drawl," "London grime accent," "Jamaican patois inflection"). Inconsistent but moves the needle; reinforce with respelled lyrics (e.g. drop g's: `runnin'`, `dancin'`).
- **Code-switching sections ⚠️:** label by language `[Verse: Spanish]` / `[Chorus: English]`. Works sometimes, fails often — test before committing.
- **Dialect via spelling:** spell the way the accent sounds (`gonna`→`gunna`, `about`→`aboot` for exaggerated Canadian, `nothing`→`nuttin'`). The respelling *is* the accent control.

---

## 12. The Word-Bypass Dictionary (force exact pronunciation)

Respell words the way they should **sound**. This is the copy-paste "goodie."

### 12a. Homographs (same spelling, two sounds — pick one)
| You want | Write it |
|---|---|
| read (past, "red") | `red` |
| read (present, "reed") | `reed` |
| live (concert, "laɪv") | `laiv` |
| live (alive, "lɪv") | `liv` |
| lead (metal/past, "led") | `led` |
| lead (guide, "leed") | `leed` |
| bass (instrument) | `bayss` |
| bass (fish) | `bass` |
| tear (crying) | `teer` |
| tear (ripping) | `tare` |
| wind (breeze) | `wind` |
| wind (to coil) | `wynd` |
| minute (60 sec) | `min-it` |
| minute (tiny) | `my-newt` |
| record (verb) | `ri-kord` |
| record (noun) | `REH-kord` |
| present (give) | `pre-zent` |
| present (gift) | `PREH-zent` |
| close (shut) | `kloz` |
| close (near) | `klohss` |
| bow (bend) / bow (ribbon) | `bau` / `boh` |
| dove (bird) / dove (dived) | `duv` / `dohv` |
| object (verb/noun) | `ub-JEKT` / `OB-jekt` |
| desert (abandon) / dessert | `dih-ZERT` / `dih-ZERT` (double-s sweet) |
| produce (verb) / produce (veg) | `pro-DEWS` / `PRO-dewss` |
| content (happy) / content (stuff) | `kun-TENT` / `KON-tent` |

### 12b. Silent letters & irregular spelling
| Word | Fix |
|---|---|
| through | `thru` |
| though | `tho` |
| throughout | `thru-out` |
| enough | `enuff` |
| rough | `ruff` |
| tough | `tuff` |
| cough | `koff` |
| knight | `nite` |
| know | `no` |
| write | `rite` |
| colonel | `kernel` |
| queue | `kew` |
| February | `Feb-roo-airy` |
| Wednesday | `Wenz-day` |
| genre | `zhon-ruh` |
| debris | `deh-bree` |
| fiancé | `fee-on-say` |
| rendezvous | `ron-day-voo` |
| epitome | `eh-pit-oh-mee` |
| hyperbole | `hy-per-boh-lee` |

### 12c. Common lyric words that mangle
| Word | Fix |
|---|---|
| tonight | `to-night` |
| gonna | `gunna` |
| wanna | `wonna` |
| your | `yore` |
| because | `becuz` |
| something | `some-thing` |
| everything | `ev-ree-thing` |
| forever | `for-ever` |
| inside | `in-side` |
| somewhere | `some-where` |
| remix | `re-mix` |
| amen | `a-men` |

### 12d. Acronyms & abbreviations (force letters vs word)
| Written | Fix |
|---|---|
| AI | `A-I` (or `A I`) |
| DJ | `dee-jay` |
| USA | `U-S-A` |
| NYC | `N-Y-C` |
| LA | `L-A` |
| R&B | `R and B` |
| ASAP | `A-S-A-P` |
| OK | `oh-kay` |
| FYI | `F-Y-I` |
| vs | `versus` |
| Jr | `junior` |
| Mr / Mrs | `Mister` / `Missus` |

### 12e. Numbers & dates — **never type raw digits**
| Written | Fix |
|---|---|
| 24/7 | `twenty four seven` |
| 2024 | `twenty twenty-four` |
| 100 | `a hundred` |
| 1000 | `a thousand` |
| 1st / 2nd / 3rd | `first` / `second` / `third` |
| $500 | `five hundred dollars` |
| 3am | `three A-M` |
| 4ever | `forever` |

### 12f. Names (highest failure rate — test in a 30s clip first, be consistent)
| Name | Fix |
|---|---|
| Siobhan | `Shi-vawn` |
| Aoife | `Ee-fa` |
| Evie | `Ee-vee` |
| Worcestershire | `Wuster-shur` |
| Leicester | `Lester` |
| Yosemite | `Yo-sem-ih-tee` |
| Selah | `Seh-lah` |
| Versace | `Ver-sah-chee` |
| Hermès | `Air-mez` |

### 12g. Syllable-binding (your `ra-ta-ra-ta` trick, generalized)
Goal: deliver something as **one fluid word/run** while still pronouncing each chunk.
- **Hyphenate to bind:** `ra-ta-ra-ta` reads as one connected utterance with each beat enunciated, not four stop-start words. Same logic: `su-per-ca-li`, `ba-da-ba-da-bing`, `ree-ah-ree-ah`.
- **Hyphenate to *split*** a too-fast word so syllables land on their own beats: `Co-llec-tions`, `un-be-liev-able`, `cat-a-stroph-ic`.
- **Glue a chant tighter:** `we-will-we-will` locks rhythm harder than `we will we will`.
- **Scat / vocalise** (keep OUT of brackets so it's sung): `doo-wop-a-doo`, `na-na-na-na`, `la-dee-da`, `sha-la-la`.
- **Invent a language:** chain phonetic syllables (`vel-na-thor-ah`, `kai-ro-men-du`) and pair with `[chant]` or `[fictional language]` ⚠️ for ritual/fantasy vibes.

---

## 13. Performance formatting (the typography layer)

| Technique | Write it | Effect |
|---|---|---|
| ALL CAPS | `I NEED you` | louder / intense on that word |
| Stretch a vowel | `lo-o-o-ove` | melisma / sustained note |
| Repeat letters | `yeaaah`, `noooo` | extended casual vowel |
| Hyphen-stretch | `ne-e-ed` | drawn-out, emotional |
| Ellipses | `I... need... you` | dramatic pauses |
| Em dash | `wait—stop` | hard clipped cut |
| Syllable split | `Co... llec... tions` | choppy / segmented |
| lowercase + soft punctuation | `i'm so tired...` | intimate, small delivery |
| Mid-phrase line break | break the line | forces a breath / phrasing point |
| Repeated word in parens | `(go) (go) (go)` | adlib stabs on the beat |

- **Stack them:** `[belted] I NEED you for-e-e-ver...` = loud + sustained + trailing ache.
- **Adlibs in parentheses on the offbeat** between lines — `(yeah)`, `(uh)`, `(come on)`, `(ay)` — tuck behind the lead like producer adlibs.

---

## 14. Sound design, SFX, adlibs & ambience

- **SFX as bracket cues in lyrics:** `[gunshot] [thunder] [rain] [wind howling] [vinyl crackle] [applause] [crowd cheering] [phone ringing] [car engine] [door slam] [heartbeat] [footsteps] [glass breaking] [clock ticking] [birdsong] [siren]`. Hit rate is genre-dependent but often surprising.
- **Adlib-labeled hits ⚠️:** label percussive stabs like adlibs in caps on the beat before a hook — `[adlib: boom]`, `[adlib: clap]`, `[adlib: hey]` — to land them rhythmically with attitude.
- **Live-concert opener:** start with `[crowd noise] / [applause] / [live concert ambience]` then `[band enters]`. For an existing track, *Extend* and paste a crowd-ambience bracket into a new intro.
- **Ambience beds:** `[ambient pad] [field recording] [ocean waves] [city at night] [campfire crackle] [rain on window]` under intros/outros for cinematic framing.
- **Wordless hooks:** `[whistling melody] [humming] [la la la hook] [oohs and aahs]` for an earworm with no lyrics.
- **Texture FX:** `[stutter edit] [vocal chop] [glitch] [tape stop] [reverse cymbal] [riser] [white noise sweep]`.

---

## 15. Structure & arrangement power-moves

- **Buildup → Drop:** `[Build]`/`[Buildup]` immediately before `[Drop]` for EDM impact exactly where you want it.
- **Quiet-verse / loud-chorus dynamic:** put it in Style ("quiet verse to loud chorus dynamic") *and* mark sections `[Verse: sparse]` → `[Chorus: explosive]`.
- **False ending / fake-out:** `[Outro]` … then `[Surprise reprise]` / `[Beat returns]` for a double-ending.
- **Final-chorus lift:** `[Final Chorus: key change, full choir, louder]` — the classic payoff.
- **Half-time bridge:** `[Bridge: half-time, stripped back]` for contrast before the last lift.
- **Vocal drone / sustained bed ⚠️:** held `[oooooh]` or `[vocal drone]` under a section for tension.
- **Beat switch:** `[Beat switch]` mid-song for a two-part track (common in modern hip-hop).
- **Tag the transition, not just the section:** "`[smooth transition into]` `[Chorus]`" sometimes smooths the seam.
- **Dynamic build skeleton:**
```
[Intro] (soft piano only)
[Verse 1] (whispered, minimal arrangement)
[Pre-Chorus] (building intensity, drums enter)
[Chorus] (full band, belted, explosive)
```

---

## 16. "Sound like any artist" — the deconstruction method

You can't name artists in the Style field (and shouldn't paste anyone's lyrics). But you *can* describe a sonic fingerprint. Four steps:

1. **Tempo range** — find their usual BPM band.
2. **Vocal character** — describe it, don't name it: "melodic male vocals, conversational rap, occasional singing, vulnerable tone" / "breathy whispered female, intimate close-mic, ASMR-like."
3. **Production palette** — the defining instruments + mix: "atmospheric reverb pads, 808 bass, sparse arrangement" / "phaser guitar, analog synths, psychedelic swirl, heavily processed vocals."
4. **Mood** — "dark, nocturnal" / "warm, campfire-feel" / "intense, jazz-influenced."

Then assemble those into a normal 5-part Style prompt. Write your *own* original lyrics — never reproduce a real song's words.

---

## 17. Consistency: Personas, Voices, Custom Models, My Taste

- **Personas:** lock a vocalist you love from a generated track and reuse that voice across songs. ⚠️ Community reports saved Personas can drift toward a *generic* version of the genre voice — verify before building a catalog on one.
- **Voices:** clone/reuse your *own* voice (Pro/Premier, identity verification via spoken phrase, v5.5 model, age/region-gated).
- **Custom Models (Pro/Premier):** train a private variant on **6+ songs you actually own** (ownership verified, ~2–5 min to train). Biases output toward your sound. Up to three private models — the most musician-respecting feature.
- **My Taste:** the system nudges toward what you keep/favorite over time — curate your likes deliberately.
- **Poor-man's consistency (no Persona):** keep the *exact same Style wording + BPM* across a project. Tiny wording drift swaps the singer.

---

## 18. Editing existing tracks: Covers, Remix, Remaster, Extend, Replace

- **Where Covers lives:** not in "Create." Open a track → 3-dot menu → **Remix/Edit → Cover.** Most "Covers is missing" confusion is entering from the wrong door.
- **Cover = transform performance direction** while keeping musical identity. Feed it a *strong source track first*, then redirect genre/voice. Don't treat Cover like a blank Create prompt — that's why bad covers happen. (Designed for **Suno-generated** tracks, not commercial recordings.)
- **Remaster = polish what's already right.** Same song identity, stronger finished sound. (Cover changes direction; Remaster cleans it up.)
- **Extend = continue a track.** Paste new bracketed sections to steer where it goes; great for grafting a live-crowd intro or a surprise ending.
- **Replace Section / inpainting:** in Studio, select a timeline region and regenerate *just that part* — fix one bad line without re-rolling the whole song. Costs credits only for that length.
- **Alternates:** generate multiple versions of one section and pick the best.

---

## 19. Studio, stems & DAW workflow (Premier)

- **Stems:** split a track into up to ~12 time-aligned WAV stems (drums, bass, vocals, etc.). Export → mix in Ableton / Logic / FL.
- **Studio = in-browser DAW:** six-band EQ, stem volume/pan/arrangement, **Warp Markers** (fix timing without re-generating), **Remove FX** (strip reverb for clean stems), time-signature support (3/4, 6/8…), **Stem Cover**, and recording.
- **MILO-style step sequencer ⚠️:** newer Studio builds expose pattern/sequencer tooling for arrangement — capabilities shift release-to-release; check your build.
- **Clean-stem trick:** Remove FX → re-process externally → you control the reverb/space instead of being stuck with Suno's baked-in mix.
- **Copyright posture:** Suno-only audio has weak/uncertain protection. Strengthen your claim with *human* input — original lyrics, live instruments over stems, real arrangement decisions in a DAW.

---

## 20. Negative prompting & exclusion

- **v5+ supports an "avoid"/negative field.** Use it: `no autotune`, `no drums`, `no fade out`, `no electric guitar`, `no spoken intro`, `no 808s`.
- **Crowd-out method (when no negative field):** be so specific about what you *want* that there's no room for what you don't — "purely electronic, synthesized sounds only" beats begging it to stop adding guitar.
- **`[no vocals]` / `[instrumental]`** for clean beats.
- **Kill the long tail:** `[End]` in lyrics + `no outro, no fade` in the avoid field cuts dead air and saves credits.

---

## 21. Instrumentals & no-vocal tracks

- Toggle **Instrumental** in Custom Mode, or put "instrumental / no vocals" in Style, or `[no vocals]` in lyrics.
- With no vocal to carry it, the **Style field must work harder** — describe arrangement in detail: "cinematic orchestral, sweeping strings, French horns, timpani rolls, builds from quiet to massive, film-score quality, 85 BPM."
- Still **mark sections** (`[Intro] [Build] [Drop] [Outro]`) so it arranges instead of meandering.
- Add "cinematic" or "soundtrack" for filmic quality; "loopable" for beat beds.

---

## 22. Song length & arrangement length control

- Suno generates roughly **1 minute per run** by default (v5.5 supports much longer single generations, up to several minutes).
- **More lyrics = denser vocals** (risk of rushing). **Fewer lyrics + `[Instrumental]` breaks = more breathing room.**
- For longer songs, **Extend** from the end of the first generation, pasting the next sections.
- Use `[End]` to force a stop where you want it instead of paying for a trailing instrumental.

---

## 23. Album / project / multi-track consistency

- **Freeze the Style prompt** verbatim across an album; vary only lyrics and a single mood word per track.
- **One Persona or Custom Model** across the record for a consistent "artist."
- **Consistent BPM family** (e.g. everything 78–92) ties tracks together.
- **Album Mode** (third-party pre-production tools) can batch-plan many tracks with a shared narrative — useful scaffolding, but verify each generation yourself.

---

## 24. Credit-saving & iteration discipline

- **20–30s test clips** for any risky element (name, accent, weird tag, hook) before a full render.
- **Re-roll cheap, edit late.** Don't tag-tune until a roll is ~80% there.
- **Section-edit, don't re-roll the whole song,** when only one part is broken.
- **Phonetic-fix everything before generating** — every mispronounced render is unrecoverable credits.
- **Save winning Style prompts** verbatim; small wording drift = different song.
- **`[End]` + `no fade`** to avoid paying for tails you'll delete.
- **Generate 3–5 of the same prompt** and pick — variation is the feature, not a bug.

---

## 25. Genre Blueprint Library (copy-paste Style prompts)

**Lo-Fi Hip-Hop**
```
lo-fi hip-hop, chill and nostalgic, pitched-down vocal sample, Rhodes piano,
tape-saturated drums, vinyl crackle, warm analog bass, lo-fi tape hiss, 75 BPM
```
**Synth-Pop / 80s**
```
synth-pop, 80s-inspired, upbeat and nostalgic, polished female vocals, analog synth pads,
gated-reverb drums, Moog bass, shimmering arpeggios, bright radio-ready mix, 118 BPM
```
**Trap**
```
trap, dark and aggressive, melodic rap delivery, heavy 808 sub-bass, hi-hat rolls,
atmospheric pads, distorted vocal effects, modern hip-hop production, 140 BPM
```
**Indie Folk**
```
indie folk, warm and intimate, soft male vocals with breathy delivery, acoustic guitar
fingerpicking, upright bass, brushed snare, harmonica, lo-fi warmth, 92 BPM
```
**Deep House**
```
deep house, groovy and hypnotic, filtered vocal chops, warm bass synth, crisp hi-hats,
shuffled beat, Rhodes stabs, spacious reverb, 122 BPM
```
**Neo-Soul / R&B**
```
neo-soul, smooth and intimate, silky female vocals with runs, Rhodes electric piano,
warm sub bass, brushed drums, layered harmonies, warm analog production, 78 BPM
```
**Alternative Rock**
```
alternative rock, raw and emotional, raspy male vocals, distorted guitar wall, driving bass,
explosive drums, quiet verse to loud chorus dynamic, 135 BPM
```
**Reggaeton**
```
reggaeton, high-energy, Latin club feel, rhythmic male vocals, dembow beat, punchy 808,
tropical synths, percussive shakers, polished urban production, 95 BPM
```
**Ambient / Atmospheric**
```
ambient, ethereal and spacious, no vocals, evolving synth pads, granular textures,
soft piano, field recordings, reverb-drenched, slow builds, 65 BPM
```
**Phonk**
```
phonk, dark and aggressive, Memphis rap influence, pitched-down vocal samples, cowbell,
heavy 808, distorted bass, tape-saturated drums, lo-fi crunch, 130 BPM
```
**Cinematic Instrumental**
```
cinematic orchestral, epic and triumphant, no vocals, full symphony orchestra, soaring
strings, French horns, timpani, building from quiet to massive, film score quality, 85 BPM
```
**Boom Bap**
```
boom bap, 90s east coast hip-hop, jazz samples, dusty drums, upright bass, conscious
rap delivery, vinyl crackle, warm analog, 90 BPM
```
**Drum & Bass**
```
liquid drum and bass, euphoric and driving, chopped vocal, rolling sub-bass, fast breakbeat,
lush pads, spacious reverb, crisp digital mix, 174 BPM
```
**Country**
```
modern country, warm storytelling, male drawl with twang, acoustic guitar, pedal steel,
fiddle, punchy live kit, polished Nashville mix, 100 BPM
```
**Metal**
```
melodic metalcore, aggressive and explosive, screamed verses with sung chorus, downtuned
guitar wall, double-kick drums, driving bass, modern loud mix, 150 BPM
```

---

## 26. Genre-blending recipes

Put the dominant genre first; 2–3 genres max + one texture word. Four+ genres = mush.
- **Jazz + Hip-Hop:** `jazz rap, boom bap, live jazz instrumentation, walking upright bass, brushed drums, sax solo, melodic rap, vintage vinyl, warm analog, 90 BPM`
- **Country + Electronic:** `country electronica, modern twang, female vocals with slight drawl, acoustic guitar over electronic beat, synth pad, four-on-the-floor kick, polished but organic, 115 BPM`
- **Soul + Drill ⚠️:** `dark soul-drill, cinematic strings, vulnerable male vocal, sliding 808s, hi-hat triplets, vinyl warmth, 140 BPM`
- **Folk + Cinematic:** `folk-noir, haunting, fingerpicked guitar, lone cello, breathy female vocal, distant reverb, slow build, 80 BPM`

---

## 27. Deliberately weird / experimental

- **Crank Weirdness >60** + add `microtonal, odd-meter, found percussion` for IDM/experimental.
- **Mismatch on purpose:** gentle lyrics over an aggressive style tag (or vice versa) for tension.
- **Whisper-to-scream arc:** `[whispered]` verse → `[building]` pre → `[screaming]` chorus for huge dynamic range.
- **Genre whiplash:** `[Beat switch]` into a totally different style halfway through.
- **Fake field recording:** open with `[field recording]` ambience, let the "song" emerge from it.
- **Tape-degradation aesthetic:** `lo-fi, bit-crushed, wow and flutter, warped tape, distant AM-radio EQ`.

---

## 28. Troubleshooting matrix (symptom → fix)

| Symptom | Likely cause | Fix |
|---|---|---|
| Sounds generic / "default" | Vague prompt | Add subgenre + mood + 3-layer vocal + 2–4 named instruments + BPM (8–15 tags) |
| Wrong genre creeps in | No tempo anchor / weak first tag | Add specific BPM; put dominant genre first; add `no [unwanted element]` |
| Mispronounced word | Spelling ambiguity | Phonetic respell (§12) before generating |
| Vocals mumble / unclear | No delivery cue | Add `[staccato]` / `[crisp]` / `[spoken word]`; reduce lyric density |
| Singer changes every run | Style wording drift | Lock exact Style text + BPM; use a Persona/Custom Model |
| Repetitive / padded | Too few section types | Add `[Pre-Chorus] [Bridge] [Instrumental]`; vary verse lyrics; cap chorus at 3× |
| No payoff / no chorus lift | Missing structure tags | Mark `[Chorus]`; add `[Build]` before it; `[Final Chorus: louder]` |
| Long dead instrumental tail | No stop tag | `[End]` + avoid `no fade, no outro` |
| Contradictory output | Conflicting mood tags | Pick one mood direction; create contrast via structure instead |
| Words rushed | Verse too long | 4–8 lines per verse; add `[Instrumental]` breaks |
| Effect baked in / can't mix | Stuck with Suno's reverb | Studio → Remove FX → export stems → process externally |

---

## 29. Myths, gotchas & things that don't reliably work

- **No real pronunciation meta-tag exists.** `[pronounce: ...]` is folklore. Respell phonetically.
- **Long bracket sentences get ignored.** One short instruction per bracket.
- **Tag overload backfires** — 30 tags ≠ 30× control; it dilutes. Pick the few that matter.
- **Raw digits, IPA symbols, and emoji** aren't reliably read as cues. Spell it out.
- **You can't fix pronunciation/timing after generation** — regenerate or section-replace.
- **Saved Personas can drift generic ⚠️** — verify per use.
- **Covers on commercial songs** are not the intended use; results are inconsistent/blocked.
- **Naming an artist in Style does nothing** (and pasting their lyrics is a copyright problem) — deconstruct the sound instead.
- **"Make it good" / vibe-only prompts** = slot-machine output. Specificity is the whole game.
- **Expecting literal interpretation** is the #1 mistake — Suno approximates intent, it doesn't execute commands.

---

## 30. Commercial / copyright notes (verify current terms yourself)

- **Pro/Premier grant commercial-use rights;** free tier is personal use only. You can distribute to Spotify/Apple/YouTube on paid tiers.
- **AI-generated audio has limited/uncertain copyright** in most jurisdictions; adding human authorship (your lyrics, live playing, arrangement) strengthens any claim.
- **Covers/remixes of others' recordings** raise licensing issues — the built-in Covers tool is meant for Suno-generated sources.
- Terms shift; check Suno's current licensing before you monetize.

---

## 31. Master cheat strip (paste-ready)

```
FORMULA:   genre+sub, mood+energy, voice(character+delivery+effect), 2-4 instruments, production, BPM  (8-15 tags)
STRUCTURE: [Intro][Verse][Pre-Chorus][Chorus][Post-Chorus][Bridge][Build][Drop][Outro][End]
EMOTION:   [whispered][trembling][belted][desperate][crying][spoken word]  (tag = intent)
TYPOGRAPHY: CAPS=loud  lo-o-ove=sustained  I... need... you=pauses  ne-e-ed=stretched  wait—stop=clip
VOICE:     character + delivery + effects, e.g. "raspy female tenor, breathy, dry close-mic"
PRONOUNCE: read->red  live->laiv  lead->led  through->thru  2024->twenty twenty-four  AI->A-I
BIND:      ra-ta-ra-ta (one fluid word, each chunk said) / Co-llec-tions (force a split)
SFX:       [crowd cheering][vinyl crackle][rain][applause]   (yeah)(uh)=adlibs in parens
NEGATIVE:  avoid field -> "no autotune, no 808s, no spoken intro, no fade"
STOP TAIL: [End] + "no outro, no fade"
SLIDERS:   Weirdness ~ low for clean / >60 for experimental;  Style Influence ~45-50 = balanced
WORKFLOW:  test 30s clip -> re-roll cheap -> lock voice/Persona -> section-replace to fix -> Extend for length
```

---

## 32. Glossary

- **Style field** — comma-separated *sound* description (genre/mood/instruments/voice/production/BPM).
- **Lyrics field** — words + bracketed performance/structure tags.
- **Meta-tag / bracket tag** — `[ ]` instruction in lyrics (structure, dynamics, SFX, vocal cue).
- **Persona** — a saved, reusable vocalist identity captured from a generated track.
- **Voice** — your own cloned voice (verification + paid tier required).
- **Custom Model** — a private model trained on songs you own; biases toward your sound.
- **Stems** — isolated instrument/vocal tracks exported as time-aligned WAVs.
- **Cover** — regenerate an existing track in a new performance direction, keeping identity.
- **Remaster** — polish/clean an existing track without changing its identity.
- **Extend** — continue a track past its current end.
- **Replace / inpaint** — regenerate one selected timeline region only.
- **Creative Sliders** — Weirdness, Style Influence, Audio Influence — weighted biases on generation.
- **Homograph** — same spelling, multiple pronunciations (read, live, lead, bass) — resolve by respelling.
- **Melisma** — one syllable stretched across many notes — induced with stretched vowels (`lo-o-ove`).

---

*Tags and feature names shift between Suno versions. When a ⚠️ item doesn't fire, it's the model rev, not you. Keep a personal log of what actually lands for your genre, voice, and tier — that beats any list, including this one.*
