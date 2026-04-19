# OSE 角色创建模板

## 创建步骤

1. 投 3d6（按顺序）决定六项属性：STR、DEX、CON、INT、WIS、CHA
2. 选择职业（须满足首要属性要求）
3. 在 `state.yaml` 的 `party` 下添加角色数据
4. 在本目录创建 `{id}.md` 记录角色背景（可选）

## 职业一览（Advanced Fantasy — 22 职业）

### 人类职业

| 职业                  | 首要属性  | HD  | 武器                                     | 护甲             | 最低属性要求   |
| --------------------- | --------- | --- | ---------------------------------------- | ---------------- | -------------- |
| 杂技师（Acrobat）     | DEX       | d4  | 投射武器、匕首、剑、短剑、长杆、矛、法杖 | 皮甲，无盾       | —              |
| 刺客（Assassin）      | DEX       | d4  | 全部                                     | 皮甲 + 盾        | —              |
| 蛮族（Barbarian）     | CON + STR | d8  | 全部                                     | 皮甲、链甲 + 盾  | DEX 9+         |
| 吟游诗人（Bard）      | CHA       | d6  | 投射武器、单手近战                       | 皮甲、链甲，无盾 | DEX 9+, INT 9+ |
| 牧师（Cleric）        | WIS       | d6  | 钝击武器                                 | 全部 + 盾        | —              |
| 德鲁伊（Druid）       | WIS       | d6  | 棍棒、匕首、投石索、矛、法杖             | 皮甲、木盾       | —              |
| 战士（Fighter）       | STR       | d8  | 全部                                     | 全部 + 盾        | —              |
| 幻术师（Illusionist） | INT       | d4  | 匕首、法杖                               | 无               | DEX 9+         |
| 骑士（Knight）        | STR       | d8  | 仅近战武器                               | 链甲、板甲 + 盾  | CON 9+, DEX 9+ |
| 魔法师（Magic-User）  | INT       | d4  | 匕首                                     | 无               | —              |
| 圣武士（Paladin）     | STR + WIS | d8  | 全部                                     | 全部 + 盾        | CHA 9+         |
| 游侠（Ranger）        | STR       | d8  | 全部                                     | 皮甲、链甲 + 盾  | CON 9+, WIS 9+ |
| 盗贼（Thief）         | DEX       | d4  | 全部                                     | 皮甲，无盾       | —              |

### 半人种族职业（Race-as-Class）

| 职业                  | 首要属性  | HD  | 武器          | 护甲            | 最低属性要求   |
| --------------------- | --------- | --- | ------------- | --------------- | -------------- |
| 卓尔（Drow）          | STR + WIS | d6  | 全部          | 全部 + 盾       | INT 9+         |
| 灰矮人（Duergar）     | STR       | d6  | 小型/正常尺寸 | 全部 + 盾       | CON 9+, INT 9+ |
| 矮人（Dwarf）         | STR       | d8  | 小型/正常尺寸 | 全部 + 盾       | CON 9+         |
| 精灵（Elf）           | STR + INT | d6  | 全部          | 全部 + 盾       | INT 9+         |
| 侏儒（Gnome）         | DEX + INT | d4  | 适合体型      | 皮甲 + 盾       | CON 9+, INT 9+ |
| 半精灵（Half-Elf）    | INT + STR | d6  | 全部          | 全部 + 盾       | CHA 9+, CON 9+ |
| 半身人（Halfling）    | DEX + STR | d6  | 适合体型      | 适合体型 + 盾   | CON 9+, DEX 9+ |
| 半兽人（Half-Orc）    | DEX + STR | d6  | 全部          | 皮甲、链甲 + 盾 | —              |
| 深侏儒（Svirfneblin） | STR       | d6  | 适合体型      | 适合体型 + 盾   | CON 9+         |

## 种族一览（可选：种族与职业分离）

Advanced Fantasy 允许将种族与职业分开选择（可选规则）。各种族可选职业如下：

