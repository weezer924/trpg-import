---
source: pdf
chaos-focus: [scenes, scene-adjustment, expected-altered-interrupt, threads, characters-list, chaos-factor, bookkeeping]
length-turns: ~20
length-scenes: 4
---

# The Big Scenes Example: Guardian Of The Chosen One

> Source: *Mythic Game Master Emulator 2nd Edition*, p.116-123.
> Demonstrates Mythic's Scene structure end-to-end: First Scene → Expected Scene → Altered Scene → Interrupt Scene, with full Threads / Characters list management and CF transitions.

## Setup

PC: **Lennz**, hunter and wilderness expert. Hired by a mountain village to escort **the Chosen One**, a child prophesied to have great powers, to a hilltop monastery through rugged terrain Lennz knows well.

Adventure seed: rolled "Public" + "Require" on Plot Twists Elements; interpreted as a public village requiring Lennz to perform the protect-and-deliver task.

**Starting Chaos Factor:** 5

**Initial Threads:** Deliver the Chosen One
**Initial Characters:** The Chosen One; Villagers; Mountains

## Scene 1: First Scene (no Chaos Factor test)

> First Scenes don't roll for Expected/Altered/Interrupt — they happen as planned.

Setup: Lennz and the boy begin trek through the mountains. Terrain near village is gentle; they walk and chat.

**Q:** "Can we use horses?" → **No**.
**Q:** "Is the terrain near the village rough?" → **Exceptional No**. (Confirms easy first leg.)

The Player wants Lennz to chat with the boy but doesn't know what he'd say.
**Meaning roll (Character Conversations):** "Careless" + "Mysterious" → boy is very trusting (answers freely) but knows little about his own past.

**Q:** "Does the Chosen One have a proper name?" → **Yes**.
**Meaning roll (Names):** "Nn" + "Fi", then more rolls for "Wr" + "Nature" → **Ninfee Wryrock**.

There's a strange mark on his arm — apparently what identified him as the Chosen One. He doesn't know the prophecy in detail.

**End of Scene 1:**
- CF transition: Lennz was in control → **CF 5 → 4**
- Lists update: prominent elements were "Chosen One", "Mountains", "Deliver the Chosen One" → add another instance of each.
- No new Threads or Characters.

State after Scene 1:
```
Threads:    Deliver (×2)
Characters: Chosen One (×2), Villagers, Mountains (×2)
```

## Scene 2: Expected Scene (rolled, succeeds)

**Expected Scene plan:** make camp at nightfall; next day they encounter more treacherous terrain.
**Test:** d10 → **8**. Exceeds CF 4 → **Expected Scene happens as envisioned**.

**Q:** "Do we run into any difficult terrain today?" → **Yes**.
**Q:** "Does Ninfee have difficulty?" → **Yes**. (Lennz helps him.)

A later Fate Question generates a Random Event.
**Event Focus:** "Move Away From A Thread" (only one Thread — no roll needed).
**Meaning roll (Actions):** "Block" + "Project". Player isn't sure → poses as Fate Question.
**Q:** "Do we encounter orcs?" → **Yes**. Interpretation: an orc warband moving through the mountains, posing a danger to their progress.

Lennz pulls Ninfee behind a boulder before they're spotted. They move cautiously the rest of the day.

**End of Scene 2:**
- CF transition: introduction of orcs forced a course change → out of control → **CF 4 → 5**
- Lists update: add Thread "Avoid the orcs"; add Character "Orc warband". Repeat "Deliver" and "The Chosen One" — both now at **3 instances (max)** so they cap.

State after Scene 2:
```
Threads:    Deliver (×3, capped), Avoid orcs (×1)
Characters: Chosen One (×3, capped), Villagers, Mountains (×2), Orc warband (×1)
```

## Scene 3: Altered Scene (Expected fails the test)

**Expected Scene plan:** Lennz knows of another nearby village; head there for help.
**Test:** d10 → **3**. Odd number within CF 5 → **Altered Scene**.

**Player's nearest alternative:** they'll meet the orc warband instead.

**Q:** "Do we encounter the orcs the next day?" → **No**. (Player interprets: encounter happens that night while they camp.)
**Q:** "Do the orcs surprise attack us?" → **Yes**.

