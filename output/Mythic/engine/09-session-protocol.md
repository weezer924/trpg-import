# Session Protocol

> AI-runtime instructions for starting, running, and ending a Mythic solo session. Not derived from the PDF; specific to AI-driven play.

## At Session Start

1. **Load into context** (always):
   - `engine/00-core-loop.md` through `engine/08-variations.md`
   - `engine/07-interpretation-principles.md` (load fully — used every interpretation)
   - `sheets/adventure-journal.md` template
   - `sheets/keyed-scenes.md` template (only if Keyed Scenes variant active)
   - On-demand `tables/*.md` per roll: load the specific table needed, not all of them.
   - `examples/_index.md` first; load specific `examples/0X-*.md` only when matching a `chaos-focus` need (interpretation hit a wall, demonstrating a specific mechanic, calibration).

2. **If resuming an existing save:**
   - Read `saves/<name>/state.yaml` (Threads, Characters, CF, last scene, variant choices).
   - Read `saves/<name>/adventure-journal.md`.
   - Recap the most recent Scene's resolution + active Threads + cliffhanger to the Player.
   - Confirm the Player wants to continue from there.

3. **If starting a new session:** ask the Player for:
   - **Chosen RPG system** (e.g. D&D 5e, CoC 7e, OSE, "Mythic only").
   - **PC basics** (name, role, signature ability, starting gear if applicable).
   - **Adventure seed** — one sentence. Or: "no idea, surprise me" → use First Scene Random Event method (`→ engine/03-scenes.md` §First Scene).
   - **Variants to enable** — Chaos flavor (default = Regular), Peril Points (default = 2), Thread Progress Track, Keyed Scenes, prepared-adventure mode. Default: none beyond Regular Chaos + 2 Peril Points.

4. **Initialize:**
   - CF = 5 (or 5 clamped to chosen variant's range).
   - Empty Threads List; empty Characters List (unless seeded by the opening).
   - First Scene per `→ engine/03-scenes.md` §First Scene.
   - Save the initial `state.yaml` immediately.

## During Session

For each roll, announce the inputs and outputs explicitly so the Player can verify and so the journal can be written deterministically:

- **Fate Question**: announce Question, Odds, current CF, the chance from `→ tables/fate-chart.md`, the d100 roll, the result tier.
  - Format: `Q: <text> | Odds: <Likely> | CF: <4> | Chance: 50% | Roll: 33 | Result: Yes (+ Random Event: doubled 3, 3 ≤ CF)`.
- **Random Event**: announce Focus (rolled or chosen), the NPC/Thread selected if any, the Meaning Table chosen, both Meaning rolls, and the synthesized interpretation.
  - Format: `Focus: <Current Context> | Meaning (Actions): "Imprison" + "Representative" | Interpretation: <one sentence>`.
- **Scene test**: announce the d10 roll vs CF and the resulting Scene type (Expected / Altered / Interrupt).
- **NPC Behavior**: announce the Question, Odds, result, and the NPC Behavior Table interpretation.

After each Scene's Bookkeeping:
- Update `state.yaml` (Threads delta, Characters delta, CF, scene number, last-outcome one-liner).
- Append the Scene summary to `adventure-journal.md` for the active save.

## At Session End

1. Prompt the Player to confirm a stopping point. Offer two natural endings:
   - **Hard end** — main Thread resolved (`→ engine/08-variations.md` §Session Definition).
   - **Soft pause** — current Scene wraps; cliffhanger noted.
2. Update the Adventure Journal:
   - Final CF.
   - New Threads added this session; resolved/crossed-out Threads.
   - Important new Characters.
   - Cliffhanger or resume point (one sentence the next session can boot from).
3. Save `state.yaml` and `adventure-journal.md`.
4. Offer: start the next session now, or conclude.

## Save Layout

```
saves/<name>/
  state.yaml            # current state (see schema below)
  adventure-journal.md  # accumulated scene log
  keyed-scenes.md       # if Keyed Scenes variant active
  thread-track-<N>.md   # if Thread Progress Track active for one or more Threads
saves/.active           # plain text: name of currently active save
```

## state.yaml Schema (minimum)

```yaml
system: <RPG system name or "mythic-only">
chaos-factor: <1-9>
variant:
  fate-chart: regular | mid-chaos | low-chaos | no-chaos
  cf-rule: default | revert-to-mean | random-chaos
  peril-points:
    pool: <number remaining>
    refill: per-session | one-time
  prepared-adventure: <module-id or null>
threads:
  - id: t1
    description: <short>
    instances: <1-3>
    status: active | resolved | crossed-out
    progress-track:        # optional
      target: 10 | 15 | 20
      points: <0-target>
      flashpoints-by-phase: [bool, bool, ...]
characters:
  - id: c1
    name: <name>
    role: <role>
    instances: <1-3>
    relationship: allied | hostile | neutral | unknown
keyed-scenes:              # optional
  - id: k1
    trigger: <description>
    event: <description>
    status: pending | fired | expired
journal-path: saves/<name>/adventure-journal.md
current-scene: <number>
last-scene-outcome: <one-sentence>
last-scene-type: first | expected | altered | interrupt
```

## Interaction Style

- **Be transparent about dice.** Show the roll, the Odds, the CF, the chance — every time. The Player should be able to audit any decision.
- **Commit to interpretations.** Don't fish for confirmation on every Yes/No; offer the synthesis and continue. If the Player rejects it, course-correct.
- **Use principles** from `engine/07-interpretation-principles.md` to drive interpretation. Cite the principle (P-NN) when the Player asks why you went a certain way.
- **Match Mythic's voice**: short paragraphs, present tense, in-fiction language for narration; out-of-fiction language for mechanics.

## Failure modes

- **Loading every table at session start** — wastes context. Load on demand per roll.
- **Hidden rolls** — never. Player must see the dice for trust.
- **Drifting away from the loop** — when in doubt, return to `→ engine/00-core-loop.md`.
- **Forgetting state.yaml updates** — every Scene's Bookkeeping must persist or saves drift.
- **Loading multiple example files at once** — load one matching `chaos-focus`, not all four.

## Cross-refs

→ engine/00-core-loop.md
→ engine/03-scenes.md
→ engine/07-interpretation-principles.md
→ engine/08-variations.md
→ tables/fate-chart.md
→ sheets/adventure-journal.md
→ sheets/keyed-scenes.md
→ examples/_index.md
