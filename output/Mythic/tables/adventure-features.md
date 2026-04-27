# Adventure Features List & Prepared Adventure Event Focus Table

> Source: *Mythic GME 2e* p.158-165 (rules), p.225-226 (collected sheets).
> When: Running a prepared/published adventure with Mythic.
> Input: Adventure Features List = a third List you maintain (alongside Threads + Characters), holding anything special or unique to this prepared adventure that could form an encounter.
> Output: When a Random Event rolls "Adventure Feature", roll on this List for which feature appears.

Full rules in `../rules/05-variations.md` §Using Mythic With Prepared Adventures.

## Adventure Features List Sheet

Mirrors the layout of the standard Threads/Characters Lists: 25 numbered slots organized into 5 sections of 5 entries each. The sections are gated by which dice you roll.

```
ADVENTURE FEATURES LIST

         1-2  CHOOSE   1
         3-4  CHOOSE   2
   1-2   5-6  CHOOSE   3
         7-8  CHOOSE   4
         9-10 CHOOSE   5

         1-2  CHOOSE   6
         3-4  CHOOSE   7
   3-4   5-6  CHOOSE   8       ← d4 covers slots 1-10
         7-8  CHOOSE   9
         9-10 CHOOSE  10

         1-2  CHOOSE  11
         3-4  CHOOSE  12
   5-6   5-6  CHOOSE  13       ← d6 covers slots 1-15
         7-8  CHOOSE  14
         9-10 CHOOSE  15

         1-2  CHOOSE  16
         3-4  CHOOSE  17
   7-8   5-6  CHOOSE  18       ← d8 covers slots 1-20
         7-8  CHOOSE  19
         9-10 CHOOSE  20

         1-2  CHOOSE  21
         3-4  CHOOSE  22
   9-10  5-6  CHOOSE  23       ← d10 covers slots 1-25
         7-8  CHOOSE  24
         9-10 CHOOSE  25
```

### Rolling on the List

Same as for the Threads / Characters Lists:

1. **Determine active sections**: A section with at least one element is active. The active section furthest down determines the first die — none, d4, d6, d8, or d10.
2. Roll the section die (if needed) for the section number.
3. Roll **1d10** for the slot within that section.
4. **Empty line** → CHOOSE: pick any element from the List, or roll again.

## Prepared Adventure Event Focus Table

> Source: *Mythic GME 2e* p.165, p.226.
> When: A Random Event fires while running a prepared adventure.
> Input: 1d100.
> Output: An Event Focus tailored to prepared-adventure play.

| 1d100 | Result |
|---:|---|
| **1-20**    | Adventure Feature |
| **21-40**   | NPC Action |
| **41-50**   | NPC Negative |
| **51-55**   | NPC Positive |
| **56-70**   | PC Negative |
| **71-80**   | PC Positive |
| **81-100**  | Current Context |

### Differences from the regular Event Focus Table

This table **removes** Remote Event, New NPC, Move Toward A Thread, Move Away From A Thread, Close A Thread, and Ambiguous Event — the prepared adventure already produces those.

It **adds** Adventure Feature: roll on the Adventure Features List above to see which feature is triggered. You may not need to roll on the Meaning Tables for further clarification (e.g., "Poison gets worse" is straightforward); but for results like "Wandering monster", roll on the Meaning Tables for clue on how the monster approaches or what it does.
