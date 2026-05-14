# matches/roster-template: 战团构建模板（Warband Roster Template）

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.144-150（Scenario Format 预算）+ `Warbands of Trench Crusade v1.0.2.pdf` p.21-23 / 103（Warband Creation）+ `Warband Roster Sheet.pdf`（仅参考布局）
> 版本：v0.1（PDF v1.0.2 对齐）
>
> **用途**：玩家（人类）构建一个合法 v0.1 战团的步骤模板。所有 faction-specific 数值（unit cost / armoury / 特殊规则）**只引用**对应 warband 文件，不复述。

## Index

- [1. 预算 Budget](#1-预算-budget)
- [2. 招募流程（6 步）](#2-招募流程6-步)
- [3. 装备槽 Equipment Slots / Armoury](#3-装备槽-equipment-slots--armoury)
- [4. Cost 公式 与 VP 计算（v0.1 单场）](#4-cost-公式-与-vp-计算v01-单场)
- [5. Roster yaml schema](#5-roster-yaml-schema)
- [6. 校验清单（玩家自查 10 条）](#6-校验清单玩家自查-10-条)
- [7. 示例 Roster A — New Antioch](#7-示例-roster-a--new-antioch)
- [8. 示例 Roster B — Heretic Legions](#8-示例-roster-b--heretic-legions)
- [跨文件引用速查](#跨文件引用速查)

---

## 1. 预算 Budget

引用 `→ ../rules/08-scenarios.md §1.1 准备对战 Preparing to Play`（PDF p.145）。

| 经验阶段 | 建议预算 | 备注 |
|---|---:|---|
| 新手第一场 | **700 👑** | 此场可计入后续 Campaign 第一局 |
| 有经验后（单场标准） | **800 👑 + 6 ☼** | 提供足够选择不至于战团失控 |

**☼（Glory Points）单场使用约定**（PDF p.144-145 + v0.1 简化）：

- ☼ **完整用法**属 Campaign Rules（v0.2.A backlog）——可花在 Mercenaries / Glory Items / Battlekit
- **v0.1 单场默认**：双方协商；若未协商 → **不允许花 ☼ 招募 Mercenaries / 购买 Glory Items**（这两类是 v0.2 内容）
- 已含 ☼ 价格的物品（如 `Sacrificial Blade` 23 👑、`Heavy Flamethrower` 55 👑 等以 👑 计价的；以 ☼ 计价的如 `Hellblade` 1 ☼、`Blasphemous Staff` 2 ☼）→ v0.1 单场如允许花 ☼，按列示 ☼ 数支付，否则该物品不可购入

> ☼ vs 👑 区分：👑 = Ducat（招募成本）； ☼ = Glory Point（战役长线 / 单场胜负 VP）。**v0.1 单场预算结算只算 👑**。

---

## 2. 招募流程（6 步）

### 步 1：选 Faction

v0.1 仅 **2 个 Faction**：

| Faction | 阵营 Alignment | 起始 👑 | 详细 |
|---|---|---:|---|
| **New Antioch（新安提阿公国）** | Faithful（圣教方） | 700 👑 | `→ ../warbands/01-new-antioch.md` |
| **Heretic Legions（异端军团）** | Fallen（地狱方） | 700 👑 | `→ ../warbands/02-heretic-legions.md` |

> 其余 4 Faction（Trench Pilgrims / The Sultanate of the Iron Wall / The Cult of the Black Grail / The Court of the Seven-Headed Serpent）属 v0.2.B backlog。

### 步 2：选 Variant（可选）

每个 faction 含数个 variants，改写主战团的部分规则（招募规则 / armoury / 单位升级 / 特殊异能）。

| Faction | v0.1 含 Variants | 跳转 |
|---|---|---|
| New Antioch | Papal States / Éire Rangers / Alba / Abyssinia（4 个） | `→ ../warbands/01-new-antioch.md#warband-variants` |
| Heretic Legions | Trench Ghosts / Knights of Avarice / Heretic Naval Raiders（3 个） | `→ ../warbands/02-heretic-legions.md#warband-variants` |

- 选 variant 后，主战团的 [Faction Special Rules] + [Armoury Tables] 默认继承（除非 variant 明确改写）
- variant 通常加 1-3 条特殊规则、解锁 unique battlekit、改 mandatory composition

### 步 3：满足 Mandatory Composition（必选单位）

每个 faction 强制必含的单位：

| Faction | Mandatory | 备注 |
|---|---|---|
| New Antioch | **1 Lieutenant** | Papal States variant 改为 **1 Trench Cleric** |
| Heretic Legions | **1 Heretic Priest** | 无 variant 改写 |

详见各 faction 文件的 [Warband Creation] 节。

### 步 4：在预算内招募 Troops + Elites

- 每个单位有 **Type**（Elite / Troops）、**Cost**、**Limit**（招募上限）
- **总模型数推荐 6-10 个**（规则强制范围，见 PDF p.74「Quick Start」）
- 单位 stats（M / Ranged / Melee / Armour / Keywords / Base）写在 warband 文件的 yaml profile 块里

**Troop / Elite 数量约束**（一般规则）：

- Elite 数量受单位 Limit 字段约束（如 Lieutenant Limit: 1、Sniper Priest Limit: 0-2）
- Troops 数量除单位自身 Limit 外，受总预算 + 总模型数 10 约束
- 部分单位有"规模门槛"：如 `Trench Mole` 第 3 个需 Warband 总成本 ≥ 1,000 👑、`Artillery Witch` 第 2 个同要求
- 例外见 `→ ../errata/rules-commentaries.md`

### 步 5：为每个单位购买 Battlekit

每个单位有 Battlekit slots（**装备槽**）。Battlekit 数据见 `→ ../rules/05-battlekit.md` + 各 faction 的 `[• Unique Battlekit]` 节。

详见 §3 装备槽。

### 步 6：（可选）标 Fireteam / 升级 / mandatory battlekit

某些 faction 有额外步骤：

- **New Antioch Fireteams**：可标记最多 2 个 Fireteam（每个 2 模型），获 `FIRETEAM` keyword（不花 👑）。Stosstruppen variant 升至 3 个。详见 `→ ../warbands/01-new-antioch.md#faction-special-rules`
- **Heretic Trooper → Legionnaire**：+10 👑 升级（不超过 Trooper 数）
- **Yeoman → Trench Mole**：+10 👑 升级（最多 2，第 3 个需 1,000 👑+ 总值）
- **Mandatory Battlekit**：如 Combat Engineer 必带 Engineer Body Armour + Shovel；Combat Medic 必带 Standard Armour + Gas Mask + Medi-kit + Misericordia；Mechanized Heavy Infantry 必带 Reinforced or Machine Armour；Anointed Heavy Infantry 必带 Reinforced Armour + Infernal Brand；Artillery Witch 必带 Infernal Bombs。**这些已含 Cost 中**（cost 字段已包含 mandatory battlekit）

---

## 3. 装备槽 Equipment Slots / Armoury

### 3.1 通用装备槽

PDF v1.0.2 没有"装备槽数量"的明确硬规则，而是用以下约束组合：

- **每个单位**可有：1 ranged weapon + 1 melee weapon（或 2 melee，副手算 Off-Hand `-1 DICE`）+ 1 shield + 1 grenade type + 1 armour + 任意 equipment（受 Limit / stipulation 限制）
- **武器 keywords 约束**：`CUMBERSOME` 武器无法同时拿 shield；`HEAVY` 武器一个单位最多 1 件（特殊单位如 Shock Trooper、Combat Engineer 有 Ignore-HEAVY 豁免）
- **Bayonet Lug**：某些 ranged 武器（Bolt-Action Rifle / Semi-Automatic Rifle 等）的 stipulation 允许同时挂 Bayonet（Shield Combo + Bayonet）

详见 `→ ../rules/05-battlekit.md`（全武器 / 装备数据） + 各 faction 的 [Armoury Tables] 节（stipulation 在 faction-specific 处加）。

### 3.2 Faction-specific Armoury

每个 faction 有自己的 **Armoury Tables**（武器价格 + stipulation 表）。同一件 battlekit 在不同 faction 的 stipulation 可能不同（→ `→ ../errata/rules-commentaries.md` BK Q1）。

- New Antioch Armoury → `→ ../warbands/01-new-antioch.md#armoury-tables`
- Heretic Legions Armoury → `→ ../warbands/02-heretic-legions.md#armoury-tables`

**[•] 标记**：表示该 battlekit 是 **faction-unique**（仅本 faction 可用）。其规则在该 faction 文件的 `[Faction] Battlekit (unique)` 节，不在共享 `rules/05-battlekit.md` 里。

### 3.3 共享 vs Unique 关系图

```
所有 faction 都可用                          仅 faction-specific
─────────────────────                         ─────────────────────
rules/05-battlekit.md     ←──── shared ───→    warbands/01 [•] / 02 [•]
  · Bolt-Action Rifle 10 👑                      · Heavy Ballistic Shield (NA only)
  · Frag Grenades 7 👑                           · Machine Armour (NA only)
  · Standard Armour 15 👑                        · Hellblade (HL only)
  · Trench Knife 1 👑                            · Tartarus Claws (HL only)
  ...                                            ...
```

faction 文件的 Armoury Tables 列出该 faction 可购的**所有** battlekit（共享 + unique 都列），并标 `[•]` 区分 unique。**stipulation / cost 以 faction 文件为准**（同件物品在不同 faction 可有不同 stipulation）。

---

## 4. Cost 公式 与 VP 计算（v0.1 单场）

### 4.1 模型总成本公式

```
model_total_cost = unit_base_cost + Σ(equipment_cost) + Σ(upgrade_cost)
warband_total_cost = Σ(model_total_cost)
```

- `unit_base_cost`：取自 warband 文件 yaml profile 的 `cost` 字段
- `equipment_cost`：取自该单位选购的 ranged / melee / shield / grenade / armour / equipment 价格
- `upgrade_cost`：如 Yeoman → Trench Mole +10 👑、Heretic Trooper → Legionnaire +10 👑
- **mandatory battlekit 已含在 unit base cost**：不要再加（如 Combat Engineer 80 👑 已含 Engineer Body Armour + Shovel）

**预算约束**：`warband_total_cost ≤ budget`（700 或 800 👑）。

### 4.2 VP 计算（单场胜负）

**关键修正**：v0.1 单场 **不用** `👑÷10、☼÷3` 之类的模型成本 VP 公式——那属 Campaign Rules（PDF p.99，v0.2.A backlog）。

v0.1 单场的 VP 完全由所选 **scenario** 的 Victory Points 条目决定：

| Scenario | VP 条目 | 引用 |
|---|---|---|
| **Scenario I — Claim No Man's Land** | 每回合末每控制 1 Objective = **2 VP**；游戏末每完成 1 Glorious Deed = **1 VP** | `→ ../rules/08-scenarios.md §2.5` |
| **Scenario II — Hunt for Heroes** | Marks（敌方暗藏目标）/ Assets（己方暗藏目标）+ Glorious Deeds — 详 scenario | `→ ../rules/08-scenarios.md §3` |

**即胜条件**：战场上无敌方模型 / 敌方战团 Morale 失败逃跑 → 立即获胜（不论 VP）。

**Glorious Deeds 简化**：单场每完成 1 项 Deed = **1 VP**（已与 PDF p.153/156/160 对齐；非 10 VP）。战后**不结算** ☼ / EXP / Promotion Pool（这些是 Campaign Rules）。

---

## 5. Roster yaml schema

参考 `→ ./match-template.yaml` §4 的 models 节。Roster 文件是战团构建产物，部署后会被 merge 进 `match-state.yaml` 的 `models[]`。

### 5.1 单文件 schema

```yaml
# matches/{name}/roster-{side}.yaml
warband:
  name: "Duke's Forlorn Hope"          # 玩家命名
  side: red                             # red | blue（match 内角色，与 faction 解耦）
  faction: new-antioch                  # → warbands/01-new-antioch.md
  variant: null                         # null | papal-states | eire-rangers | alba | abyssinia
  alignment: Faithful                   # Faithful | Fallen（v0.2+ Mercenaries 可中立）
  budget:
    ducats: 700                          # 👑 预算上限
    glory_points: 0                      # ☼ 预算（v0.1 单场默认 0）
  spent:
    ducats: 695                          # 实际花费（玩家或 MCP 计算后填）
    glory_points: 0

# Fireteams（仅 New Antioch）— Pass 8 §FIRETEAM
fireteams:
  - id: ft_alpha
    members: [red.shock_trooper_1, red.yeoman_1]
  - id: ft_bravo
    members: [red.yeoman_2, red.yeoman_3]

# 模型列表 — 复用 match-template.yaml §4 schema
models:
  - id: red.lieutenant
    side: red
    profile: lieutenant                  # → warbands/01-new-antioch.md#lieutenant
    base_cost: 70                        # unit base cost in 👑
    base_size: [1, 1]                    # grid 占用，→ coordinate-system.md §5
    base_shape: circle                   # 视觉层
    base_dimensions_mm: [32, 32]
    equipment:
      ranged: blessed-revolver           # → rules/05-battlekit.md or faction Battlekit
      melee: blessed-sabre
      armour: standard-armour
      shield: null
      grenade: null
      equipment: [combat-helmet, binoculars]
    equipment_cost: 35                   # Σ equipment 👑（不含 mandatory battlekit）
    total_cost: 105                      # base + equipment + upgrades
    # 部署后由 match-state.yaml 填充：pos / markers / activated
```

### 5.2 跨字段约束

- `fireteams[*].members` 只能引用 `models[*].id`，且必须属于 New Antioch faction
- 每个 model 的 `equipment` 必须在该 faction 的 [Armoury Tables] 内且符合 stipulation
- `total_cost` 加总必须 ≤ `budget.ducats`
- Mandatory battlekit 在 yaml 中可显式列也可省略（base_cost 已含），**MCP 校验时按 warband 文件的 `mandatory_battlekit` 字段补全**

---

## 6. 校验清单（玩家自查 10 条）

部署前自查（也是 MCP `validate_roster` 接口该实现的检查）：

- [ ] 1. **预算未超**：`Σ total_cost ≤ budget.ducats`（700 或 800 👑）
- [ ] 2. **模型数 6-10**：`6 ≤ len(models) ≤ 10`
- [ ] 3. **Mandatory composition**：含必选单位（New Antioch = 1 Lieutenant / Papal States = 1 Trench Cleric / Heretic Legions = 1 Heretic Priest）
- [ ] 4. **单位 Limit**：每个 unit 的数量未超其 Limit 字段（如 Lieutenant ≤ 1、Sniper Priest ≤ 2、Death Commando ≤ 1）
- [ ] 5. **装备 stipulation 满足**：每个 equipment 在该 faction Armoury 内、对应单位类型允许（如 `ELITE only` / `Combat Engineer only` / `Death Commando only`）、未超 Limit
- [ ] 6. **武器 keywords 不冲突**：无 `CUMBERSOME` + shield 同装、`HEAVY` 武器 ≤ 1 件（Shock Trooper / Combat Engineer 除外）
- [ ] 7. **基座 / 视觉字段**：每个非默认 base 标了 `base_shape` + `base_dimensions_mm`（默认 circle + [28,28] 可省）
- [ ] 8. **Fireteams**（New Antioch）：≤ 2 个（Stosstruppen variant ≤ 3），每个 Fireteam **正好 2 模型**，模型仅属于 1 个 Fireteam
- [ ] 9. **规模门槛**：触发"需 1,000 👑+"门槛的单位（Trench Mole 第 3 个、Artillery Witch 第 2 个）的条件已满足
- [ ] 10. **☼ 预算约定**：双方在 match 开始前已就 ☼ 单场使用约定达成一致（默认不允许）

---

## 7. 示例 Roster A — New Antioch

**战团**："Duke's Forlorn Hope"（公爵的孤注一掷队）
**Faction**：New Antioch · **Variant**：无（主战团）· **预算**：700 👑

### 7.1 招募明细

| # | Unit | Type | Base | Equipment | Equip 👑 | Total 👑 |
|---|---|---|---:|---|---:|---:|
| 1 | **Lieutenant**（mandatory）| Elite | 70 | Bolt-Action Rifle (10) + Standard Armour (15) + Combat Helmet (5)＊ | 30 | 100 |
| 2 | Sniper Priest | Elite | 50 | Sniper Rifle (35) + Trench Knife (1) | 36 | 86 |
| 3 | Shock Trooper | Troops | 45 | Bolt-Action Rifle (10) + Bayonet (2) + Standard Armour (15) | 27 | 72 |
| 4 | Yeoman | Troops | 30 | Bolt-Action Rifle (5＊＊) + Bayonet (2) | 7 | 37 |
| 5 | Yeoman | Troops | 30 | Bolt-Action Rifle (5＊＊) + Bayonet (2) | 7 | 37 |
| 6 | Yeoman | Troops | 30 | Bolt-Action Rifle (5＊＊) + Bayonet (2) | 7 | 37 |
| 7 | Yeoman | Troops | 30 | Bolt-Action Rifle (5＊＊) + Bayonet (2) | 7 | 37 |
| 8 | Yeoman | Troops | 30 | Shotgun (10) + Bayonet (2) + Trench Shield (10) | 22 | 52 |
| 9 | **Trench Mole**（Yeoman + INFILTRATOR upgrade）| Troops | 30 | Submachine Gun (30) + Trench Knife (1) + 10 (upgrade) | 41 | 71 |
| 10 | **Combat Engineer**（incl. Engineer Body Armour + Shovel 必带）| Troops | 80 | Shotgun (10) + Trench Knife (1) + Satchel Charge (15) | 26 | 106 |

> ＊ Lieutenant Battlekit slots 允许 any from Armoury Tables；上表武器选择是示例（无近战武器以省 👑；可改用 Sword/Axe 4 👑 等）。`Blessed Sabre` / `Blessed Revolver` 等"圣武器"是 faction-themed flavor 词汇（见 `→ ../narrative/world-primer.md`），**不在 New Antioch Armoury Table 中**——本示例只用 Armoury 内列出的物品，确保数据在 v0.1 内核验。
>
> ＊＊ **Yeoman 折扣**：Yeoman 可以 5 👑（而非标价 10 👑）购入 1 件 Bolt-Action Rifle。见 `→ ../warbands/01-new-antioch.md#yeoman`。
>
> Combat Engineer Cost = 80 已含 Engineer Body Armour + Shovel；上表 equipment 列只加额外的 Shotgun + Trench Knife + Satchel Charge。
>
> Trench Mole = 30 (Yeoman base) + 10 (upgrade) = 40 unit cost；表中第 1 列直接写 30 base + 表第 5 列把 10 写进 equipment_cost。

### 7.2 预算校验

```
Total = 100 + 86 + 72 + 37 + 37 + 37 + 37 + 52 + 71 + 106
      = 635 👑

预算上限 = 700 👑
余款 = 65 👑
```

- ✅ 1. 预算未超（635 ≤ 700）
- ✅ 2. 模型数 = 10（6 ≤ 10 ≤ 10）
- ✅ 3. Mandatory：1 Lieutenant ✓
- ✅ 4. Limits：Lieutenant 1/1、Sniper Priest 1/2、Shock Trooper 1/5、Yeoman 5/∞、Trench Mole 1/2、Combat Engineer 1/2
- ✅ 5. Stipulations：Sniper Rifle Limit 3 / Satchel Charge Limit 3 / Engineer Body Armour Combat-Engineer-only — 全符合
- ✅ 6. 无 CUMBERSOME + shield 冲突；无 HEAVY 武器
- ✅ 7. 全部 base_size [1,1]、视觉默认 25-32mm circle
- ✅ 8. Fireteams：示例标 2 个（见下）
- ✅ 9. Trench Mole 1 个 < 第 3 个门槛，不触发
- ✅ 10. ☼ = 0，无须协商

### 7.3 Fireteams 示例

```yaml
fireteams:
  - id: ft_alpha
    members: [shock_trooper_1, yeoman_1]     # 突击-步枪兵组合
  - id: ft_bravo
    members: [yeoman_4, yeoman_5]            # 散弹枪 + 步枪+盾 防御组
```

两个 Fireteam 可在战斗中触发 `New Antioch Fireteams` + `Concentrated Attack`（3 BLOOD MARKERS 转 Bloodbath Roll）。详 `→ ../warbands/01-new-antioch.md#faction-special-rules`。

### 7.4 yaml roster（节选 — 前 3 个模型）

```yaml
warband:
  name: "Duke's Forlorn Hope"
  side: red
  faction: new-antioch
  variant: null
  alignment: Faithful
  budget:
    ducats: 700
    glory_points: 0
  spent:
    ducats: 635
    glory_points: 0

fireteams:
  - id: ft_alpha
    members: [red.shock_trooper_1, red.yeoman_1]
  - id: ft_bravo
    members: [red.yeoman_4, red.yeoman_5]

models:
  - id: red.lieutenant
    profile: lieutenant
    base_cost: 70
    base_size: [1, 1]
    base_shape: circle
    base_dimensions_mm: [32, 32]
    equipment:
      ranged: bolt-action-rifle
      melee: bayonet
      armour: standard-armour
      equipment: [combat-helmet]
    equipment_cost: 30
    total_cost: 100

  - id: red.sniper_priest
    profile: sniper-priest
    base_cost: 50
    base_size: [1, 1]
    base_shape: circle
    base_dimensions_mm: [25, 25]
    equipment:
      ranged: sniper-rifle
      melee: trench-knife
    equipment_cost: 36
    total_cost: 86

  - id: red.shock_trooper_1
    profile: shock-trooper
    base_cost: 45
    base_size: [1, 1]
    base_shape: circle
    base_dimensions_mm: [25, 25]
    equipment:
      ranged: bolt-action-rifle
      melee: bayonet
      armour: standard-armour
    equipment_cost: 27
    total_cost: 72
  # ... 其余 7 模型同构
```

---

## 8. 示例 Roster B — Heretic Legions

**战团**："The Sevenfold Maw"（七重利齿连）
**Faction**：Heretic Legions · **Variant**：无（主战团）· **预算**：700 👑

### 8.1 招募明细

| # | Unit | Type | Base | Equipment | Equip 👑 | Total 👑 |
|---|---|---|---:|---|---:|---:|
| 1 | **Heretic Priest**（mandatory）| Elite | 80 | Bolt-Action Rifle (10) + Sword/Axe (4) + Standard Armour (15) + Infernal Brand (5) | 34 | 114 |
| 2 | Death Commando | Elite | 90 | Silenced Pistol (15) + Trench Knife (1) | 16 | 106 |
| 3 | Heretic Trooper | Troops | 30 | Bolt-Action Rifle (10) + Bayonet (2) | 12 | 42 |
| 4 | Heretic Trooper | Troops | 30 | Bolt-Action Rifle (10) + Bayonet (2) | 12 | 42 |
| 5 | Heretic Trooper | Troops | 30 | Shotgun (10) + Trench Knife (1) | 11 | 41 |
| 6 | **Heretic Legionnaire**（Trooper + Melee+1 upgrade）| Troops | 30 | Great Sword/Axe (12) + Standard Armour (15) + 10 (upgrade) | 37 | 67 |
| 7 | Wretched | Troops | 25 | Trench Club (3) | 3 | 28 |
| 8 | Wretched | Troops | 25 | Trench Knife (1) + Bayonet (2) | 3 | 28 |
| 9 | Wretched | Troops | 25 | Trench Club (3) | 3 | 28 |
| 10 | War Wolf Assault Beast | Troops | 145 | (Chainsaw Mouth + Shredding Claws 内置 0 👑；无其他 battlekit) | 0 | 145 |

> Heretic Priest mandatory composition ✓。
>
> Heretic Legionnaire = Heretic Trooper base 30 + 10 upgrade = 40 unit cost。upgrade 选 Melee +1。
>
> Wretched battlekit 限 ≤ 10 👑 / 件，且**必须**至少 1 件武器。
>
> War Wolf 不可装外加 battlekit（Chainsaw Mouth + Shredding Claws 已包含）。
>
> `Infernal Brand` 详 `→ ../rules/05-battlekit.md#infernal-brand`。

### 8.2 预算校验

```
Total = 114 + 106 + 42 + 42 + 41 + 67 + 28 + 28 + 28 + 145
      = 641 👑

预算上限 = 700 👑
余款 = 59 👑
```

- ✅ 1. 预算未超（641 ≤ 700）
- ✅ 2. 模型数 = 10
- ✅ 3. Mandatory：1 Heretic Priest ✓
- ✅ 4. Limits：Heretic Priest 1/1、Death Commando 1/1、War Wolf 1/1、Wretched 3/∞、Heretic Trooper 3/∞、Heretic Legionnaire 1（≤ Trooper 数 3 ✓）
- ✅ 5. Stipulations：Silenced Pistol ELITE-only ✓（Death Commando）/ Hellbound Soul Contract Trooper-only（未取）/ Anti-Materiel Rifle Limit 1（未取）— 全符合
- ✅ 6. 无 CUMBERSOME + shield 冲突；Wretched battlekit 全 ≤ 10 👑 ✓
- ✅ 7. War Wolf base [2,2] + 50mm oval 已标
- ✅ 8. （N/A — Heretic 无 Fireteams）
- ✅ 9. 无 Artillery Witch（第 2 个才需 1,000 👑+ 门槛）
- ✅ 10. ☼ = 0，无须协商

### 8.3 yaml roster（节选 — 关键单位）

```yaml
warband:
  name: "The Sevenfold Maw"
  side: blue
  faction: heretic-legions
  variant: null
  alignment: Fallen
  budget:
    ducats: 700
    glory_points: 0
  spent:
    ducats: 641
    glory_points: 0

models:
  - id: blue.heretic_priest
    profile: heretic-priest
    base_cost: 80
    base_size: [1, 1]
    base_shape: circle
    base_dimensions_mm: [32, 32]
    equipment:
      ranged: bolt-action-rifle
      melee: sword-axe
      armour: standard-armour
      equipment: [infernal-brand]
    equipment_cost: 34
    total_cost: 114

  - id: blue.death_commando
    profile: death-commando
    base_cost: 90
    base_size: [1, 1]
    base_shape: circle
    base_dimensions_mm: [32, 32]
    equipment:
      ranged: silenced-pistol
      melee: trench-knife
    equipment_cost: 16
    total_cost: 106

  - id: blue.war_wolf
    profile: war-wolf-assault-beast
    base_cost: 145
    base_size: [2, 2]                     # 50mm 椭圆 → 升 [2,2]，见 coordinate-system.md §5.2
    base_shape: oval
    base_dimensions_mm: [50, 50]
    equipment:
      built_in: [chainsaw-mouth, shredding-claws]
    equipment_cost: 0
    total_cost: 145

  - id: blue.wretched_1
    profile: wretched
    base_cost: 25
    base_size: [1, 1]
    base_shape: circle
    base_dimensions_mm: [25, 25]
    equipment:
      melee: trench-club
    equipment_cost: 3
    total_cost: 28
  # ... 其余 6 模型同构
```

---

## 跨文件引用速查

- 项目主入口：`→ ../rules/00-overview.md`
- 招募预算（Scenario Format）：`→ ../rules/08-scenarios.md#11-准备对战-preparing-to-play`
- VP / 胜负条件：`→ ../rules/08-scenarios.md#17-胜利条件-victory-conditions`
- New Antioch 全单位 + Armoury + 4 Variants：`→ ../warbands/01-new-antioch.md`
- Heretic Legions 全单位 + Armoury + 3 Variants：`→ ../warbands/02-heretic-legions.md`
- 共享 Battlekit（全 faction）：`→ ../rules/05-battlekit.md`
- Warband 合集独有 keywords：`→ ../warbands/00-warband-keywords.md`
- 通用关键词词典：`→ ../rules/03-keywords-glossary.md`
- 基座 / 距离 / LOS / 地形 schema：`→ ./coordinate-system.md`
- match-state.yaml schema：`→ ./match-template.yaml`
- 官方 errata 关键 Q&A（双重招募 / Stealth Generator / Tough 叠加等）：`→ ../errata/rules-commentaries.md`
- 项目整体导入指南 §3.7 中英术语锚定：`→ ../../../.claude/trenchcrusade-import-guide.md`
