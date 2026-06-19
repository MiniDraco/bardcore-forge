# Introduction

This guide is for anyone who’s new to Suno or looking to level up how they use it — whether you're a casual user making fun tracks or a serious creator chasing a specific sound. You don’t need a background in music theory or songwriting to get value here. The goal isn’t to teach music from the ground up, but to give you a **working vocabulary** and some foundational concepts that help you write better prompts, get more intentional results, and avoid generic-sounding output.

We’ll cover how Suno’s AI actually works, how to shape a song’s emotional tone with **keys, modes, and time signatures**, how to write lyrics that flow well with the rhythm, and how to use **meta tags** to guide structure and instrumentation. Think of this as a creative toolbox — you can go as deep as you want, but even a few small changes to how you prompt can unlock entirely new musical directions.

---

# What Is an AI and How Does It Work?

AI might feel like magic, type something in, and a song appears, but under the hood, it’s more like a hyper-educated guess machine. Instead of composing like a human, it generates music by recognizing patterns and probabilities from the massive amount of data it was trained on.

Suno’s AI doesn’t “understand” music or emotion the way you do. It responds based on what’s most statistically likely to match your prompt, based on genre patterns, lyrical structure, and instrumental combinations it’s seen before. That’s why vague prompts often produce generic results, and why good prompting matters so much.

## Generative AI \= Pattern Matching \+ Probability Tables

Think of the AI like a weighted dice roller. It rolls based on a giant set of learned musical patterns, chord progressions, vocal styles, lyrical phrases, instrument choices, and the more commonly something appears in the training data, the more likely it is to get picked.

This is why genres like pop or country often produce similar-sounding songs unless you tell it otherwise. The AI isn’t copying, it’s just playing the odds.

## Influence Weighting: How the AI Responds to Your Prompt

Your prompt acts like a series of dials. Every word you use: “slow,” “soulful,” “gritty,” “ambient pads”, pushes the AI toward different regions of its internal probability space.

For example:

* Saying *"lo-fi trap"* pulls it toward a blend of vinyl textures and 808s.  
* Saying *"melancholic post-rock with ambient swells"* activates different chord structures, guitar effects, and progressions.

Think of prompting as shaping the gravity of the song, the more precise you are, the more the song bends toward your intended sound.

### **Why Prompts Can Sound "Samey" Without Variation**

If you don’t vary your inputs, especially for intros, keys, and structure, you’ll quickly notice songs that feel like remixes of each other. That’s because:

* Genre defaults are heavily weighted (e.g., country \= 4–5 chords, verse-chorus-verse).  
* Without specific instructions, Suno fills in gaps with *statistical averages*.  
* Even lyrics can follow overused rhyme patterns unless you change up meter, structure, or vocabulary.  
  * NEON, AABB rhyme, All of the “Ai isms” are examples of this

---

# Introduction to Music Theory for Prompting

You don’t need to be a theory wizard to make smarter prompts, but a little musical vocabulary can go a long way. Knowing how to ask for a *key*, *mode*, or *time signature* helps you avoid generic outputs and gives you more control over a song’s **emotion**, **groove**, and **style**.

Let’s break down what each of these terms actually does, and how to use them in your prompts.

## Key: Major vs Minor \= Happy vs Sad (Mostly)

**The key of a song** determines the overall emotional center, the tonal “home” the melody and harmony return to.

**Major Keys – Brighter Tones:**

* **C Major** – Pure, open, neutral, balanced (clean pop, folk, beginner-friendly)  
* **G Major** – Warm, natural, uplifting (country, Americana, classic rock)  
* **D Major** – Triumphant, regal, bold (orchestral, rock ballads, anthemic)  
* **A Major** – Bright, confident, joyful (pop rock, upbeat country, singalongs)  
* **E Major** – Brash, energetic, exciting (rock, blues, aggressive pop)  
* **B Major** – Radiant, assertive, polished (gospel, R\&B, cinematic)  
* **F Major** – Pastoral, calm, gentle (classical, singer-songwriter, soft rock)  
* **Bb Major** – Noble, rich, full (jazz, brass-heavy arrangements, classical)  
* **Eb Major** – Lush, mellow, expressive (soul, funk, ballads)

**Minor Keys – Darker Tones:**