| 种族                  | 可选职业                                                                     | 特殊能力                                 |
| --------------------- | ---------------------------------------------------------------------------- | ---------------------------------------- |
| 人类（Human）         | 所有非半人职业                                                               | 无等级限制                               |
| 矮人（Dwarf）         | 刺客、牧师、战士、盗贼                                                       | 60' 黑暗视觉、侦测建筑机关 2/6、魔法抗性 |
| 精灵（Elf）           | 杂技师、刺客、牧师、德鲁伊、战士、骑士、魔法师、游侠、盗贼                   | 60' 黑暗视觉、食尸鬼麻痹免疫             |
| 半身人（Halfling）    | 德鲁伊、战士、盗贼                                                           | 投射攻击 +1、对大型生物 AC +2            |
| 卓尔（Drow）          | 杂技师、刺客、牧师、战士、骑士、魔法师、游侠、盗贼                           | 90' 黑暗视觉、光敏感                     |
| 灰矮人（Duergar）     | 刺客、牧师、战士、盗贼                                                       | 90' 黑暗视觉、精神力量、光敏感           |
| 侏儒（Gnome）         | 刺客、牧师、战士、幻术师、盗贼                                               | 90' 黑暗视觉、穴居哺乳动物语言           |
| 半精灵（Half-Elf）    | 杂技师、刺客、吟游诗人、牧师、德鲁伊、战士、骑士、魔法师、圣武士、游侠、盗贼 | 60' 黑暗视觉、侦测暗门                   |
| 半兽人（Half-Orc）    | 杂技师、刺客、牧师、战士、盗贼                                               | 60' 黑暗视觉、背刺能力                   |
| 深侏儒（Svirfneblin） | 刺客、牧师、战士、幻术师、盗贼                                               | 融入岩石、大地元素语言、光敏感           |

## 小队管理

- `party` — 当前出战的角色
- `roster` — 休息/退役的角色（保留数据，不参战）
- `retainers` — 雇佣的仆役

## state.yaml 角色模板

