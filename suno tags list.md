# Suno v5.5 Cheat Sheet — Exhaustive Reference: Instruments, Vocals, SFX/Ambience, Tempo/Dynamics & Genre-Specific In-Lyric Tags

## TL;DR
- This is a fully enumerated, deduped reference covering five families — instruments + articulations, vocals (delivery/rap/character/effects), SFX/ambience, tempo/dynamics/energy, and genre-specific in-lyric moment tags — with each item tagged by field placement (LYRICS bracket vs. STYLE descriptor) and reliability (verified / biases-output / placebo-folklore), optimized for Suno v5.5 (released March 26, 2026, described by Suno as "our best and most personal model yet," adding Voices, Custom Models and My Taste).
- The single most important operating rule: square-bracket `[Tags]` go in the LYRICS field as section/performance directives (AceTagGen's testing of a 308-tag database rates square brackets "most reliable, ~90% compliance" and says "bracket instructions are roughly 10x more powerful than Style field descriptors for arrangement control"); comma-separated descriptors go bracket-free in the STYLE field, where bracket tags can glitch the generation. Keep to 2–4 bracket tags per section and 2–4 named instruments — beyond that Suno drops later/lower-priority tags.
- v5.5 did not change tag syntax (it added personalization), but its improved expressiveness means subtle descriptors "land harder." The biggest reliability traps are unchanged: literal SFX get SUNG ALOUD instead of rendered, in-song accelerando/ritardando will not change BPM, exact key-lock is placebo, and numeric BPM is a target not a metronome lock.

## Key Findings

**Field placement is the master variable.** Per tagasong.com: "Lyrics Box: Commands require [Brackets]. Without them, the AI will attempt to sing your instructions as lyrics. Styles Box: Commands must be bracket-free. Adding brackets here can cause the model to ignore your genre or glitch the generation entirely." Most instrument and texture control is therefore stronger as a STYLE descriptor, while section/performance moments are stronger as LYRICS brackets.

**Reliability tiers (used throughout):**
- **Verified** — consistently produces the intended result (e.g., `[Whispered]`, `[Guitar Solo]`, `[Instrumental Break]`, numeric BPM in Style field as a target).
- **Biases-output** — nudges the model but is not guaranteed; works best paired with matching genre/instrumentation (most instrument brackets, mood tags, dynamics).
- **Placebo-folklore** — community-circulated but unverified or actively failure-prone (percentage tags like `[Reverb: 30%]`, `[hard cut]`, exact key-lock, in-render `[Accelerando]` BPM change).

**Priority stack within a LYRICS section** (AceTagGen): section identifier → vocal delivery → instrumentation → effects/dynamics. Effects/dynamics are dropped first when a section exceeds ~2–4 tags. Combined tags such as "[Soft Verse] [Powerful Chorus] [Gentle Bridge] [Explosive Final Chorus]" "consistently outperform using two separate tags like [Chorus] followed by [powerful] because they're processed as a unified instruction rather than two competing directives" — and they count as a single tag against the per-section limit (AceTagGen).

**v5.5 specifics.** Per Suno's official release notes and HookGenius: v5.5 launched March 26, 2026 as a personalization layer (Voices; Custom Models — train a personalized version of v5.5 from "at least 6 tracks," with "Pro and Premier subscribers" able to create "up to three"; and My Taste) on top of v5's audio engine. "All v5 prompts, metatags, negative prompts, and style tags work identically in v5.5. Nothing was removed or changed." v5.5 "is better at interpreting subtle descriptors. Where v5 might ignore 'slightly detuned vintage keys,' v5.5 actually delivers it." Suno recognizes "roughly 300+ genre tags cleanly, and subgenre beats parent genre almost every time."

---

## Details

### 1. COMPLETE INSTRUMENTS LIST (instruments + playing-style/articulation)

Convention: **Bracket form** (LYRICS) / **Style descriptor** (STYLE). Suno often responds to an instrument in the LYRICS field only if that instrument is also present/plausible in the STYLE field/genre (suno.wiki: "You may need to describe the instrument within the Style Prompt if you want to manipulate it with metatags"). Most instrument brackets are **biases-output**; solo brackets ([Guitar Solo] etc.) are **verified**.

**GUITARS**
- Instruments: `[Acoustic Guitar]` / "acoustic guitar"; `[Electric Guitar]` / "electric guitar"; `[Classical Guitar]` / "classical guitar, nylon-string"; `[12-String Guitar]` / "12-string guitar"; `[Slide Guitar]` / "slide guitar"; `[Lap Steel]` / "lap steel guitar"; `[Resonator Guitar]` / "resonator/dobro"; `[Baritone Guitar]` / "baritone guitar"; `[Nylon Guitar]` / "nylon-string guitar"; `[Flamenco Guitar]` / "flamenco guitar"; `[Steel-String]`.
- Playing styles/articulations (STYLE descriptors, biases-output): "fingerpicked / fingerstyle", "palm-muted", "power chords", "arpeggiated guitar", "tremolo picking", "shredding / technical shredding", "chicken pickin'", "wah / wah-pedal", "distorted guitar", "clean guitar", "jangly guitar", "surf reverb / surf guitar", "chugging guitar" (suno.wiki lists `[chugging guitar]` as a working onomatopoeic instrument cue), "open-chord guitar", "bottleneck slide", "twangy", "high-gain", "scooped mids", "djent", "octave guitar".
- Solo/feature brackets (LYRICS, verified): `[Guitar Solo]`, `[Electric Guitar Solo]`, `[Acoustic Guitar Solo]`, `[Fingerstyle Guitar Solo]` (suno.wiki), `[Slide Guitar Solo]`, `[Shred Solo]`, `[Wah Guitar Solo]`, `[Guitar Riff]`, `[Riff]`, `[Palm Mute]`, `[Pinch Harmonic]`.

**BASS**
- `[Bass]` / "bass guitar"; `[Electric Bass]` / "electric bass / P-bass / J-bass"; `[Upright Bass]` / "upright/double bass"; `[Slap Bass]` / "slap bass"; `[Fretless Bass]` / "fretless bass"; `[Synth Bass]` / "synth bass"; `[808]` / "808 / 808 bass / sub 808"; `[Sub Bass]` / "sub bass / deep sub"; `[Wobble Bass]` / "wobble bass"; `[Acid Bass]` / "acid bass / 303 bass"; `[Reese Bass]` / "Reese bass".
- Articulations (STYLE): "picked bass", "fingered bass", "slapped", "walking bass" (also `[Walking Bass]` LYRICS), "rubbery bass", "distorted 808", "sliding/gliding 808".
- Solo/feature brackets (LYRICS): `[Bass Solo]`, `[Melodic Bass]` (suno.wiki), `[Syncopated Bass]` (suno.wiki), `[Bass Drop]`, `[808 Bass]`.

**KEYS / PIANO**
- `[Piano]` / "piano"; `[Grand Piano]` / "grand piano"; `[Upright Piano]` / "upright piano"; `[Electric Piano]` / "electric piano"; `[Rhodes]` / "Rhodes / Fender Rhodes"; `[Wurlitzer]` / "Wurlitzer"; `[Hammond Organ]` / "Hammond organ / Hammond B3"; `[Organ]` / "organ"; `[Church Organ]` / "church/pipe organ"; `[Harpsichord]` / "harpsichord"; `[Clavinet]` / "clavinet / clav"; `[Celesta]` / "celesta"; `[Accordion]` / "accordion"; `[Melodica]` / "melodica"; `[Toy Piano]` / "toy piano"; `[Prepared Piano]` / "prepared piano"; `[Bubble Organ]` / "bubble organ" (reggae).
- Solo brackets (LYRICS, verified): `[Piano Solo]`, `[Organ Solo]`, `[Rhodes Solo]`, `[Honky-Tonk Piano Solo]`.

**SYNTHS**
- `[Synth]` / "synthesizer / synth"; "analog synth", "digital synth", `[Modular Synth]` / "modular synth", "FM synth", "supersaw", `[Synth Pads]` / "synth pads / atmospheric pads / ambient pads", `[Synth Lead]` / "synth lead", `[Arpeggiated Synth]` / "arpeggiated synth / arpeggios / arp", `[Synth Stabs]` / "synth stabs", "synth brass", "plucks / rave pluck", "bell synth", "vintage analog", "Moog / Moog bass", "Juno", "303 (acid)", "Prophet-5", "ARP 2600", "808/909/707 (drum machines — see Drums)".
- Solo brackets (LYRICS): `[Synth Solo]`, `[Analog Lead]`, `[Portamento]`.

**DRUMS & PERCUSSION**
- Kits/machines: `[Drums]` / "drums"; `[Acoustic Drums]` / "acoustic kit / live drums"; `[Electronic Drums]` / "electronic kit"; `[Drum Machine]` / "drum machine"; `[808]`/`[909]`/`[707]` / "808/909/707 drum machine"; `[Trap Hi-Hats]` / "trap hi-hats / rolling hi-hats / triplet hi-hats"; `[Hi-Hat Roll]`; `[Breakbeat]` / "breakbeat / amen break"; `[Brushed Drums]` / "brushed drums"; `[Four on the Floor]` / "four-on-the-floor".
- Hand/world percussion (STYLE, biases-output): "congas", "bongos", "timbales", "tabla", "djembe", "taiko", "frame drum", "cajon", "tambourine", "shaker", "claps / handclaps", "finger snaps", "woodblock", "cowbell", "vibraslap", "dhol", "talking drum", "bone rattles".
- Pitched percussion: "timpani" (also `[Timpani Roll]`), "gongs", "handpan", "marimba", "xylophone", "glockenspiel", "vibraphone", "steel drums / steel pan", "tubular bells".
- Solo/feature brackets (LYRICS, verified): `[Drum Solo]`, `[Drum Break]`, `[Percussion Break]` (suno.wiki), `[Blast Beat]`, `[Double Bass]` (metal), `[Timpani Roll]`, `[Drum Roll]`.

**STRINGS**
- `[Violin]` / "violin"; `[Viola]` / "viola"; `[Cello]` / "cello"; `[Double Bass]` / "double bass / contrabass"; `[String Quartet]` / "string quartet"; `[String Section]` / "string section / full string ensemble / lush strings"; `[Strings]` / "strings"; `[Harp]` / "harp"; `[Fiddle]` / "fiddle".
- Articulations (STYLE): "pizzicato" (also `[Pizzicato]`), "staccato strings", "legato strings", "tremolo strings", "string ostinato", "sweeping/soaring strings", "syncopated violins".
- Solo/feature brackets (LYRICS, verified): `[Violin Solo]`, `[Cello Solo]`, `[Strings Swell]`, `[Strings Rise]`, `[String Break]`.

**BRASS**
- `[Trumpet]` / "trumpet"; `[Trombone]` / "trombone" (suno.wiki notes `[sad trombone]` as an onomatopoeic cue); `[French Horn]` / "french horn"; `[Tuba]` / "tuba / contrabass trombone"; `[Flugelhorn]` / "flugelhorn"; `[Cornet]` / "cornet"; `[Brass Section]` / "brass section / horn section / big band brass"; `[Muted Trumpet]` / "muted trumpet".
- Feature brackets (LYRICS): `[Trumpet Solo]`, `[Horn Stabs]` / "horn stabs / brass stabs", `[Brass Stabs]`, `[Brass Fanfare]` / "brass fanfare / horn fanfare", `[Brass Swell]`.

**WOODWINDS**
- Saxes: `[Saxophone]` / "saxophone"; `[Alto Sax]` / "alto saxophone"; `[Tenor Sax]` / "tenor saxophone"; `[Baritone Sax]` / "baritone saxophone"; `[Soprano Sax]` / "soprano saxophone". Style-descriptor examples: "smoky saxophone", "soulful sax".
- Others: `[Flute]` / "flute"; `[Clarinet]` / "clarinet"; `[Oboe]` / "oboe"; `[Bassoon]` / "bassoon"; `[Piccolo]` / "piccolo"; `[Recorder]` / "recorder"; `[Pan Flute]` / "pan flute"; `[Harmonica]` / "harmonica"; `[Bagpipes]` / "bagpipes / Uilleann pipes"; `[Didgeridoo]` / "didgeridoo"; `[Nadaswaram]`.
- Solo brackets (LYRICS, verified): `[Sax Solo]`, `[Saxophone Solo]`, `[Flute Solo]`, `[Harmonica Solo]`, `[Clarinet Solo]`.

**WORLD / FOLK / ETHNIC**
- `[Sitar]` / "sitar"; `[Oud]` / "oud"; `[Koto]` / "koto"; `[Shamisen]` / "shamisen"; `[Erhu]` / "erhu"; `[Guzheng]` / "guzheng"; `[Kalimba]` / "kalimba / mbira"; `[Mbira]`; `[Balalaika]` / "balalaika"; `[Banjo]` / "banjo"; `[Mandolin]` / "mandolin"; `[Ukulele]` / "ukulele"; `[Dulcimer]` / "hammered/Appalachian dulcimer"; `[Bouzouki]` / "bouzouki"; `[Charango]` / "charango"; `[Hurdy-Gurdy]` / "hurdy-gurdy"; `[Theremin]` / "theremin"; `[Tagelharpa]`; `[Veena]`; `[Sarangi]`; `[Tumbi]`; `[Berimbau]`; `[Pedal Steel]` / "pedal steel" (country); `[Sarod]`.
- Feature brackets (LYRICS): `[Banjo Solo]`, `[Bluegrass Banjo Interlude]` (suno.wiki — works inside country, not orchestral), `[Sitar Solo]`, `[Mandolin Solo]`.

> **Onomatopoeia trick (placebo-leaning, occasionally works):** suno.wiki notes "Suno will sometimes respond to un-singable text as a musical instrument" — e.g., punctuation-only lines under `[Percussion Break]`, or onomatopoeic words to trigger an instrument; "Often they are sung as lyrics, but sometimes trigger the intended instrument."

### 2. COMPLETE VOCAL LIST

**(a) Delivery / technique** (mostly LYRICS brackets; many double as STYLE descriptors). `[Whispered]`/`[Whisper]`/`[Whispers]` is the single most reliable delivery tag (AceTagGen). Verified-to-biases:
`[Whispered]`, `[Breathy]`, `[Spoken]`, `[Spoken Word]`, `[Spoken Word Verse]`, `[Sung]`, `[Belted]`/`[Belting]`, `[Shouted]`, `[Screamed]`/`[Screaming]`/`[Screams]`, `[Growled]`/`[Growl]`, `[Falsetto]`, `[Head Voice]`, `[Chest Voice]`, `[Raspy]`, `[Smooth]`, `[Soulful]`, `[Operatic]`, `[Crooning]`, `[Nasal]`, `[Airy]`, `[Vibrato]`, `[Melisma]`/`[Melismatic]`, `[Vocal Run]`/`[Runs]`, `[Riffs]`, `[Staccato]`, `[Legato]`, `[Chant]`/`[Chant Vocals]`, `[Scat]`, `[Yodel]`, `[Vocal Fry]`, `[Throat Singing]`, `[Beatbox]`, `[Humming]`, `[Ad-libs]`, `[Call and Response]`, `[Gang Vocals]`, `[Doubled Vocals]`/`[Doubled]`, `[Vocalization]`, `[Sprechgesang]`, `[Gregorian Chant]`, `[Lounge Singer]`, `[Vocaloid]`, `[Acapella]`/`[a cappella]` (no space before "cappella" per AceTagGen). STYLE descriptors for delivery: "intimate close-mic", "conversational", "group harmonies", "stacked harmonies".

**(b) Rap flow** (LYRICS brackets / STYLE descriptors, biases-output): `[Rapped]`/`[Rap]`, `[Fast Rap]`, `[Slow Flow]`, `[Melodic Rap]`, `[Trap Flow]`, `[Boom Bap Flow]`, `[Mumble Rap]`, `[Double Time]`/`[Double-Time Flow]`, `[Triplet Flow]`, `[Drill Flow]`, `[Conscious]`/"conscious rap", `[Aggressive]`/"aggressive rap", `[Laid-Back]`/"laid-back flow", `[Spoken Flow]`/"spoken flow / rhythmic delivery", "deadpan delivery", "toasting" (dancehall), "hard bars", "storytelling rap". Note: Suno defaults toward melody — to force rapping, tag "rap vocals", "spoken flow", or "rhythmic delivery" explicitly (HookGenius).

**(c) Character / tone / emotion** (LYRICS brackets/STYLE):
- Gender/character: `[Male Vocal]`/`[Male Vocalist]`, `[Female Vocal]`/`[Female Vocalist]`, `[Androgynous Vocal]`, `[Child Vocal]`/`[Boy]`/`[Girl]`, `[Duet]`, `[Choir]`, `[Gospel Choir]`, `[Gang Vocals]`, `[Backing Vocals]`, `[Male + Female Harmony]`, `[Announcer]`, `[Reporter]`, `[Female Narrator]`, `[Diva Solo]`, `[Primal Scream]`, `[Male Tenor]`, `[Female Soprano]`, `[Baritone]`, `[Alto]`, `[Elderly Vocal]`. Age cues: "young", "mature". SATB: `[SATB]`, `[Multiple voice chorus s a t b]`, `[Choir: Gospel]`, `[Choir Vocals]` — best used only on the chorus per the sovietmenace master cheatsheet "SATB Rule" (using it throughout removes the dramatic impact).
- Emotion (place on its own line before the lyric; do not pipe-stack): `[Vulnerable]`, `[Confident]`, `[Aggressive]`/`[Angry tone]`, `[Melancholic]`, `[Sultry]`, `[Defiant]`, `[Joyful]`, `[Angry]`, `[Sad]`, `[Playful]`, `[Seductive]`, `[Desperate]`, `[Tender]`, `[Haunting]`/`[Haunted]`, `[Ethereal]`, `[Powerful]`, `[Fragile]`, `[Crying Voice]`, `[Spoken Word Crying]`, `[Mocking Laughter]`, `[Intimate]`, `[Mysterious]`, `[Triumphant]`. The "killer combo" (sovietmenace): `[spoken word crying]` … `[laughter]` for emotional whiplash within one line.

**(d) Vocal effects** (LYRICS brackets/STYLE descriptors, biases-output): `[Autotune]`/`[AutoTune]`/`[Voice: Auto-tune]`, `[No Autotune]`, `[Vocoder]`, `[Talkbox]`, `[Distorted Vocals]`, `[Telephone Effect]`/`[Telephone Voice]`/`[Filtered Vocals]` (phone/radio), `[Megaphone]`, `[Lo-fi Vocal]`, `[Double-Tracked]`/`[Doubled]`, `[Harmonized]`/`[Harmonized Chorus]`/`[Stacked Harmonies]`, `[Vocal Chops]`, `[Glitched Vocals]`, `[Reverse Vocals]`, `[Pitched Up]`, `[Pitched Down]`, `[Formant Shift]`, `[Whisper Layer]`, `[Reverb]`/`[Reverb Heavy]`, `[Delay]`/`[Echoing Vocals]`, `[Tape-Saturated]`. **Placebo warning:** percentage/parameter vocal tags do nothing — HookGenius: "Percentage tags ([Reverb: 30%], [Bass: 80%]) are placebo. Stop pasting them." Use descriptive words ("reverb-drenched", "dry close-mic") in the Style field instead.

### 3. COMPLETE SFX & AMBIENCE LIST

**Critical failure mode (well-documented):** Suno frequently SINGS the SFX word aloud as a lyric instead of rendering the actual sound. AceTagGen on `[hard cut]`: "SUNO often interprets the text literally and sings 'hard cut' into your song instead of performing the cut… 'I commanded it to add a hard cut just after it sings the word song and it actually sang the instruction.'" Stoke McToke: meta tags "used badly, get ignored… or sung out loud, which is always a moment." The mechanism (tagasong): without brackets, "the AI will attempt to sing your instructions as lyrics."

**Reliability tiers for SFX (community consensus, not official):**
- **Most reliable** — vocal/human-adjacent sounds that sit naturally in a vocal track: `[Applause]`, `[Cheering]`, `[Cheers and Applause]`, `[Clapping]`, `[Laughing]`/`[Audience Laughing]`, `[Chuckles]`, `[Giggling]`, `[Sighs]`, `[Cough]`, `[Clears Throat]`, `[Whispers]`, `[Whistling]`, `[Crowd Cheering]`, `[Screams]`. Also reliable as STYLE descriptors (not brackets): "vinyl crackle / lo-fi crackle", "crowd ambience / stadium crowd ambience", "tape hiss". (sunoaiwiki.com lists the human/vocal SFX set; Blake Crosley uses "vinyl crackle" as a style descriptor.)
- **Coin-flip / needs retries** — literal environmental & mechanical SFX brackets: `[Rain]`/`[Rainfall]`, `[Thunder]`/`[Thunderstorms]`, `[Wind]`/`[Wind Howling]`/`[Soft Breeze]`, `[Ocean Waves]`/`[Waves]`, `[River Sounds]`/`[Flowing Water]`, `[Fire Crackling]`, `[Birds Chirping]`/`[Birdsong]`, `[Crickets Chirping]`, `[Dog Barking]`/`[Barking]`, `[Cat Meow]`, `[Wolf Howl]`, `[Footsteps]`/`[Footsteps on Gravel]`/`[Footsteps on Pavement]`, `[Heartbeat]`, `[Breathing]`/`[Breath]`, `[Clock Ticking]`, `[Phone Ringing]`/`[Telephone Ringing]`, `[Alarm]`, `[Doorbell]`, `[Knock]`, `[Door Slam]`/`[Door Shutting]`/`[Creaking Doors]`, `[Glass Breaking]`, `[Gunshot]`, `[Explosion]`, `[Siren]`, `[Car Engine]`, `[Motorcycle]`, `[Helicopter]`, `[Train]`/`[Train Whistle]`/`[Railroad Sounds]`, `[Horse Galloping]`, `[Camera Shutter]`, `[Cash Register]`, `[Coins]`, `[Sword Clash]`, `[Magic Sparkle]`, `[Laser]`, `[8-bit Blip]`, `[Typing]`, `[Record Scratch]`/`[Turntablism]`, `[Vinyl Crackle]` (as bracket), `[Tape Stop]`, `[Tape Rewind]`, `[Radio Static]`/`[Static]`/`[TV Static]`, `[White Noise]`, `[Church Bells]`/`[Bell Ringing]`/`[Bell Dings]`, `[Beeping]`/`[Beep]`/`[Bleep]` (censor), `[Construction Sounds]`, `[Traffic Noise]`/`[City Noise]`/`[Urban Street Noise]`, `[Industrial Sounds]`, `[Nature Ambience]`/`[Natural Ambience]`, `[Bar Ambience]`, `[Restaurant Chatter]`, `[Rain on Window]`, `[Nighttime Atmosphere]`/`[Daytime Atmosphere]`, `[Crowd Chant]`, `[Stadium Ambience]`.
- **Reliable special-function tags:** `[Silence]` ("Complete silence, no sound" — sunoaiwiki) and `[Censored]`/`[Bleep]` (silenced/censored part) are recognized; `[Mic Feedback]`/`[Feedback]` works in rock/noise contexts.
- **Placebo / avoid:** `[hard cut]` (sung aloud); any `[Effect: NN%]` percentage tag.

**Best practice:** For ambience, prefer a STYLE-field descriptor ("smoky club ambience"; or a bracketed intro cue like `[stadium crowd ambience, big applause, stage reverb]`) over a bare literal SFX bracket; regenerate 3–5 times since rendering vs. singing varies per generation.

### 4. COMPLETE TEMPO / DYNAMICS / ENERGY LIST

**BPM (STYLE field):** Numeric BPM works as a strong target/bias, NOT a metronome lock. Blake Crosley: "'127 BPM' is treated as approximate guidance, not a metronome lock." HookGenius: put BPM in the style prompt, not lyrics; v5.5 respects numeric BPM (e.g., "128 BPM") cleanly. Don't write a range ("120–130 BPM") — the model picks one. Descriptive fallback tempo words also work: "slow", "ballad tempo", "mid-tempo", "uptempo", "fast", "breakneck speed", "downtempo", "half-time groove", "double-time".

**Tempo drift (confirmed inherent, official):** Suno's official "Fixing Tempo Drift" help article states: "The tempo is not consistent over time, just like live music, which characteristically drifts around a little bit in speed." The fix is post-generation in Suno Studio: set Project Tempo → "Manual BPM" to lock the grid before exporting stems (not a prompt tag).

**Tempo-change tags within one generation (KNOWN FAILURE):** sunoprompt.com: "You cannot reliably program a tempo change (accelerando or ritardando) within a single Suno prompt." `[Accelerando]`/`[Ritardando]`/`[Rallentando]`/`[Stringendo]`/`[Allargando]` bias "feel" only; for a real tempo change, generate the slow and fast parts separately and edit in a DAW. AceTagGen notes `[Tempo Change: X BPM]` works only at musical boundaries (verse→chorus), not mid-bar.

**Dynamics (LYRICS brackets, verified-to-biases; affect volume/intensity, NOT BPM):** `[Crescendo]` and `[Decrescendo]`/`[Diminuendo]` swell/reduce intensity (AceTagGen; sunoprompt: crescendo "create[s] a feeling of increasing energy, but won't change the BPM"). Also: `[Sforzando]` (volume accent), `[Swell]`, `[Build]`/`[Build-Up]`, `[Drop]`, `[Soft]`/`[Quiet]`/`[Pianissimo]`, `[Loud]`/`[Forte]`/`[Fortissimo]`, `[Thunderous]`, `[Climactic]`, `[Big Finish]`, `[Stop]`/`[Stop-Time]` (brief dramatic pause), `[Half-Time]`/`[Drop to Half-Time]`, `[Double-Time]`.

**Rhythm-feel / groove (STYLE descriptors, biases-output — often stronger than tempo words):** "four-on-the-floor", "syncopated", "swung / swing", "shuffle", "triplet feel", "polyrhythm / polyrhythmic", "straight", "halftime trap bounce", "rolling breakbeat", "dembow rhythm" (reggaeton), "skank / syncopated guitar skanks" (reggae). Jack Righteous: groove nouns ("four-on-the-floor kick", "halftime trap bounce", "shuffle groove") often "explain the feel more clearly" than a BPM number.

**Energy descriptors (STYLE):** "high energy / energetic", "driving", "pulsing", "pumping", "laid-back", "chill", "mellow", "frenetic", "climactic", "sparse", "dense", "building intensity", "low energy". `[Building Intensity]` is a verified LYRICS dynamic.

**Time-signature tags (UNRELIABLE for generation):** `[3/4 Time]`, `[6/8 Time]`, `[7/8]`, `[5/4]` — Suno's own Studio 1.2 docs state the time-signature control "adjusts the Studio grid and metronome for editing and recording. This setting is not yet sent to generative models when creating new clips." Reliable odd meter exists only in the Studio editor post-generation; in prompts, describe it in natural language ("slow waltz", "6/8 compound time") as a weak bias.

**Key-lock (PLACEBO):** Exact key-locking via a tag (e.g., `[Key: G minor]`, `[Change key to G minor]`) is unreliable/folklore — AceTagGen lists `[Change key to G minor]` among tags that fail; HookGenius notes Suno "doesn't parse parameter-based controls — the tag enters the context as text." `[Key Change]`/`[Key Modulation]` as a directional lift (usually upward) for a final chorus is a weak bias that sometimes works, but the specific target key is not honored.

### 5. GENRE-SPECIFIC IN-LYRIC BRACKET TAGS

These go in the LYRICS field as moment/section markers (NOT style-field genre names). They work best when the matching genre/instrument is also in the Style field (suno.wiki: a `[Bass Drop]` "makes no sense in an acoustic guitar solo").

**EDM / Dubstep / Bass:** `[Drop]`, `[Bass Drop]`, `[Dubstep Drop]`, `[Beat Drop]`, `[Second Drop]`, `[Build]`/`[Build-Up]`, `[Riser]`/`[White Noise Riser]`, `[Wub]`, `[Wobble Bass]`/`[Bass Wobble]`, `[Breakdown]`, `[Beat Switch]`, `[Filter Sweep]`, `[Kick Drop]`, `[Glitch]`, `[Stutter Edit]`, `[Drop to Silence]`. `[Build]`/`[Drop]`/`[Breakdown]` are well-supported in EDM contexts (Undetectr: "an EDM prompt without an explicit drop instruction will almost never produce a satisfying drop").

**Hip-hop / Trap:** `[808 Bass]`, `[Trap Hi-Hats]`, `[Hi-Hat Roll]`, `[Beat Switch]`, `[Ad-libs]`, `[Skrrt]`, `[Producer Tag]`, `[Bass Boost]`, `[Triplet Flow]`, plus ad-lib brackets in the sovietmenace format: `[adlib hey]`, `[adlib yeah]`, `[adlib whoa]`, `[adlib uh]`, `[adlib ayy]`, `[adlib boom]`, `[adlib clap]`.

**Rock / Metal:** `[Guitar Solo]`, `[Power Chords]`, `[Breakdown]`, `[Blast Beat]`, `[Double Bass]`, `[Riff]`, `[Palm Mute]`, `[Pinch Harmonic]`, `[Wall of Sound]`, `[Feedback]`, `[Chugging Riffs]`, `[Tremolo Picking]`, `[Half-Time Breakdown]`, `[Metalcore Breakdown]`. `[Breakdown]` is "essential for Metalcore/Deathcore" and "forces a tempo drop and heavy rhythm" (sunoprompt).

**Pop / Electronic:** `[Vocal Chops]`, `[Synth Solo]`, `[Key Change]`, `[Final Chorus]`/`[Final Chorus Lift]`, `[Post-Chorus Drop]`, `[Post-Chorus]`, `[Anthemic Chorus]`, `[Powerful Chorus]`.

**Jazz / Funk / Soul:** `[Sax Solo]`, `[Walking Bass]`, `[Brass Stabs]`/`[Horn Stabs]`, `[Horn Section]`, `[Scat]`, `[Call and Response]`, `[Vamp]`, `[Trading Fours]`, `[Piano Comping]`, `[Talkbox Solo]`, `[Keytar Solo]`.

**Orchestral / Cinematic:** `[Strings Swell]`/`[Strings Rise]`, `[Orchestra Hit]`, `[Choir]`, `[Timpani Roll]`, `[Crescendo]`, `[Brass Fanfare]`, `[Brass Swell]`, `[Grand Finale]`, `[Tutti]`, `[Solo Cello]`, `[Percussion Decay]`.

**Other genres:**
- Reggae/Dub: `[Skank]`, `[Dub Echo]`, `[Toasting]`, `[Riddim]`, `[Bubble Organ]`.
- Country/Folk/Bluegrass: `[Banjo Solo]`, `[Bluegrass Banjo Interlude]`, `[Fiddle Solo]`, `[Pedal Steel Solo]`, `[Harmonica Solo]`, `[Hoedown]`.
- Gospel: `[Gospel Choir]`, `[Choir: Gospel]`, `[Call and Response]`, `[Hammond Organ]`, `[Vamp]`.
- Classical: `[Cadenza]`, `[Movement II]`, `[Pizzicato]`, `[Ritardando]`, `[Tutti]`.
- Lo-fi/Ambient: `[Vinyl Crackle]`, `[Tape Hiss]`, `[Drone]`, `[Field Recording]`, `[Ambient Pad]`.
- Latin: `[Montuno]`, `[Brass Mambo]`, `[Percussion Break]`, `[Dembow]`.

---

## Recommendations

1. **Build your HTML reference tables with three columns: Bracket form (LYRICS) | Style descriptor (STYLE) | Reliability.** Default field placement: instruments/textures/genre/mood/BPM → STYLE (bracket-free); section moments + vocal delivery + dynamics + SFX → LYRICS brackets.
2. **Respect the per-section cap.** Max 2–4 bracket tags per section; lead with the section identifier, then vocal delivery, then instrumentation, then (optional) one dynamic. Use combined tags (`[Explosive Final Chorus]`) to save slots.
3. **For instruments, name 2–4 max in the Style field and specify a role** (per the Soundverse/James99 instrument guide: "Rule 1: Don't Overcrowd — Mentioning 2–4 key instruments is usually perfect. Too many can confuse Suno," then "Rule 2: Specify the Role"). Examples: "wailing electric guitar solo", "walking bass line". Reinforce any LYRICS instrument bracket with the same instrument in the Style field, or it may be ignored or sung.
4. **For SFX, prefer Style-field ambience descriptors over literal brackets, and regenerate 3–5×.** Treat human/vocal SFX as reliable and environmental/mechanical SFX as coin-flips. Flag `[hard cut]` and percentage tags as placebo in your sheet.
5. **For tempo/dynamics, set numeric BPM in the Style field (single value) and use `[Crescendo]`/`[Build]`/`[Drop]` for intensity. Do NOT rely on `[Accelerando]`/`[Ritardando]` or time-signature/key tags for generation** — handle real BPM locks and odd meters in Suno Studio (Manual BPM / grid) post-generation.
6. **Thresholds that change the approach:** if a tag is ignored after 3–5 regenerations, move it to the other field or rephrase descriptively; if output gets generic, you're under-specified (add a subgenre + one production/texture term); if it gets chaotic, you're over-stacked (trim to 4–8 total style descriptors / 2–4 brackets per section).

## Caveats
- **Source quality:** Most enumerated lists come from creator/SEO and affiliate sites (HookGenius, AceTagGen, tagasong, Jack Righteous, Musci.io, the sovietmenace and stayen GitHub repos) that claim hundreds of test generations but whose methodology is not independently verifiable. Only help.suno.com and suno.com/blog are first-party. Reliability tiers reflect community consensus, not official Suno specs.
- **Tags are probability weights, not commands** (sovietmenace master cheatsheet): "Not guaranteed commands — generate 3–4 versions." Identical prompts yield different takes.
- **No official exhaustive tag list exists.** Suno's own docs barely document the bracket system; community lists vary and include folklore. Inclusion in a list ≠ verified reliability.
- **A definitive reliable/placebo SFX tier list and an explicit key-lock verdict** were sought from the Scribd "Suno AI Meta Tags — Verification and Usage Guide," but that document is paywalled; the SFX tiers here are assembled from sunoaiwiki, AceTagGen, Stoke McToke and tagasong and should be treated as strong consensus rather than a single authoritative test.
- **v5.5 is additive.** It changed personalization (Voices, Custom Models, My Taste), not tag syntax; everything above applies to v5 and v5.5 alike, with v5.5 simply more responsive to subtle/detailed descriptors.