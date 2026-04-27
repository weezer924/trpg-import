# Scenes

> The structural unit of a Mythic adventure: First / Expected / Altered / Interrupt.

## When To Use

- At the start of every Scene after the First.
- When the current Scene's main action resolves and you need the next.
- When stuck for "what's next" and need a forced reset (Automatic Interrupt).

## Procedure

### First Scene

1. Pick a generation method:
   - **Inspired Idea** — the Player invents the opening directly.
   - **Random Event** — roll Event Focus (`→ engine/02-random-events.md`); ignore empty-list Focuses, default to Current Context. Roll Meaning. Interpret as the opening.
   - **Meaning Tables** — skip Focus; roll word pairs on `→ tables/meaning-actions.md` / `tables/meaning-descriptions.md` / `tables/meaning-elements.md` directly until the opening forms.
   - **4W** — roll Who (Characters Elements), What (Actions), Where (Locations Elements), Why (Actions). Combine.
2. **No Chaos Factor test** for the First Scene; it happens as conceived.
3. Optionally seed Threads/Characters Lists from the opening (`→ engine/04-threads-and-characters.md`).

### Subsequent Scenes (Expected → Altered / Interrupt)

1. **Form the Expected Scene** — what the PC plans / what most plausibly happens next.
2. **Test against CF.** Roll d10 vs current Chaos Factor.
   - Roll **>** CF → **Expected Scene** runs as imagined.
   - Roll **≤** CF and **odd** → **Altered Scene**.
   - Roll **≤** CF and **even** → **Interrupt Scene**.
3. **Resolve the Scene type:**

#### Altered Scene

Begins like the Expected Scene but with one shift. Pick whichever method fits:
- **Next Expectation** — the second-most-likely opening.
- **A Tweak** — change one element (NPC, activity, object, location).
- **Fate Question** — "Is the alteration X?" Use Yes/No/Exc to settle ambiguity.
- **Meaning Tables Inspiration** — roll a word pair on `→ tables/meaning-actions.md` / `meaning-descriptions.md` / matching `meaning-elements.md` theme.
- **Scene Adjustment Table** — roll d10 on `→ tables/scene-adjustment.md` for one mechanical change (Add/Remove Character/Object, Increase/Reduce Activity, or Make 2 Adjustments). Reroll if result doesn't apply.

#### Interrupt Scene

Generated like a Random Event:
1. Roll Event Focus (`→ tables/random-event-focus.md`) or choose.
2. Roll Meaning per the Focus.
3. Interpret as a wholly new Scene that derails the Expected one. Connect it back to the prior Scene's Context for continuity.

### End of Scene

1. Decide it's over (Interest, Time/Location, Narrative Shift, Mood, or Automatic Interrupt — see `→ rules/04-scenes.md` §Beginning And Ending Scenes).
2. Run Bookkeeping: Lists (`→ engine/04-threads-and-characters.md`), CF (`→ engine/05-chaos-factor.md`), Journal (`→ sheets/adventure-journal.md`).

### Automatic Interrupt

When stuck on what's next: skip the CF test. Make the next Scene an Interrupt directly. Optional: skip the Focus roll too and use **Move Toward A Thread** to force forward momentum.

## Decision Tree

- "How do I end this Scene?" — Interest (default) ends when the interesting moment resolves; Time/Location ends on jump; Narrative Shift ends on focus change; Mood ends when you feel like it.
- "Altered or Interrupt?" — use the d10 parity from the test, not preference. Odd = Altered (close to expected); Even = Interrupt (anything goes).
- "Which Altered method?" — Next Expectation if obvious; Tweak if Expected has clear elements to change; Fate Question if torn between options; Meaning Tables / Scene Adjustment if no idea.
- "Adventure feels stuck after several Scenes" — Automatic Interrupt with Move Toward A Thread.

## Failure modes

- **Testing the First Scene against CF** — don't. First Scenes are exempt.
- **Interpreting Altered as "completely different"** — Altered keeps the Expected's bones; one element shifts. If everything changes, that's an Interrupt.
- **Disconnecting an Interrupt from prior Context** — even surprising scenes must land in the same world the previous Scene built. Tie back to ongoing Threads / recent NPCs / current location.
- **Rolling Scene Adjustment and ignoring impossible results** — reroll if the result has no target (Remove A Character with no NPCs in the Expected Scene).
- **Forgetting to Bookkeeping at end of Scene** — CF and Lists drive the next Scene's test; skipping them silently breaks the loop.

## Cross-refs

→ tables/scene-adjustment.md
→ tables/random-event-focus.md
→ engine/02-random-events.md
→ engine/04-threads-and-characters.md
→ engine/05-chaos-factor.md
→ sheets/adventure-journal.md
→ rules/04-scenes.md
→ examples/03-guardian-of-chosen-one.md
→ examples/04-the-big-example.md