```yaml
party:
  character_id: # 英文ID
    name: 角色名
    gender: Male # Male/Female
    race: Human # Human/Dwarf/Elf/Halfling/Drow/Duergar/Gnome/Half-Elf/Half-Orc/Svirfneblin
    class:
      Fighter # 人类: Acrobat/Assassin/Barbarian/Bard/Cleric/Druid/Fighter/Illusionist/Knight/Magic-User/Paladin/Ranger/Thief
      # 种族职业: Drow/Duergar/Dwarf/Elf/Gnome/Half-Elf/Halfling/Half-Orc/Svirfneblin
    level: 1
    title: 老兵 # 经验等级头衔（按职业和等级查表）
    alignment: Neutral # Lawful/Neutral/Chaotic
    xp:
      current: 0
      next: 2000 # 升级所需
      prime_req_mod: 0 # 主要属性 XP 调整值（-20%/-10%/0/+5%/+10%）
    hp:
      current: 8
      max: 8
      con_mod: 1 # 体质调整值（每 HD 加减）
    ac:
      value: 5 # 当前 AC（含护甲+盾+DEX）
      unarmored: 9 # 无甲 AC = 9 – DEX 调整值（下行）
      dex_mod: -1 # AC 的敏捷调整值（下行时为负=更好）
    aac:
      value: 14 # 上行 AC（可选）
      unarmored: 10 # 无甲 AAC = 10 + DEX 调整值
    attack_bonus: 0 # 上行 AC 系统攻击奖励
    thac0: 19 # 命中 AC 0 所需投骰
    combat_mod:
      melee: 2 # 近战攻击/伤害调整值 = STR 调整值
      missile: 1 # 投射攻击调整值 = DEX 调整值
    movement:
      base: 120 # 基础移动速率（英尺），受负载影响
      exploration: "120'" # 探索移动 = 基础（英尺/回合）
      encounter: "40'" # 遭遇移动 = 基础 ÷ 3（英尺/轮）
      overland: 24 # 长途跋涉 = 基础 ÷ 5（英里/天）
    stats:
      STR: 16 # 近战攻击/伤害、开门
      INT: 10 # 语言、识字
      WIS: 12 # 魔法豁免调整值
      DEX: 14 # 投射攻击、AC、先攻
      CON: 14 # 生命值
      CHA: 8 # 反应、仆役数量、忠诚度
    modifiers: # 属性调整值速查（由属性值查表得出）
      STR: 2
      INT: 0
      WIS: 0
      DEX: 1
      CON: 1
      CHA: -1
    saves: # 五类豁免值（d20 ≥ 此值成功）
      D: 12 # 死亡/毒素
      W: 13 # 魔杖
      P: 14 # 麻痹/石化
      B: 15 # 喷吐攻击
      S: 16 # 法术/权杖/法杖
      wis_mod: 0 # 魔法豁免的睿知调整值
    encounter:
      initiative_mod: 1 # 先攻调整值 = DEX 调整值（可选规则）
      reaction_mod: -1 # 反应投骰调整值 = CHA 调整值
    exploration: # 探索技能（X-in-6）
      listen: 1 # 聆听门后（1/6，矮人/精灵/半身人可能不同）
      open_doors: 2 # 打开卡住的门（基于 STR）
      secret_doors: 1 # 发现暗门（1/6，精灵 2/6）
      find_traps: 1 # 发现房间陷阱（1/6，矮人 2/6）
    languages:
      list: [通用语]
      literate: true # 识字（INT 决定：3=文盲，4-5=简单读写，6+=正常识字）
    equipment:
      weapons:
        - { name: 长剑, dmg: 1d8, type: melee, range: null }
      armor: { name: 链甲, ac: 5, aac: 14 }
      shield: { name: 盾牌, ac_bonus: -1, aac_bonus: +1 }
      other: [背包, 火把×6, 铁口粮×7日, 水袋, 绳索50']
    magic_items: [] # 魔法物品（独立于普通装备）
    coins: # 钱币（1 枚 = 1 钱币重量单位）
      pp: 0 # 白金币（1 pp = 5 gp）
      gp: 0 # 金币
      ep: 0 # 银金币（1 ep = ½ gp）
      sp: 0 # 银币（1 sp = 1/10 gp）
      cp: 0 # 铜币（1 cp = 1/100 gp）
    treasure: [] # 非钱币财宝（宝石、珠宝、艺术品等）
    encumbrance: # 负载（可选规则）
      treasure_weight: 0 # 财宝与钱币的重量（钱币单位）
      equipment_weight: 0 # 武器、护甲和其他装备的重量
      total: 0 # 总负载重量（上限 = 1600 钱币）
    spells: null # 非施法者为 null
    class_features: []
    notes: ""
```

## 施法者法术模板

### 神术施法者（牧师 / 德鲁伊）

```yaml
spells:
  slots: # 每日可记忆法术数
    "1": 1 # 1级法术 1个
  memorized: # 当日已记忆的法术（用完即止）
    - { name: 治愈轻伤, level: 1, used: false }
  spellbook: null # 神术施法者无法术书，可自由选择记忆
```

牧师使用牧师法术列表，德鲁伊使用德鲁伊法术列表（吟游诗人也使用德鲁伊法术列表）。

### 奥术施法者（魔法师 / 精灵 / 死灵法师）

```yaml
spells:
  slots:
    "1": 1
  memorized:
    - { name: 魔法飞弹, level: 1, used: false }
  spellbook: # 法术书中已知法术
    - { name: 魔法飞弹, level: 1 }
    - { name: 护盾, level: 1 }
    - { name: 阅读魔法, level: 1 }
```

### 幻术施法者（幻术师 / 侏儒）

```yaml
spells:
  slots:
    "1": 1
  memorized:
    - { name: 变色术（Colour Spray）, level: 1, used: false }
  spellbook: # 法术书中已知法术
    - { name: 变色术（Colour Spray）, level: 1 }
```

幻术师和侏儒使用幻术师法术列表。

## 仆役模板

