# Chaos Factor

> A 1–9 throttle that shifts the adventure's tone between calm and chaotic.

## When To Use

- At session start: initialize CF = **5**.
- At the end of every Scene: adjust ±1 based on PC control judgment.
- When rolling on the Fate Chart: the column for the current CF.
- When testing an Expected Scene: the d10 vs current CF (`→ engine/03-scenes.md`).
- When checking a Random Event trigger on a Fate roll: matching-digits roll where digit ≤ CF.

## Procedure

1. **Default end-of-Scene adjustment.** Decide if the PC was *in control* of the just-ended Scene:
   - Mostly in control (succeeded, made progress, set the agenda) → **CF −1**.
   - Mostly out of control (forced into reaction, suffered losses, surprised) → **CF +1**.
   - Borderline → judgment call; small successes inside a chaotic Scene can still tip toward "out of control."
2. **Clamp** the result to [1, 9]. Modifications that would exceed the bounds are ignored.
3. **Effects of CF on subsequent play:**
   - **Higher CF** → higher chance of Yes on Fate Questions; more frequent Random Events; more often Scenes start non-as-Expected.
   - **Lower CF** → tone calms; No answers more common; Scenes start as Expected more often; in low-control situations, "No" tends to be bad news for the PC.
4. **Track in the Adventure Journal** alongside each Scene's summary (`→ sheets/adventure-journal.md`).

## Decision Tree

- "Was the PC in control?"
  - Did they meaningfully drive the Scene's outcome → **−1**.
  - Did they react, retreat, or get blindsided → **+1**.
  - Survived an ambush by improvising a magical reveal → likely **+1** (the reveal was out of their control).
- "Should I use a different CF rule?"
  - Want pendulum / mean-reverting tone → **Revert Toward The Mean** (`→ engine/08-variations.md`): CF goes UP after success, DOWN after failure.
  - Want random tone shifts → **Random Chaos**: roll d10; ≤ CF → −1, > CF → +1.
  - Want CF to influence Fate Questions less → switch to Mid/Low/No-Chaos Fate Charts (`→ tables/fate-chart-variants.md`).

## Failure modes

- **Forgetting to adjust CF** — the system's primary throttle freezes; play feels flat.
- **Always adjusting toward 5** — defeats the snowball dynamic. Let CF drift up during chaos and down during calm.
- **Treating CF as a per-Question dial** — adjust *between* Scenes, not within them.
- **Ignoring the [1, 9] clamp** — out-of-range adjustments simply don't apply.
- **Using CF when replacing RPG mechanics with Fate Questions** — for rule-replacement Questions, treat CF as 5 (`→ engine/01-fate-questions.md` Failure modes).

## Cross-refs

→ tables/fate-chart.md
→ tables/fate-chart-variants.md
→ engine/01-fate-questions.md
→ engine/02-random-events.md
→ engine/03-scenes.md
→ sheets/adventure-journal.md
→ rules/02-fate-questions.md
→ rules/04-scenes.md
→ engine/08-variations.md
