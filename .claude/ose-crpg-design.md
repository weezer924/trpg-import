# OSE CRPG 游戏设计文档

> 基于 Old-School Essentials 规则的老派 CRPG 设计方案。
> 产品形态：规则引擎 + 编辑器 + Mod 支持，类似 Neverwinter Nights 对 D&D 3e 的做法。

---

## 1. 设计哲学

### 1.1 忠实还原，不做妥协

**规则书怎么写，引擎就怎么跑。** 不为迎合现代玩家习惯而提供便利化替代或降低难度。

- **下降式 AC + THAC0** 为底层计算（UI 可选显示 AAC）
- **3d6 按序生成属性**，不可自由分配
- **XP 双来源**：宝物（1 GP = 1 XP，魔法物品不算）+ 击败怪物（按 HD 查表）。书中明确指出宝物是主要来源，通常占 ¾ 以上。"击败"包括击杀、智取、俘获、吓跑等方式
- **资源管理是核心玩法**：火把（6 turn）、灯笼（24 turn + 油）、口粮、水、弹药，全部严格追踪。用完就是用完，没有无限光源
- **负重严格计算**：按 coin 重量单位计算，超重直接降低移动速率。不提供简化负重选项
- **角色极度脆弱**：1 级 Magic-User 只有 1d4 HP。没有"掷到 1 或 2 可重掷"的保护机制。死了就是死了
- **遭遇不做平衡**：随机遭遇表决定出现什么怪物，不考虑队伍等级。3 级队伍碰到龙是完全可能的，正确决策是跑
- **等级上限不可取消**：亚人类的等级天花板是规则的一部分，不提供取消选项。这是选择亚人类的代价
- **没有自动存档 / 随时存档**：只在安全地点（城镇、营地）允许存档，防止 save scum。死亡有重量

### 1.2 模块化 + 开放平台

提供系统和工具，让社区创造内容：

- **规则引擎**：OSE 规则的完整实现
- **编辑器**：地下城/荒野/城镇地图、遭遇、NPC、事件脚本
- **Mod 系统**：新职业、种族、法术、怪物、物品、战役模组均可通过数据文件添加

### 1.3 可选规则

仅保留 OSE 书中明确标注为"Optional Rule"的规则作为可配置项。这些是**书中原有的可选规则**，不是我们发明的便利化选项：

- 个人先攻（默认团体先攻）
- Variable Weapon Damage（默认所有武器 1d6）
- Weapon Proficiency（武器熟练，Advanced）
- Secondary Skills（副业技能，Advanced）
- Multiple Classes（多职业，Advanced）
- Lifting Class and Level Restrictions（取消种族等级上限，Advanced，需同时启用 Human 可选种族能力）
- Morale（士气，默认启用）

以下**不作为可选项**，而是硬编码为默认行为：

- 严格负重计算（不提供简化模式）

Mod 作者可在模组配置中指定哪些可选规则必须启用/关闭。

---

## 2. 开发路线

### Phase 1：Classic

以 OSE Classic Fantasy 为基础，实现完整游戏系统。

**职业（7 个，种族即职业）**：

| 职业 | HD | 护甲 | 武器 | Prime Req | 最高等级 |
|------|----|------|------|-----------|---------|
| Cleric | d6 | 全部 | 钝器 | WIS | 14 |
| Dwarf | d8 | 全部 | 小型/普通 | STR | 12 |
| Elf | d6 | 全部 | 全部 | INT & STR | 10 |
| Fighter | d8 | 全部 | 全部 | STR | 14 |
| Halfling | d6 | 全部 | 小型/普通 | DEX & STR | 8 |
| Magic-User | d4 | 无 | 仅匕首 | INT | 14 |
| Thief | d4 | 皮甲 | 全部 | DEX | 14 |

**法术系统（2 套列表）**：

- Cleric：1-5 级法术
- Magic-User：1-6 级法术

**核心系统**：

- 属性值与调整值
- 战斗（THAC0 / 攻击矩阵、先攻、士气、远程/近战）
- 豁免检定（5 类）
- 探索（地下城 10 分钟 turn 制、荒野、航海）
- 遭遇流程（距离 → 惊讶 → 反应掷骰 → 先攻 → 战斗/谈判/逃跑）
- 经验值与升级
- 负重与移动
- 装备与经济
- 随从（Retainer）系统
- 雇佣兵与专家
- 据点建造与领地管理

### Phase 2：Advanced

在 Classic 基础上扩展，不改动核心引擎。

**新增内容**：

