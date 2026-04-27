# NPC Behavior

> How to decide what an NPC does next, from one-line passers-by to round-by-round combat.

## When To Use

- An NPC's next action is in doubt and matters to the Scene.
- Combat / chase / negotiation — round-by-round behavior decisions for an active NPC.
- A new NPC is introduced and needs an initial action.
- Conversation: deciding what the NPC says (tone + intent, not exact words).

**Skip** for background NPCs whose actions are obvious or irrelevant — let expectation handle them.

## Procedure

Pick whichever path matches your level of commitment:

### Expectation (default)

If the NPC's action is obvious in Context, just narrate it. ("The barkeeper comes over to take your order.")

### Discovering Meaning

If you have no expectation, roll a Meaning word pair on the most fitting table:
- **Actions** — generic doings.
- **Characters Elements** — broad behaviors.
- **Animal Actions** — feral / out-of-control creatures.
- **Character Actions, Combat** — fights.
- **Character Actions, General** — non-combat NPC choices.
- **Character Conversations** — what they say / how.

Interpret the pair as the NPC's action. Don't agonize for the perfect literal match — broad reading is fine (`→ engine/07-interpretation-principles.md`).

### Fate Question (preferred for tense moments)

Frame an expected behavior as a Fate Question, assign Odds, roll. Apply the **NPC Behavior Table** (`→ tables/npc-behavior.md`):

| Result          | Interpretation                                                                                                    |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Yes             | NPC does what you expected, or continues their ongoing action.                                                    |
| Exceptional Yes | Expected/ongoing action, but more intense.                                                                        |
| No              | Next most expected behavior. If unclear, roll a Meaning Table for inspiration.                                    |
| Exceptional No  | Opposite of expectation, or next-most-expected intensified. Meaning Table if stuck.                               |
| Random Event    | Add a second action layered on top: roll Meaning for an additional behavior. Combine with the original if it fits; otherwise treat as a sequel beat. |

### Round-by-round combat shortcut

Once an NPC has taken an action you're happy with, ask **"Does the NPC continue with their current action?"** each round. Yes = same; No = pick the next-most-expected change (often a tactical pivot — break off, retreat, switch target). This sustains combat without inventing intent each round.

### Conversations

Pick a tone/intent first, then phrase the words.
- Use Fate Questions to test "does the NPC say X?" — Yes/No tells you tone.
- Roll on **Character Conversations** Elements when stuck for content.
- Don't randomize every line; the dice supply intent, you supply words.

### Social Skills (chosen RPG)

If the chosen RPG has Persuasion / Diplomacy / etc., resolve the skill roll first; the result becomes Context that shifts subsequent Fate Question Odds (`→ engine/01-fate-questions.md`). E.g., a great Persuasion roll might shift the Odds from 50/50 to Very Likely on "Does she help us?"

## Decision Tree

- "Important action, you have a guess" → Fate Question with Odds matching your confidence.
- "Important action, no guess" → Meaning roll.
- "Background action, obvious" → narrate from expectation.
- "Round 5 of combat, no time" → "Does the NPC continue?" loop.
- "NPC must speak, line content matters" → tone/intent via Fate Question or Meaning roll, then write the line.
- "NPC was rolled by a Random Event but they aren't physically here" → the Event involves them indirectly (`→ engine/04-threads-and-characters.md` §But They're Not Here).

## Failure modes

- **Rolling for every NPC action** — slows play to a crawl. Reserve dice for important moments.
- **Treating Exceptional Yes as just Yes** — it's "Yes, with more intensity." Crank the dial.
- **Treating Exceptional No as just No** — it can flip to *opposite* of expected, not just "next most expected."
- **Letting a Meaning roll dictate too literally** — Meaning words are seeds; the resulting action must still fit the Scene.
- **Asking too many Fate Questions in one combat round** — choose one (continue? switch target? flee?) and run with the answer.

## Cross-refs

→ tables/npc-behavior.md
→ tables/meaning-actions.md
→ tables/meaning-elements.md
→ engine/01-fate-questions.md
→ engine/02-random-events.md
→ engine/04-threads-and-characters.md
→ engine/07-interpretation-principles.md
→ rules/04-scenes.md
→ examples/03-guardian-of-chosen-one.md
