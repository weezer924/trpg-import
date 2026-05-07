# Chapter 6: Monsters 怪物

> 来源：Record of Lodoss War Companion I（1989, Group SNE）PDF p.52–61
> 译本：英文同人翻译版

As you know, various types of monsters appear on Lodoss Island. This chapter introduces some representative examples. **However, the most formidable monsters in the world are humans.** If the GM needs a powerful enemy, we recommend creating humans in the same way as PCs.

## Index

- [How to Read the Data 数据读法](#how-to-read-the-data-数据读法)
- [Special Abilities 特殊能力](#special-abilities-特殊能力)
- [Monster Stat Blocks 怪物数据](#monster-stat-blocks-怪物数据)

---

## How to Read the Data 数据读法

Each monster entry contains the following fields:

| 字段                | 中译         | 说明                                                                       |
| ------------------- | ------------ | -------------------------------------------------------------------------- |
| Monster Name        | 名称         | The common-language name used by people to refer to the creature.          |
| LP                  | 生命点       | The monster's Life Points, expressed as a dice roll (e.g., 2D10).          |
| MP                  | 精神点       | The monster's Mental Points.                                               |
| RE                  | 抗性         | The monster's Resistance value.                                            |
| IV                  | 先攻值       | Initiative Value (1–10). PCs roll D10 — if ≥ this, the player side acts first. |
| AV                  | 装甲值       | Armor Value — points absorbed by armor / hide.                             |
| Attack %            | 攻击命中率   | Monster's attack success rate.                                             |
| Damage              | 伤害         | Damage dealt on a successful hit.                                          |
| Evasion % (DE)      | 闪避值       | Monster's Defense value — subtracted from PC's hit rate.                   |
| Magic               | 法术         | Spells the monster knows. **For spells using "caster's level" damage, treat caster's level as 0.** |
| Movement            | 移动         | Compared to humans (assume Human-level AG = 10).                           |
| Experience Points   | 经验值       | XP awarded per monster.                                                    |
| Special Abilities   | 特殊能力     | See list below.                                                            |

---

## Special Abilities 特殊能力

### Poison 毒

When an attack by a monster with this ability hits, the character makes a **DE check**. On failure, they are poisoned. Poison damages LP and is either:

- **Fast-acting** — deals damage immediately, affects only once. Notation: `2D10 (fast)` / `(immediate)`
- **Slow-acting** — continues to deal damage every hour until cured by magic, antidote, or death. Notation: `D8 (slow)` / `(delayed)`

> **Translator's Note**: Some monsters may have damage that differs from the default damage.

### Paralysis 麻痹

Similar to poison: when hit, make a **DE check**; on failure, the nerves are paralyzed and the body cannot move. Duration varies from **10 minutes to permanent**. Cured by **Cure Paralysis** spell.

### Breath 吐息

The ability to breathe fire / ice / etc. to deal damage. Damage range and other details vary by monster (noted individually).

### Magic Defense 魔法防御

**Cannot be harmed by normal weapons.** Magic weapons or weapons enhanced with spells like **Enchant Weapon** are required.

### Mental Defense 精神防御

Immune to spells that affect the mind (such as Sleep or Confusion). **Also does not fall unconscious when MP reaches zero.**

### Level Drain 等级吸取

Causes the opponent to **lose experience accumulated in their body**:

- Reduces the level by **1**
- MP and LP are recalculated by **rolling the dice again**
- Experience points drop to **the midpoint between the points needed for the current level and one level lower**
- **Probability** of triggering on a successful hit varies by monster

### Darkvision 黑暗视觉

The ability to sense enemies even in darkness.

### Flight 飞行

The ability to fly through the air.

---

## Monster Stat Blocks 怪物数据

> 数据按 PDF p.54–61 的顺序整理。多栏排版导致顺序略有混杂——以下按字母排序。

### Bear 熊

| LP        | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| --------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| D10+10    | 10 | 30 |  5 |  4 |   65 | D10+5  |   10 | Human-level  | 30 |

- **Magic:** None **Special:** None

### Dark Elf 黑暗精灵

| LP            | MP   | RE   | IV | AV | Atk%  | Damage     | Eva% | Movement     | XP |
| ------------- | ---: | ---: | -: | -: | ----: | ---------- | ---: | ------------ | -: |
| 2D10+10 or +  | 40+  | 60+  |  7 | 4+ | 65+   | D10+4 or + |   25 | Human-level  | 50 |

- **Magic:** Firebolt, Silence, Shade, Shadow Body **Special:** None

### Dark Lord 暗黑王

| LP             | MP   | RE     | IV | AV | Atk%  | Damage              | Eva% | Movement     | XP   |
| -------------- | ---: | -----: | -: | -: | ----: | ------------------- | ---: | ------------ | ---: |
| 2D10+10 or +   | 20+  | 70–90  |  6 |  5 | 80+   | 2D10+2 (×2) or +    |  30+ | Human-level  | 80+  |

- **Magic:** None **Special:** None

### Dark Magician 暗黑魔术师

| LP          | MP   | RE     | IV | AV | Atk% | Damage         | Eva% | Movement     | XP  |
| ----------- | ---: | -----: | -: | -: | ---: | -------------- | ---: | ------------ | --: |
| D10+10 or + | 40+  | 70–90  |  6 |  3 | 50+  | 2D10 (×2) or + |  30+ | Human-level  | 80+ |

- **Magic:** Sorcerer, Common, Demon Scream **Special:** None

### Dark Priest 暗黑神官

| LP            | MP   | RE     | IV | AV | Atk% | Damage      | Eva% | Movement     | XP  |
| ------------- | ---: | -----: | -: | -: | ---: | ----------- | ---: | ------------ | --: |
| 2D10+10 or +  | 30+  | 70–90  |  5 |  4 | 60+  | D10+4 or +  |  30+ | Human-level  | 80+ |

- **Magic:** Priest, Demon Scream **Special:** None

### Dragon Tooth Warrior 龙牙战士

| LP       | MP | RE | IV | AV | Atk% | Damage     | Eva% | Movement     | XP  |
| -------- | -: | -: | -: | -: | ---: | ---------- | ---: | ------------ | --: |
| 4D10+10  | 20 | 80 |  5 |  5 |   75 | 2D10 (×2)  |   30 | Human-level  | 200 |

- **Magic:** None **Special:** Magic Defense, Mental Defense

### Dryad 树精

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | -------- | -: |
| D10+5 | 20 | 40 |  6 |  4 |   40 | D10+3  |   10 | Human×2  | 30 |

- **Magic:** Shield, Push **Special:** Mental Defense

### Flesh Golem 血肉魔像

| LP       | MP | RE | IV | AV | Atk% | Damage      | Eva% | Movement     | XP  |
| -------- | -: | -: | -: | -: | ---: | ----------- | ---: | ------------ | --: |
| 8D10+50  | 20 | 80 |  3 |  0 |  100 | 2D10+2 (×2) |    0 | Human-level  | 200 |

- **Magic:** None **Special:** Magic Defense, Mental Defense

### Ghoul 食尸鬼 *(Undead Monster)*

| LP        | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| --------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| 2D10+10   |  0 | 70 |  4 |  2 |   60 | 2D6+3  |   10 | Human-level  | 40 |

- **Magic:** None **Special:** Mental Defense

### Giant Ant 巨蚁

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement   | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | ---------- | -: |
| D10+6 | 10 | 10 |  4 |  6 |   50 | D10+2  |   10 | Human×½    | 10 |

- **Magic:** None **Special:** None

### Giant Bat 巨蝙蝠

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | -------- | -: |
| D10+5 | 10 | 10 |  3 |  1 |   50 | 2D6    |   30 | Human×3  | 30 |

- **Magic:** None **Special:** Darkvision, Flight

### Goblin 哥布林

| LP      | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| ------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| 2D10    | 15 | 10 |  4 |  3 |   45 | D6+4   |    0 | Human-level  | 10 |

- **Magic:** None **Special:** Darkvision

### Goblin Shaman 哥布林萨满

| LP      | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| ------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| 2D10+5  | 30 | 20 |  5 |  2 |   40 | D6+2   |   20 | Human-level  | 30 |

- **Magic:** Firebolt, Snare **Special:** Darkvision

### Gremlin 小妖精

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| D10+5 | 20 | 30 |  6 |  4 |   50 | D10+2  |   30 | Human-level  | 40 |

- **Magic:** Sleep **Special:** None

### Hobgoblin 大哥布林

| LP       | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| -------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| 3D10+10  | 20 | 15 |  2 |  4 |   70 | D10+5  |   10 | Human-level  | 30 |

- **Magic:** None **Special:** Darkvision

### Kobold 狗头人

| LP      | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| ------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| 2D10+5  | 10 | 10 |  3 |  3 |   55 | D8+4   |    5 | Human-level  | 15 |

- **Magic:** None **Special:** Darkvision

### Minotaur 牛头怪

| LP        | MP | RE | IV | AV | Atk% | Damage          | Eva% | Movement     | XP  |
| --------- | -: | -: | -: | -: | ---: | --------------- | ---: | ------------ | --: |
| 4D10+30   | 20 | 60 |  5 |  6 |   90 | 2D10+5 (×2)     |    0 | Human-level  | 100 |

- **Magic:** None **Special:** None

### Rat 巨鼠

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement   | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | ---------- | -: |
| D10+3 | 10 | 10 |  6 |  1 |   45 | D10    |   20 | Human×1.5  | 10 |

- **Magic:** None **Special:** None

### Shade 暗影精灵

| LP    | MP | RE | IV | AV | Atk% | Damage          | Eva% | Movement | XP |
| ----- | -: | -: | -: | -: | ---: | --------------- | ---: | -------- | -: |
| 3D10  | 35 | 60 |  6 |  4 |   60 | D10+2 (×2)      |   30 | Human×2  | 45 |

- **Magic:** Shadow Body **Special:** Flight, Mental Defense

### Slime 史莱姆

| LP      | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement | XP |
| ------- | -: | -: | -: | -: | ---: | ------ | ---: | -------- | -: |
| 2D10+5  | 10 | 40 |  2 |  0 |   60 | D10+5  |   10 | Human×⅓  | 20 |

- **Magic:** None **Special:** Mental Defense

### Snake 巨蛇

| LP    | MP | RE | IV | AV | Atk% | Damage      | Eva% | Movement     | XP |
| ----- | -: | -: | -: | -: | ---: | ----------- | ---: | ------------ | -: |
| D10+5 |  0 | 50 |  3 |  2 |   60 | 2D10 (×2)   |   10 | Human-level  | 20 |

- **Magic:** None **Special:** Mental Defense, Poison D10 (immediate or delayed)

### Spider 巨蛛

| LP   | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| ---- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| D10  | 10 | 10 |  4 |  2 |   40 | D10    |   10 | Human-level  | 20 |

- **Magic:** None **Special:** Poison D10 (immediate)

### Sylph 风精灵

| LP      | MP | RE | IV | AV | Atk% | Damage     | Eva% | Movement | XP |
| ------- | -: | -: | -: | -: | ---: | ---------- | ---: | -------- | -: |
| 2D10+8  | 30 | 40 |  7 |  4 |   60 | 2D6 (×2)   |   30 | Human×4  | 50 |

- **Magic:** Silence **Special:** Magic Defense, Mental Defense

### Werebear 熊化人

| LP       | MP | RE | IV | AV | Atk% | Damage      | Eva% | Movement     | XP |
| -------- | -: | -: | -: | -: | ---: | ----------- | ---: | ------------ | -: |
| 3D10+20  | 10 | 40 |  5 |  5 |   80 | D10+4 (×2)  |   20 | Human-level  | 60 |

- **Magic:** None **Special:** Magic Defense

### Wererat 鼠化人

| LP      | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| ------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| 2D10+5  | 10 | 40 |  6 |  4 |   65 | D10+4  |   20 | Human-level  | 40 |

- **Magic:** None **Special:** None

### Werewolf 狼化人

| LP       | MP | RE | IV | AV | Atk% | Damage     | Eva% | Movement     | XP |
| -------- | -: | -: | -: | -: | ---: | ---------- | ---: | ------------ | -: |
| 2D10+20  | 15 | 35 |  6 |  4 |   60 | 2D6+2 (×2) |   20 | Human-level  | 50 |

- **Magic:** None **Special:** Darkvision

### Wight 食魂鬼 *(Undead Monster)*

| LP        | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP  |
| --------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | --: |
| 3D10+20   |  0 | 80 |  5 |  5 |   50 | D10+5  |   30 | Human-level  | 150 |

- **Magic:** None **Special:** Mental Defense, **Level Drain (20%)**

### Will-o'-Wisp 鬼火

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | -------- | -: |
| 2D10  | 20 | 50 |  6 |  3 |   50 | D10+5  |   20 | Human×2  | 20 |

- **Magic:** Silence **Special:** Flight, Mental Defense

### Wolf 狼

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | -------- | -: |
| 2D10  |  5 | 10 |  7 |  3 |   50 | D6+4   |   10 | Human×2  | 10 |

- **Magic:** None **Special:** Darkvision

### Wood Golem 木魔像

| LP        | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP  |
| --------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | --: |
| 8D10+30   | 20 | 60 |  3 |  3 |   70 | 2D6+2  |    0 | Human-level  | 100 |

- **Magic:** None **Special:** Mental Defense

### Wraith 幽灵 *(Undead Monster)*

| LP       | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP  |
| -------- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | --: |
| 2D10+10  |  0 | 70 |  5 |  3 |   70 | D10+5  |   40 | Human-level  | 110 |

- **Magic:** None **Special:** Mental Defense, **Level Drain (30%)**

### Zombie 僵尸 *(Undead Monster)*

| LP    | MP | RE | IV | AV | Atk% | Damage | Eva% | Movement     | XP |
| ----- | -: | -: | -: | -: | ---: | ------ | ---: | ------------ | -: |
| D10+5 |  0 | 50 |  3 |  2 |   50 | D10+2  |   10 | Human-level  | 20 |

- **Magic:** None **Special:** Mental Defense

---

> **GM 提示**：本表是 1 至 4 级冒险常用怪物。更强大的对手可参照怪物数据自行扩展，或将敌方塑造为「敌对的人类 NPC」按 PC 创建规则制作。