- 种族/职业分离（13 个职业 + 10 个种族，可自由组合）
- 多职业系统（最多 3 个职业，XP 分配、HP 减半、取最优豁免/THAC0）
- 6 个新人类职业：Acrobat, Assassin, Barbarian, Bard, Knight, Paladin, Ranger
- 4 个新亚人类种族：Drow, Duergar, Gnome, Half-Elf, Half-Orc, Svirfneblin
- 2 套新法术列表：Druid（1-5 级）、Illusionist（1-6 级）
- 毒药系统（血液毒 4 级 + 摄入毒 5 级）
- 武器熟练子系统
- 副业技能（30 种中世纪职业）

**架构影响**：主要是加数据。唯一需要新增的机制是多职业系统（Phase 1 预留接口）。

### Phase 3：官方扩展与 Mod 生态

- 支持官方扩展（如 Necrotic Tome 的 Necromancer 职业 + 72 个死灵法术）
- 开放 Mod 工具
- 社区战役模组

---

## 3. 数据架构

所有游戏内容均为外部数据文件（JSON/YAML），引擎不硬编码任何具体职业、法术、怪物。

### 3.1 角色相关

**职业（Class）**：

```yaml
id: fighter
name: Fighter
hit_die: d8
max_level: 14
prime_requisite: [STR]
armour: all
weapons: all
languages: [alignment, common]
thac0_progression: [19,19,19,17,17,17,14,14,14,12,12,12,10,10]
saving_throws:
  1: { death: 12, wands: 13, paralysis: 14, breath: 15, spells: 16 }
  4: { death: 10, wands: 11, paralysis: 12, breath: 13, spells: 14 }
  # ...
spell_lists: []          # 无法术
special_abilities: []
# Advanced 模式下的种族等级限制
race_level_limits:
  dwarf: 10
  elf: 7
  halfling: 6
  # human: unlimited (默认)
```

**种族（Race）**：

```yaml
id: elf
name: Elf
requirements: { INT: 9 }
ability_modifiers: { CON: -1, DEX: +1 }
languages: [alignment, common, elvish, gnoll, hobgoblin, orcish]
abilities:
  - detect_secret_doors: { chance: 2-in-6 }
  - ghoul_paralysis_immunity: true
  - infravision: 60
  - listen_at_doors: { chance: 2-in-6 }
available_classes: [acrobat, assassin, cleric, druid, fighter, knight, magic-user, ranger, thief]
```

Classic 模式下，种族即职业的 Elf/Dwarf/Halfling 是将种族能力和职业能力合并在一个 class 定义中。Advanced 模式下拆分为独立的 race + class。

### 3.2 法术系统

**法术（Spell）** — 独立实体：

```yaml
id: protection_from_evil
name: Protection from Evil
range: 0 (self)
duration: 6 turns       # Magic-User 版
                         # Cleric 版 12 turns，在 spell_list_entry 中覆盖
description: ...
reversible: true
reverse_name: Protection from Evil 10' Radius  # 如果有
```

**法术列表（Spell List）** — 引用集合，关联职业与法术：

```yaml
id: necromancer_spells
name: Necromancer Spell List
entries:
  1:  # 1级法术
    - spell: chill_touch
    - spell: command_dead
    - spell: protection_from_evil   # 共享法术
    - spell: read_magic             # 共享法术
    # ...
  2:  # 2级法术
    - spell: bone_armour
    - spell: detect_magic           # 在 MU 列表里是 1 级，这里是 2 级
    # ...
```

同一个法术可以出现在多个列表中，且等级可以不同（如 Detect Magic 在 Magic-User 是 1 级，在 Necromancer 是 2 级）。

### 3.3 物品与怪物

**物品标签系统**：

```yaml
id: ring_of_controlling_animals
name: Ring of Controlling Animals
type: ring
tags: [magic, targets_living, non_necromantic]
# Necromancer 的物品过滤规则可据此判断能否使用
```

**怪物（Monster）**：

```yaml
id: skeleton
name: Skeleton
hd: 1
ac: 7 [12]
attacks: [{ name: weapon, damage: 1d6 }]
thac0: 19 [0]
movement: 60 (20)
saving_throws: { death: 12, wands: 13, paralysis: 14, breath: 15, spells: 16 }
morale: 12
alignment: chaotic
xp: 10
tags: [undead]
treasure_type: none
special: [undead_immunities]
```

### 3.4 遭遇表与宝物表

均为可扩展的数据表，Mod 可以追加条目：

```yaml
# Mod 可以往现有遭遇表追加条目
extends: dungeon_encounter_level_1
additions:
  - weight: 1
    monster: skeletal_servant    # Necromancer 模组新增怪物
```

---

## 4. Mod 系统设计

### 4.1 Mod 能做什么

