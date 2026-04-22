# OSE Advanced PDF ↔ Markdown Consistency Check

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a classified consistency report comparing `output/OSE/rules/ose-advanced-*.md` (8 files, ~12,500 lines) against the OSE Advanced Fantasy v1.2 PDFs (Player's Tome + Referee's Tome + Reference Booklet + Optional Rules Checklist). Every discrepancy is either (a) a PDF-faithfulness bug to fix, (b) a deliberate campaign annotation to keep, (c) missing content, or (d) extra content with no PDF source.

**Architecture:** Verification-only, read-only against source PDFs. Each MD file is checked in its own task with identical structure: header → Index ↔ PDF ToC → spot-check ≥10 numeric values → table row counts → special-section pass → record findings. A final task aggregates and classifies, plus a cross-file consistency task binds the files together.

**Tech Stack:** `pdf_extract.py` (pymupdf) for PDF page extraction; pre-extracted txt files in `Rule Books/OSE/OSE Advanced/txt/`; Grep/Read tools on both sides. No code is written; only a report file is produced.

**Output:** One report file — `docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md` — updated incrementally by each task. Each finding is one line: `[severity] <file>:<line>  |  PDF p.<nn>  |  <issue>  |  <classification>`.

**Source PDFs (absolute paths):**
- `/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/Advanced Fantasy Player's Tome v1.2.pdf` (257 p)
- `/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/Advanced Fantasy Referee's Tome v1.2.pdf` (257 p)
- `/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/sets/` — Reference Booklet v1.0, Optional Rules Checklist v1.0 (see the `txt/` folder for names)

**Pre-extracted txt (faster than PDF grep):**
- `/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/txt/OSE Advanced Fantasy Player's Tome v1.2.txt`
- `/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/txt/OSE Advanced Fantasy Referee's Tome v1.2.txt`
- `/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/txt/OSE Advanced Fantasy Reference Booklet v1.0.txt`
- `/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/txt/OSE Advance Fantasy Optional Rules Checklist v1.0.txt`

**MD files under test** (all under `output/OSE/rules/`):

| File | Line count | PDF source | Primary pages |
|---|---:|---|---|
| `ose-advanced-rules.md` | 1808 | Player's Tome + Referee's Tome | Player p.6-27, 90-100, 102-108, 112-116, 120-122, 124; Referee Adventuring + Combat sections |
| `ose-advanced-classes.md` | 1868 | Player's Tome | p.30-78 (22 classes), p.80-89 (10 races) |
| `ose-advanced-spells.md` | 2587 | Player's Tome | Cleric p.136-145; Druid p.148-157; Illusionist p.160-…; Magic-User (later section) |
| `ose-advanced-monsters.md` | 3616 | Referee's Tome | p.20-120+ |
| `ose-advanced-treasures.md` | 1938 | Referee's Tome | p.146-202+ (Treasures + Magic Items + Potions + Rings + …) |
| `ose-advanced-referee.md` | 732 | Referee's Tome | p.5-18 Running Adventures; p.142-144 NPC Encounters |
| `ose-advanced-reference-booklet.md` | 1596 | Reference Booklet v1.0 | entire booklet |
| `ose-advanced-optional-rules-checklist.md` | 80 | Optional Rules Checklist v1.0 | entire booklet |

**Known intentional deviations (DO NOT flag as bugs):**

The working tree has an uncommitted diff to `output/OSE/rules/ose-advanced-rules.md` (237-line diff, sections around Player Characters → Character Creation Options + Creating a Character: Advanced/Basic Method, plus Combat → advanced combat options). It adds phrases like *"This campaign uses the Advanced Method"* and *"enabled in this campaign"* with `CLAUDE.md` cross-references. These are **campaign annotations**, not PDF content errors — classify as `[campaign-annotation]` and exclude from pass/fail counts.

**Severity levels used in the report:**