* **A Minor** – Sad, introspective, sincere (acoustic ballads, emo, lo-fi)  
* **E Minor** – Haunting, melancholic, mysterious (metal, alt rock, cinematic)  
* **D Minor** – Dramatic, tragic, emotional (classical, folk noir, film scoring)  
* **B Minor** – Dark, brooding, poetic (indie, alt-pop, gothic rock)  
* **F\# Minor** – Tense, sorrowful, expressive (experimental, downbeat pop, EDM)  
* **C\# Minor** – Ethereal, romantic, haunting (dream pop, ambient, solo piano)  
* **G Minor** – Bold, mournful, stormy (classical, jazz, moody pop)  
* **D\# Minor** – Strange, eerie, alien (horror, avant-garde, glitch)  
  ---

## Mode: Add Personality and Genre Flavor

Modes are variations of scales that shift the emotional color even further. Suno does respond to modal prompts, especially when paired with genre cues.

Each mode is derived from the **major scale**, but starts on a different scale degree, changing the mood and feel while using the same notes.

**1\. Ionian (Major Scale)**

* **Mood:** Bright, happy, stable  
* **Feel:** Optimistic, confident  
* **Used in:** Pop, country, classical, folk, children's music  
* **Example Key Prompt:**  
   *"A cheerful pop anthem in C Ionian with bright synths and an upbeat groove."*

**2\. Dorian (Minor with lift)**

* **Mood:** Cool, soulful, moody but hopeful  
* **Feel:** A minor scale with a jazzy or gospel uplift   
* **Used in:** Funk, soul, gospel, R\&B, jazz, Celtic folk  
* **Example Key Prompt:**  
   *"A groovy soul jam in D dorian with clavinet and smooth background vocals."*

**3\. Phrygian (Minor with tension)** 

* **Mood:** Dark, exotic, tense  
* **Feel:** Intense, dramatic,  
* **Used in:** Flamenco, metal, Middle Eastern or Spanish-influenced music  
* **Example Key Prompt:**  
   *"A moody instrumental in E phrygian with nylon guitar and haunting strings."*

**4\. Lydian (Major with lift)**

* **Mood:** Dreamy, ethereal, expansive  
* **Feel:** Bright but floaty, surreal  
* **Used in:** Film scores, dream pop, progressive rock, fusion  
* **Example Key Prompt:**  
   *"A cinematic ambient track in F lydian with shimmering pads and reverb-heavy guitar."*

**5\. Mixolydian (Major with edge)**

* **Mood:** Gritty, bluesy, relaxed confidence  
* **Feel:** Like major, but more swagger,  
* **Used in:** Blues, rock, country, funk, jam band music  
* **Example Key Prompt:**  
   *"A laid-back country rock tune in G mixolydian with twangy guitars and warm organ."*

**6\. Aeolian (Natural Minor)**

* **Mood:** Sad, introspective, dramatic  
* **Feel:** Classic minor feel with emotional pull  
* **Used in:** Alt rock, ballads, EDM, cinematic, folk  
* **Example Key Prompt:**  
   *"A melancholic indie track in A aeolian with layered guitars and breathy vocals."*

**7\. Locrian (Dissonant / unstable)**

* **Mood:** Unsettling, chaotic, unresolved  
* **Feel:** Darkest mode, diminished tonic chord makes it unstable  
* **Used in:** Experimental music, avant-garde, some black metal  
* **Example Key Prompt:**  
   *"An experimental horror soundscape in B locrian with distorted drones and glitch textures."*  
  ---

## What Is a Time Signature, Really?

Time signatures define the **beat structure** of a song, how the rhythm is grouped and counted. It’s usually written as two numbers stacked like a fraction (e.g., **4/4**, **6/8**, **3/4**).

* The **top number** tells you **how many beats** are in each measure (a “bar” of music).  
* The **bottom number** tells you **what kind of note** counts as one beat (usually a quarter note \= 4, eighth note \= 8, etc.).

For example:

* **4/4** \= four quarter-note beats per measure (standard pop/rock feel)  
* **3/4** \= three quarter-note beats per measure (waltz feel)  
* **6/8** \= six eighth-note beats, felt as two groups of three (flowing or lilting)  
  ---

**4/4 – “Common Time”**

* **Feel:** Even, stable, easy to follow  
* **Used in:** Almost everything, pop, rock, hip hop, EDM, funk, etc.  
* **Notes:** Suno defaults to this unless told otherwise  
* **Prompt example:** “A pop-punk anthem in 4/4 with driving guitars and upbeat drums.”

**3/4 – “Waltz Time”**

* **Feel:** Lyrical, swaying, dance-like  
* **Used in:** Waltzes, folk, ballads, older pop  
* **Prompt example:** “A tender acoustic waltz in 3/4 with fingerpicked guitar and gentle vocals.”

**6/8 – “Compound Waltz” or “Slow Shuffle”**

