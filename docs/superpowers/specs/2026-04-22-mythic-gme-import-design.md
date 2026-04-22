# Mythic GME 2nd Edition Import — Design Spec

> **Date**: 2026-04-22
> **Source**: `Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf` (230 pages)
> **Status**: Approved for implementation planning

---

## 1. Framing

Mythic 2nd Edition is a **solo storytelling engine**, not a game system. It provides procedures and random tables that emulate a Game Master for solo or GM-less play, pairing with any TRPG system the player chooses.

**Primary consumer**: AI running solo play sessions. The AI needs executable procedures and lookup tables, not a passive rulebook.

**Language**: English original, no Chinese translation. Mythic's terminology is semantically designed; translation risks losing the procedural crispness.

**Sibling AI project**: Not created at this time. Output lives only at `output/Mythic/`. A sibling project at `/Users/jack/Projects/trpg-projects/Mythic/` may be added later; design leaves room for it.

## 2. Two-Tier Architecture

Output splits into two tiers plus shared assets:

| Tier | Role | When loaded | Characteristic |
|---|---|---|---|
| `engine/` (Tier 2) | **Primary entry point** | Loaded wholesale at solo session start | Compact procedures, decision trees, interpretation heuristics. No narrative prose. |
| `rules/` (Tier 1) | **Fallback reference** | Loaded on rule-ambiguity lookups | Full PDF transcription preserving Crane's explanations and edge cases. |
| `tables/` | **On-demand data** | Loaded per roll/check | Pure data tables, one per file. |
| `examples/` | **Style calibration** | Loaded when interpretation feels stale | Full Big Example transcriptions; extensible with user-added play logs. |
| `sheets/` | **Templates** | Reference when setting up a session | Adventure Journal, Keyed Scenes Record Sheet. |

## 3. Directory Layout

```
output/Mythic/
  rules/
    00-mythic-journey.md
    01-mythic-adventures.md
    02-fate-questions.md
    03-random-events.md
    04-scenes.md
    05-variations.md
    06-rules-summary.md
  engine/
    00-core-loop.md
    01-fate-questions.md
    02-random-events.md
    03-scenes.md
    04-threads-and-characters.md
    05-chaos-factor.md
    06-npc-behavior.md
    07-interpretation-principles.md
    08-variations.md
    09-session-protocol.md
  tables/
    fate-chart.md
    fate-chart-variants.md
    fate-question-answers.md
    fate-check-modifiers.md
    random-event-focus.md
    meaning-actions.md
    meaning-descriptions.md
    meaning-elements.md
    scene-adjustment.md
    npc-behavior.md
    npc-statistics.md
    thread-progress-track.md
    adventure-features.md
  examples/
    _index.md
    01-henny-in-z-land.md
    02-wutwo-labs.md
    03-guardian-of-chosen-one.md
    04-the-big-example.md
  sheets/
    adventure-journal.md
    keyed-scenes.md
```

## 4. Tier Specifications

### 4.1 `rules/` — Base Transcription

- Linear PDF transcription organized by book chapter.
- Preserves Crane's concept explanations, design rationale, and edge-case discussion.
- Inline mini-examples (the 2-4 paragraph "suppose the PC is…" vignettes) stay in the flow; they belong to the concepts they illustrate.
- **All four Big Examples migrate out of `rules/` and into `examples/`**: Henny In Z Land (p.32-35, end of Ch2), Weird Times At Wutwo Labs (p.55-59, end of Ch3), Guardian Of The Chosen One (p.116-123, end of Ch4), and The Big Example (Ch6, p.178-186). Each `rules/` chapter ends at the page immediately preceding its Big Example.
- Ch8 "Collected Tables & Sheets" (p.193-227) is NOT duplicated; its content lives in `tables/` and `sheets/`.
- Ch7 "Rules Summary" (p.187-192) IS retained — it is Crane's own terse recap and serves as a memory anchor complementary to `engine/`.
- Credits / Cover Art / Patrons pages are skipped.

### 4.2 `engine/` — AI Execution Layer

Each file follows the same compact structure:

```markdown
# <Topic>

## When To Use
- [triggers]
- [anti-patterns: when not to use]

## Procedure
1. [step]
2. [step]
...

## Decision Tree
[compact branching logic]

## Failure modes
- [common mistakes]

## Cross-refs
→ tables/<file>.md
→ engine/<file>.md
```

**Critical files**:

- `00-core-loop.md` — the top-level Scene → play → event check → bookkeeping cycle.
- `07-interpretation-principles.md` — ~25 distilled heuristics extracted from Big Examples and inline mini-examples. Each principle cites the originating example by file + line so future maintainers can audit. This file is the highest-leverage new artifact.
- `09-session-protocol.md` — AI-specific meta-instructions (what to load at session start, what state to maintain, what to record at end). This does not exist in the PDF and is invented for the AI runtime.

Writing rules:
- No narrative connectors ("Now let's discuss...", "As we've seen...").
- All cross-file refs use relative paths.
- Concise imperative voice.

### 4.3 `tables/` — Pure Data

- One table per file.
- Each file begins with 2-3 lines of use-context ("When: …; Input: …; Output: …") so the AI can act on the table without round-tripping through `engine/`.
- Markdown tables, right-aligned numeric columns.
- `meaning-elements.md` is the most complex: ~100 thematic sub-tables (Location, Weather, Creature, etc.) separated by `## <Theme>` headings for AI keyword lookup.

