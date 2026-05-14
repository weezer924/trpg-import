# rules/03-keywords-glossary: Keywords Glossary

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.52-57
> 版本：v1.0.2
> 范围：Digital Rulebook 核心规则手册的 KEYWORDS GLOSSARY 章节。Warbands 合集独有的关键词（如 `PENETRATING`、`RELIABLE` 等）由 Pass 8 的 `warbands/00-warband-keywords.md` 负责。

> **概念**：Keywords（关键词）是 Trench Crusade 中附着于 model（模型）、Battlekit（装备）、Marker（标记）或 terrain piece（地形块）的核心规则单元。每个关键词要么充当 **Tag（标签，可被其他规则引用）**，要么附带 **Effect（效果，赋予特殊规则）**。带 Effect 的关键词同时也是 Tag。
>
> PDF 原文中关键词以 **ALL CAPS** 形式出现，便于识别；本文件保留此约定并以反引号包裹。

## Index

按字母序排列：

- [`+/- DICE`](#--dice)
- [`+/- INJURY DICE`](#--injury-dice)
- [`+/- INJURY MODIFIER`](#--injury-modifier)
- [`ACTION`](#action)
- [`AMMUNITION (KEYWORD)`](#ammunition-keyword)
- [`ARMOUR PIERCING`](#armour-piercing)
- [`ARTIFICIAL`](#artificial)
- [`ASSAULT`](#assault)
- [`AUTOMATIC (X)`](#automatic-x)
- [`BLACK GRAIL`](#black-grail)
- [`BLAST (X")`](#blast-x)
- [`BLESSED (X)`](#blessed-x)
- [`BLESSING MARKER`](#blessing-marker)
- [`BLOCK`](#block)
- [`BLOOD MARKER`](#blood-marker)
- [`CLEAVE (X)`](#cleave-x)
- [`CONSUMABLE`](#consumable)
- [`COVER`](#cover)
- [`CRITICAL`](#critical)
- [`CUMBERSOME`](#cumbersome)
- [`DANGEROUS TERRAIN`](#dangerous-terrain)
- [`DEADLY`](#deadly)
- [`DEMONIC`](#demonic)
- [`DEPLOYABLE`](#deployable)
- [`DIFFICULT TERRAIN`](#difficult-terrain)
- [`ELITE`](#elite)
- [`FEAR`](#fear)
- [`FIRE`](#fire)
- [`FIRETEAM`](#fireteam)
- [`FLAMETHROWER`](#flamethrower)
- [`FLYING`](#flying)
- [`GAS`](#gas)
- [`GOLEM`](#golem)
- [`HEAVY`](#heavy)
- [`HELD`](#held)
- [`HERETIC`](#heretic)
- [`IGNORE ARMOUR`](#ignore-armour)
- [`IGNORE [MODIFIER]`](#ignore-modifier)
- [`IMPASSABLE TERRAIN`](#impassable-terrain)
- [`IMPERVIOUS`](#impervious)
- [`INFECTION MARKERS`](#infection-markers)
- [`INFILTRATOR`](#infiltrator)
- [`LEADER`](#leader)
- [`MINED`](#mined)
- [`NEGATE [KEYWORD]`](#negate-keyword)
- [`NEW ANTIOCH`](#new-antioch)
- [`PILGRIM`](#pilgrim)
- [`PISTOL`](#pistol)
- [`REGENERATE (X)`](#regenerate-x)
- [`RELOAD`](#reload)
- [`RISKY`](#risky)
- [`SCATTER`](#scatter)
- [`SHOTGUN`](#shotgun)
- [`SHRAPNEL`](#shrapnel)
- [`SKIRMISHER`](#skirmisher)
- [`STRONG`](#strong)
- [`SULTANATE`](#sultanate)
- [`THE COURT`](#the-court)
- [`TOUGH`](#tough)

---

### `+/- DICE`

**类型**：Effect

**定义**：附加在 Success Roll（成功判定）上的额外骰子（详见 `→ rules/02-comprehensive-rules.md#success-rolls`）。若关键词作用于武器，则只对该武器的 Attack（攻击）所做的 Success Roll 生效。

**触发时机**：每次执行该武器或该模型的 Success Roll 时（射击/近战/移动等行动判定），将相应数量的骰子加入投骰池后取高（`+X DICE`）或取低（`-X DICE`）。

### `+/- INJURY DICE`

**类型**：Effect

**定义**：附加在 Injury Roll（受伤判定）上的额外骰子（详见 `→ rules/02-comprehensive-rules.md#injury-rolls`）。若关键词作用于武器，则只对该武器的 Attack 所做的 Injury Roll 生效。

**触发时机**：攻击命中后，结算 Injury Roll 时加入；多投取高（`+X INJURY DICE`）或取低（`-X INJURY DICE`）。

### `+/- INJURY MODIFIER`

**类型**：Effect

**定义**：附加在 Injury Roll 结果上的修正值（详见 `→ rules/02-comprehensive-rules.md#injury-rolls`）。若关键词作用于武器，则只对该武器的 Attack 所做的 Injury Roll 生效。

**触发时机**：Injury Roll 投骰完成后，将修正值加到结果上（如 Standard Armour + Trench Shield 提供 `-2 INJURY MODIFIER`）。

### `ACTION`

**类型**：Tag

**定义**：模型在 Activation（激活）时可执行的活动。常见 ACTIONS 包括 Move（移动行动）、Dash（疾行行动）、Shoot（射击行动）、Fight（近战行动）。

**触发时机**：作为 Tag 被规则引用——例如 `ASSAULT` 规则中"不阻止本次 Activation 内再 take a Charge or Fight ACTION"即引用此 Tag。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#actions`、`→ rules/01-core-rules.md#activation-phase`

### `AMMUNITION (KEYWORD)`

**类型**：Effect

**定义**：模型拥有标有此关键词的 Battlekit 时，将在下一场参战的游戏中使用之。模型部署时声明该 Battlekit 用于哪件 Ranged Weapon（远程武器），该武器获得 `(KEYWORD)` 直到游戏结束。所选武器**不能**已带有 `BLAST`、`FIRE`、`GAS` 或 `SHRAPNEL` 关键词，且**不能**有多于一种 AMMUNITION 类型。

**触发时机**：部署阶段声明绑定武器；该武器在整场战斗中获得相应 keyword 效果。

**跨文件引用**：`→ rules/05-battlekit.md`（具体 AMMUNITION 种类）

### `ARMOUR PIERCING`

**类型**：Effect

**定义**：带此关键词的武器在攻击时，将目标来自 Armour Characteristic（装甲值）以及任何 Armour 或 Shield 提供的 **总 `-INJURY MODIFIER` 减 1**，最低降至 0。例：目标拥有 Standard Armour 与 Trench Shield，原本 `-INJURY MODIFIER` 为 `-2`，被 ARMOUR PIERCING 降至 `-1`。

**触发时机**：Injury Roll 阶段，结算目标装甲减免时。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#injury-rolls`、`→ rules/03-keywords-glossary.md#impervious`（豁免规则）

### `ARTIFICIAL`

**类型**：Tag

**定义**：该模型并非自然生物来源，而是由非有机元素构造而成。

**触发时机**：纯 Tag，由其他规则引用（例如某些武器或法术对 `ARTIFICIAL` 单位有特殊效果）。

### `ASSAULT`

**类型**：Effect

**定义**：以带此关键词的武器进行 Ranged Attack（远程攻击）**不会**阻止该模型在同一 Activation 内再 take a Charge ACTION 或 Fight ACTION。

**触发时机**：模型先 Shoot 再 Charge/Fight 时启用；通常 Shoot ACTION 后不能再 Charge/Fight，本关键词解除该限制。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#shoot-action`、`→ rules/02-comprehensive-rules.md#charge-action`

### `AUTOMATIC (X)`

**类型**：Effect

**定义**：当 take Shoot ACTION 并选择带此关键词的武器进行 Ranged Attack 时，可使用该武器连续进行 X 次 Ranged Attack。各次攻击可指向**不同**敌方模型，但所有目标必须互相处于 6" 之内。每次攻击单独以 Ranged Attack Sequence 步骤 2-6 结算。本次 Activation 中花费的 `BLOOD MARKERS` 或 `BLESSING MARKERS` 只修正其所花费攻击对应的 Injury Roll。

**触发时机**：声明 Shoot ACTION 后；每次攻击独立判定与结算。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#ranged-attack-sequence`、`→ rules/02-comprehensive-rules.md#blood-markers`、`→ rules/02-comprehensive-rules.md#blessing-markers`

### `BLACK GRAIL`

**类型**：Tag

**定义**：该模型属于 The Cult of the Black Grail（黑圣杯邪教）Faction。

**触发时机**：纯 Tag，用于派系识别（v0.2+ 才有该 faction 详细 profile）。

### `BLAST (X")`

**类型**：Effect

**定义**：带 `BLAST (X")` 的 Ranged Weapon 拥有以英寸为单位、半径等于 X 的爆破范围（**含垂直方向**）。攻击时必须指定目标：可为敌方模型，或战场上、地形块上的可见点。所选目标须在攻击方的 Line of Sight 内、且在武器射程内。

- Success Roll 为 **Failure**：攻击落空，无效（除非武器同时带 `SCATTER` 关键词，详见 `SCATTER`）。
- Success Roll 为 **Success 或 Critical Success**：每个对该目标有 Line of Sight、且在武器爆破半径内的模型都被命中；此外，与被击中的敌方模型 1" 内的友方模型也被命中。
- 测量：从目标模型基座中心，或所选可见点，量至其他模型基座最近点。
- 对每个被命中的模型进行 Injury Roll。Critical Success 触发的 +`INJURY DICE` **只**加给被选为攻击目标的模型。

**触发时机**：宣告 Shoot ACTION + 使用 `BLAST` 武器 + 完成 Success Roll。

**跨文件引用**：`→ matches/coordinate-system.md` §6（Line of Sight 三态规约）、`→ rules/02-comprehensive-rules.md#ranged-attack-sequence`、`→ rules/03-keywords-glossary.md#scatter`

> **Errata 裁决**（5 条，全部围绕 BLAST 实战细节）：
> - **Q1（目标点高度）**：BLAST 的目标点**不可**设在模型基座之下——必须是 1mm 高的"点"，攻击方对该点有 LOS。（→ `errata/rules-commentaries.md` Keywords Q1）
> - **Q6（半径量起点）**：BLAST 半径从**被选目标模型的基座最近点**（或所选可见点）量起，**不是**模型中心。（→ `errata/rules-commentaries.md` Keywords Q6）
> - **Q7（LOS 到点判定）**：检测 LOS 到点时，**能看到该点的任何部分**即算 LOS；该点视作 1mm 高。（→ `errata/rules-commentaries.md` Keywords Q7）
> - **Q8（战壕沿 / 台阶波及范围）**：手雷扔到 trench wall / 台阶时，BLAST 半径**穿越垂直地形**——半径以 3D 空间球面计算，不阻于地形垂直面。（→ `errata/rules-commentaries.md` Keywords Q8）
> - **Q9（接触链不传染）**：BLAST 命中的"1" 内友军"**不再**继续向 1" 外的更远模型传染——接触链**只展开一层**。（→ `errata/rules-commentaries.md` Keywords Q9）

### `BLESSED (X)`

**类型**：Effect

**定义**：当带此关键词的模型在游戏中首次部署时，在该模型旁放置 X 个 `BLESSING MARKERS`。

**触发时机**：模型首次部署到战场时。

**跨文件引用**：`→ rules/03-keywords-glossary.md#blessing-marker`

### `BLESSING MARKER`

**类型**：Tag

**定义**：该模型处于一项超自然或化学增益效应下，获得临时收益。

**触发时机**：纯 Tag；标记本身的产生、消费、效果由 `→ rules/02-comprehensive-rules.md#blessing-markers` 描述。

### `BLOCK`

**类型**：Effect

**定义**：若攻击方在本回合内已 take Charge ACTION，对带此关键词的模型（或持有带此关键词武器的模型）进行 Melee Attack 时加 `-1 DICE`。

**触发时机**：Charge → Fight 的序列中，进行 Melee Attack 的 Success Roll 时。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#melee-attack`、`→ rules/02-comprehensive-rules.md#charge-action`

### `BLOOD MARKER`

**类型**：Tag

**定义**：`BLOOD MARKERS` 放置在受伤的模型上。

**触发时机**：纯 Tag；标记本身的产生、消费、效果由 `→ rules/02-comprehensive-rules.md#blood-markers` 描述。

### `CLEAVE (X)`

**类型**：Effect

**定义**：当 take Fight ACTION 并选择带此关键词的武器进行 Melee Attack 时，可使用该武器连续进行 X 次 Melee Attack。各次攻击可指向不同敌方模型。每次攻击单独以 Melee Attack Sequence 步骤 2-4 结算。本次 Activation 中花费的 `BLOOD MARKERS` 或 `BLESSING MARKERS` 只修正其所花费攻击对应的 Injury Roll。

**触发时机**：宣告 Fight ACTION 后；每次攻击独立判定与结算。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#melee-attack-sequence`

### `CONSUMABLE`

**类型**：Effect

**定义**：在 campaign 中，带此关键词的 Battlekit 在使用其的游戏结束时丢失（消耗）。

**触发时机**：仅 campaign 规则生效（v0.1 单场对战不涉及）。

**跨文件引用**：`→ Campaign Rules`（v0.2+ 导入；PDF p.87-143）

### `COVER`

**类型**：Effect

**定义**：带此关键词的模型获得 Cover 或 Defended Obstacle 的攻击修正。

**触发时机**：作为远程攻击目标或近战目标时；具体的"是否取得 cover"判定与修正数值由坐标系契约决定，**不在此散文复述**。

**跨文件引用**：
- 完整 cover 三问判定与三态 `clear` / `partial_cover` / `blocked` → `matches/coordinate-system.md` §6
- 地形 cover 属性字段语义 → `matches/coordinate-system.md` §7.2（`cover: none / partial / full` 字段）
- 战场上 cover 的具体来源（trench / ruins / abandoned corner / hill / dangerous / difficult / landmark 七类地形）→ `matches/coordinate-system.md` §7.3
- Cover 触发的 ranged `-1 DICE` 修正与近战 Defended Obstacle 修正 → `rules/02-comprehensive-rules.md#combat-modifiers`

### `CRITICAL`

**类型**：Effect

**定义**：以带此关键词的武器进行攻击并掷出 Critical Success 时，加 **`+2 INJURY DICE`** 而非常规的 `+1 INJURY DICE`。

**触发时机**：Success Roll 出 Critical Success 后，结算对应 Injury Roll 的 `+INJURY DICE` 数量时。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#critical-success`

### `CUMBERSOME`

**类型**：Effect

**定义**：带此关键词的武器需要双手使用，**即使**模型带有 `STRONG` 关键词亦然。但仍可依 Shield Combo 条款与 Shield 同时使用。

**触发时机**：模型选择装备/使用武器时检查手部占用。

**跨文件引用**：`→ rules/05-battlekit.md#shield-combo`、`→ rules/03-keywords-glossary.md#strong`

### `DANGEROUS TERRAIN`

**类型**：Effect

**定义**：若 Activate 一个处于带此关键词的地形中的模型，或将一个模型移动**进入**带此关键词的地形（在一次 move 中），必须为该模型 take a Risky Success Roll。

- Success / Critical Success：模型可继续移动；同一 move 中再进入其他带 `DANGEROUS TERRAIN` 的地形**无须**再次判定。
- Failure：必须为该模型做一次 Injury Roll，且其 Activation 立即结束。

**括号中关键词继承**：`DANGEROUS TERRAIN` 有时后接括号中的关键词（如 `DANGEROUS TERRAIN (FIRE)`）。由此地形规则触发的所有 Injury Rolls 将携带括号中的关键词。

**触发时机**：模型在地形中被 Activate、或移动进入该地形时。

**跨文件引用**：
- 地形 `dangerous: true` 字段语义、`subtype` 取值（barbed_wire / minefield / poison_gas / fire）→ `matches/coordinate-system.md` §7.2
- 完整 yaml 例 → `matches/coordinate-system.md` §7.3.E
- Risky Success Roll → `rules/02-comprehensive-rules.md#risky-success-roll`
- Injury Roll → `rules/02-comprehensive-rules.md#injury-rolls`

### `DEADLY`

**类型**：Effect

**定义**：以带此关键词的武器进行攻击的 Injury Roll，掷 **3D6** 并将 3 个骰子全部相加。任何 `+INJURY DICE` 或 `-INJURY DICE` 正常加入投骰池；但从池中选**最高 3 个**或**最低 3 个**（而非通常的 2 个）。

**触发时机**：以 `DEADLY` 武器攻击命中后的 Injury Roll 阶段。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#injury-rolls`、`→ rules/02-comprehensive-rules.md#bloodbath-roll`（Bloodbath 通常 3D6；`DEADLY` 触发时为 4D6 — 详见 02）

### `DEMONIC`

**类型**：Effect

**定义**：带此关键词的模型自动获得 `NEGATE FIRE` 关键词。

**触发时机**：被 `FIRE` 武器攻击时，`FIRE` 效果被无效化（详见 `NEGATE [KEYWORD]`）。

**跨文件引用**：`→ rules/03-keywords-glossary.md#fire`、`→ rules/03-keywords-glossary.md#negate-keyword`

### `DEPLOYABLE`

**类型**：Tag

**定义**：由一个模型或地形块所代表的 Battlekit，可在游戏过程中设置（部署）。

**触发时机**：纯 Tag；具体部署规则由对应 Battlekit profile 给出。

**跨文件引用**：`→ rules/05-battlekit.md`

### `DIFFICULT TERRAIN`

**类型**：Effect

**定义**：模型在带此关键词的地形上每移动 1" 视作 2"。

**触发时机**：移动结算时；对该地形上每一段距离做 2× 计算。

**跨文件引用**：
- 地形 `movement_cost` 字段语义（通常 `DIFFICULT TERRAIN = movement_cost: 2`）→ `matches/coordinate-system.md` §7.2
- 完整 yaml 例 → `matches/coordinate-system.md` §7.3.F
- 移动距离测量 → `matches/coordinate-system.md` §3

### `ELITE`

**类型**：Tag

**定义**：Warband 中最资深、最英勇的模型。

**触发时机**：纯 Tag，由战团构建规则与某些剧本/规则引用。

**跨文件引用**：`→ matches/roster-template.md`

### `FEAR`

**类型**：Effect

**定义**：对带此关键词的模型进行 Melee Attack 时加 `-1 DICE`。产生 FEAR 的模型自身免疫 FEAR。

**触发时机**：以该模型为目标的 Melee Attack 之 Success Roll。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#melee-attack`

### `FIRE`

**类型**：Effect

**定义**：对带此关键词武器的攻击进行 Injury Roll **之后**，无论结果（包括 No Effect）都在目标模型旁额外放置 1 个 `BLOOD MARKER`。

**触发时机**：Injury Roll 结算完毕后。

**跨文件引用**：`→ rules/03-keywords-glossary.md#blood-marker`、`→ rules/03-keywords-glossary.md#demonic`（DEMONIC 抗 FIRE）

### `FIRETEAM`

**类型**：Effect

**定义**：带此关键词的模型属于一组 2 人的 Fireteam，两人都必须带 `FIRETEAM` 关键词。可在招募 Warband 时或 Quartermaster Step 中组建 Fireteam，并记录于 Warband Roster。

- 可**同时**激活同一 Fireteam 的两个模型；其 ACTIONS 顺序任意，可自由交替。
- 但**任一**成员的 Activation 在同时激活中结束时，**另一**成员的 Activation 也立即结束。
- 一个模型不能属于多于 1 个 Fireteam。

**触发时机**：招募/Quartermaster Step 组建；战场 Activation Phase 选择同时激活时。

**跨文件引用**：`→ rules/01-core-rules.md#activation-phase`、`→ matches/roster-template.md`、`→ Campaign Rules / Quartermaster Step`（v0.2+）

> **Errata 裁决（Q2，激活顺序）**：可以**先单独激活** Fireteam 的一名成员（按普通 Activation 流程），随后**当回合**再以 Fireteam 同时激活的方式激活第二名成员——**前提是后者尚未激活**。但一旦选择"同时激活"模式启动两者，则不可再回到独立流程。（→ `errata/rules-commentaries.md` Keywords Q2）

### `FLAMETHROWER`

**类型**：Effect

**定义**：以带此关键词武器进行 Ranged Attack 时**自动成功**，**不**掷 Success Roll。注意：因此该攻击**不能**达成 Critical Success。

**触发时机**：宣告 Shoot ACTION 并选择 FLAMETHROWER 武器时——直接进入 Injury Roll 阶段。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#ranged-attack-sequence`、`→ rules/02-comprehensive-rules.md#critical-success`

### `FLYING`

**类型**：Effect

**定义**：进行 move / retreat move / charge move 时，可让模型的行进路径**穿过空中**测量。须在战场或一块地形上结束移动。

- 若 Activate 时或结束移动时位于 Dangerous terrain，仍须 take Risky Success Roll。
- 不能在 Impassable terrain 上结束移动。
- 此外，FLYING 模型 Fall（坠落）时**不**做 Injury Roll。

**触发时机**：每次该模型的移动结算。

**跨文件引用**：
- 距离测量（3D 欧氏，z 层差参与）→ `matches/coordinate-system.md` §3
- 移动合法性与 Risky Success 触发条件 → `matches/coordinate-system.md` §8 (`validate_move`)
- 坠落（Falling）规则 → `rules/02-comprehensive-rules.md#climbing-and-jumping`
- `IMPASSABLE TERRAIN` → `rules/03-keywords-glossary.md#impassable-terrain`

### `GAS`

**类型**：Effect

**定义**：对带此关键词武器的攻击进行 Injury Roll **之后**，无论结果（包括 No Effect）都在目标模型旁额外放置 1 个 `BLOOD MARKER`。

**触发时机**：Injury Roll 结算完毕后。

**跨文件引用**：`→ rules/03-keywords-glossary.md#blood-marker`、`→ rules/03-keywords-glossary.md#golem`（GOLEM 自带 NEGATE GAS）

### `GOLEM`

**类型**：Effect

**定义**：带此关键词的模型将 Injury Roll Table 上的 Out of Action 结果视作 Down 结果，**除非**该结果由 Bloodbath Roll 触发。此外：

- **不能**从带此关键词的友方模型上移除 `BLOOD MARKERS`（对方玩家仍可正常使用）。
- 模型自动获得 `NEGATE FEAR` 与 `NEGATE GAS` 关键词。
- 模型**不能**同时带 `TOUGH` 关键词。

**触发时机**：Injury Roll Table 解读时、移除 `BLOOD MARKERS` 时。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#injury-roll-table`、`→ rules/02-comprehensive-rules.md#bloodbath-roll`、`→ rules/03-keywords-glossary.md#tough`

### `HEAVY`

**类型**：Effect

**定义**：

- 模型不能装备多于 1 件带 `HEAVY` 关键词的 Battlekit。
- 模型进行 charge move 时**不**获得 Charge Bonus。
- 若 Ranged Weapon 或 Grenade 带此关键词，则**不能**在同一 Activation 中既使用该武器/手雷做 Ranged Attack，又 take Move、Charge、Retreat 或 Dash ACTION（用攻击者作主体）。

**触发时机**：装备校验、Charge 结算、同 Activation 内动作组合校验。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#charge-action`、`→ rules/03-keywords-glossary.md#strong`（STRONG 自带 NEGATE HEAVY）

### `HELD`

**类型**：Effect

**定义**：带此关键词的 Battlekit 需要**一只**手携带，且**不能**放下。因此带 `HELD` 的模型仅能装备/使用：

- 1-Handed Weapon **或**
- Shield

它**不能**装备 2-Handed Weapons，亦**不能**同时持有 Weapon + Shield（即使 Shield 有 Shield Combo 规则）。仍可携带 Grenades。

**触发时机**：装备校验。

**跨文件引用**：`→ rules/05-battlekit.md#shield-combo`

### `HERETIC`

**类型**：Tag

**定义**：该模型属于 Heretic Legions（异端军团）Faction。

**触发时机**：纯 Tag，用于派系识别。

**跨文件引用**：`→ warbands/02-heretic-legions.md`

### `IGNORE ARMOUR`

**类型**：Effect

**定义**：对带此关键词的攻击，**忽略**目标 Armour Characteristic 及其任何 Armour 或 Shield Battlekit 提供的 `-INJURY DICE` 与 `-INJURY MODIFIERS`。

**触发时机**：Injury Roll 阶段。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#injury-rolls`、`→ rules/03-keywords-glossary.md#impervious`（豁免规则）

> **Errata 裁决（Q3）**：`IGNORE ARMOUR` 与 `IGNORE (MODIFIER)` **只忽略数值修正**——**不**忽略 Armour Battlekit 附带的**特殊规则**（如 Machine Armour 的 Standfast、Heavy Ballistic Shield 的 BLOCK 等）。例：War Wolf 的 IGNORE ARMOUR 攻击 Lieutenant 时，仍受 Machine Armour 的 Standfast 改写 Down → Minor Wound 等独立规则约束。（→ `errata/rules-commentaries.md` Keywords Q3）

### `IGNORE [MODIFIER]`

**类型**：Effect

**定义**：忽略所指定的 Success Roll 或 Injury Roll 修正。

**常见实例**：
- `IGNORE COVER` → 带此关键词的 Ranged Weapon 攻击不受目标 Cover `-1 DICE` 影响
- `IGNORE LONG RANGE` → 不受 long range `-1 DICE` 影响
- `IGNORE OFF-HAND WEAPON` → 模型用 Off-Hand Weapon 做 Melee Attack 时不受 `-1 DICE` 影响（PDF p.45 Melee Attack Modifiers；由 Berserker / Gunslinger 等 Promotion Skill 赋予，详见 `→ rules/06-campaign-rules.md` §4 Skill Tables）
- `IGNORE ELEVATED POSITION` → 不受目标 high-ground `+1 DICE`（对自己不利）影响

**触发时机**：Success Roll 或 Injury Roll 结算时；按括号内具体修正名匹配跳过。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#combat-modifiers`

> **Errata 裁决（Q3）**：同 `IGNORE ARMOUR` —— `IGNORE (MODIFIER)` 只跳过数值修正（-1 DICE / -1 INJURY DICE 等），**不**绕过赋予该修正的 Battlekit / Keyword 自带的**独立特殊规则**。（→ `errata/rules-commentaries.md` Keywords Q3）

### `IMPASSABLE TERRAIN`

**类型**：Effect

**定义**：模型不能被移动**到**带此关键词的地形上、亦不能**穿越**之。

**触发时机**：移动合法性校验。

**跨文件引用**：
- 地形 `impassable: true` 字段语义 → `matches/coordinate-system.md` §7.2
- Landmarks（地标）默认即 `IMPASSABLE`（PDF p.60）→ `matches/coordinate-system.md` §7.3.G
- 移动合法性 → `matches/coordinate-system.md` §8 (`validate_move`)
- `FLYING` 例外 → `rules/03-keywords-glossary.md#flying`

### `IMPERVIOUS`

**类型**：Effect

**定义**：`ARMOUR PIERCING` 与 `IGNORE ARMOUR` 的 Effects **不**影响带 `IMPERVIOUS` 的 Battlekit 所提供的 `-INJURY DICE` 与 `-INJURY MODIFIERS`。目标的其他 Battlekit 正常受影响。

**触发时机**：Injury Roll 阶段，结算 Armour Piercing / Ignore Armour 时。

**跨文件引用**：`→ rules/03-keywords-glossary.md#armour-piercing`、`→ rules/03-keywords-glossary.md#ignore-armour`

### `INFECTION MARKERS`

**类型**：Tag

**定义**：该模型处于一项超自然或化学疾病效应下，获得临时效果。

**触发时机**：纯 Tag；产生、消费、效果详见 Warbands of Trench Crusade（Black Grail 章节）。

**跨文件引用**：`→ warbands/`（v0.2+ Black Grail faction）

### `INFILTRATOR`

**类型**：Effect

**定义**：带此关键词的模型在游戏中首次部署时，可置于战场任意位置，前提是：

- 处于**所有**敌方模型的 Line of Sight **之外**；
- 与最近的敌方模型距离至少 **8"**。

`INFILTRATORS` 在所有不带此关键词的模型部署完毕**之后**部署。无法以此方式部署的 `INFILTRATORS` 改回在自己部署区内正常部署。

**触发时机**：剧本部署阶段，常规部署之后。

**跨文件引用**：
- Line of Sight 三态判定 → `matches/coordinate-system.md` §6
- 距离测量 → `matches/coordinate-system.md` §3
- 部署区与战场默认 → `matches/coordinate-system.md` §4
- 部署顺序由 scenario 给出 → `rules/08-scenarios.md`

### `LEADER`

**类型**：Effect

**定义**：若你的 Warband 在战场上有至少 1 个带此关键词的模型且**未** Down 或 Out of Action，Morale Checks 加 `+1 DICE`。

**触发时机**：Morale Phase 进行 Morale Check 时。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#morale-phase`

### `MINED`

**类型**：Effect

**定义**：当模型移动至与一个带 `MINED` 关键词的 Marker 或地形块**接触**时，地雷引爆——除非该模型带 `NEGATE MINED`。为引爆地雷的模型做一次带 `SHRAPNEL` 关键词的 Injury Roll，随后该 Marker 或地形块失去 `MINED` 关键词。

- 若引爆地雷的模型未被 take Down 或 Out of Action，可继续其移动。
- 带 `FLYING` 关键词的模型只有在 `MINED` Marker/地形块**接触处**结束移动时才引爆（飞越不引爆）。

**触发时机**：模型移动进入与 MINED 标记/地形接触时。

**跨文件引用**：`→ rules/03-keywords-glossary.md#shrapnel`、`→ rules/03-keywords-glossary.md#flying`、`→ rules/03-keywords-glossary.md#negate-keyword`

### `NEGATE [KEYWORD]`

**类型**：Effect

**定义**：带 `NEGATE` 关键词的模型**不**受所指定关键词的 Effect 影响。例：带 `NEGATE SHRAPNEL` 的模型忽略 `SHRAPNEL` 关键词的 Effect。

**触发时机**：当对应被指定 Effect 触发时检查；若目标带 `NEGATE [该 Effect]`，则该 Effect 对其无效。

**跨文件引用**：本节中所有具体 NEGATE 应用（`NEGATE FIRE` / `NEGATE GAS` / `NEGATE FEAR` / `NEGATE HEAVY` / `NEGATE MINED` / `NEGATE SHRAPNEL` 等）

### `NEW ANTIOCH`

**类型**：Tag

**定义**：该模型属于 Principality of New Antioch（新安提阿公国）Faction。

**触发时机**：纯 Tag，用于派系识别。

**跨文件引用**：`→ warbands/01-new-antioch.md`

### `PILGRIM`

**类型**：Tag

**定义**：该模型属于 Trench Pilgrim（战壕朝圣者）Faction。

**触发时机**：纯 Tag，用于派系识别（v0.2+ 才有该 faction 详细 profile）。

### `PISTOL`

**类型**：Effect

**定义**：Pistol 可作为 Melee Weapon **或** Ranged Weapon 使用，且可在同一 Activation 中**两者皆用**。

- 作 Ranged Weapon 时使用 Profile 上的 Range，并使用攻击方的 Ranged Characteristic。
- 作 Melee Weapon 时，可使用攻击方的 **Ranged 或 Melee Characteristic**；并可作为 Off-Hand Weapon（副手武器）使用。

**触发时机**：装备与攻击宣告时。

**跨文件引用**：`→ rules/05-battlekit.md`（具体 pistol 型号）、`→ rules/02-comprehensive-rules.md#multiple-melee-weapons`（Off-Hand Weapon 机制定义在 PDF p.45 该段）

> **Errata 裁决（3 条，PISTOL / Off-Hand 实战）**：
> - **Q4（近战时弹药效果）**：`PISTOL` 在 Melee 模式下做攻击时，仍**保留其 Ranged Weapon 弹药相关特性**（如 `RELOAD` / `BLESSED (X)` 等需消耗/产生标记的关键词），按 Ranged 攻击同样的方式触发/耗用。（→ `errata/rules-commentaries.md` Keywords Q4）
> - **Camp Q2（Gunslinger + 双自动手枪）**：装备两把带 `AUTOMATIC (X)` 的 PISTOL 的 Gunslinger 模型，**两把武器各自独立享有 AUTOMATIC 的额外攻击**——每把先做自身完整 Shoot ACTION（含 AUTOMATIC 额外攻击）再切到另一把。（→ `errata/rules-commentaries.md` Camp Q2）
> - **Camp Q6（双 PISTOL 中途换近战）**：Gunslinger 在 Activation 中先用双 PISTOL 做 Ranged，再切到 Melee Weapon 时，**先前的 PISTOL 不再作为 Off-Hand Weapon 参与近战**——同一 Activation 内 Off-Hand 槽位的占用按攻击宣告时刻判定。（→ `errata/rules-commentaries.md` Camp Q6）

### `REGENERATE (X)`

**类型**：Effect

**定义**：Activate 一个带此关键词的模型时，在执行任何 ACTIONS **之前**，可从该模型上移除最多 X 个 `BLOOD MARKERS`。

**触发时机**：Activation 开始、所有 ACTIONS 之前。

**跨文件引用**：`→ rules/03-keywords-glossary.md#blood-marker`

### `RELOAD`

**类型**：Effect

**定义**：若模型以带此关键词的武器进行攻击，则在该次攻击所属的 ACTION 完成后，该模型的 Activation **立即结束**。

**触发时机**：完成允许该攻击的 ACTION（通常 Shoot ACTION）后。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#shoot-action`

### `RISKY`

**类型**：Effect

**定义**：若你必须为一个使用带此关键词 Battlekit 的模型做 Success Roll，则该 Success Roll 变为 Risky Success Roll（若 Risky Success Roll 失败，该模型的 Activation 或 ACTION 结束）。例：使用带 `RISKY` 武器进行攻击的 Success Roll 变为 Risky Success Roll。若该 Success Roll 本来就是 Risky Success Roll，则忽略此 Effect。

**触发时机**：Success Roll 宣告时。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#risky-success-roll`

### `SCATTER`

**类型**：Effect

**定义**：某些带 `BLAST` 关键词的武器同时带 `SCATTER`。攻击时按 `BLAST` 规则选目标并结算。**但**若 Success Roll 为 Failure，攻击 scatter（散射偏移）而非直接落空：

- 用 7 减去 Success Roll → 偏移距离（英寸）。例：Success Roll 为 4，目标点 scatter (7-4=) **3"**。
- **对方玩家**选方向，将攻击点恰好移动该英寸至战场上、地形块上、或某模型基座上的某点。
- 所选偏移点与原目标之间必须有 Line of Sight；若不可能，则视作 miss。
- 然后按 `BLAST` 规则结算谁被命中。

**触发时机**：BLAST 武器掷出 Failure 的 Success Roll 后。

**跨文件引用**：`→ rules/03-keywords-glossary.md#blast-x`、`→ matches/coordinate-system.md` §6（LOS 判定）

### `SHOTGUN`

**类型**：Effect

**定义**：以带此关键词的武器在 Long Range 进行攻击的 Injury Roll 加 **`-1 INJURY DICE`**，**取代**通常的 Long Range 修正（`-1 DICE`）。

**触发时机**：Long Range 攻击的 Injury Roll 结算时（注意是 Injury Dice 而非 Dice，且替换而非叠加）。

**跨文件引用**：
- Long Range 定义（武器射程的一半为界）→ `matches/coordinate-system.md` §3.2
- 通常的 Long Range `-1 DICE` 修正 → `rules/02-comprehensive-rules.md#combat-modifiers`

### `SHRAPNEL`

**类型**：Effect

**定义**：对带此关键词武器的攻击进行 Injury Roll **之后**，无论结果（包括 No Effect）都在目标模型旁额外放置 1 个 `BLOOD MARKER`。

**触发时机**：Injury Roll 结算完毕后。

**跨文件引用**：`→ rules/03-keywords-glossary.md#blood-marker`、`→ rules/03-keywords-glossary.md#mined`（`MINED` 引发的 Injury Roll 携带 `SHRAPNEL`）

### `SKIRMISHER`

**类型**：Effect

**定义**：若敌方选定带此关键词的模型作为 Charge 目标，可在 Charge 进行**之前** evade（闪避）——前提是你的模型不在敌方 1" 内。

- 闪避时掷 1D3，将模型移动相应英寸数。
- 必须在结束闪避时与所有敌方模型距离 > 1"。
- 若闪避导致一个 interposing model（阻隔模型）出现在闪避模型与发起 Charge 的模型之间，则 Charge 模型必须改选该阻隔模型为 Charge 目标。

**触发时机**：被敌方选为 Charge 目标时（Charge 投骰前）。

**跨文件引用**：
- Charge ACTION 规则 → `rules/02-comprehensive-rules.md#charge-action`
- 距离测量（≤ 1" / 模型间距）→ `matches/coordinate-system.md` §3
- Interposing model 与合法 Charge 路径 → `matches/coordinate-system.md` §8 (`valid_charge_paths`)

> **Errata 裁决（Q10）**：SKIRMISHER 模型若**闪避后离开 charging 模型的 LOS**，charging 模型**仍按已宣告的 Charge 流程**继续——即可继续 Charge Move 到原 SKIRMISHER 现位置，并可能在 Move 结束后无目标可击（视为 charge 失败但移动已发生）。Charge 宣告与 LOS 锁定**仅在宣告瞬间检查**，之后 SKIRMISHER 移出 LOS 不取消 Charge。（→ `errata/rules-commentaries.md` Keywords Q10）

### `STRONG`

**类型**：Effect

**定义**：带此关键词的模型自动获得 `NEGATE HEAVY` 关键词。此外，可将一件 2-Handed Melee Weapon **当作** 1-Handed Melee Weapon 装备与使用。

**触发时机**：装备校验、Charge 时的 Heavy 限制检查。

**跨文件引用**：`→ rules/03-keywords-glossary.md#heavy`、`→ rules/03-keywords-glossary.md#cumbersome`（CUMBERSOME 不被 STRONG 豁免）

### `SULTANATE`

**类型**：Tag

**定义**：该模型属于 The Sultanate of the Iron Wall（钢墙苏丹国）Faction。

**触发时机**：纯 Tag，用于派系识别（v0.2+ 才有该 faction 详细 profile）。

### `THE COURT`

**类型**：Tag

**定义**：该模型属于 The Court of the Seven-Headed Serpent（七首蛇圣庭）Faction。

**触发时机**：纯 Tag，用于派系识别（v0.2+ 才有该 faction 详细 profile）。

### `TOUGH`

**类型**：Effect

**定义**：带此关键词的模型在 Injury Table 上**首次**承受 Out of Action 结果时，该结果改作 Down 结果。

**触发时机**：Injury Roll Table 解读时（仅一次，整场游戏限定）。

**注**：视频教程 transcript 明确指出"Tough 仅首次"是新玩家最易混淆条目之一；后续 Out of Action 结果**不再**降级。

**跨文件引用**：`→ rules/02-comprehensive-rules.md#injury-roll-table`、`→ rules/03-keywords-glossary.md#golem`（GOLEM 类似但范围更广，且与 TOUGH 互斥）