* **Feel:** Flowing, lilting, more emotional than 3/4  
* **Used in:** Irish folk, soul ballads, cinematic scores, gospel  
* **Prompt example:** “A gospel soul piece in 6/8 with organ swells and call-and-response vocals.”

**2/4 – “March Time” or “Ragtime”**

* **Feel:** Snappy, driving, rigid  
* **Used in:** Military marches, polka, early country  
* **Prompt example:** “A traditional folk march in 2/4 with fiddle and snare drum.”

**12/8 – “Triplet Blues” or “Shuffle Time”**

* **Feel:** Swinging, bluesy, expressive  
* **Used in:** Classic blues, doo-wop, R\&B, soul  
* **Prompt example:** “A soulful blues track in 12/8 with walking bass and reverb-soaked vocals.”

**5/4 – “Asymmetrical Groove”**

* **Feel:** Uneven, progressive, hypnotic  
* **Used in:** Jazz fusion, prog rock, soundtracks   
* **Prompt example:** “A moody prog instrumental in 5/4 with layered synths and odd-meter drums.”

**7/8 – “Staggered Time”**

* **Feel:** Angular, complex, experimental  
* **Used in:** Math rock, Balkan folk, prog metal  
* **Prompt example:** “An experimental math rock piece in 7/8 with tapped guitar riffs and glitchy drums.”

**9/8 – “Compound Triple”**

* **Feel:** Rolling, energetic, elegant  
* **Used in:** Classical dances, some Afro-Cuban or Celtic music  
* **Prompt example:** “A lively folk dance in 9/8 with pipes and hand percussion.”  
  ---

## Tempo and Phrasing: Speed Affects Emotion

**Tempo** sets the pace of your song, but *speed doesn’t equal emotion*. A fast song can be gentle; a slow one can feel intense. It all depends on **context**, especially when paired with **time signature**.

* **60–80 BPM**: Slow, intimate, meditative.  
* **80–110 BPM**: Mid-tempo, groovy, versatile.  
* **120+ BPM**: High energy, dance, urgency.

Pair tempo with phrasing hints like:

* “slow-burning”  
* “punchy and upbeat”  
* “laid-back groove”  
* “driving rhythm”

### Tempo and Time Signature Are Connected

Tempo doesn’t act alone, the **time signature defines the beat grouping**, and that radically changes how a tempo feels.

* **240 BPM in 2/4** \= Rapid-fire, marching urgency  
   *(like drumline snare rolls or aggressive punk)*

* **240 BPM in 12/8** \= Swinging triplets, flowing and soulful  
   *(think classic blues shuffle or gospel groove)*

That’s why **120 BPM in 6/8** feels very different than **120 BPM in 4/4**, one rolls, the other marches.

---

## What Is Poetic Meter?

Poetic meter describes the **rhythmic pattern** of a line of lyrics — how **stressed (emphasized)** and **unstressed** syllables fall in sequence. Each pattern is built from repeating units called **“feet.”** Different types of feet create different feels, and some pair more naturally with certain time signatures or genres.

### **Simple Meters (1–2 stresses per foot)**

* Iamb (iambic) – da-DUM  
   Unstressed → Stressed  
   → “I walked alone beneath the sky.”  
   Smooth, natural. Great for pop, folk, ballads.

* Trochee (trochaic) – DA-dum  
   Stressed → Unstressed  
   → “Shadows fall on ruined stone.”  
   More forceful or chant-like. Good for rock, gothic, or chanty hooks.

### **Triple/Compound Meters (3 syllables per foot)**

* Anapest (anapestic) – da-da-DUM  
   Two unstressed → One stressed  
   → “In the dead of the night, I was gone.”  
   Flowing, builds momentum. Great for rap, gospel, theatrical pieces.

* Dactyl (dactylic) – DA-da-dum  
   One stressed → Two unstressed  
   → “Memories fade away from me.”  
   Rolling, dramatic. Matches well with 6/8 or 12/8 feel.

### **Advanced/Irregular Meters**

These are less common but add texture and unpredictability — especially useful in avant-garde, prog, or poetic lyrics.

* Amphibrach (amphibrachic) – da-DUM-da  
   Unstressed → Stressed → Unstressed  
   → “I walked along the ruins.”  
   Balanced yet flowing. Useful in 3/4 or 9/8 feels.

* Amphimacer (cretic) – DA-dum-DA  
   Stressed → Unstressed → Stressed  
   → “Time has gone, but still we wait.”  
   Punchy and emphatic. Works well in odd or shifting time signatures.