Combat plays out in the chosen RPG. To guide tactics:
**Q:** "Do the orcs focus on Lennz?" → **Yes** (he's the bigger threat).

**NPC Behavior loop (per round):** "Do the orcs continue with their current action?"
- Round 1: Yes
- Round 2: Yes
- Round 3: Yes
- Round 4: **No** → one orc breaks off toward Ninfee.

Lennz yells for Ninfee to run.
**Q:** "Does Ninfee run?" → **No, with a Random Event**.
**Event Focus:** NPC Action.
**Picking the NPC:** d4 → 3 → second populated section of Characters List; d10 → 2 → "**The Chosen One**".
**Meaning roll (Actions):** "Open" + "Power". Given prophecy Context → Ninfee unleashes a burst of raw magical defense; the attacking orc is hurled back.

**Q:** "Do the orcs flee?" → **Yes**.
**Q:** "Does Ninfee seem surprised by what he did?" → **Yes**.

**End of Scene 3:**
- CF transition: survived ambush, but Ninfee's surprise display was out of Lennz's control → **CF 5 → 6**
- Lists update: "Deliver" already maxed (no add). Add another "Avoid the orcs". Add another "Orc warband".

State after Scene 3:
```
Threads:    Deliver (×3, capped), Avoid orcs (×2)
Characters: Chosen One (×3, capped), Villagers, Mountains (×2), Orc warband (×2)
```

## Scene 4: Interrupt Scene (Expected fails on even number)

**Expected Scene plan:** pack up and move while it's still dark; cover tracks; don't experiment with Ninfee's powers yet.
**Test:** d10 → **4**. Even number within CF 6 → **Interrupt Scene** (something unexpected).

**Interrupt Focus roll:** "PC Negative".
**Meaning roll (Actions):** "Hinder" + "Weather" → a snowstorm rolls in. Lennz must stay ahead of orcs while contending with cold.

They trudge through worsening snow. By dawn they need shelter.

**Q:** "Does Lennz spot a cave?" → Odds **Very Unlikely**, roll → **Exceptional No**.

> Player interprets Exceptional No as the *opposite* of a cave — or a more intense next expectation. They settle on "sign of life."

**Meaning roll (Descriptions):** "Slowly" + "Dirty" → a column of smoke slowly drifting up, as from a campfire.

Approaching cautiously, they reach the ridge and look down on a small mountain village.

**Q:** "Is it the orcs?" → Odds **50/50** (no clue) → **No**. (So: a real village.)
**Q:** "Do they look capable?" → **Exceptional Yes**. (Well-equipped against cold + fighters among them.)

Two spear-wielding warriors approach. On seeing Ninfee, their demeanor shifts to welcome — they recognize him.

**Q:** "Do they recognize Ninfee?" → **Yes**.
**Q:** "Are they aware of the warband?" → **Yes**. (They've been fending off raiders for months; willing to help defend the boy.)

**End of Scene 4:**
- CF transition: lucky break, allies found → in control → **CF 6 → 5**
- Lists update: add "Avoid the orcs" → reaches max (×3); add "Mountains" (storm acted against them); add "Villagers".

State after Scene 4:
```
Threads:    Deliver (×3, capped), Avoid orcs (×3, capped)
Characters: Chosen One (×3, capped), Villagers (×2), Mountains (×3), Orc warband (×2)
```

## Outcome / Scene Summary Table

| Scene | Type            | d10 / CF in | Description                                        | CF out |
|------:|-----------------|-------------|----------------------------------------------------|-------:|
|     1 | First (no test) | — / 5       | Lennz begins journey; gets to know Ninfee.         |      4 |
|     2 | Expected        | 8 / 4       | A roving orc warband is spotted.                   |      5 |
|     3 | Altered         | 3 / 5       | Orcs ambush at camp; Ninfee displays raw power.    |      6 |
|     4 | Interrupt       | 4 / 6       | Snowstorm; discover a friendly mountain village.   |      5 |

## Lessons (for engine/07-interpretation-principles)

- **First Scene** is exempt from the Chaos Factor test — establish, don't randomize.
- d10 vs CF (1–CF inclusive triggers non-Expected outcomes): **odd within range = Altered**, **even within range = Interrupt**, **outside CF range = Expected**.
- An **Altered Scene** uses the player's *next most plausible* expectation, not random invention. (Heading to village → instead the orcs catch up.)
- An **Interrupt Scene** is determined by an Event Focus + Meaning roll, treating the Scene start as a Random Event.
- **Threads/Characters lists cap at 3 instances per element** — that cap is the only mechanism limiting how skewed list-rolls become.
- CF transitions follow a "did the PC have control of this Scene" judgment — surviving an ambush ≠ being in control if it forced an unplanned magical reveal.
- **Exceptional results can flip to "opposite of expectation"** as well as "intensify expectation" — Exceptional No on "spot a cave" became the opposite of a cave (a sign of human life).
- A clarifying Fate Question is a legitimate way to resolve ambiguous Meaning rolls — "Block + Project" became "Do we encounter orcs?" rather than forcing a literal interpretation.
- NPC Behavior Table loops sustain combat without per-round intent invention; one round's "No" is enough to introduce a new tactic.
- "Move Away From A Thread" Event Focus with only one Thread on the list skips the roll — applies the focus directly.
