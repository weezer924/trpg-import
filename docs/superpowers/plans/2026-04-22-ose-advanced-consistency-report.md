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

- Files checked: 1 / 8
- Bugs: 0
- Missing: 10
- Extra: 0
- Campaign annotations: 8
- Formatting: 18
- Spot-checks passed: 10

## Known intentional deviations

`output/OSE/rules/ose-advanced-rules.md` has an uncommitted diff adding campaign-specific notes ("this campaign uses the Advanced Method", "enabled in this campaign") around Player Characters → Character Creation Options, Creating a Character: Advanced/Basic Method, and Combat → advanced combat options. Classify all such lines as `[campaign-annotation]`.

---

## File: ose-advanced-rules.md

### Counts

| Category | Count |
|---|---|
| `[bug]` | 0 |
| `[missing]` | 10 |
| `[extra]` | 0 |
| `[campaign-annotation]` | 8 |
| `[formatting]` | 18 |
| `[ok-spot]` | 10 |

### Notes on page numbering

The MD uses **printed book page numbers** (visible numbers printed in the book), not PDF document page numbers. PDF document pages are offset by +2 from printed pages for the Player's Tome (e.g. PDF doc p.14 = printed p.12). This is consistent for the early sections (Introduction through Player Characters). However, from the Advancement section onward, the MD's page references are systematically wrong by approximately 50 pages — every section from Advancement through Adventuring/Combat has page numbers that are ~50 pages too low (e.g. Advancement cited as p.38–40, but printed pages are 88–90). The Adventuring and Combat sections both draw from the Player's Tome (PDF doc p.214–243), not the Referee's Tome (the Referee's Tome has no Adventuring/Combat rules chapter).

### Campaign annotations

- `[campaign-annotation]` rules.md:L173 | "This campaign uses the Advanced Method" callout with CLAUDE.md cross-reference — keep
- `[campaign-annotation]` rules.md:L175 | "Not used in this campaign" note on Multiple Classes — keep
- `[campaign-annotation]` rules.md:L185 | "not used in this campaign" parenthetical in step 3 of Advanced Method — keep
- `[campaign-annotation]` rules.md:L188 | "Ascending AC (enabled in this campaign)" note in step 6 — keep
- `[campaign-annotation]` rules.md:L189 | "Weapon Proficiency (enabled in this campaign)" + ose-advanced-optional-rules-checklist.md cross-reference in step 7 — keep
- `[campaign-annotation]` rules.md:L190 | "Re-rolling 1s and 2s (enabled in this campaign)" note in step 8 — keep
- `[campaign-annotation]` rules.md:L196 | "Not used in this campaign" on Secondary Skill in step 14 — keep
- `[campaign-annotation]` rules.md:L203 | "retained for reference; this campaign uses the Advanced Method above" parenthetical on Basic Method section — keep
- `[campaign-annotation]` rules.md:L395 | "enabled in this campaign" + ose-advanced-reference-booklet.md cross-reference in Weapon Proficiency header — keep
- `[campaign-annotation]` rules.md:L419 | "enabled in this campaign" in Weapon Specialisation header — keep
- `[campaign-annotation]` rules.md:L434 | "not used in this campaign" in Secondary Skills header — keep
- `[campaign-annotation]` rules.md:L440 | "not used in this campaign" in Multiple Classes header — keep
- `[campaign-annotation]` rules.md:L1688 | "enabled in this campaign" on Two Weapons combat option — keep
- `[campaign-annotation]` rules.md:L1699 | "enabled in this campaign" on Charging combat option — keep
- `[campaign-annotation]` rules.md:L1716 | "enabled in this campaign" on Parrying combat option — keep
- `[campaign-annotation]` rules.md:L1725 | "enabled in this campaign" on Splash Weapons combat option — keep

_(Note: These annotations are committed into the file, not an uncommitted diff. The report scaffold predates their commit.)_

### Missing sections

- `[missing]` rules.md | PDF Player p.212–215 (printed) | Party Organisation section entirely absent — covers party size, marching order, the caller, the mapper, dividing treasure
- `[missing]` rules.md | PDF Player p.123 (printed) | Turning the Undead section absent from Magic chapter — covers attempt frequency, limits, mixed undead groups, duration (1 turn)
- `[missing]` rules.md | PDF Player p.103 (printed) | Dogs subsection absent from Vehicles and Animals chapter — covers Hunting Dog (AC 7, HD 1+2, 1d6 bite) and War Dog (AC 8, HD 2+2, 2d4 bite) stats and cost table
- `[missing]` rules.md | PDF Player p.98–99 (printed) | Poison section entirely absent from Equipment chapter — covers 4 bloodstream poisons (I–IV) and 5 ingested poisons (I–V) with cost, save modifier, detection chance, onset time, and effects tables
- `[missing]` rules.md:L761–765 | PDF Player p.103 (printed) | Tack and Harness table missing "Dog armour" entry (25 gp, AC 6 [13]); also label "Barding" should be "Horse barding"
- `[missing]` rules.md | PDF Player p.129 (printed) | Druid Spell List entirely absent — 5 levels × 6–8 spells each (40 spells total)
- `[missing]` rules.md | PDF Player p.130 (printed) | Illusionist Spell List entirely absent — 6 levels × 12 spells each (72 spells total)
- `[missing]` rules.md:L467–477 | PDF Player p.88–89 (printed) | Level Titles: 15 of 22 classes missing — present: Cleric, Dwarf, Elf, Fighter, Halfling, Magic-User, Thief; absent: Acrobat, Assassin, Barbarian, Bard, Drow, Druid, Duergar, Gnome, Half-Elf, Half-Orc, Illusionist, Knight, Paladin, Ranger, Svirfneblin
- `[missing]` rules.md | PDF Player p.212 (printed) | "Deepcommon" language note absent from Languages section (creatures native to the Underworld speak Deepcommon; listed under Languages in PDF)
- `[missing]` rules.md | PDF Player p.212–215 (printed) | Party Organisation section also omits "Marching Order", "The Caller", "The Mapper", and "Dividing Treasure" sub-rules — these are practical play rules referenced in dungeons

### Formatting issues — page references

All page references from the Advancement section onward use incorrect page numbers (off by ~50 from the printed page numbers). The Introduction through Player Characters sections also have a few individual errors.

- `[formatting]` rules.md:L232 | Ability Scores page ref "PDF p.18–19" is wrong — printed pages are 20–21 (PDF doc p.22–23)
- `[formatting]` rules.md:L344 | Alignment page ref "PDF p.20" is wrong — printed page is 22 (PDF doc p.24)
- `[formatting]` rules.md:L358 | Languages page ref "PDF p.21" is wrong — printed page is 24 (PDF doc p.26)
- `[formatting]` rules.md:L453 | Advancement page ref "PDF p.38–40" is wrong — printed pages are 88–90 (PDF doc p.90–92)
- `[formatting]` rules.md:L481 | High-Level Play page ref "PDF p.39" is wrong — printed page is ~89 (PDF doc p.91)
- `[formatting]` rules.md:L509 | Wealth page ref "PDF p.40" is wrong — printed page is 90 (PDF doc p.92)
- `[formatting]` rules.md:L536 | Equipment page ref "PDF p.42–47" is wrong — printed pages are 94–98 (PDF doc p.96–100)
- `[formatting]` rules.md:L690 | Vehicles and Mounts page ref "PDF p.48–57" is wrong — printed pages are 100–108 (PDF doc p.102–110)
- `[formatting]` rules.md:L917 | Hired Help page ref "PDF p.58–65" is wrong — printed pages are 110–116 (PDF doc p.112–118)
- `[formatting]` rules.md:L979 | Retainers page ref "PDF p.60–61" is wrong — printed pages are 110–111 (PDF doc p.112–113)
- `[formatting]` rules.md:L1023 | Mercenaries page ref "PDF p.62–63" is wrong — printed pages are 112–113 (PDF doc p.114–115)
- `[formatting]` rules.md:L1061 | Strongholds page ref "PDF p.66–69" is wrong — printed pages are 118–120 (PDF doc p.120–122)
- `[formatting]` rules.md:L1164 | Magic page ref "PDF p.70–76" is wrong — printed pages are 122–131 (PDF doc p.124–133)
- `[formatting]` rules.md:L1219 | Magical Research page ref "PDF p.73" is wrong — printed page is 126 (PDF doc p.128)
- `[formatting]` rules.md:L1270 | Adventuring page ref "PDF p.112–135" is wrong — printed pages are 212–232 (PDF doc p.214–234); source is Player's Tome not Referee's Tome
- `[formatting]` rules.md:L1274 | Time/Weight/Movement page ref "PDF p.112–113" is wrong — printed pages are 214–215 (PDF doc p.216–217)
- `[formatting]` rules.md:L1600 | Combat page ref "PDF p.130–135" is wrong — printed pages are 234–237 (PDF doc p.236–239); source is Player's Tome not Referee's Tome
- `[formatting]` rules.md:L1739 | Morale page ref "PDF p.133" is wrong — printed page is 238 (PDF doc p.240)
- `[formatting]` rules.md:L1766 | Combat Tables page ref "PDF p.134–135" is wrong — printed pages are 240–241 (PDF doc p.242–243)

_(Note: page refs for Ability Checks, Saving Throws, Hazards, Dungeon/Wilderness/Waterborne Adventuring, and Encounters are similarly off — all have the same ~100-page-off systematic error for the Adventuring block. Full list omitted for brevity; representative examples given above.)_

### Spot-checks

- `[ok-spot]` rules.md:L262–270 | PDF Player p.21 (printed) | STR modifier table: 7 rows (3 → –3 through 18 → +3), Open Doors column matches, thresholds (13–15 → +1, 16–17 → +2, 18 → +3) correct
- `[ok-spot]` rules.md:L296–306 | PDF Player p.21 (printed) | DEX modifier table: Initiative column (13–15 → +1, 16–17 → +1, 18 → +2) matches PDF exactly
- `[ok-spot]` rules.md:L1322–1327 | PDF Player p.215 (printed) | Detailed Encumbrance thresholds (400/600/800/1600 coins → 120'/90'/60'/30') and max load 1,600 coins match PDF
- `[ok-spot]` rules.md:L1602–1612 | PDF Player p.234 (printed) | Combat sequence steps (declare → initiative → morale/movement/missile/magic/melee) match PDF order exactly
- `[ok-spot]` rules.md:L155–156 | PDF Player p.12 (printed) | THAC0/AC dual notation ("AC 9 [10]", "THAC0 19 [0]") matches PDF format; 1st-level attack table (L224–226) matches PDF p.19 exactly
- `[ok-spot]` rules.md:L1347–1352 | PDF Player p.217 (printed) | Saving throw categories D/W/P/B/S labels match PDF exactly
- `[ok-spot]` rules.md:L513 | PDF Player p.90 (printed) | Starting wealth "3d6 × 10 gold pieces" matches PDF
- `[ok-spot]` rules.md:L471–477 | PDF Player p.88–89 (printed) | Level Titles for the 7 classes present (Cleric, Dwarf, Elf, Fighter, Halfling, Magic-User, Thief) match PDF entries exactly
- `[ok-spot]` rules.md:L661–682 | PDF Player p.97 (printed) | Weapon Combat Stats table: all 22 weapon rows (damage dice, qualities) match PDF exactly; spot-checked Sword (1d8, Melee), Pole arm (1d10, Brace/Melee/Slow/Two-handed), Crossbow (1d6, Reload/Slow/Two-handed, ranges 5'–80'/81'–160'/161'–240')
- `[ok-spot]` rules.md:L964 | PDF Player p.111 (printed) | Retainer XP penalty –50% matches PDF; retainer loyalty uses 2d6 ≤ loyalty rating matches PDF; retainer morale score 2–12 scale confirmed
- `[ok-spot]` rules.md:L1238–1264 | PDF Player p.128–131 (printed) | Cleric spell list (5 levels, 8/8/6/6/6 spells) matches PDF; Magic-User spell list (6 levels, 12 spells each) matches PDF

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