| Severity | Meaning |
|---|---|
| `[bug]` | PDF-faithfulness violation — numeric/textual content contradicts PDF |
| `[missing]` | PDF section / table / entry absent from MD |
| `[extra]` | MD contains content with no PDF source (and is not a campaign annotation) |
| `[campaign-annotation]` | Deliberate customisation by the campaign — keep |
| `[formatting]` | Structure/markup issue (heading level, table row count off, anchor broken) — low-priority |
| `[ok-spot]` | Spot-check passed — kept as audit trail (not a finding) |

---

## File Structure

**Created by this plan (one file, appended to across tasks):**
- `docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md` — the findings report

**Read-only (MD files under test):**
- `output/OSE/rules/ose-advanced-rules.md`
- `output/OSE/rules/ose-advanced-classes.md`
- `output/OSE/rules/ose-advanced-spells.md`
- `output/OSE/rules/ose-advanced-monsters.md`
- `output/OSE/rules/ose-advanced-treasures.md`
- `output/OSE/rules/ose-advanced-referee.md`
- `output/OSE/rules/ose-advanced-reference-booklet.md`
- `output/OSE/rules/ose-advanced-optional-rules-checklist.md`

**Read-only (sources):**
- PDFs and txt files listed above.

No code files are created or modified. No tests are added. This is an audit.

---

## Task 0: Scaffold the Consistency Report

**Files:**
- Create: `docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md`

- [ ] **Step 1: Create the report file with fixed header, severity legend, and one empty section per MD file**

Write this exact content to `docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md`:

```markdown
# OSE Advanced PDF ↔ Markdown Consistency Report

> Generated: 2026-04-22
> Sources: OSE Advanced Fantasy Player's Tome v1.2, Referee's Tome v1.2, Reference Booklet v1.0, Optional Rules Checklist v1.0
> MD files under test: `output/OSE/rules/ose-advanced-*.md` (8 files)

## Severity legend

| Severity | Meaning |
|---|---|
| `[bug]` | PDF-faithfulness violation — numeric/textual content contradicts PDF |
| `[missing]` | PDF section / table / entry absent from MD |
| `[extra]` | MD contains content with no PDF source and is not a campaign annotation |
| `[campaign-annotation]` | Deliberate customisation by the campaign — keep |
| `[formatting]` | Structure/markup issue — low-priority |
| `[ok-spot]` | Spot-check passed (audit trail) |

## Summary

- Files checked: 0 / 8
- Bugs: 0
- Missing: 0
- Extra: 0
- Campaign annotations: 0
- Formatting: 0
- Spot-checks passed: 0

## Known intentional deviations

`output/OSE/rules/ose-advanced-rules.md` has an uncommitted diff adding campaign-specific notes ("this campaign uses the Advanced Method", "enabled in this campaign") around Player Characters → Character Creation Options, Creating a Character: Advanced/Basic Method, and Combat → advanced combat options. Classify all such lines as `[campaign-annotation]`.

---

## File: ose-advanced-rules.md

_(Task 2 populates this section.)_

## File: ose-advanced-classes.md

_(Task 3 populates this section.)_

## File: ose-advanced-spells.md

_(Task 4 populates this section.)_

## File: ose-advanced-monsters.md

_(Task 5 populates this section.)_

## File: ose-advanced-treasures.md

_(Task 6 populates this section.)_

## File: ose-advanced-referee.md

_(Task 7 populates this section.)_

## File: ose-advanced-reference-booklet.md

_(Task 8 populates this section.)_

## File: ose-advanced-optional-rules-checklist.md

_(Task 8 populates this section.)_

## Cross-file consistency

_(Task 9 populates this section.)_

## Final classification and recommended fixes

_(Task 10 populates this section.)_
```

- [ ] **Step 2: Verify all 4 txt sources are readable**

Run:
```bash
ls -la "/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/txt/"
```
Expected: 4 non-empty `.txt` files present. If any are missing, extract the missing PDF(s) with `python3 pdf_extract.py "<pdf-path>" > "<txt-path>"` before proceeding.

