# D&D Basic（Mentzer Red Box）角色创建模板

## 创建步骤（完整见 `rules/dnd-basic-rules.md` 附录 D）

```
1. 掷 3d6 六次（按顺序）→ STR/INT/WIS/DEX/CON/CHA
2. 查属性表评估适合的职业（主属性 ≥9 合理）
3. 选择职业（Fighter/Cleric/Magic-User/Thief/Dwarf/Elf/Halfling）
4. （可选）属性点交换：2 点非主属性换 1 点主属性
   - 禁止: 交换到使任何属性 <9；CON 永不交换
5. 查属性调整表（3=-3 … 18=+3）
6. 选阵营（Lawful / Neutral / Chaotic）
7. 掷 HP：职业 HD + CON 调整（最低 1）
8. 掷起始金钱：3d6 × 10 gp
9. 购买装备（见 §3 价目表）
10. 计算 AC：9 - 护甲值 - 盾 - DEX 调整（越低越好）
11. 填豁免表（查 §5 各职业豁免）
12. XP = 0，记 2 级所需 XP + 主属性 XP 加成
13. 特殊能力：MU/Elf 选 1 法术 + 必带 Read Magic；Cleric 1 级无法术；Thief 记技能 %
14. 命名 + 简短描述
```

**绝望角色**：若 ≥2 个属性在 3-6 → DM 可允许重掷整份角色。

---

## Basic 职业（7 选 1，种族即职业）

| 职业        | 主属性 | HD  | 武器                                 | 护甲           | 最低属性     |
| ----------- | ------ | --- | ------------------------------------ | -------------- | ------------ |
| Fighter     | STR    | d8  | 全部                                 | 全部 + 盾      | —            |
| Cleric      | WIS    | d6  | 钝击（Mace/Hammer/Staff/Club/Sling） | 全部 + 盾      | —            |
| Magic-User  | INT    | d4  | Dagger / Short Sword / Staff         | 无             | —            |
| Thief       | DEX    | d4  | 全部                                 | 皮甲，无盾     | —            |
| Dwarf       | STR    | d8  | 全部（适合体型）                     | 全部 + 盾      | STR 9, CON 9 |
| Elf         | INT+STR | d6  | 全部                                 | 全部 + 盾      | INT 9        |
| Halfling    | STR+DEX | d6  | 全部（适合体型）                     | 全部 + 盾      | STR 9, CON 9, DEX 9 |

### Basic 范围内的职业特性速查

- **Fighter**：2 级起 +1 to hit 变化（查 Hit Roll 表）
- **Cleric**：Turn Undead 从 1 级；法术从 2 级起每日 1 个
- **Magic-User**：1 级每天 1 法术；必带 Read Magic
- **Thief**：1 级技能 — 开锁 15%、拆陷阱 10%、攀爬 87%、潜行 20%、躲藏 10%、聆听 1-2/d6、扒窃 20%、背刺 ×2 伤害
- **Dwarf**：60' 红外视觉、侦测石工机关 1-2/d6、矮小武器限制、矮人语
- **Elf**：60' 红外视觉、侦测暗门 1-2/d6（主动 1-4/d6）、免疫 Ghoul 麻痹、精灵语
- **Halfling**：远程 +1、大型敌人 AC +2（闪避）、室外躲藏 1-9/d10、室内 1-2/d6、半身人语

---

## 主属性 XP 加成

| 主属性 | 调整 |
| ----: | ----: |
| 3-5 | -20% |
| 6-8 | -10% |
| 9-12 | 0 |
| 13-15 | +5% |
| 16-18 | +10% |

---

## 升级 XP（Basic 等级 1-3）

| 职业       | 2 级 | 3 级 |
| ---------- | ---: | ---: |
| Fighter    | 2000 | 4000 |
| Cleric     | 1500 | 3000 |
| Magic-User | 2500 | 5000 |
| Thief      | 1200 | 2400 |
| Dwarf      | 2200 | 4400 |
| Elf        | 4000 | 8000 |
| Halfling   | 2000 | 4000 |

**3 级封顶**——本战役不扩展 Expert+。

---

## 属性调整值表

| 属性 | 调整 |
| ---: | ---: |
| 3    | -3 |
| 4-5  | -2 |
| 6-8  | -1 |
| 9-12 | 0  |
| 13-15 | +1 |
| 16-17 | +2 |
| 18   | +3 |

## 开门概率（基于 STR）

| STR | 开门 |
| ---: | ---: |
| 3-8 | 1/6 |
| 9-12 | 2/6 |
| 13-15 | 3/6 |
| 16-17 | 4/6 |
| 18 | 5/6 |

## 负重与移动（cn）

| 负重 | 基础移动 | 探索 | 遭遇 |
| ---: | ---: | ---: | ---: |
| ≤ 400 | 120' | 120'/回合 | 40'/轮 |
| 401-800 | 90' | 90'/回合 | 30'/轮 |
| 801-1200 | 60' | 60'/回合 | 20'/轮 |
| 1201-1600 | 30' | 30'/回合 | 10'/轮 |

---

## state.yaml 角色模板

