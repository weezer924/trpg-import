# Core Loop

> The end-to-end cycle for running a Mythic solo session. Load first at session start.

## When To Use

- At the start of every Mythic session — load this and `→ engine/09-session-protocol.md` together.
- As the outer loop governing when to invoke other engine/ files mid-session.
- Whenever you lose the thread of "what comes next" — return here to re-orient.

## Procedure

1. **Scene Setup.** If this is the First Scene, skip the test (`→ engine/03-scenes.md` §First Scene). Otherwise:
   1. Form an Expected Scene from the PC's intent.
   2. Roll d10 vs current Chaos Factor → Expected / Altered / Interrupt.
2. **Play the scene.**
   1. Improvise based on expectations and prior Context.
   2. At each uncertainty: invoke `→ engine/01-fate-questions.md`.
   3. On a Fate Chart roll with matching digits where the digit ≤ CF: a Random Event fires (`→ engine/02-random-events.md`) — answer the original Question first, then layer the Event.
   4. For NPC actions/reactions: invoke `→ engine/06-npc-behavior.md`.
   5. For named details when expectation is empty: roll on `→ tables/meaning-actions.md` / `tables/meaning-descriptions.md` / `tables/meaning-elements.md` and synthesize per `→ engine/07-interpretation-principles.md`.
3. **End of Scene Bookkeeping.**
   1. Update Threads/Characters Lists (`→ engine/04-threads-and-characters.md`).
   2. Adjust Chaos Factor (`→ engine/05-chaos-factor.md`).
   3. Record the Scene in the Adventure Journal (`→ sheets/adventure-journal.md`).
4. **Loop to step 1** for the next Scene, OR conclude the session per `→ engine/09-session-protocol.md`.

## Decision Tree

- Scene boundary reached → run step 1 (Scene Setup).
- Mid-scene uncertainty → Fate Question (`→ engine/01-fate-questions.md`).
- Fate Chart roll has matching digits, single digit ≤ CF → Random Event (`→ engine/02-random-events.md`).
- NPC's next action matters and isn't obvious → NPC Behavior (`→ engine/06-npc-behavior.md`).
- Need a detail and have no expectation → Meaning roll (`→ engine/07-interpretation-principles.md` for synthesis).
- Adventure has stalled with no clear next Scene → automatic Interrupt (`→ engine/03-scenes.md` §Automatic Interrupt).
- Player wants narrative override → Variations (`→ engine/08-variations.md`: Keyed Scenes / Peril Points / Thread Progress Track).

## Failure modes

- Skipping CF updates after a Scene → tempo flattens; the system loses its primary throttle.
- Asking Fate Questions for things you can simply decide → undermines expectation-led play (`→ engine/07-interpretation-principles.md` P-01).
- Treating Random Events as separate from the original Fate Question → loses the layered Yes/No + Event dynamic.
- Forgetting to add prominent Threads/Characters after a Scene → next Random Event rolls on stale lists.
- Maxing out Threads with low-stakes goals → important Threads compete with noise on every list roll.

## Cross-refs

→ engine/01-fate-questions.md
→ engine/02-random-events.md
→ engine/03-scenes.md
→ engine/04-threads-and-characters.md
→ engine/05-chaos-factor.md
→ engine/06-npc-behavior.md
→ engine/07-interpretation-principles.md
→ engine/08-variations.md
→ engine/09-session-protocol.md
→ sheets/adventure-journal.md
