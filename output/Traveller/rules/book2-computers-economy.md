# Classic Traveller — Book 2: Computers / Experience / Drugs / Trade & Commerce

> 源 PDF：`Rule Books/Traveller/Classic Traveller/Classic Traveller (Facsimile 1981 edition).pdf`
> 版本：1981 年修订版（GDW LBB 1-2-3 合订复刻）
> 对应原书页：Book 2 pp. 38–48（PDF p. 93–104）
> 配套文件：Travelling / Economics / Design → `book2-starships.md`；Space Combat 单独位于 `book2-space-combat.md`（另行导入）。
> Errata：本文件已合并 Don McKinney's Consolidated Traveller Errata 中的修订（Non-Agricultural 分类、Trade Speculation 基价），原 1981 版错误见源 PDF p.154–158。

## Index

1. [Computers](#computers)
   - [Offensive Programs](#offensive-programs)
   - [Defensive Programs](#defensive-programs)
   - [Routine Programs](#routine-programs)
   - [Writing Computer Programs](#writing-computer-programs)
   - [Small Craft Computers](#small-craft-computers)
   - [Computer Software List](#computer-software-list)
2. [Experience](#experience)
   - [Self-Improvement](#self-improvement)
   - [Alternatives](#alternatives)
3. [Drugs](#drugs)
   - [Specific Drug Types](#specific-drug-types)
   - [Drug Availability](#drug-availability)
   - [Drugs Table](#drugs-table)
4. [Trade and Commerce](#trade-and-commerce)
   - [Procedure](#procedure)
   - [Actual Value Table](#actual-value-table)
   - [Broker DMs & World Types](#broker-dms--world-types)
   - [Trade and Speculation Table](#trade-and-speculation-table)

## Key Terms

| 缩写 | 含义 |
|---|---|
| CPU | 计算机主处理器容量（可同时处理程序总点数） |
| Storage | 计算机待命存储容量 |
| Space | 程序占用点数 |
| Thr | 编写程序每周成功掷 |
| DM | Dice Modifier |
| A / NA | Agricultural / Non-Agricultural World |
| I / NI | Industrial / Non-Industrial World |
| R / P | Rich / Poor World |
| Cr / MCr | Credit / Megacredit（1 MCr = 1,000,000 Cr） |

---

## Computers

> Book 2 pp. 38–41（PDF p. 93–96）

船载计算机控制所有船内系统活动，尤其用于增强武器火控与防御。它也传递机动与跃迁驱动的控制脉冲并维持例行船务。计算机实际完成什么由当前运行中的程序决定。

计算机以 **CPU 容量** 与 **Storage 容量** 描述：CPU 中的程序**并行同时处理**，storage 中的程序在需要时轮转进入 CPU。

**示例**（Model/1：CPU=2，Storage=4）：可能存 6 个 space-1 程序（return fire、predict-1、gunner interact、auto/evade、maneuver、target），但任一阶段只有 2 个可实际运行。例如 laser return fire phase 需 target + return fire 两个程序占满 CPU；laser fire phase 需 target 必开，剩余位可选 predict-1 或 gunner interact。

在 **computer reprogramming phase** 可撤出/装入程序。例如执行 jump-1 需 jump-1 + navigation 都在 CPU 中，须先移出当下不需的 maneuver、auto-evade 等程序。

### The Software List

[Computer Software List](#computer-software-list) 列出所有可用程序：
- **Space** 一栏表示该程序在 CPU 或 storage 中占多少点。
- **MCr** 为购买价。
- 右两列为自制该程序所需 **Skills** 与每周 **Thr**。

程序分 **Offensive / Defensive / Routine** 三类。

### Offensive Programs

目标：利用舰载武器攻击敌舰。

**Target** — 识别敌舰并控制舰上所有 turret。**所有 laser fire 与 ordnance launch 都需要 Target**（反导除外）。本身无 DM。

**Predict** — 五个程序的系列（Predict-1 至 Predict-5），预测目标未来位置并为 laser 加入预引。**仅适用于 laser fire**，提供命中 DM。

**Gunner Interact** — 将指定 turret 上 gunner 的专业水平接入命中率。使用 laser fire 时 gunner 技能等级成为正 DM。

**Select** — 允许 gunner 尝试选择击中目标船的部位。**Select-1、Select-2** 附带命中 DM 惩罚，**Select-3** 无惩罚；三者均给 gunner **1/3 概率** 命中他选定的部位（前提是武器先命中）。

**Launch** — 允许从 launcher 发射 missile 或 sand。**Target 程序也必须同时运行**。

**Multi-target** — 系列程序，将舰船探测器与多个 turret 连接，允许在一个 phase 内同时攻击多个目标。**每个 turret 仍只能对准一个目标**，但不同 turret 可打不同目标。同一 phase 攻击 1 艘以上敌舰时**必须**装载此程序。**Target 也必须同时运行**。

**Double Fire** — 允许从 power plant 抽取额外功率增强 laser 输出。适用条件：
- 船舶的 power plant 字母等级须 **至少高过 maneuver drive 一级**
- 当前未因战损致 power plant 等级降至 ≤ maneuver drive 等级

启用时每件 laser 的正常命中骰**掷两次**。每次使用 double fire 须掷过 **Overload 存活**：
- 第 1 phase 使用：掷 **1+**
- 第 2 phase：掷 **2+**
- 依次递增，DM **−1** 每个未开火的回合
- 未掷过 → 该舰 **power plant 受 1 次伤害**

### Defensive Programs

**Maneuver/Evade** — 六个程序（1–6），自动执行小幅规避机动以降低被 laser 命中概率。每个程序提供 **基于 pilot skill 分数** 的防御 DM（取 pilot skill 的分数并舍去小数）。另外此程序可**替代** Maneuver 程序实现常规机动。

**Auto/Evade** — Maneuver/Evade 的低阶版，laser 防御 DM **−2**。

**ECM** — 电子对抗，扰乱来袭导弹的寻的头。在 laser return fire phase 中，所有已触舰的 missile 掷 **7+** 即提前自毁且不伤船。

**Return Fire** — 允许本舰 laser 在**紧邻的**对方 fire phase 后向攻击过本舰的敌舰还击。**需 Target 程序**；他程序（如 gunner interact）的 DM 可叠加使用。若同时对多艘敌舰还击，需 Multi-target 程序。

**Anti-Missile** — 允许全部或部分 laser 在 laser return fire phase 向前一 movement phase 触舰的敌方 missile 射击。**不需要 Target 或 Multi-target**，其他程序的 DM 也不影响本程序。

### Routine Programs

**Maneuver** — 使用 maneuver drive 所必需。在战斗中常被 Maneuver/Evade 替代。

**Jump-N** — 执行 N 级跃迁所必需。jump-6 舰若要 jump-3，须用 **Jump-3** 程序，**不能**用更高级程序代替。

**Navigation** — 控制 jump 过程。须先有 flight plan（由 Generate 程序或 starport 提供的一次性 cassette 生成），随后将 flight plan 输入 Navigation 程序，跃迁时 Navigation 与 Jump-N **必须同时在 CPU 中运行**（Generate 仅需运行足够长以生成 flight plan）。

**Generate** — 自行创建 flight plan。若无 Generate 程序，starport 可按 **Cr 10,000 × Jump 号** 出售单次一次性 cassette（用毕自擦）。

**Library** — 区域信息百科，crew 与乘客登陆前常参考。裁判可用它向玩家传递常识。**并非无所不包、也可能有误。**

**Anti-Hijack** — 监控船内情况、发生劫机时自动锁定驾驶舱门禁。非绝对可靠，劫机者仍可能以 **5−**（5 或更低）闯入桥楼。

### Writing Computer Programs

PC 可自编新程序。编写要求：
- 最低 **computer skill** 等级（见软件列表第一 skill 列）
- 另一项**相关技能**（第二 skill 列）
- 超出最低 computer skill 的等级可作正 DM
- 相关技能可由同伴持有，非必须自持

每周掷一次 **Thr**；掷过即完成。

**Fatal Flaws**：自写程序可能潜藏致命 bug，直到关键时才发作。裁判可在需要时掷 **11+** 判断是否触发。

### Small Craft Computers

小艇默认**无计算机**，开火 **DM −1** 且不能加 gunner skill。若小艇加装计算机，按常规程序规则处理，但编写程序时需 **ship's boat skill**（而非 pilot skill）。

### Computer Software List

> PDF p. 41 抄录。`Space` 指 CPU 或 storage 占用点数；`Skills` 列「computer skill / 相关 skill」；`Thr` 为自编成功掷。

#### Offensive Programs

| Space | MCr | Program | Effect | Skills | Thr |
|:---:|---:|---|---|---|:---:|
| 1 | 2. | Predict-1 | +1 on to-hit throw | 1, Navig-1 | 10+ |
| 2 | 4. | Predict-2 | +2 on to-hit throw | 1, Navig-2 | 10+ |
| 1 | 6. | Predict-3 | +2 on to-hit throw | 1, Navig-3 | 10+ |
| 3 | 8. | Predict-4 | +3 on to-hit throw | 1, Navig-4 | 11+ |
| 2 | 10. | Predict-5 | +3 on to-hit throw | 2, Navig-5 | 10+ |
| 1 | 1. | Gunner Interact | adds gunner expertise | 2, Gunnery-2 | 11+ |
| 1 | 1. | Target | required in order to fire turrets | 2, Navig-2 | 10+ |
| 1 | 0.5 | Select-1 | allows target selection but −2 to hit | 1, Gunnery-2 | 9+ |
| 2 | 0.8 | Select-2 | as select-1 but −1 to hit | 2, Gunnery-3 | 9+ |
| 1 | 1. | Select-3 | as select-1 but no hit penalty | 3, Gunnery-4 | 9+ |
| 1 | 1. | Multi-target-2 | allows engagement of 2 targets | 2, Gunnery-2 | 9+ |
| 2 | 2. | Multi-target-3 | allows engagement of 3 targets | 2, Gunnery-3 | 10+ |
| 4 | 3. | Multi-target-4 | allows engagement of 4 targets | 3, Gunnery-4 | 8+ |
| 1 | 2. | Launch | allows launch of missiles and sand | 1, Gunnery-2 | 11+ |
| 4 | 4. | Double Fire | allows firing twice | 2, Engineer-3 | 11+ |

#### Defensive Programs

| Space | MCr | Program | Effect | Skills | Thr |
|:---:|---:|---|---|---|:---:|
| 1 | 1. | Maneuver/Evade-1 | −¼ pilot skill | 1, Pilot-2 | 10+ |
| 2 | 2. | Maneuver/Evade-2 | −½ pilot skill | 1, Pilot-3 | 11+ |
| 3 | 3. | Maneuver/Evade-3 | −¾ pilot skill | 2, Pilot-4 | 10+ |
| 4 | 4. | Maneuver/Evade-4 | −pilot skill | 2, Pilot-5 | 11+ |
| 2 | 5. | Maneuver/Evade-5 | −pilot skill | 3, Pilot-6 | 10+ |
| 3 | 6. | Maneuver/Evade-6 | −5 | 3, Pilot-7 | 11+ |
| 1 | 0.5 | Auto/Evade | −2 | 2, Pilot-4 | 11+ |
| 1 | 0.5 | Return Fire | automatic response if attacked | 2, Gunnery-3 | 12+ |
| 2 | 1. | Anti-Missile | allows laser anti-missile fire | 3, Gunnery-3 | 10+ |
| 3 | 4. | ECM | may explode incoming missiles | 4, Electronics-3 | 9+ |

#### Routine Programs

| Space | MCr | Program | Effect | Skills | Thr |
|:---:|---:|---|---|---|:---:|
| 1 | 0.1 | Maneuver | allows use of maneuver drive | 1, Pilot-1 | 9+ |
| 1 | 0.1 | Jump-1 | allows use of jump drive | 1, Pilot/Navig-1 | 10+ |
| 2 | 0.3 | Jump-2 | allows use of jump-2 | 2, Pilot/Navig-2 | 11+ |
| 3 | 0.4 | Jump-3 | allows use of jump-3 | 2, Pilot/Navig-3 | 12+ |
| 4 | 0.5 | Jump-4 | allows use of jump-4 | 3, Pilot/Navig-4 | 11+ |
| 5 | 0.6 | Jump-5 | allows use of jump-5 | 3, Pilot/Navig-5 | 12+ |
| 6 | 0.7 | Jump-6 | allows use of jump-6 | 4, Pilot/Navig-6 | 11+ |
| 1 | 0.4 | Navigation | controls use of jump drive | 3, Navig-3 | 10+ |
| 1 | 0.8 | Generate | produces flight plans for jump | 3, Navig-4 | 10+ |
| 1 | 0.1 | Anti-Hijack | helps prevent hijacking | 1, Tactics-1 | 9+ |
| 1 | 0.3 | Library | contains local information | 1, no others | 4+ |

**Standard Software Packages**：每台计算机出厂含一套软件包，面额为 **Model 号 × MCr**（1bis 按 1 计、2bis 按 2 计）。额度仅用于购买软件，**不可兑换现金**。

---

## Experience

> Book 2 pp. 42–43（PDF p. 97–98）

角色完成兵役后基本属性已定型。之后能力的继续提升只能通过**长期专注训练**实现——游戏上表现为 PC 学习扮演角色的能力增强。

### Self-Improvement

同一时间只能进行 **1 种** 4 年期计划，四种可选：
- **Education**（教育）
- **Weapon Expertise**（武艺）
- **Skill Improvement**（其他技能）
- **Physical Fitness**（体能）

选定后掷 **Dedication Throw 8+** 判定是否坚持：
- **Physical Fitness** 专用 DM：Intelligence ≤ 8 则 +2；Intelligence ≤ 5 则 +4
- 其他类目无 DM

失败 → 该计划未实施，**1 年内不能再次尝试** 自我提升。成功 → 正式进入 4 年计划。

**Education**：仅当 Education 属性 **< Intelligence** 时可提升。通过函授或家教，基价 **Cr 50/周**；通常每周 1 节（可 2 节）。每完成 **50 节** Education +1。**一个 4 年计划最多 +6 级**，且**永久**生效。

**Sabbatical（一生一次）**：任意角色可在一生一次取 4 年 sabbatical 专门经由教育学习某一**非武器技能**，直达该技能 **level 2**。学费 **Cr 70,000**。

**Weapon Expertise**：选 1 种枪械 + 1 种冷兵器。
- 计划期间两者 **各 +1**（临时）
- 若原技能为 **skill-0**，进步为 **skill-1** 并**永久**
- 计划结束时临时 +1 回落
- 连续完成**第 2 个** 4 年计划 → 提升**永久化**；此新等级仍可在后续计划再次临时 +1
- 可换选不同武器；异世界新型武器（Book 1 未列的）亦可通过本途径学习

**Skill Improvement**：同 Weapon Expertise 的机制，但对象为非武器技能。限制：
- 每次最多选 **2 项**
- 所选技能每项**最少 level-1**
- 完成第 2 个 4 年计划后永久化

**Physical Fitness**：掷 Dedication 8+ 成功后 **Str、End、Dex 各 +1**，计划期内维持；**三围上限 15**。

**中断**：所需物资/教师不可得时计划**暂停**；中断 < 3 月不损失已获得的加成；更长则取消。

### Alternatives

以上为常规路径。科幻设定允许更奇异的提升途径：RNA 智力/教育植入、手术改造、军方/雇佣军特训等。具体细节由裁判裁定。

---

## Drugs

> Book 2 pp. 44–45（PDF p. 99–100）

### Specific Drug Types

为统一，药物一般以**单剂药丸**形式供应。下述 6 类通用型广为人知；**Psi 类**药物见 Book 3 Psionics 一节。其他药物由裁判裁定。

**Slow drug**：加快服用者代谢，令宇宙看起来**变慢**（约自身约是**常人 2 倍速**）。
- 服用后 3 个 combat round（45 秒）生效，持续 **40 个真实 combat round**
- 效果结束：受 **1D hit points** 伤害；疲劳（视为 endurance 能提供的全部 combat swings 已用光，需休息恢复）
- 生效期间每 1 个普通 round 可执行 **2 round 的行动**（射 2 次、挥 2 次、移动 2 倍距离）

**Medical Slow drug**：用于加速伤病恢复。一剂令服用者**昏睡 1 天等于 30 天**，期间正常愈合进行。无额外伤害。

**Fast drug**：减慢代谢至 **1 : 60**，对服用者宇宙变快。容易受伤，但衰老也同步减慢、补给消耗亦减少。
- 摄入即刻生效，一剂 **60 天等于 1 天**
- 有对应的 Fast Antidote 可抵消剩余效果

**Combat drug**：战前服用。Str 与 End **各 +2**。
- 2 个 combat round 后生效，持续 **30 combat round**
- 药效退去：受 **1D wounds**

**Medical drug**：medical 人员使用的一般治疗药物。**须由 Medic 技能者施用**，配合 Medical Slow 使用。

**Anagathics**：抗衰老药。按月持续服用可**免去 aging throws**。稀缺且昂贵，常无价可得。

**Truth drug**：讯问用，一剂可使对象**约 2 分钟诚实作答**。药效过后对象**昏迷 1 小时**并受 **2D wounds**。

### Drug Availability

在某世界寻药：从 Drug 表查该药在 pill 形式下常售的 **TL**，与 **当前世界 TL** 作差作为 DM 加到 Availability throw 上。

- 例：Slow drug 基准 TL 8。在 TL 12 世界 DM +4；在 TL 4 世界 DM −4。
- 可再追加：贿赂、Streetwise、Medical 等技能 DM。

**Synergy**：同时服 ≥ 2 种药物（**Medical 除外**），对每种药物掷 1D，**把结果相乘**，得到 synergy 额外伤害（药效结束时结算）。

**Legality**：世界 Law Level 可限制药物持有/使用。**掷 ≥ 当前世界 Law Level 为合法**；舰员、medic 等授权身份可附 DM。

### Drugs Table

| Drug Type | Effect | Price (Cr) | Tech Level | Available |
|---|---|---:|:---:|:---:|
| Slow | 2:1 slower than normal | 5,000 | 8 | 9+ |
| Medical Slow | 30:1 slower than normal | 100 | 7 | 7+ |
| Slow Antidote | counteracts slow drug | 600 | 10 | 10+ |
| Fast | 60:1 faster than normal | 2,000 | 9 | 8+ |
| Fast Antidote | counteracts fast drug | 900 | 12 | 9+ |
| Anagathic | voids aging throws | 200,000 | 15 | 10+ |
| Truth | compels two minutes of truth | 5,000 | 8 | 7+ |
| Combat | provides +2 stren and endur | 750 | 9 | 6+ |
| Medical | aids recovery | 100 | 6 | 9+ |
| Psi-Booster | see Psionics | 1,000 | see Psionics | see Psionics |
| Psi-Double | see Psionics | 4,000 | see Psionics | see Psionics |
| Psi-Special | see Psionics | 10,000 | see Psionics | see Psionics |

> 原表对「变慢/变快」一列的表述：Slow = 2:1 slower（代谢加快→主观时间变慢）；Fast = 60:1 faster than normal（代谢减慢→主观时间变快）。按 PDF 原页照抄，不作文字修订。

---

## Trade and Commerce

> Book 2 pp. 46–48（PDF p. 101–104）

商船默认以 **Cr 1,000/ton** 的固定运费承运公共货物。除此之外，自有资本的船东可**低价购入、高价卖出**投机赚差价。

**基价**：所有 trade goods 均有一个基价（绝对价值）。
- **购买价** = 基价 × 某百分比（由 [Actual Value Table](#actual-value-table) 决定）
- **售卖价** = 基价 × 某百分比（独立再掷）

### Procedure

1. **寻货**（每世界每周限 1 次）：裁判掷 **2D 连读成 11–66 的两位数**。第一位数字 DM：
   - 当前世界 Pop **9+**：DM **+1**
   - 当前世界 Pop **5−**：DM **−1**
   - 修正后 < 1 取 1，> 6 取 6。
   - 结果对照 [Trade and Speculation Table](#trade-and-speculation-table)。
2. **定量**：按表列 `Quantity` 掷（例 `3Dx5` = 3 骰之和 × 5）。
3. **定价**：掷 2D（带 DM）查 [Actual Value Table](#actual-value-table) 得购买百分比；基价 × 百分比 × 数量 = 总价。
4. **卸货销售**：到港后再掷 2D（带 Resale DM）查 Actual Value Table 得售出百分比。
5. **部分采购**：可以拆散采购，**额外收 1% 手续费**。

**单位**：11–46、61–66 的货物数量以 **吨** 计；51–56 的货物以 **件** 计（其吨位与单件基价由裁判另定）。

### Actual Value Table

| Dice Roll | Percentage of Base Price |
|:---:|:---:|
|  2 |  40% |
|  3 |  50% |
|  4 |  70% |
|  5 |  80% |
|  6 |  90% |
|  7 | 100% |
|  8 | 110% |
|  9 | 120% |
| 10 | 130% |
| 11 | 150% |
| 12 | 170% |
| 13 | 200% |
| 14 | 300% |
| 15 | 400% |

### Broker DMs & World Types

**Brokers**（仅 4 档，不可叠加、每笔仅用 1 名；无论成交与否均须付费）：

| DM | 佣金（售价百分比） |
|:---:|:---:|
| +1 | 5% |
| +2 | 10% |
| +3 | 15% |
| +4 | 20% |

Broker DM 封顶 +4。

**Character Skills**：Bribery 与 Admin 可按技能等级作 DM 使用。一次交易中仅 **1 人** 用技能；技能、broker、world-type 三类 DM 可叠加。

**World Types 分类**（Book 3 详述，按 UWP 代码判定）：

| 分类 | 判定条件 |
|---|---|
| **Agricultural** (A) | atmos 4-9 AND hydro 4-8 AND popul 5-7 |
| **Non-Agricultural** (NA) | atmos 3− AND hydro 3− AND popul 6+ |
| **Industrial** (I) | atmos 0, 1, 2, 4, 7, or 9 AND popul 9+ |
| **Non-Industrial** (NI) | popul 6− |
| **Rich** (R) | atmos 6 or 8 AND popul 6-8 AND govt 4-9 |
| **Poor** (P) | atmos 2-5 AND hydro 3− |

一颗世界可**同时符合多个**标签（例：poor, non-industrial），其对应 DM **全部叠加** 使用。

### Trade and Speculation Table

> PDF p. 47 完整抄录。
> **缩写**：A=Agricultural, NA=Non-Agricultural, P=Poor, R=Rich, I=Industrial, NI=Non-Industrial。
> 11–46 与 61–66 数量按 **吨** 计；**51–56 按件计**（每件吨位另定）。

| Die | Trade Goods        | Base Price | Purchase DMs          | Resale DMs            | Quantity |
|:---:|---|---:|---|---|:---:|
| 11 | Textiles             |      3,000 | A−7, NA−5, NI−3       | A−6, NA+1, R+3        | 3Dx5  |
| 12 | Polymers             |      7,000 | I−2, R−3, P+2         | I−2, R+3              | 4Dx5  |
| 13 | Liquor               |     10,000 | A−4                   | A−3, I+1, R+2         | 1Dx5  |
| 14 | Wood                 |      1,000 | A−6                   | A−6, I+1, R+2         | 1Dx10 |
| 15 | Crystals             |     20,000 | NA−3, I+4             | NA−3, I+3, R+3        | 1D    |
| 16 | Radioactives         |  1,000,000 | I+7, NI−3, R+5        | I+6, NI−3, R−4        | 1D    |
| 21 | Steel                |        500 | I−2, R−1, P+1         | I−2, R−1, P+3         | 4Dx10 |
| 22 | Copper               |      2,000 | I−3, R−2, P+1         | I−3, R−1              | 2Dx10 |
| 23 | Aluminum             |      1,000 | I−3, R−2, P+1         | I−3, NI+4, R−1        | 5Dx10 |
| 24 | Tin                  |      9,000 | I−3, R−2, P+1         | I−3, R−1              | 3Dx10 |
| 25 | Silver               |     70,000 | I+5, R−1, P+2         | I+5, R−1              | 1Dx5  |
| 26 | Special Alloys       |    200,000 | I−3, NI+5, R−2        | I−3, NI+4, R−1        | 1D    |
| 31 | Petrochemicals       |     10,000 | NA−4, I+1, NI−5       | NA−4, I+3, NI−5       | 6Dx5  |
| 32 | Grain                |        300 | A−2, NA+1, I+2        | A−2                   | 8Dx5  |
| 33 | Meat                 |      1,500 | A−2, NA+2, I+3        | A−2, R+2, P+3         | 4Dx5  |
| 34 | Spices               |      6,000 | A−2, NA+3, I+2        | A−2, R+2, P+3         | 1Dx5  |
| 35 | Fruit                |      1,000 | A−3, NA+1, I+2        | A−2, I+3, R+2         | 1Dx5  |
| 36 | Pharmaceuticals      |    100,000 | NA−3, I+4, P+3        | NA−3, I+5, R+4        | 1D    |
| 41 | Gems                 |  1,000,000 | I+4, NI−8, P−3        | I+4, NI−2, R+8        | 1D    |
| 42 | Firearms             |     30,000 | I−3, R−2, P+3         | I−2, R−1, P+3         | 2D    |
| 43 | Ammunition           |     30,000 | I−3, R−2, P+3         | I−2, R−1, P+3         | 2D    |
| 44 | Blades               |     10,000 | I−3, R−2, P+3         | I−2, R−1, P+3         | 2D    |
| 45 | Tools                |     10,000 | I−3, R−2, P+3         | I−2, R−1, P+3         | 2D    |
| 46 | Body Armor           |     50,000 | I−1, R−3, P+3         | I−2, R+1, P+4         | 2D    |
| 51 | Aircraft             |  1,000,000 | I−4, R−3              | NI+2, P+1             | 1D    |
| 52 | Air/Raft             |    600,000 | I−3, R−2              | NI+2, P+1             | 1D    |
| 53 | Computers            | 10,000,000 | I−2, R−2              | NI+2, P+1, A−3        | 1D    |
| 54 | All Terrain Vehicles |     30,000 | I−2, R−2              | NI+2, P+1, A+1        | 1D    |
| 55 | Armored Vehicles     |     70,000 | I−5, R−2, P+4         | NA−2, A+2, R+1        | 1D    |
| 56 | Farm Machinery       |    150,000 | I−5, R−2              | A+5, NA−8, P+1        | 1D    |
| 61 | Electronics Parts    |    100,000 | I−4, R−3              | NI+2, P+1             | 1Dx5  |
| 62 | Mechanical Parts     |     70,000 | I−5, R−3              | NI+3, A+2             | 1Dx5  |
| 63 | Cybernetic Parts     |    250,000 | I−4, R−1              | NI+4, A+1, NA+2       | 1Dx5  |
| 64 | Computer Parts       |    150,000 | I−5, R−3              | NI+3, A+1, NA+2       | 1Dx5  |
| 65 | Machine Tools        |    750,000 | I−5, R−4              | NI+3, A+1, NA+2       | 1Dx5  |
| 66 | Vacc Suits           |    400,000 | NA−5, I−3, R−1        | NA−1, NI+2, P+1       | 1Dx5  |

**吨位/单价一致性**（重要）：决定一 lot 的实际单品数量时须让「基价总额」与「按吨计价」**自洽**。例：shotgun 基价 Cr 150/支，1 ton 的 firearms 基价 Cr 30,000 → 按 **单价换算** 得 200 支/ton（而非按实际重量 3.75 kg/支的 266 支/ton）。差额视作包装箱重量。裁判为其他类目按同法核算。

51–56 与 66 的结果**按件计**而非按吨，具体每件的吨位与基价由 PC 与裁判按相应装备实际规格决定。

---

## 校对记录

抽查与 PDF 原页交叉验证的 5 处关键数值：

1. **Computer Software List - Predict 系列**（PDF p. 41）— Predict-1（space 1, MCr 2, +1 to-hit, Navig-1, 10+）至 Predict-5（space 2, MCr 10, +3 to-hit, Navig-5, 10+）。md OCR 将 Predict-2 space 误写为 2，实际是 2（保持原值）；Predict-4 space 3（与 md 一致）。✓
2. **Double Fire**（PDF p. 41）— Space 4、MCr 4、Engineer-3、Thr 11+，效果「allows firing twice」。覆盖 md 3094 行。✓
3. **Drugs Table - Anagathic**（PDF p. 45）— Price **Cr 200,000**、Tech Level **15**、Available **10+**。md OCR 将多个药名错写（"Frast"→"Fast", "Anagathic"→"Anagathic voids"），全部以 PDF 为准。✓
4. **Trade and Speculation - Radioactives**（PDF p. 47 die 16）— Base Price **Cr 1,000,000**、Purchase **I+7 / NI−3 / R+5**、Resale **I+6 / NI−3 / R−4**、Quantity **1D**。✓
5. **Trade and Speculation - Computers**（PDF p. 47 die 53）— Base Price **Cr 10,000,000**、Purchase **I−2 / R−2**、Resale **NI+2 / P+1 / A−3**、Quantity **1D**。md OCR 该表几乎全部丢失，本次按 PDF p. 47 完整重建 36 行。✓

> md 原文在 Drugs 表中「Slow / 2:1 slower than normal」与「Fast / 60:1 faster」同时出现；按 PDF 原版照抄，逻辑层面解释已在正文段落补充（代谢加快 → 主观时间变慢，反之亦然）。