```yaml
party:
  character_id: # 英文 ID（例：morwen）
    name: 角色名
    gender: Female
    class: Fighter # Fighter/Cleric/Magic-User/Thief/Dwarf/Elf/Halfling
    level: 1
    alignment: Lawful # Lawful/Neutral/Chaotic
    xp:
      current: 0
      next: 2000 # 2 级所需
      prime_req_mod: "+10%" # -20% / -10% / 0 / +5% / +10%
    hp:
      current: 6
      max: 6
      con_mod: 1
    ac: # Basic 使用下行 AC，越低越好（无甲=9，板甲+盾=2）
      value: 3
      unarmored: 9
      dex_mod: -1 # DEX 正值 = AC 减少（更好）
    stats:
      STR: 16
      INT: 9
      WIS: 9
      DEX: 13
      CON: 14
      CHA: 10
    modifiers:
      STR: 2
      INT: 0
      WIS: 0
      DEX: 1
      CON: 1
      CHA: 0
    combat_mod:
      melee: 2    # 近战命中 + 伤害 = STR 调整
      missile: 1  # 远程命中 = DEX 调整
      open_doors: "4/6" # 基于 STR
    saves: # d20 ≥ 此值成功
      D: 12 # Death Ray or Poison
      W: 13 # Magic Wands
      P: 14 # Paralysis or Turn to Stone
      B: 15 # Dragon Breath
      S: 16 # Rods, Staves, or Spells
      wis_mod: 0 # 加到 W/S vs 心智法术
    movement:
      base: 120 # 英尺（受负载影响）
      exploration: "120'/回合"
      encounter: "40'/轮"
      overland: 24 # 英里/天
    encumbrance:
      total: 0 # 钱币单位 cn
      limit: 1600
    encounter:
      initiative_mod: 1 # DEX 调整（可选规则：个人先攻）
      reaction_mod: 0   # CHA 调整
    languages: [Common, Lawful] # 阵营语 + 通用语 + 职业/种族语 + INT 额外
    literate: true # INT 9+ 可读写通用语与阵营语
    class_features: [] # 例：Thief 技能、Cleric Turn Undead、Elf 免疫麻痹
    equipment:
      weapons:
        - { name: Long Sword, dmg: 1d8, type: melee }
        - { name: Short Bow, dmg: 1d6, type: missile, range: "50'/100'/150'" }
      ammo:
        - { name: Arrow, count: 20 }
      armor: { name: Chain Mail, ac_reduction: 4 }
      shield: { name: Shield, ac_bonus: 1 }
      other:
        - { name: Backpack }
        - { name: Torch, count: 6 }
        - { name: Tinderbox }
        - { name: Rope 50', count: 1 }
        - { name: Iron Rations, count: 7 }
    magic_items: []
    coins: # Basic 用 pp/gp/ep/sp/cp
      pp: 0
      gp: 5
      ep: 0
      sp: 0
      cp: 0
    treasure: []
    spells: null # 非施法者
    notes: ""
```

---

## 施法者法术模板

### Cleric（神术）

1 级**无法术**；2 级起每日 1 个 1 级法术；3 级每日 2 个 1 级法术。可自由选择记忆（不需要法术书）。

```yaml
spells:
  slots:
    "1": 1 # 2 级：1；3 级：2
  memorized:
    - { name: Cure Light Wounds, level: 1, used: false }
```

### Magic-User & Elf（奥术）

```yaml
spells:
  slots:
    "1": 1 # 1 级：1；2 级：2；3 级：2 个 1 级 + 1 个 2 级（仅 Elf；MU 3 级为 2 个 1 级 + 1 个 2 级）
  memorized:
    - { name: Magic Missile, level: 1, used: false }
  spellbook:
    - { name: Read Magic, level: 1 } # 必带
    - { name: Magic Missile, level: 1 }
```

---

## 随从模板（Retainer）

雇主 CHA 决定最大数量与基础忠诚：

| CHA | 最大随从 | 士气调整 |
| ---: | ---: | ---: |
| 3 | 1 | -2 |
| 4-5 | 2 | -1 |
| 6-8 | 3 | -1 |
| 9-12 | 4 | 0 |
| 13-15 | 5 | +1 |
| 16-17 | 6 | +1 |
| 18 | 7 | +2 |

```yaml
retainers:
  retainer_id:
    name: 随从名
    class: Fighter # 通常 Normal Man 或 1 级职业
    level: 0 # Normal Man 为 0
    hp: [4, 4]
    ac: 7
    morale: 7 # 基础 7 ± 雇主 CHA 调整
    wage: "5-10 gp/月" # 视职业
    share: "半份 XP 和宝藏"
    equipment:
      weapons:
        - { name: Spear, dmg: 1d6 }
      armor: { name: Leather, ac_reduction: 2 }
    notes: "忠诚检定 2d6 ≤ morale = 通过"
```

---

## 示例角色卡（Morwen the Fighter）

```
===================================
姓名: Morwen        职业: Fighter
等级: 1             阵营: Lawful
===================================
STR 16 (+2)  INT 9   WIS 9
DEX 13 (+1)  CON 14 (+1)  CHA 10
HP: 6       AC: 3
XP: 0 / 2000 (+10%)
-----------------------------------
豁免:
  Poison 12  Wands 13  Paralysis 14
  Breath 15  Spells 16
-----------------------------------
装备: Chain Mail, Shield, Long Sword,
      Short Bow + 20 箭, 火把×6, 背包
负重: ~1025 cn (60'/回合)
钱: 5 gp
===================================
```

见附录 D.3（Felonius the Magic-User）和 D.4（Thornbeard the Dwarf）了解其他职业完整案例。