| 操作 | 说明 | 示例 |
|------|------|------|
| **添加** | 新实体 | 新职业 Necromancer、新法术 Chill Touch、新怪物 |
| **扩展** | 往现有集合追加 | 把死灵法术加入 Magic-User 法术列表 |
| **覆盖** | 替换现有实体的部分字段 | 修改 Fighter 的 max_level |
| **配置** | 指定规则开关 | 此模组要求启用 Variable Weapon Damage |

### 4.2 Mod 结构

```
my_mod/
  mod.yaml           # 元数据：名称、作者、依赖、规则开关要求
  classes/            # 新职业定义
  races/              # 新种族定义
  spells/             # 新法术定义
  spell_lists/        # 新法术列表或对现有列表的扩展
  monsters/           # 新怪物
  items/              # 新物品
  tables/             # 遭遇表、宝物表扩展
  maps/               # 地图数据
  scripts/            # 事件脚本
```

### 4.3 加载顺序

1. Core（Classic 基础规则数据）
2. Advanced（如果启用）
3. Mod（按依赖顺序加载，后加载的可以扩展/覆盖先加载的）

---

## 5. 桌游到电子游戏的关键翻译

### 5.1 探索系统

桌游的地下城探索是 10 分钟/turn 的回合制。电子游戏实现方案：

- 地下城内采用回合制探索，每步消耗时间
- 每个 turn 结算：火把耗时、随机遭遇掷骰、徘徊怪物
- 荒野旅行按天结算（每日行军距离 = 基础移动速率 ÷ 5 英里）

### 5.2 遭遇流程

必须完整实现，这是老派游戏的核心体验：

1. **遭遇距离**掷骰（地下城 2d6×10'，荒野按地形）
2. **惊讶判定**（双方各 2-in-6）
3. **NPC 反应掷骰**（2d6 + CHA 调整）→ 不是所有遭遇都要打
4. **先攻**（每轮 1d6 团体先攻）
5. **战斗**（攻击、法术、移动、撤退/逃跑）
6. **士气检定**（首次阵亡时 + 半数倒下时，2d6 ≤ 士气值则继续战斗）

NPC 反应掷骰特别重要 — 很多遭遇可以通过谈判、贿赂、威吓解决，而不是战斗。

### 5.3 随从（Retainer）系统

老派游戏队伍不只是 PC。完整实现：

- CHA 决定最大随从数和忠诚度调整
- 随从有独立的职业/等级/HP/士气
- 忠诚度检定（危险情况、分赃不公时）
- 随从可能叛变、逃跑、拒绝执行危险命令
- 雇佣兵（纯战斗用，不进地下城）和专家（铁匠、贤者、间谍等）

### 5.4 开放式问题解决

桌游中玩家可以自由描述行动，DM 裁定结果。电子游戏无法完全复刻，但可以通过丰富的环境交互来近似：

- OSE 装备表中的实用物品都应该有对应的交互功能：
  - 撑杆（10' pole）→ 探测地板陷阱
  - 铁钉（iron spikes）→ 钉门防止怪物追来
  - 油瓶（oil flask）→ 泼地点火制造火墙
  - 绳索（rope）→ 攀爬、捆绑、制作陷阱
- 编辑器应支持 Mod 作者定义物品-环境交互规则

---

## 6. 参考规则来源

| 来源 | 用途 | 路径 |
|------|------|------|
| OSE Classic Fantasy Rules Tome | 核心规则（Phase 1） | `source/OSE/` |
| OSE Advanced Fantasy Player's Tome | 高级选项（Phase 2） | `source/OSE/OSE Advanced/` |
| OSE Necrotic Tome / Necromancer | Mod 系统验证参考 | `source/OSE/Settings/` |
| D&D Mentzer Basic Red Box | 规则对照参考 | `source/D&D Mentzer Classic Basic/` |

OSE 基于 OGL（Open Game License v1.0a）发行。

---

## 7. 与 B/X 原版及 Mentzer 的关系

OSE Classic 是 B/X D&D (Moldvay/Cook 1981) 的忠实复刻：

- 核心机制、数值完全一致（属性调整表、豁免值、XP 需求、THAC0 等）
- OSE 修正了原版的明显错误和歧义
- OSE 的编排是参考手册式（按主题分章），而非 Mentzer 的教学式编排
- 等级范围 1-14（Basic 1-3 + Expert 4-14）
- Mentzer 15 级以上的内容（Companion/Master/Immortal）不在 OSE 范围内

OSE Advanced 额外融入了 AD&D 1e 的元素（种族/职业分离、新职业、新法术系），但核心引擎仍然是 B/X。
