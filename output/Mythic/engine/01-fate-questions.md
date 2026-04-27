# Fate Questions

> The core query mechanism. Anything you'd ask a live GM, you ask Mythic with a Fate Question.

## When To Use

- Player faces an in-fiction uncertainty whose answer would reshape the next moment.
- An NPC's reaction is in doubt and matters.
- A specific detail (door locked? guard hostile?) needs a binary answer to proceed.
- An expectation feels uncertain enough to test.

**Don't use when** the answer is already obvious from Context, or when the chosen RPG's mechanics already resolve it (combat hits, skill checks). Default to expectations; ask only when stuck.

## Procedure

1. **Phrase the Question.** Yes/No only. Action-oriented (Yes = the more interesting/active outcome). Stay within what the PC could plausibly know.
2. **Pick Odds** based on Context: Certain / Nearly Certain / Very Likely / Likely / 50/50 / Unlikely / Very Unlikely / Nearly Impossible / Impossible. If you have no idea, **50/50**.
3. **Cross-reference** Odds × current Chaos Factor on `→ tables/fate-chart.md`. Cell shows `<Exc-Yes max> / <Yes max> / <Exc-No min>`. (For 2d10 alternative, see `→ tables/fate-check-modifiers.md`.)
4. **Roll 1d100.**
   - ≤ left number → **Exceptional Yes** (intensify the Yes)
   - ≤ middle number → **Yes**
   - ≥ right number → **Exceptional No** (opposite of Yes, or No intensified)
   - otherwise → **No** (next most expected outcome)
   - Cell shows `X` → that tier is unreachable at these Odds × CF.
5. **Check for Random Event.** If both digits match (11, 22, …, 99) **and** that single digit ≤ current CF, a Random Event fires (`→ engine/02-random-events.md`). Apply the Yes/No first, then layer the Event.
6. **Interpret** within Context (`→ engine/07-interpretation-principles.md`). Narrate. Continue play.

## Decision Tree

- "What Odds?" — judge from Context: how many in-fiction reasons point toward Yes vs No.
  - Several reasons toward Yes, few toward No → **Likely** to **Very Likely**.
  - Roughly balanced or genuinely unsure → **50/50**.
  - Several reasons against Yes → **Unlikely** down to **Nearly Impossible**.
  - Use **Certain** / **Impossible** when an answer would be a foregone conclusion *but* you want to leave room for a surprise.
- "Two answers tugging at me, I want clarification" — ask **one** follow-up Fate Question, max two. Then commit to interpretation.
- "I'm replacing an RPG rule with this Question" — treat CF as 5 (ignore current CF) and treat Exceptional results as regular unless the rule has degrees of success/failure.
- "This Question would close a storyline if it goes wrong" — that's a tension-building Question; ask it. Don't ask narrative-killing Questions whose No just ends a plot.

## Failure modes

- **Asking too many Questions for the same detail** — pick the broadest Question; let expectations fill the rest. Hard cap: 2 Questions per detail.
- **Phrasing as desire instead of expectation** — "Do I look down and see a +5 sword?" has no Context basis. Ask "Do I find anything useful?"
- **Re-rolling after a result you don't like** — never. Accept the answer; reverse-engineer the cause from Context (P-01).
- **Asking Questions outside PC scope** — "Is the place haunted?" before the PC has any reason to suspect → Player learns what the PC shouldn't. See `→ engine/08-variations.md` §Character vs Player Knowledge.
- **Ignoring Exceptional results** — they're load-bearing. Yes intensifies; No flips to opposite (or intensifies the next-most-expected).

## Cross-refs

→ tables/fate-chart.md
→ tables/fate-question-answers.md
→ tables/fate-check-modifiers.md
→ engine/02-random-events.md
→ engine/05-chaos-factor.md
→ engine/07-interpretation-principles.md
→ rules/02-fate-questions.md
→ examples/01-henny-in-z-land.md