- [ ] **Step 3: Commit the scaffold**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: scaffold consistency report"
```

---

## Task 2: Audit `ose-advanced-rules.md`

**Files:**
- Read: `output/OSE/rules/ose-advanced-rules.md` (1808 lines)
- Read: Player's Tome PDF pages 6-11 (Introduction), 14-27 (Player Characters), 90-92 (Advancement), 96-100 (Equipment), 102-108 (Vehicles), 112-116 (Hired Help), 120-122 (Strongholds), 124-133 (Magic overview + spell lists)
- Read: Referee's Tome PDF — Adventuring + Combat sections (search for "Combat Sequence" and "Adventuring" headings in the Referee's txt)
- Modify: `docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md` → section `## File: ose-advanced-rules.md`

- [ ] **Step 1: Load MD file-level metadata and Index**

Run:
```bash
sed -n '1,30p' output/OSE/rules/ose-advanced-rules.md
```
Confirm:
- Line 1 is `# OSE Advanced Fantasy — Core Rules Reference`
- Source line cites Player's Tome v1.2 + Referee's Tome v1.2
- Index lists 10 sections (Introduction → Combat)

Record any deviation as `[formatting]`.

- [ ] **Step 2: Exclude campaign-annotation lines from bug-hunting**

Run:
```bash
git diff output/OSE/rules/ose-advanced-rules.md > /tmp/ose-advanced-rules-campaign.diff
wc -l /tmp/ose-advanced-rules-campaign.diff
```
Read `/tmp/ose-advanced-rules-campaign.diff`. Every added line that mentions "this campaign", "enabled in this campaign", "Not used in this campaign", or cross-references `CLAUDE.md` / `ose-advanced-optional-rules-checklist.md` is a campaign annotation — log each range once as `[campaign-annotation] rules.md:<line-range> | campaign customisation, keep`.

- [ ] **Step 3: ToC coverage — Player's Tome front matter vs MD**

Player's Tome ToC (from `--info`):
```
Introduction p.6-11 (About This Game, Advanced Fantasy Gaming, Terminology, In This Book, Other Books, Compatibility)
Player Characters p.14-27 (Game Statistics, Character Creation Options, Multiple Classes, Basic/Advanced Method, Ability Scores, Alignment, Weapon Proficiency, Languages, Secondary Skills)
Advancement p.90-92 (Experience, Level Titles, Wealth)
Equipment p.96-100 (Adventuring Gear, Weapons and Armour, Poison)
Vehicles and Animals p.102-108 (Rules For Vehicles, Animals of Burden, Dogs, Tack and Harness, Land Vehicles, Water Vessels)
Hired Help p.112-116 (Retainers, Mercenaries, Specialists)
Strongholds p.120-122 (Construction, Domain Management, Structures)
Magic p.124-133 (Spells, Turning the Undead, Spell Books, Magical Research, 4 spell lists)
```
Grep in MD for each heading:
```bash
grep -n '^###\? ' output/OSE/rules/ose-advanced-rules.md | head -200
```
For every PDF sub-heading missing from the MD, write `[missing] rules.md | PDF p.<nn> <section> | absent from MD`. For every MD sub-heading not in the PDF ToC (and not a campaign annotation), write `[extra] rules.md:<line> | not in PDF ToC`.

- [ ] **Step 4: Referee's Tome content (Adventuring + Combat)**

The rules.md also pulls Adventuring and Combat from the Referee's Tome. Locate them:
```bash
grep -n -iE '^(Adventuring|Combat)$|Combat Sequence|Initiative' "/Users/jack/Projects/trpg-projects/Rule Books/OSE/OSE Advanced/txt/OSE Advanced Fantasy Referee's Tome v1.2.txt" | head -30
```
Confirm the MD's `## Adventuring` and `## Combat` sections cover what the Referee's Tome offers (Time/Weight/Movement, Encumbrance, Ability Checks, Hazards, Dungeon/Wilderness/Waterborne, Encounters, Evasion; Combat Sequence, Initiative, Attacking, Morale, Combat Tables, and advanced combat options). Record gaps.