```yaml
retainers:
  retainer_id:
    name: 仆役名
    class: Fighter
    level: 1
    hp: [6, 6]
    ac: 6
    aac: 13
    morale: 7 # 基础 7 + 雇主 CHA 调整值
    wage: "25 gp/月"
    share: "半份 XP 和宝藏"
    equipment:
      weapons:
        - { name: 矛, dmg: 1d6 }
      armor: { name: 皮甲, ac: 7, aac: 12 }
    notes: ""
```

## 升级 XP 对照表

### 人类职业

| 职业                  |   2级 |   3级 |    4级 |
| --------------------- | ----: | ----: | -----: |
| 杂技师（Acrobat）     | 1,200 | 2,400 |  4,800 |
| 刺客（Assassin）      | 1,500 | 3,000 |  6,000 |
| 蛮族（Barbarian）     | 2,500 | 5,000 | 10,000 |
| 吟游诗人（Bard）      | 2,000 | 4,000 |  8,000 |
| 牧师（Cleric）        | 1,500 | 3,000 |  6,000 |
| 德鲁伊（Druid）       | 2,000 | 4,000 |  8,000 |
| 战士（Fighter）       | 2,000 | 4,000 |  8,000 |
| 幻术师（Illusionist） | 2,500 | 5,000 | 10,000 |
| 骑士（Knight）        | 2,500 | 5,000 | 10,000 |
| 魔法师（Magic-User）  | 2,500 | 5,000 | 10,000 |
| 圣武士（Paladin）     | 2,750 | 5,500 | 12,000 |
| 游侠（Ranger）        | 2,250 | 4,500 |  9,000 |
| 盗贼（Thief）         | 1,200 | 2,400 |  4,800 |

### 种族职业（Race-as-Class）

| 职业                  |   2级 |   3级 |    4级 |
| --------------------- | ----: | ----: | -----: |
| 卓尔（Drow）          | 4,000 | 8,000 | 16,000 |
| 灰矮人（Duergar）     | 2,800 | 5,600 | 11,200 |
| 矮人（Dwarf）         | 2,200 | 4,400 |  8,800 |
| 精灵（Elf）           | 4,000 | 8,000 | 16,000 |
| 侏儒（Gnome）         | 3,000 | 6,000 | 12,000 |
| 半精灵（Half-Elf）    | 2,500 | 5,000 | 10,000 |
| 半身人（Halfling）    | 2,000 | 4,000 |  8,000 |
| 半兽人（Half-Orc）    | 1,800 | 3,600 |  7,000 |
| 深侏儒（Svirfneblin） | 2,400 | 4,800 | 10,000 |

## 属性调整值表

| 属性值 | 调整值 |
| -----: | -----: |
|      3 |     –3 |
|    4–5 |     –2 |
|    6–8 |     –1 |
|   9–12 |      0 |
|  13–15 |     +1 |
|  16–17 |     +2 |
|     18 |     +3 |

## 开门概率（基于 STR）

|   STR | 开门 |
| ----: | ---: |
|   3–8 |  1/6 |
|  9–12 |  2/6 |
| 13–15 |  3/6 |
| 16–17 |  4/6 |
|    18 |  5/6 |

## 主要属性 XP 调整值

| 首要属性值 | XP 调整 |
| ---------: | ------: |
|        3–5 |    –20% |
|        6–8 |    –10% |
|       9–12 |      0% |
|      13–15 |     +5% |
|      16–18 |    +10% |

## 负载与移动速率

| 负载（钱币） | 基础移动 |      探索 |   遭遇 |       长途 |
| -----------: | -------: | --------: | -----: | ---------: |
|        ≤ 400 |     120' | 120'/回合 | 40'/轮 | 24 英里/天 |
|        ≤ 600 |      90' |  90'/回合 | 30'/轮 | 18 英里/天 |
|        ≤ 800 |      60' |  60'/回合 | 20'/轮 | 12 英里/天 |
|       ≤ 1600 |      30' |  30'/回合 | 10'/轮 |  6 英里/天 |
