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

- Files checked: 2 / 8
- Bugs: 1
- Missing: 10
- Extra: 0
- Campaign annotations: 8
- Formatting: 26
- Spot-checks passed: 20

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

### Counts

| Category | Count |
|---|---|
| `[bug]` | 1 |
| `[missing]` | 0 |
| `[extra]` | 0 |
| `[formatting]` | 8 |
| `[ok-spot]` | 10 |

### Notes on structure and page numbering

Classes and races are H3 headings under two H2 sections (`## Character Classes` and `## Character Races`), not individual H2 headings. All 22 class H3s and all 10 race H3s are present.

The file uses **PDF document page numbers** throughout (not printed page numbers as the task convention expects). For the 15 advanced classes (Acrobat, Assassin, Barbarian, Bard, Drow, Druid, Duergar, Gnome, Half-Elf, Half-Orc, Illusionist, Knight, Paladin, Ranger, Svirfneblin) the doc-page numbers are internally consistent with each other (doc = printed + 2).

However, the 7 classic classes (Cleric, Dwarf, Elf, Fighter, Halfling, Magic-User, Thief) have page references that match neither the doc pages nor the printed pages in the Player's Tome. These appear to have been copied from the OSE Classic B/X book (where these same classes appear at lower page numbers). The character races section also uses doc page numbers consistently.

### Bug

- `[bug]` classes.md:L1146 | PDF Player printed p.66 (doc p.68) | Magic-User **Weapons** stat block lists "Dagger only" — PDF states "Dagger, staff (optional)". The optional staff rule is omitted entirely.

### Formatting issues — page references

**Classic classes (wrong page numbers — appear copied from OSE Classic B/X, not this Player's Tome):**

- `[formatting]` classes.md:L382 | Cleric page ref "(PDF p.24–25)" is wrong — printed p.36–37 (doc p.38–39); "p.24" is the Alignment section, not the Cleric class
- `[formatting]` classes.md:L642 | Dwarf page ref "(PDF p.26–27)" is wrong — printed p.46–47 (doc p.48–49)
- `[formatting]` classes.md:L690 | Elf page ref "(PDF p.28–29)" is wrong — printed p.48–49 (doc p.50–51)
- `[formatting]` classes.md:L743 | Fighter page ref "(PDF p.30–31)" is wrong — printed p.50–51 (doc p.52–53); "p.30–31" is where Acrobat lives
- `[formatting]` classes.md:L899 | Halfling page ref "(PDF p.32–33)" is wrong — printed p.56–57 (doc p.58–59)
- `[formatting]` classes.md:L1137 | Magic-User page ref "(PDF p.34–35)" is wrong — printed p.66–67 (doc p.68–69)
- `[formatting]` classes.md:L1405 | Thief page ref "(PDF p.36–37)" is wrong — printed p.74–75 (doc p.76–77)

**Overview range (wrong start):**

- `[formatting]` classes.md:L49 | Character Classes overview ref "(PDF p.24–77)" — p.24 is the Alignment section; classes start at printed p.28 (doc p.30). Should be "(PDF printed p.28–75)" or "(PDF doc p.30–77)"

### Spot-checks — class stat blocks

- `[ok-spot]` classes.md:L741–783 | PDF Player printed p.50–51 (doc p.52–53) | Fighter: Requirements None, Prime Requisite STR, HD 1d8, Max Level 14, Armour any/shields, Weapons any; XP table 14 rows: L1=0/19[0]/D12W13P14B15S16, L2=2000, L3=4000, L14=840,000/10[+9]/D4W5P6B5S8; all values match PDF exactly
- `[ok-spot]` classes.md:L380–455 | PDF Player printed p.36–37 (doc p.38–39) | Cleric: Requirements None, Prime Requisite WIS, HD 1d6, Max Level 14, Armour any/shields, Weapons any blunt; XP table 14 rows: L1=0/19[0]/D11W12P14B16S15, L5=12,000, L14=700,000/12[+7]/D3W5P7B8S7; all values match PDF exactly
- `[ok-spot]` classes.md:L1135–1180 | PDF Player printed p.66–67 (doc p.68–69) | Magic-User: Requirements None, Prime Requisite INT, HD 1d4, Max Level 14, Armour none; XP table 14 rows: L1=0/19[0]/D13W14P13B16S15/spells:1–0–0–0–0–0, L11=600,000/14[+5], L14=1,050,000/14[+5]/D8W9P8B11S8/spells:4–4–4–4–3–3; all values match PDF exactly
- `[ok-spot]` classes.md:L1270–1343 | PDF Player printed p.70–71 (doc p.72–73) | Ranger: Requirements CON 9/WIS 9, Prime Requisite STR, HD 1d8, Max Level 14, Armour leather/chainmail/shields; XP table 14 rows: L1=0/19[0]/D12W13P14B15S16, L7=90,000/14[+5], L14=925,000/10[+9]/D4W5P6B5S8; all values match PDF exactly
- `[ok-spot]` classes.md:L1403–1485 | PDF Player printed p.74–75 (doc p.76–77) | Thief: Requirements None, Prime Requisite DEX, HD 1d4, Max Level 14, Armour leather/no shields, Weapons any; XP table 14 rows: L1=0/19[0]/D13W14P13B16S15, L5=9,600/17[+2], L14=760,000/12[+7]/D8W9P7B10S8; Thief Skills table 14 rows (L1: CS 87, TR 10, HN 1–2, HS 10, MS 20, OL 15, PP 20; L14: CS 99, TR 99, HN 1–5, HS 99, MS 99, OL 99, PP 125); all values match PDF exactly

### Spot-checks — race ability modifiers

- `[ok-spot]` classes.md:L1507 | PDF Player printed p.79 (doc p.81) | Drow (Race): Ability Modifiers –1 CON, +1 DEX; matches PDF "–1 CON, +1 DEX" exactly
- `[ok-spot]` classes.md:L1546 | PDF Player printed p.80 (doc p.82) | Duergar (Race): Ability Modifiers –1 CHA, +1 CON; matches PDF "–1 CHA, +1 CON" exactly
- `[ok-spot]` classes.md:L1672 | PDF Player printed p.83 (doc p.85) | Gnome (Race): Ability Modifiers None; matches PDF "None" exactly
- `[ok-spot]` classes.md:L1792 | PDF Player printed p.86 (doc p.88) | Half-Orc (Race): Ability Modifiers –2 CHA, +1 CON, +1 STR; matches PDF exactly
- `[ok-spot]` classes.md:L1837 | PDF Player printed p.87 (doc p.89) | Svirfneblin (Race): Ability Modifiers None; matches PDF "None" exactly

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
