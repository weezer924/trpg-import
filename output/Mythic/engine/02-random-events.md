# Random Events

> Mythic's mechanism for surprise. An Event Focus + a Meaning roll, interpreted through Context.

## When To Use

- Triggered automatically:
  - Fate Chart roll with matching digits, digit ≤ CF (`→ engine/01-fate-questions.md` step 5).
  - Scene test produced an Interrupt Scene (`→ engine/03-scenes.md`) — generate as if a Random Event.
- Triggered by you:
  - First Scene generation from scratch (`→ engine/03-scenes.md` §First Scene).
  - Discovery Check / Flashpoint / Conclusion in Thread Progress Track (`→ engine/08-variations.md`).
  - Keyed Scene Event with Current Context Focus (`→ engine/08-variations.md`).

## Procedure

1. **Note the Context.** Everything currently happening in the Scene + the originating Question (if any) is part of the Event's interpretive backdrop.
2. **Determine Event Focus.**
   - Default: roll d100 on `→ tables/random-event-focus.md`.
   - Choose instead of roll when: Context strongly implies the Focus, current Scene is already crowded, you have a budget of "1 choice per 5 Scenes" and want to use it (`→ rules/03-random-events.md` §When To Choose The Focus).
   - If the rolled Focus calls for an empty list (no Threads / no Characters yet) → use **Current Context** instead.
3. **Resolve list-based Focuses** (NPC Action, NPC Negative/Positive, Move Toward/Away/Close A Thread):
   - Roll on the relevant List (`→ engine/04-threads-and-characters.md` §Rolling On A List).
   - On a blank line → **Choose** an existing element OR reroll.
   - "But they're not here" — the Event involves the rolled NPC even if they're not physically present (radio chatter, evidence, news; see `→ rules/03-random-events.md` §But, They're Not Here).
4. **Roll Event Meaning.** Pick a Meaning Table fitting the Focus and roll twice:
   - **Actions** (`→ tables/meaning-actions.md`) for verbs, behaviors, doings.
   - **Descriptions** (`→ tables/meaning-descriptions.md`) for adjectives, qualities, appearance.
   - **Elements** (`→ tables/meaning-elements.md`) for themed nouns — pick a theme matching the Focus (Characters, Locations, Powers, Names, Cryptic Message, etc.).
5. **Interpret** Focus + Meaning + Context as one synthesis (`→ engine/07-interpretation-principles.md`). Narrate the Event into the Scene.

## Decision Tree

- **What Focus to choose (when not rolling):**
  - Adventure stalled or aimless → **Move Toward A Thread**.
  - Already in chaos, more chaos would muddle → **Current Context** (Event explains what's already happening).
  - PC has been struggling → **PC Positive**.
  - PC needs a fresh challenge → **Move Away From A Thread** or **PC Negative**.
  - Want to thin a bloated Threads List → **Close A Thread**.
  - Want to expand the cast → **New NPC**.
  - Want a quiet beat or foreshadowing → **Ambiguous Event**.
- **Which Meaning Table to use:**
  - Verb-heavy / "what's happening" → Actions.
  - Visual / atmospheric → Descriptions.
  - Themed and the theme exists → matching Elements sub-table (e.g., Spell Effects, Cryptic Message, Names, Smells).
  - Stuck after one roll → re-roll on a different table for a second word pair (Mining For Meaning).
- **Interpretation won't come:**
  - Try connectors: word-1 *of* word-2; word-1*ly* word-2; word-1 *and* word-2; word-1 *but* word-2 (`→ rules/04-scenes.md` §Meaning Word Connectors).
  - Pose a clarifying Fate Question: "Does this Event mean X?"
  - Last resort: **I Dunno Rule** — drop the Event and continue. Use sparingly.

## Failure modes

- **Treating the Focus literally and the Meaning literally as separate constraints** — they're inputs to one synthesis, not boxes to tick.
- **Forcing a strict literal reading** — "Attack + Needs" doesn't have to be "attacking something it needs"; it can be a robot attacking a locker for an energy cell. Stretch is fine if the words are recognizable in the result.
- **Generating a Random Event during an in-progress Random Event** — the second-tier roll is allowed for clarification (Mining For Meaning), but don't cascade indefinitely.
- **Skipping the originating Fate Question's Yes/No** — the Event layers on, it doesn't replace; resolve both.
- **Over-using "I Dunno"** — distinguish "stuck for 30 seconds" from "stuck for genuinely no fit." Default is to commit to the first workable reading.

## Cross-refs

→ tables/random-event-focus.md
→ tables/meaning-actions.md
→ tables/meaning-descriptions.md
→ tables/meaning-elements.md
→ engine/01-fate-questions.md
→ engine/03-scenes.md
→ engine/04-threads-and-characters.md
→ engine/07-interpretation-principles.md
→ rules/03-random-events.md
→ examples/02-wutwo-labs.md