### 4.4 `examples/` — Extensible Collection

- Initial 4 files transcribed from PDF Big Examples.
- Extensible: user may later add their own solo playthrough logs or additional reference sessions.
- Naming: `NN-{short-name}.md` starting at `01`; `05+` reserved for additions.
- Each file opens with frontmatter:

```yaml
---
source: pdf | user-log | other
chaos-focus: [fate-questions, random-events, scenes, interrupt-scenes, threads, ...]
length-turns: <int>
length-scenes: <int>
---
```

- `_index.md` lists all examples with their frontmatter summaries; AI reads the index first to pick which example to load.

### 4.5 `sheets/` — Templates

Straight transcription of:
- Adventure Journal (Threads List, Characters List, Scene Log sections)
- Keyed Scenes Record Sheet

## 5. Import Guide File

Create `.claude/mythic-import-guide.md` per CLAUDE.md §4. Contents:

- Directory structure overview (from §3 of this spec).
- Tier writing conventions (rules fidelity, engine de-narrativization, tables purity).
- `interpretation-principles.md` extraction methodology:
  - Read all 4 Big Examples + scan inline mini-examples.
  - Abstract patterns into imperative principles.
  - Each principle must cite its source ("from `examples/02-wutwo-labs.md`, turn 3" or "from `rules/02-fate-questions.md` §When To Run With Expectations").
  - Target ~25 principles; cap at 30 to prevent bloat.
- Chapter → file page-range map (from §7 below).
- Quality validation checklist (§6).
- Per-conversation work plan (§7).

## 6. Quality Validation

Mythic-specific checks beyond the standard CLAUDE.md §3.3 list:

- [ ] **Fate Chart 9×9 matrix**: every cell verified against PDF p.20. This matrix is the single most memorization-prone error source.
- [ ] **Meaning Tables completeness**: each sub-table contains exactly 100 entries (not 99, not 101).
- [ ] **Engine prose check**: no narrative connectors. Engine files should read as runbooks, not essays.
- [ ] **Cross-file refs**: all `→ path/file.md` references resolve to real files.
- [ ] **Big Examples fidelity**: dice rolls, Chaos Factor transitions, and scene boundaries in `examples/` match the PDF source turn-by-turn.
- [ ] **Principle citations**: every entry in `engine/07-interpretation-principles.md` cites a concrete source location.

## 7. Import Work Plan

Split across ~8 conversations. Each conversation: 1-2 chapters, immediate post-section validation.

| # | Topic | Output | PDF pages |
|---|---|---|---|
| 1 | rules/ Ch1 + Ch2 | `00-mythic-journey.md`, `01-mythic-adventures.md`, `02-fate-questions.md` | 4, 8-17, 18-31 |
| 2 | rules/ Ch3 + Ch4 | `03-random-events.md`, `04-scenes.md` | 36-54, 60-115 |
| 3 | rules/ Ch5 + Rules Summary | `05-variations.md`, `06-rules-summary.md` | 124-177, 187-192 |
| 4 | tables/ Fate + Event + NPC + Scene | `fate-chart.md`, `fate-chart-variants.md`, `fate-question-answers.md`, `fate-check-modifiers.md`, `random-event-focus.md`, `npc-behavior.md`, `npc-statistics.md`, `scene-adjustment.md`, `thread-progress-track.md`, `adventure-features.md` | 19-27, 38-44, 71, 110, 128, 217-226 |
| 5 | tables/ Meaning Actions + Descriptions | `meaning-actions.md`, `meaning-descriptions.md` | 48-49, 200-201 |
| 6 | tables/ Meaning Elements (~100 sub-tables) | `meaning-elements.md` — may split across 2 conversations | 88-106, 202-216 |
| 7 | examples/ + sheets/ | `examples/_index.md` + `01-04`, `sheets/adventure-journal.md`, `sheets/keyed-scenes.md` | 32-35, 55-59, 116-123, 154, 178-186, 193, 224 |
| 8 | engine/ full suite | `engine/00` through `09` | synthesis of all prior material |

**Ordering rationale**:
- `rules/` first — establishes semantic context for everything else.
- `tables/` second — mechanical transcription, no interpretation required.
- `examples/` + `sheets/` before `engine/` — supplies raw material for the principle extraction step.
- `engine/` last — must synthesize rules + examples; extracting principles without examples in hand will produce empty heuristics.

Conversation 6 is the largest single body of work; split into 6a (first 50 sub-tables) + 6b (second 50) if context pressure warrants.

## 8. Out of Scope

- Chinese translation of any content (see §1).
- Sibling AI project at `/Users/jack/Projects/trpg-projects/Mythic/` (see §1).
- MCP server for dice rolls / state management. May be added later once import is complete.
- Integration wiring into existing system projects (OSE, CoC, etc.). Mythic stands alone.
- PDF pages: Cover (1), Credits (2), Cover Art (228), Patrons (229).

## 9. Open Questions Deferred To Planning

- `engine/08-variations.md` scope: all 20+ variation rules, or only the subset most useful for solo AI play? Resolve during conversation 8.
- `meaning-elements.md` thematic sub-table ordering: PDF order vs. alphabetical vs. by domain. Resolve during conversation 6.
- Whether `examples/` frontmatter should include a machine-readable step-by-step index of which Mythic mechanism is demonstrated on which turn. Defer until we see how the AI actually uses the examples.