* Molossus – DA-DA-DA  
   Three stressed syllables  
   → “Burn that name now dead.”  
   Rare, intense. Good for chant-like moments or breakdowns.

### **Don’t Get Too Hung Up on Meter**

Poetic meter is a tool, **not a rule**. Most songwriters and poets never follow meter perfectly, and very few write in strict form. Think of meter as **a scaffold or guide**: it helps give your lines rhythm and flow, but slight variations and breaks are what make lyrics sound natural and expressive.

If you match every syllable perfectly, your lyrics can start to feel robotic or forced. It’s often better to find **a general pattern** (like iambic or anapestic) and **repeat it loosely**, allowing for the natural stresses of speech and melody to take over.

---

### **Poetic Meter Can Fight the Music**

Even if your lyrics rhyme and sound great on paper, if the **syllable stresses** land in the wrong places compared to the beat, Suno might sing them awkwardly.

**4/4 Time (Common Time)**

* **Feel:** Balanced, steady, fits most modern music  
* **Best-fit Meters:**  
  * **Iambic (da-DUM)** → “I *walked* a*lone* to*night* in *pain*”  
     *Natural, conversational – great for pop, indie, folk*  
  * **Trochaic (DA-dum)** → “*Win*ter *comes*, the *sky* turns *gray*”  
     *Punchy and lyrical – fits rock, alt-pop, ballads*  
  * **Anapestic (da-da-DUM)** → “On the *edge* of the *storm*, I was *done*”  
     *Adds bounce or swing – useful in rap, theatrical rock*  
  * **Genre Matches:** Pop, rock, indie, hip-hop, EDM, alt-country

**3/4 Time (Waltz Time)**

* **Feel:** Swaying, lyrical, circular  
* **Best-fit Meters:**  
  * **Iambic** (with triple groupings): “I *saw* her *face* in *dreams* a*gain*”  
  * **Dactylic (DA-da-dum)** → “*Winter is* falling down”  
     *Works with the triple swing feel*  
  * **Mix of 6/6 syllables per line** can maintain balance  
  * **Genre Matches:** Waltz, folk ballads, acoustic love songs, old-time country

**6/8 Time (Compound Waltz / Shuffle)**

* **Feel:** Flowing, soulful, rolling triplets  
* **Best-fit Meters:**  
  * **Anapestic (da-da-DUM)** → “In the *dark* of the *night*, I was *gone*”  
     *Perfect triplet feel – works great for soul, gospel, blues*  
  * **Dactylic (DA-da-dum)** → “*Memory* fades a*way from* me”  
     *Can feel elegant or mournful*  
  * **Genre Matches:** Blues, gospel, cinematic, soul ballads, Irish/Celtic folk

 **5/4 or 7/8 Time (Odd Meters)**

* **Feel:** Unbalanced, off-kilter, progressive  
* **Best-fit Meters:**  
  * Use **irregular syllable patterns** to match the groove  
     → “*Drifting away* / *I still feel lost*” (7 syllables, 5 syllables)  
  * Don’t force symmetry — embrace tension and asymmetry  
  * **Genre Matches:** Prog rock, math rock, avant-garde, soundtrack

# ---

 How to Use Meta Tags in Suno

Meta tags are special instructions you can insert inside the lyrics box, not the style prompt, to control how Suno structures your song, what instruments play in each section, and how transitions feel.  
They look like this:

\[Intro: ambient pads\]  
\[Verse: soft piano\]  
\[Chorus: distorted guitars, big drums\]  
\[Bridge: synth arpeggios, rising tension\]

## How to Format Meta Tags

* Always use square brackets: \[Section: instrument(s), mood\]  
* Suno understands both **section names** and **instrument descriptors**  
* Keep descriptions concise: 1–3 elements per tag is best

\[Intro: ambient pads, soft piano\]  
\[Chorus: distorted guitars, high energy\]  
\[Verse 2: acoustic guitar, mellow tone\]

## Common Sections You Can Tag

You don’t need to use all of these, but you can tag:

* \[Intro:\]  
* \[Verse:\]  
* \[Chorus:\]  
* \[Bridge:\]  
* \[Drop:\] (especially for EDM/hip-hop)  
* \[Breakdown:\]  
* \[Outro:\]

## How Tags Influence Transitions and Dynamics

Meta tags help Suno:

* Control instrument layering  
* Handle section builds and drops  
* Create clear contrasts between parts  
* Avoid flat, repetitive arrangements

## Tags help editing\!

Using meta tags breaks up the song into sections in the editor, this makes finding and selecting the part you want to change much easier.

Untagged song  
![][image1]

Tagged song  
![][image2]

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>