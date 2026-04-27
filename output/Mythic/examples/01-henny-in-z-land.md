---
source: pdf
chaos-focus: [fate-questions, interpretation, odds-selection, exceptional-results]
length-turns: 4
length-scenes: 1
---

# The Big Fate Question Example: Henny In Z Land

> Source: *Mythic Game Master Emulator 2nd Edition*, p.32-35.
> Demonstrates the full Fate Question loop: Odds selection → Fate Chart → roll → interpret → narrate → iterate.

## Setup

PC: **Henny Lassiter**, a barista turned zombie-apocalypse survivor. Companion: **Malcolm**, rescued earlier. They've made it into a forest in search of shelter, staying alert for zombies. Played with the Player's favorite end-of-the-world RPG; Mythic acts as GM.

Starting Chaos Factor: **4**.

## Play

### Turn 1 — Watching for movement in the forest

**Question:** "Do I see any movement in the trees ahead?"
**Odds:** Very Unlikely (deep in forest)
**Chaos Factor:** 4
**Fate Chart chance of Yes:** 15%
**Roll:** 50
**Result:** No
**Interpretation:** The coast is clear. Henny and Malcolm continue on.

### Turn 2 — Looking for useful supplies

After about an hour of walking on the city outskirts.

**Question:** "Do we find anything useful along the way?"
**Odds:** Likely (city outskirts, walked a while)
**Chaos Factor:** 4
**Fate Chart chance of Yes:** 50%
**Roll:** 33 (a 3 and a 3 — double digits → check for Random Event; 3 ≤ CF 4, so an Event fires)
**Result:** Yes + Random Event
**Interpretation:** Player first considers the expected Yes — random supplies dropped by people fleeing the city. The Random Event (rolled per Ch3 rules, not detailed here) is interpreted as Henny and Malcolm coming across a seemingly abandoned encampment. Synthesis: they discover an abandoned camp in the woods — fire remnants, a tattered backpack, a torn tent — and dig up a few cans of food (the "useful" find for the original Question). They haven't eaten in 24 hours, so this matters.

> **Sidebar (p.32):** When interpreting the Yes, the Player chose to run with their first expectation rather than ask a follow-up Fate Question like "Do we find food?" Both approaches are valid; commit to the one that fits the moment.

### Turn 3 — Searching for shelter before nightfall

The day is wearing on; they need shelter before temperatures drop.

**Question:** "Do we find shelter in the woods before night?"
**Odds:** Likely (hours of walking ahead)
**Chaos Factor:** 4
**Fate Chart chance of Yes:** 50%
**Roll:** 9
**Result:** Exceptional Yes (within lower 20% of Yes range; for 50% Odds that's ≤10)
**Interpretation:** As the sun dips, Henny and Malcolm spot a **two-story house** — a full domicile — nestled deep among the trees. Not just shelter; potentially supplies and goods inside.

### Turn 4 — Trying the door

They cautiously approach, wary of zombies or other survivors.

**Question:** "Is the door locked?"
**Odds:** 50/50 (Player unsure: nice house in evacuated area cuts both ways)
**Chaos Factor:** 4
**Fate Chart chance of Yes:** 35%
**Roll:** 92
**Result:** Exceptional No (intensify the answer)
**Interpretation:** Not only is the door unlocked — the interior is **in excellent shape**. Well-stocked with food and goods; running water and electricity still work. Whoever lived here evacuated quickly, taking only essentials. Henny and Malcolm appear to be the first to find the place since the outbreak.

> **Sidebar (p.33):** 50/50 Odds work for "about even" chances **and** for "I have no idea what the Odds should be."

## Outcome

Scene resolves with the PCs safely inside a stocked, intact house — a windfall outcome built from one Likely Yes (find supplies) + one Exceptional Yes (find shelter) + one Exceptional No (door locked) chained together. CF was held at 4 throughout (no scene-end transitions in this excerpt; CF rules in `../engine/05-chaos-factor.md`).

## Lessons (for engine/07-interpretation-principles)

- The Player picks Odds from in-fiction Context, not from a sense of "what should happen narratively."
- Double-digit rolls within a Yes/No band still trigger Random Event checks (3 ≤ CF).
- An Exceptional result intensifies in the direction the answer is already pointing — Yes amplifies the Yes; No amplifies the No.
- 50/50 is the legitimate fallback when Context is ambiguous; don't stall trying to compute "real" Odds.
- A Yes can be interpreted from the most likely real-world cause (refugees dropped supplies) before any randomization adds flavor.