- [ ] **Step 5: Numeric spot-checks (minimum 10, must cover different sections)**

For each spot-check, log `[ok-spot]` or `[bug]`. Write exact MD line and PDF page in the finding. Perform these 10:

1. **Ability score modifier table** — MD's STR/INT/WIS/DEX/CON/CHA modifier rows (3 → -3 through 18 → +3) must match Player's Tome p.22-23. Check row count and the +2 threshold (13-15 → +1, 16-17 → +2, 18 → +3 in OSE).
2. **Encumbrance thresholds** (rules.md Adventuring section) — unencumbered / encumbered / heavily encumbered / max thresholds in coins. Compare to Player's Tome Adventuring or Referee's Tome Adventuring.
3. **Combat sequence steps** — OSE B/X order: declare spells/retreats, initiative (group), then for each side in order: morale, movement, missile, magic, melee. Verify the MD lists these in that order.
4. **THAC0 formula / Ascending AC conversion note** — MD should describe `AC 9 [10]`, `THAC0 19 [+0]` dual notation matching Player's Tome p.14 + Referee's Tome combat section.
5. **Saving throw categories** — D/W/P/B/S (Death, Wands, Paralysis, Breath, Spells). Verify labels match PDF.
6. **Starting wealth** — 3d6 × 10 gp (Player's Tome p.18/20 in Creating a Character steps).
7. **Level Titles table** (Advancement) — row count per class; verify 14 entries for Fighter/Cleric/MU or whatever PDF shows.
8. **Weapon combat stats table** (Equipment) — spot-check 3 weapons: damage die, weight, cost, properties (2-handed, missile range, etc.). Cross-reference Player's Tome p.98-99.
9. **Retainer morale and share of XP** (Hired Help) — verify morale score range and XP-share rule.
10. **Spell list indexes** — count spells per level per class against the 4 spell list tables in PDF p.130-133.

Record all 10 as `[ok-spot]` or `[bug]` with a one-sentence detail.

- [ ] **Step 6: Table row count audit**

For each numeric table in MD (Encumbrance, Weapons, Armour, Stronghold structures, Spell lists), count rows:
```bash
awk '/^\|/{c++} /^[^|]/{if(c>0){print c; c=0}}' output/OSE/rules/ose-advanced-rules.md
```
Compare against PDF counts (read `--pages` for each). Any off-by-one row or missing row → `[bug]` or `[missing]`.

- [ ] **Step 7: Update the report**

Append all `[…]` findings to the `## File: ose-advanced-rules.md` section of `docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md`. Update the Summary counters at top.

- [ ] **Step 8: Commit**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: rules.md findings"
```

---

## Task 3: Audit `ose-advanced-classes.md`

**Files:**
- Read: `output/OSE/rules/ose-advanced-classes.md` (1868 lines)
- Read: Player's Tome PDF p.30-78 (22 classes) + p.80-89 (10 races)
- Modify: report → section `## File: ose-advanced-classes.md`

- [ ] **Step 1: Class list coverage**

Player's Tome lists these 22 classes (from ToC):
```
Acrobat, Assassin, Barbarian, Bard, Cleric, Drow, Druid, Duergar, Dwarf, Elf, Fighter, Gnome, Half-Elf, Halfling, Half-Orc, Illusionist, Knight, Magic-User, Paladin, Ranger, Svirfneblin, Thief
```
Run:
```bash
grep -nE '^## ' output/OSE/rules/ose-advanced-classes.md
```
Confirm all 22 class H2 headings present. For each missing class → `[missing]`. For each extra class not in PDF → `[extra]`.

- [ ] **Step 2: Race list coverage**

PDF Character Races p.80-89: Drow, Duergar, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, Svirfneblin (10 races).
Confirm all 10 race entries present in MD.

- [ ] **Step 3: Per-class stat block spot-check (5 classes, one from each "group")**

Check: **Fighter, Magic-User, Cleric, Ranger, Thief.** For each, verify:
- Requirements / Prime Requisite
- Hit Dice (d6/d8/d4 etc.)
- Maximum Level
- Armour and Weapons lists
- XP table: row count = 14 (or class-specific max), and first 3 rows' XP values match PDF exactly
- THAC0 column: 1st-level is 19 [+0]; 14th-level value matches PDF
- Saves (D/W/P/B/S) at 1st and at highest level

For each class, log one `[ok-spot]` line or a `[bug]` per discrepancy. Cite MD line and PDF page.

- [ ] **Step 4: Race ability score modifiers spot-check**

For Drow, Duergar, Gnome, Half-Orc, Svirfneblin: verify the racial ability modifiers (e.g. Drow -1 CON / +1 DEX). Read Player's Tome p.81-89 and compare to MD's race section.

- [ ] **Step 5: Update report + commit**

Append findings. Update Summary. Commit:
```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: classes.md findings"
```

---

## Task 4: Audit `ose-advanced-spells.md`

**Files:**
- Read: `output/OSE/rules/ose-advanced-spells.md` (2587 lines)
- Read: Player's Tome PDF Cleric/Druid/Illusionist/Magic-User spells sections (p.136-…)
- Modify: report → `## File: ose-advanced-spells.md`

- [ ] **Step 1: Spell-list coverage by level**

For each of 4 classes, count spells per level in MD:
```bash
awk '/^## (Cleric|Druid|Illusionist|Magic-User) Spells/{cls=$2; lvl=""} /^### .+ Level Spells/{lvl=$2; printf "%s L%s: ", cls, lvl} /^#### /{c++} {} END{}' output/OSE/rules/ose-advanced-spells.md
```
Compare counts against Player's Tome ToC numbers (which list individual spells by level — e.g. Cleric 1st has 8 spells: Cure Light Wounds, Detect Evil, Detect Magic, Light, Protection from Evil, Purify Food and Water, Remove Fear, Resist Cold). Record any mismatch as `[missing]` or `[extra]`.

- [ ] **Step 2: Detailed spot-check of 10 spells**

Pick 10 spells spanning the four lists and levels. Suggested:
1. Cleric 1: *Cure Light Wounds* (range, duration, dual use)
2. Cleric 3: *Striking* (+1d6 dmg, 1 turn)
3. Cleric 5: *Raise Dead* (range, constraints by cleric level)
4. Druid 1: *Entangle* (area, Str save)
5. Druid 3: *Call Lightning* (damage, weather restriction)
6. Illusionist 1: *Chromatic Orb* (damage by type — may be OSE-Advanced-specific)
7. Illusionist 2: *Hypnotic Pattern* (HD affected)
8. Magic-User 1: *Magic Missile* (per-3-levels scaling)
9. Magic-User 3: *Fireball* (damage dice, radius)
10. Magic-User 5: *Cloudkill* (area, HD threshold)

For each, compare: **Duration, Range, Area, Damage dice, Save type, Level/HD thresholds**. Each is `[ok-spot]` or `[bug]`.

- [ ] **Step 3: Update report + commit**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: spells.md findings"
```

---

## Task 5: Audit `ose-advanced-monsters.md`

**Files:**
- Read: `output/OSE/rules/ose-advanced-monsters.md` (3616 lines)
- Read: Referee's Tome PDF p.20-120+ (Monsters section — ~200+ monsters)
- Modify: report → `## File: ose-advanced-monsters.md`

- [ ] **Step 1: Monster count**

Count H3 monster entries in MD:
```bash
grep -cE '^### [A-Z]' output/OSE/rules/ose-advanced-monsters.md
```
Count monster entries in Referee's Tome ToC (from `python3 pdf_extract.py ... --info`) — every `    <Name> ... p.<nn>` under `Monster Descriptions`.
Numbers should match. Record diff.

- [ ] **Step 2: First/last monster check**

Alphabetical first (Acolyte) and last monster (verify via ToC — likely Zombie or similar). Confirm both in MD.

- [ ] **Step 3: Stat-block spot-check (10 monsters)**

Pick a spread covering HD range and special-ability diversity:
- Goblin (1-HD, common)
- Ogre (mid-HD)
- Basilisk (special: petrification)
- Dragon, Red (multi-variant entry)
- Medusa (save-or-die gaze)
- Demon/Devil representative (high HD)
- Beholder equivalent (Eye of Terror)
- Golem, Iron
- Lich
- Tarrasque / Purple Worm (high-end)

For each, verify **AC (both [descending] [ascending]), HD, HP (if given), Att × Dmg, THAC0 (both forms), MV, SV, ML, AL, XP, TT**. One `[ok-spot]` per monster or `[bug]` per wrong number.

- [ ] **Step 4: Combat Tables & Encounter tables (if included)**

Referee's Tome p.22 — Combat Tables. If these are in monsters.md, verify each THAC0 row. If moved to rules.md or referee.md, note the location and defer to that file's task.

- [ ] **Step 5: Update report + commit**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: monsters.md findings"
```

---

## Task 6: Audit `ose-advanced-treasures.md`

**Files:**
- Read: `output/OSE/rules/ose-advanced-treasures.md` (1938 lines)
- Read: Referee's Tome PDF p.146-202+ (Treasures, Magic Items, Potions, Rings, Rods/Staves/Wands, Scrolls/Maps, Swords, Weapons)
- Modify: report → `## File: ose-advanced-treasures.md`

- [ ] **Step 1: Section coverage**

PDF Treasures chapter (p.146-152): Placing Treasure, Items of Value, Treasure Types, Magic Items (category breakdown), Gems and Jewellery.
PDF Magic Items chapter: Armour and Shields, Miscellaneous Items (huge list p.158-195), Potions (p.198-201), Rings (p.202-), Rods/Staves/Wands, Scrolls/Maps, Swords, Weapons.
Grep for each category heading in MD:
```bash
grep -nE '^## |^### ' output/OSE/rules/ose-advanced-treasures.md | head -120
```
Record any missing category.

- [ ] **Step 2: Treasure Types table row count**

PDF Treasure Types (p.148-149) is a multi-column table with ~22 rows (A through V or similar). Verify MD table row count and spot-check 3 rows (A, L, R) for exact gp/gem/jewellery/magic-item probabilities.

- [ ] **Step 3: Magic Items spot-check (10 items)**

Pick a spread across categories (use Referee's Tome ToC p.158-195 Miscellaneous Items list to avoid AI hallucination):
1. *Bag of Holding* — capacity and weight
2. *Boots of Speed* — movement multiplier, duration
3. *Cube of Force* — charges, force field levels
4. *Deck of Many Things* — card count and effects
5. *Girdle of Giant Strength* — STR equivalence
6. *Helm of Teleportation* — required spell
7. *Ioun Stones* — variants count
8. *Potion of Healing* — dice
9. *Ring of Protection* — AC bonus
10. *Sword +3, Frost Brand* — damage bonuses, special

For each: `[ok-spot]` or `[bug]` with MD line + PDF page.

- [ ] **Step 4: Update report + commit**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: treasures.md findings"
```

---

## Task 7: Audit `ose-advanced-referee.md`

**Files:**
- Read: `output/OSE/rules/ose-advanced-referee.md` (732 lines)
- Read: Referee's Tome PDF p.5-18 (Intro + Running Adventures) + p.142-144 (NPC Encounters) + any Encounter Tables in p.120s
- Modify: report → `## File: ose-advanced-referee.md`

- [ ] **Step 1: Section coverage**

Referee's Tome Running Adventures sub-sections (p.6-18): The Referee's Role, Handling PCs, Running the Game, Monsters and NPCs, Adventure Scenarios, Designing a Dungeon, Designing a Wilderness, Designing a Base Town, Awarding XP. Plus NPC Encounters p.142-144 (Adventuring Parties, Strongholds).

Grep headings in MD and match against this list. Record any missing or extra.

- [ ] **Step 2: Encounter tables**

Locate Dungeon and Wilderness encounter tables in Referee's Tome (use `--info` or grep the txt for "Dungeon Encounter" / "Wilderness Encounter"). Verify tables are present in MD with matching row counts and level/terrain brackets.

- [ ] **Step 3: XP awarding rules**

Referee's Tome p.18 Awarding XP — confirm MD captures: monster XP values by HD, treasure = 1 XP per gp, party share division rule.

- [ ] **Step 4: Update report + commit**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: referee.md findings"
```

---

## Task 8: Audit Reference Booklet & Optional Rules Checklist

**Files:**
- Read: `output/OSE/rules/ose-advanced-reference-booklet.md`
- Read: `output/OSE/rules/ose-advanced-optional-rules-checklist.md`
- Read: `Rule Books/OSE/OSE Advanced/txt/OSE Advanced Fantasy Reference Booklet v1.0.txt`
- Read: `Rule Books/OSE/OSE Advanced/txt/OSE Advance Fantasy Optional Rules Checklist v1.0.txt`
- Modify: report → two sections

- [ ] **Step 1: File line counts and headers**

Run:
```bash
wc -l output/OSE/rules/ose-advanced-reference-booklet.md output/OSE/rules/ose-advanced-optional-rules-checklist.md
```
Read first 30 lines of each; confirm source attribution + Index.

- [ ] **Step 2: Reference Booklet coverage**

The Reference Booklet v1.0 is a condensed quick-reference extract. Open the txt, list its section headings, and compare to MD H2/H3 headings. Each section present? Record `[missing]`/`[extra]`.

- [ ] **Step 3: Reference Booklet spot-check (5 values)**

Pick 5 quick-reference values the booklet provides (e.g. combat modifier summary, encumbrance rates, turning-undead table, spell-per-day progression excerpt). Verify each matches the full rule in the source book (Player's Tome or Referee's Tome) — if the booklet itself is consistent with the full book, the MD should match both.

- [ ] **Step 4: Optional Rules Checklist coverage**

The Optional Rules Checklist v1.0 is a flat list of toggleable optional rules. Count entries in both the txt and the MD; they must match.
Spot-check 5 optional rules: rule name, page reference, default state (on/off) — compare MD to source.

- [ ] **Step 5: Update report + commit**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: reference-booklet + optional-rules-checklist findings"
```

---

## Task 9: Cross-File Consistency

**Files:**
- Read: all 8 MD files listed above
- Modify: report → `## Cross-file consistency`

- [ ] **Step 1: Spell references in classes.md / monsters.md / treasures.md all resolve in spells.md**

Extract every spell reference pattern from the three files:
```bash
grep -oE '\*[A-Z][a-zA-Z ]+\*' output/OSE/rules/ose-advanced-classes.md output/OSE/rules/ose-advanced-monsters.md output/OSE/rules/ose-advanced-treasures.md | sort -u > /tmp/ose-adv-spell-refs.txt
```
Filter to known spell-like terms (cross-reference the 4 spell lists in spells.md). For each referenced spell name, grep spells.md:
```bash
grep -c "^#### <SpellName>$" output/OSE/rules/ose-advanced-spells.md
```
If 0 matches, record `[bug] <file>:<line> | references spell "X" not defined in spells.md`.

- [ ] **Step 2: Monster special abilities that call out specific spells**

Monsters like Couatl, Djinni, Drow all cast spells. Grep monsters.md for "casts <X>" / "spell-like" / "as <spell>":
```bash
grep -nE 'cast|spell-like|as (per )?[a-z]+ spell' output/OSE/rules/ose-advanced-monsters.md | head -40
```
Verify each referenced spell exists in spells.md (same as Step 1).

- [ ] **Step 3: Class armour/weapon restrictions ↔ Equipment tables**

For each class in classes.md, note the `Armour:` and `Weapons:` lines. Confirm every named armour/weapon type appears in the rules.md equipment tables. Cross-check both sides.

- [ ] **Step 4: Optional Rules Checklist entries ↔ rules.md "Optional Rule" callouts**

The checklist is a summary. Each entry in `ose-advanced-optional-rules-checklist.md` should correspond to an "Optional Rule" callout somewhere in rules.md, classes.md, or spells.md. Grep for `(Optional Rule)`:
```bash
grep -rn 'Optional Rule' output/OSE/rules/ose-advanced-*.md
```
Every checklist entry maps? Every MD callout is in the checklist? Record asymmetries.

- [ ] **Step 5: Level-title consistency**

`ose-advanced-rules.md` has a Level Titles table under Advancement. Each class's XP table in `ose-advanced-classes.md` has a "Title" column. Cross-check: Level-9 Fighter title in rules.md == Level-9 Fighter title in classes.md, etc. Spot-check 3 classes.

- [ ] **Step 6: Update report + commit**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: cross-file consistency findings"
```

---

## Task 10: Final Classification & Recommended Fixes

**Files:**
- Modify: report → `## Final classification and recommended fixes`

- [ ] **Step 1: Roll up the Summary counters**

At the top of the report, update:
- Files checked: 8 / 8
- `[bug]` / `[missing]` / `[extra]` / `[campaign-annotation]` / `[formatting]` / `[ok-spot]` totals.

- [ ] **Step 2: Group `[bug]` + `[missing]` findings by priority**

For each finding, assign priority:
- **P0 — must fix:** numeric errors in combat-critical tables (AC, HD, THAC0, saves, damage, XP), wrong spell range/damage, missing monster from core list.
- **P1 — should fix:** minor numeric in tables (price, encumbrance), missing sub-section, missing non-core spell.
- **P2 — nice to have:** formatting, ordering, missing flavour text.

Write a P0/P1/P2 list with file:line + one-line fix suggestion per finding.

- [ ] **Step 3: List `[extra]` findings**

For each MD block not traceable to any source PDF and not flagged as campaign annotation: either mark for deletion (if content is incorrect) or upgrade to `[campaign-annotation]` (if it's a deliberate house rule that was un-flagged).

- [ ] **Step 4: Recommendation block**

Write a short recommendation section:
- Whether the MD set is safe to use as-is for play (depends on P0 count).
- Any files that should be re-imported from PDF.
- Any patterns of error (e.g. "all Magic-User spell ranges are 10' short — suggests unit-conversion bug").

- [ ] **Step 5: Commit final report**

```bash
git add docs/superpowers/plans/2026-04-22-ose-advanced-consistency-report.md
git commit -m "ose-advanced audit: final classification and fix recommendations"
```

- [ ] **Step 6: Decide on the uncommitted `ose-advanced-rules.md` diff**

The working tree has uncommitted campaign-annotation changes to `ose-advanced-rules.md`. These are not part of the audit but the user should decide:
- If the audit found no bugs in those sections → commit the campaign annotations:
  ```bash
  git add output/OSE/rules/ose-advanced-rules.md
  git commit -m "ose-advanced: add campaign annotations (Advanced Method, optional rules in use)"
  ```
- If the audit found bugs entangled with the annotations → fix bugs first, then commit annotations in a second commit.

Report this decision to the user — do not commit `ose-advanced-rules.md` automatically.

---

## Self-Review Checklist (author-run)

After completing all tasks, verify:

1. **All 8 MD files have a populated section** in the report (no placeholder `_(Task N populates …)_` left).
2. **The Summary counters** at the top of the report add up across file sections.
3. **Every finding has file:line + PDF page.** No finding says "somewhere in X".
4. **Every spot-check has a verdict** (`[ok-spot]` or `[bug]`), not just a description of what was checked.
5. **Campaign annotations are not double-counted** as bugs.
6. **Cross-file findings live only in the Cross-file section,** not duplicated in per-file sections.

If any check fails, loop back and fix the report in a final follow-up commit.
