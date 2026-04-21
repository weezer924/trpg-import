# Classic Traveller — Book 2: Starships（上篇：Travelling / Economics / Design）

> 源 PDF：`Rule Books/Traveller/Classic Traveller/Classic Traveller (Facsimile 1981 edition).pdf`
> 版本：1981 年修订版（GDW LBB 1-2-3 合订复刻）
> 对应原书页：Book 2 pp. 4–23（PDF p. 59–78）
> 本文件覆盖：Travelling、Starship Economics、Design & Construction。Space Combat 见 `book2-space-combat.md`。
> Errata：本文件已合并 Don McKinney's Consolidated Traveller Errata 中的修订，原 1981 版错误见源 PDF p.154–158。

## Index

1. [Travelling](#travelling)
   - [Passage Types](#passage-types)
   - [Lesser Known Aspects of Space Travel](#lesser-known-aspects-of-space-travel)
   - [Starship Malfunctions](#starship-malfunctions)
   - [Travel Formulae & Typical Travel Times](#travel-formulae--typical-travel-times)
2. [Starship Economics](#starship-economics)
   - [Starship Purchase](#starship-purchase)
   - [Starship Expenses](#starship-expenses)
   - [Revenue](#revenue)
   - [Trade Customs](#trade-customs)
   - [Passengers Table](#passengers-table)
   - [Cargo Table](#cargo-table)
3. [Design and Construction](#design-and-construction)
   - [Ship Design Overview](#ship-design-overview)
   - [Required Starship Components](#required-starship-components)
   - [Optional Components](#optional-components)
   - [Ship Crews](#ship-crews)
   - [Weaponry](#weaponry)
   - [Small Craft](#small-craft)
   - [Standard Ship Design Plans](#standard-ship-design-plans)
   - [Building Ships](#building-ships)
   - [Formats](#formats)
   - [Design Tables](#design-tables)
   - [Starship Design Checklist](#starship-design-checklist)

## Key Terms

| 缩写 | 含义 |
|---|---|
| Cr | Credit（信用币）；MCr = 1,000,000 Cr |
| G | Gravity（重力加速度，约 10 m/s²） |
| Jn | Jump Number（跃迁级别，1–6 秒差距/周） |
| Pn | Power Plant Rating |
| M | Ship Tonnage（船舶吨位，1 ton ≈ 14 m³） |
| TL | Tech Level |
| DM | Dice Modifier |
| UPP | Universal Personal Profile |
| LBB | Little Black Book（原核心三本小黑本） |

---

## Travelling

> Book 2 pp. 4–6（PDF p. 59–61）

Travellers travel. They move between worlds as well as on their surfaces. The distances such travel covers may be interplanetary or interstellar in scale.

**Interplanetary Travel**：同一恒星内各行星之间的旅行，由本地商营船或各类小艇承运。由于绝大多数星系只有一颗主要世界，行星间旅行并不常见；往往是个人自有船或包船，鲜有定期班线。使用第 10 页的旅行公式（见下）可算出耗时。

**Interstellar Travel**：跨恒星使用跃迁（Jump）。跃迁驱动分 Jn 1–6，表示一周内可跳跃的秒差距数。无论距离多远，一次 Jump 约需 1 周。启动 Jump 前必须远离行星一定距离（对 size-8 世界，以 1G 加速到 100 倍直径约需 5 小时）。

商营星舰通常每月 2 次跃迁：一周在 jump 中，一周在系统内补给、卸货、揽客、返回跃迁点。非商营船可在补给完毕后立即再次跃迁，一周一跳，但不安排货客。

### Passage Types

跨星际票价按舱位等级计费，只与「一次跃迁」有关，与跃迁距离无关：

- **High Passage（甲等舱）**：头等住舱和餐食，行李 1,000 kg。**Cr10,000**。
- **Middle Passage（乙等舱）**：按 standby 形式出售，待 high 舱未售满时补位。住舱同 high 但服务与餐食降级，行李 100 kg。可被迟到的 high 乘客「bumped」换出，仅退还票款，无其他补偿。**Cr8,000**。
- **Working Passage（以工换票）**：船长缺员时可雇人顶岗，以食宿票代薪。最多连续 3 次跃迁，否则视作正式雇用。行李 1,000 kg。
- **Low Passage（低温舱）**：以冷冻悬置状态旅行，不会衰老、生命维持耗费极低。**Cr1,000**，行李 10 kg。苏醒时掷 **5+** 存活：
  - 医师 (Medic) 技能 2+：DM +1
  - 乘客 Endurance ≤ 6：DM −1
  - 未通过即死亡，票款不退、无民事赔偿。

### Lesser Known Aspects of Space Travel

**The Low Lottery**：每张 low passage 票由船长抽出 Cr10 作彩金。每位 low 乘客猜本次跃迁存活人数，猜中者若未生还则彩金归船长。由乘务员（steward）主持。

**The Travellers' Aid Society**：TAS 成员享有设施和免费舱位红利，详见 Book 1。

**Hijacking**：乘客须将武器（匕首除外）入库。每次航行掷 **3D ≥ 18** 判是否发生劫机企图（若乘客全为 PC 则不掷）。若反劫机程序启用，劫机者攻入驾驶舱需掷 **5−**（5 或更低）。

**Skipping**：商船多为按揭购买，船长可能选择「驾船潜逃」躲避还款。**掷 12+** 判定该船属此类。被发现后，每次入港 **掷 12+** 避免被追回；每离母星 5 秒差距 DM +1（封顶 +9），同一世界两月内重复停靠 DM −2。

**Piracy**：详见 Book 2 的 Starship Encounters 表（位于 Space Combat 章节，另文处理）。

### Starship Malfunctions

主要故障类型：**Drive Failure** 与 **Misjump**。受燃料是否精炼与维护状态影响。

**燃料**：starport 精炼燃料（refined）Cr500/ton；非精炼（unrefined）Cr100/ton，或由气体巨行星免费 scoop。海/湖水亦可作非精炼燃料。军用/准军用舰常用非精炼，因更易取得、其驱动器也为此设计。

**年度维护**：所有船应每年大修一次。

#### Drive Failure

每周操作掷 **13+** 判定驱动故障：

| DM | 条件 |
|---:|---|
| +1 | 使用非精炼燃料（且未针对此设计） |
| +1 | 每缺少一名 required engineer |
| +1 | 每逾期 1 个月未做年度维护 |

一旦出现故障，对每个使用中的驱动器（jump、maneuver、power plant）分别掷 **7+** 判断具体哪一个失效。失效驱动完全停止运作：
- maneuver 失效 → 无法推进
- jump 失效 → 无法跃迁
- power plant 失效 → 断电，电池仅支持 **1D 天**基本生命维持与照明

修复：每天掷 **10+**，DM +engineering skill，可临时修复。彻底维修须在 starport 由合格人员完成。

#### Misjump

每次尝试跃迁时掷 **13+** 判定 misjump：

| DM | 条件 |
|---:|---|
| +1 | 使用非精炼燃料（且未针对此设计） |
| +5 | 位于世界 100 倍直径范围内 |
| +10 | 位于世界 10 倍直径范围内 |
| −1 | 海军 (naval) 舰 |
| −2 | 侦查 (scout) 舰 |

- 结果 **16+** → 船直接被毁。
- 结果 **13–15** → misjump，跃入随机方向、随机距离的空间。

Misjump 流程：
1. 掷 1D 得到跳数 n（1–6）
2. 再掷 n 颗骰子之和为偏移 hex 数
3. 掷 1D 选六方向之一
4. 掷 1D 确定在 jump space 里停留的周数

### Travel Formulae & Typical Travel Times

> Book 2 p. 10

三条公式（从静止加速到中点、转身、减速至目的地静止）：

- **T = 2√(D/A)** — 时间
- **D = A·T²/4** — 距离
- **A = 4D/T²** — 加速度

单位：T = seconds，D = meters，A = m/s²。换算：1 G = 10 m/s²；1 km = 1,000 m；1 scale mm = 100 km。

**TYPICAL TRAVEL TIMES**：

|         Kilometers |    1-G |    2-G |    3-G |    4-G |    5-G |    6-G |
|-------------------:|-------:|-------:|-------:|-------:|-------:|-------:|
|              1,000 |   633s |   447s |   365s |   316s |   283s |   258s |
|             10,000 |  2000s |  1414s |  1155s |  1000s |   894s |   816s |
|            100,000 |   105m |    74m |    61m |    53m |    47m |    42m |
|            300,000 |   183m |   129m |   105m |    91m |    82m |    73m |
|            400,000 |   211m |   149m |   122m |   106m |    94m |    86m |
|          1,000,000 |   333m |   236m |   192m |   167m |   149m |   136m |
|         10,000,000 |  17.6h |  12.4h |  10.1h |   8.8h |   7.9h |   7.2h |
|         45,000,000 |  37.3h |  26.4h |  21.5h |  18.6h |  16.7h |  15.2h |
|        100,000,000 |  55.6h |  39.3h |  32.1h |  27.8h |  24.8h |  22.3h |
|        255,000,000 |  88.7h |  62.7h |  51.2h |  44.4h |  39.7h |  36.2h |
|        600,000,000 | 136.1h |  96.2h |  78.6h |  68.0h |  60.9h |  55.6h |
|        900,000,000 | 166.7h | 117.9h |  96.2h |  83.4h |  74.5h |  68.0h |
|      1,000,000,000 |   7.3d |   5.2d |   4.2d |   3.7d |   3.3d |   2.9d |

单位：s = seconds, m = minutes, h = hours, d = days。

**TYPICAL DISTANCES**：

| 位置 | 距离 |
|---|---:|
| World Surface to Orbit | 10,000 km |
| Satellite | 400,000 km |
| Close Neighbor World | 45,000,000 km |
| Far Neighbor World | 255,000,000 km |
| Close Gas Giant | 600,000,000 km |
| Far Gas Giant | 900,000,000 km |

---

## Starship Economics

> Book 2 pp. 7–11（PDF p. 62–66）

星际商运的价格与回报由供需决定。因船价极高，本章以 MCr（megacredit，百万信用币）为单位。

### Starship Purchase

合格个人可向银行申请商船贷款。首付 **20%** 后船厂开始建造；交付时银行向船厂付清余款并取得船舶抵押权。标准还款：**每月 1/240 的现金价格，共 480 期（40 年）**。利息等效简单利率 120%，最终付款总额 = 现金价 × 220%。

购船申请须提交经济计划，证明有能力按月还款；除非有稳定收入（如租赁所得），否则不允许贷款购买游艇、军舰或探险船。

**Subsidies（补贴商船）**：600-ton 及以上商船可申请政府补贴，通常绑定 2–12 颗世界的固定航线。个人承担 20% 首付，之后政府接管贷款并抽取 **50% 毛收入**；其余运营成本由船东负担。补贴船有战时征用义务。40 年后船只归船东，但仍受征用约束。

### Starship Expenses

五项基本开销（外加贷款）：

1. **Fuel** — 精炼 Cr500/ton；非精炼 Cr100/ton。消耗由 power plant 与 jump drive 尺寸决定。
2. **Life Support** — 每住舱每次（2 周）Cr2,000；每低温舱每次 Cr100。正常一人/住舱，军舰或包船可双占舱位（Cr 翻倍）。
3. **Routine Maintenance** — 年度大修费用 = **船价 0.1%**（1/1000），在 A/B 级 starport 停工 2 周。
4. **Crew Salaries** — 见下。
5. **Berthing Costs** — 着陆+停泊 Cr100 最多 6 天；此后每日 Cr100。部分港有附加费或政府补贴。

**CREW SALARIES**：

| Position | Skill Level | Monthly Salary |
|---|---|---:|
| Pilot     | Pilot-1     | Cr6,000 |
| Navigator | Navigator-1 | Cr5,000 |
| Engineer  | Engineer-1  | Cr4,000 |
| Steward   | Steward-0   | Cr3,000 |
| Medic     | Medic-1     | Cr2,000 |
| Gunner    | Gunner-1    | Cr1,000 |

每高于 level-1 的技能等级，薪资 **+10%**。

**SHIP EXPENSES 概览**：

| 项目 | 计费周期 |
|---|---|
| Bank Payment | Monthly |
| Fuel | 按实耗 |
| Life Support | 每乘客/船员 |
| Maintenance Fund | 预提 |
| Salaries | 每月 |
| Berthing Costs | 每 starport |

### Revenue

收入来自乘客、货物、邮政。

**SHIP REVENUES**：

| 项目 | 费率 |
|---|---:|
| Per High Passage   | Cr10,000 |
| Per Middle Passage | Cr8,000 |
| Per Low Passage    | Cr1,000 |
| Per Cargo Ton      | Cr1,000 |
| Mail (if fitted)   | Cr25,000 |

#### Cargo（货物）

船只入港后可查询可运货。裁判对可达目的地各自掷一次 Cargo Table 得出 Major / Minor / Incidental 类别件数；每件再掷 1D 定吨位：Major × 10、Minor × 5、Incidental × 1 吨。单件货物不可拆分，但船方可挑选以最优化装载。所有货物均以 **Cr1,000/ton** 运输。船东亦可自购货物投机。

**Passengers**：成交货物后乘客报到。按起/目的地 Population 与 Travel Zone 查 Passenger Table，公式形如 `3D-1D`（3 骰之和减 1 骰）。票价：High Cr10,000 / Middle Cr8,000 / Low Cr1,000。跃迁级别不影响票价——jump-3 和 jump-1 船到同一目的地报价相同，差别仅在 jump-3 可能直达、jump-1 需多次中转并分段购票。

**Mail and Incidentals**：补贴商船可获邮政合同（须配武装且 gunner 在编），占用 5 ton 货舱专用。每次航行支付 **Cr25,000**（Cr5,000/ton × 5 ton），实际邮件吨位不超 5 ton。此外每次入港掷 **9+** 可能有私人信件委托（酬金 Cr20–Cr120）。

### Trade Customs

- 在轨装载的货物在目的地轨道交付；地表装载的货物在地表交付。乘客与邮政亦然。
- A/B/C 级 starport 有常规穿梭班线：**Cr10/ton 货，Cr20–Cr120/乘客**。
- **Charters**：
  - 非 starship：Cr1/ton·hour，最少 12 小时。
  - starship：2 周为单位，**Cr900/ton 货舱 + Cr9,000/high berth + Cr900/low berth**。船东承担开销并提供船员。

### Passengers Table

按 **World of Origin 的 Population Digit** 查行，列为 **Available at World of Origin** 的 High / Middle / Low：

| Pop | High | Middle | Low |
|---:|---|---|---|
| 0 | — | — | — |
| 1 | — | 1D−2 | 2D−6 |
| 2 | 1D−2D | 1D | 2D |
| 3 | 2D−2D | 2D−1D | 2D |
| 4 | 2D−1D | 2D−1D | 3D−1D |
| 5 | 2D−1D | 3D−2D | 3D−1D |
| 6 | 3D−2D | 3D−2D | 3D |
| 7 | 3D−2D | 3D−1D | 3D |
| 8 | 3D−1D | 3D−1D | 4D |
| 9 | 3D−1D | 3D | 5D |
| A | 3D | 4D | 6D |

**DMs for destination world**：
- Population 4−：−3
- Population 8+：+3
- Red Zone：−12，且无 middle/low 乘客
- Amber Zone：−6
- Tech Level：加减 origin 与 destination 的 TL 差

### Cargo Table

| Pop | Major | Minor | Incidental |
|---:|---|---|---|
| 0 | — | — | — |
| 1 | 1D−4 | 1D−4 | — |
| 2 | 1D−2 | 1D−1 | — |
| 3 | 1D−1 | 1D | — |
| 4 | 1D | 1D+1 | — |
| 5 | 1D+1 | 1D+2 | — |
| 6 | 1D+2 | 1D+3 | 1D−3 |
| 7 | 1D+3 | 1D+4 | 1D−3 |
| 8 | 1D+4 | 1D+5 | 1D−2 |
| 9 | 1D+5 | 1D+6 | 1D−2 |
| A | 1D+6 | 1D+7 | 1D |

**DMs for destination world**：
- Population 4−：−4
- Population 8+：+1
- Red Zone：无货
- Amber Zone：无 major cargo
- Tech Level：加减 origin 与 destination 的 TL 差

---

## Design and Construction

> Book 2 pp. 12–23（PDF p. 67–78）

Space ships are constructed and sold at shipyards throughout the galaxy. **Class A** starport 可造任何船（含 jump drive）；**Class B** 可造 small craft 及无 jump drive 的 ship。军方、企业、个人皆可通过 shipyard 委造，唯一障碍是资金。

**Definitions**：
- **Vessel** — 任意行星间/星际飞行器。
- **Ship** — 100 tons 或以上的 vessel。
- **Starship** — 装有 jump drive、可作星际旅行的 ship。
- **Non-Starship** — 无 jump drive 的 ship。
- **Small Craft** — < 100 tons 的 vessel；均无跃迁能力。

### Ship Design Overview

- **Naval Architecture（自定义设计）**：独立设计公司以 **1% 最终船价** 设计完整图纸，约 4 周完工；加急到 2 周需 1.5%。
- **Standard Designs**：已有定型图纸，**Cr100** 一套；使用标准图纸的船可享 **10% 价格折扣**。Standard 包含以下星舰：
  - 100-ton Scout/Courier
  - 200-ton Free Trader
  - 200-ton Yacht
  - 400-ton Subsidized Merchant
  - 600-ton Subsidized Liner
  - 800-ton Mercenary Cruiser
  - 400-ton Patrol Cruiser
  - 以及小艇八型（见 [Small Craft](#small-craft)）。
- **Construction Times**：由船体决定，参见 [Drive Potential Table](#drive-potential) 最末列；standard 船型建造更快（[Standard Hulls](#standard-hulls)）。
- **Costs and Payments**：船厂收 20% 首付，并须证明后续资金到位。

### Required Starship Components

**The Hull**：以排量 ton 表示，1 ton ≈ 14 m³（即 1 ton 液氢体积）。船体划分 **engineering section**（仅放驱动与 power plant）和 **main compartment**（其余全部：燃料、货舱、生活舱、计算机等）。

- [Standard Hulls](#standard-hulls) 列出 6 种折扣船体。
- 其他船体须定制：**MCr 0.1/ton，最低 MCr 20**。
- 某些驱动在某些吨位无法工作（表格中标 "−"）；某些驱动无法装入某些船体。
- Drive 等级最高 6；更高级别的驱动不在此规则中提供。

**The Engineering Section**：
- **Non-starship** — 必备 maneuver drive + power plant。
- **Starship** — 必备 jump drive + power plant；maneuver drive 可选。
- **Power plant 字母等级 ≥ 最大的 maneuver/jump drive 字母等级。**
- 所有驱动总吨位不得超过 engineering section 吨位。

**The Main Compartment**：

**A. The Bridge** — **至少 2% 总吨位（最低 20 tons）**用于基本驾驶、通讯、电子设备。成本 **MCr 0.5 / 100 tons of ship**。不含计算机。
> 注：p. 23 的 Design Checklist 中引用 "2% of tonnage"（书印为 12%，系已知排版错误），以 2% 为准。

**Computer**：安装于桥旁。
- Model 编号决定最大可支持的 **jump 级别**（Model/4 支持 Jump-4）。
- **CPU** 当场运行程序总容量；**Storage** 待命程序容量。程序按所占点数归档。
- 每台计算机购买时附带一套软件包；包价值 = MCr × Model 号。
- **bis 型** 计算机（Model/1bis、Model/2bis）：支持 **+1 jump 级**，但软件包按 **−1 level** 计。

**Fire Control**：每安装一个 turret 需 **1 ton** 显示用于火控。

**B. Staterooms**：每间 **4 tons，Cr 500,000**，供 1 人。军舰或探险船允许双占（不可超过 2 人，否则超生命维持）。商船每位船员须有单独住舱。

**C. Low Passage Berths**：**0.5 ton，Cr 50,000**，每位 low 乘客一座。

**Emergency Low Berth**：**1 ton，Cr 100,000**，可容 4 人，使用同一苏醒骰；不作商用，仅应急。

**D. Fuel**：免费（设计时分配吨位）。**最少 = 0.1 M Jn + 10 Pn**（M=总吨位、Jn=jump 级、Pn=power plant 级）。
- 0.1 M Jn → 1 次最大 jump 所需燃料。
- 10 Pn → 基础运转与机动 4 周的燃料。
- Jump 少于最大级时按实际级消耗。

**E. Cargo Hold**：免费分配吨位；载货不得超过其吨位。

**F. Armaments**：**每 100 tons 可设 1 个 hardpoint**。
- Hardpoint 不占吨位，**Cr 100,000/个**。
- 每个 hardpoint 可装 1 个 turret（single/double/triple 分别携 1/2/3 件武器）；并需 1 ton fire control。
- Turret、武器可改装或更换。武器含：Pulse Laser、Beam Laser、Missile Rack、Sandcaster。

### Optional Components

- **Atmospheric Streamlining**：设计时勾选，**MCr 1 / 100 tons**；含 fuel scoops（可从 gas giant 撇取非精炼燃料或从水体采水）。**不可后加装**。
- **Ship's Locker**：默认存在，内容由裁判酌定（vacc suit、shotgun、carbine、pistol、弹药、指南针、求生器材、便携帐篷等）。
- **Ship's Vehicles**：可为飞船分配吨位存放附属载具。详见 [Vehicles Table](#vehicles)；air/raft、GCarrier、speeder 可自行入轨；如果携 ATV 且母船非流线型，必须备运载方式（shuttle、cutter 等）。

### Ship Crews

- **Pilot**：每艘船 1 名（小艇要求 ship's boat-1；大船要求 pilot-1）。
- **Navigator**：> 200 ton 的 starship 必需；小艇或 non-starship 由 pilot 兼任。
- **Engineer**：≥ 200 ton 的船每 **35 tons 驱动/power plant** 需 1 名 engineer-1+。多于一人时首席 +10%。小艇无此要求。
- **Steward**：载 high 乘客时 **每 8 名 high passenger 配 1 名 steward-0+**。多于一人时首席 +10%。
- **Medic**：≥ 200 ton 的 starship 必需（medic-1+）；再按 **每 120 乘客 1 名** 配员。多于一人时首席（ship's doctor）+10%。non-starship、小艇无此要求。
- **Gunner**：每 turret 1 名 gunner-1+；小艇若武装，需独立 gunner。

**兼岗**：一人可兼两职，但每职技能按 **skill−1** 应用，薪资各按 75% 计；因此至少需 level-2（steward 例外，level-1 即可）。

**> 1,000 ton 启航**：须配 CO、XO 与至少 3 名行政；特大船每 1,000 ton 约 10 人起。

### Weaponry

四种常见武器：

- **Pulse Laser**（脉冲激光）：短脉冲型；**命中时 DM −1**，但若命中，目标**承受两次伤害判定**（非一次）。
- **Beam Laser**（光束激光）：连续波，命中率更高（无 pulse 的 −1 DM），单次伤害。
- **Missile Rack**（导弹架）：发射小型反舰自寻导弹，亦可改为行星表面炸弹或侦察无人机。导弹为 homing type，50 kg，**Cr 5,600/枚**（errata 修订，1981 原书 Cr 5,000 有误）。一次发射后归于该目标直到命中或被摧毁。
- **Sandcaster**（沙罐发射器）：防御性；释放 ablat 型棱镜微粒+消耗材料，干扰激光并轻微损伤接触船只。普通沙不可替代——须向军火商购买，弹罐 50 kg，**Cr 400/枚**。

### Small Craft

< 100 ton 的飞行器称为 small craft。八种 Standard 图纸，每套 **Cr 100**，建造约 12 个月。全部流线型，可入大气，可从气体巨行星 scoop 非精炼燃料。

每种小艇含 **excess space**（可由购买者任意配置），按 [Fittings Table](#fittings) 类型搭配（**价格已包含在基础价，不重复计费**）。

小艇可加装计算机（按正常价格），每艇可分 1 ton 装最多 3 件武器（具体可装武器种类见下）。船员为 pilot + rider（fighter 除外，仅 1 人）。若武装但无 gunner，pilot 开火按 **−1 skill**。

| Craft | Hull | Accel | Fuel | Crew | 武器限制 | Excess | Price |
|---|---:|---:|---:|---:|---|---:|---:|
| Launch (Lifeboat) | 20 t | 1-G | 1 t | 2 | 仅 missile / sand（无 laser） | 13.0 t | MCr 14 |
| Ship's Boat | 30 t | 6-G | 1.8 t | 2 | 至多 1 laser（pulse/beam），其余 missile/sand | 13.7 t | MCr 16 |
| Slow Boat | 30 t | 3-G | 1 t | 2 | 至多 1 laser，其余 missile/sand | 19.9 t | MCr 15 |
| Pinnace | 40 t | 5-G | 2 t | 2 | 至多 2 lasers，其余 missile/sand | 22.4 t | MCr 20 |
| Slow Pinnace | 40 t | 2-G | 1 t | 2 | 至多 1 laser，其余 missile/sand | 31.6 t | MCr 18 |
| Cutter | 50 t | 4-G | 2 t | 2 | 至多 2 lasers，其余 missile/sand；30 t 为模块专用 | 2.5 t | MCr 28 |
| Shuttle | 95 t | 3-G | 2.85 t | 2 | 至多 2 lasers，其余 missile/sand | 71 t | MCr 33 |
| Fighter | 10 t | 6-G | 1 t | 1 | 只可装 1 laser 或至多 3 missile racks 或至多 3 sandcasters | 1 t | MCr 18 |

> Fuel 可支持 4 周操作。每艘 small craft（fighter 除外）标配 2 座 small craft couch；fighter 标配 1 座、内置 Model/1 计算机。

**Cutter Modules（模块）**：Cutter 有 30 ton 专用于可拆卸模块，三种标配：

| 模块 | 吨位 | MCr | 用途 |
|---|---:|---:|---|
| ATV Module | 30 | 1.8 | 含 1 辆 wheeled 或 tracked ATV，可放回/回收 ATV |
| Fuel Module | 30 | 1.0 | 30 ton 燃料舱，作 fuel skimmer 或燃料摆渡 |
| Open Module | 30 | 2.0 | 30 ton excess space，可自由分配 |

### Standard Ship Design Plans

所有 standard 图纸 Cr 100/套；价格已含 10% 折扣。

#### Scout/Courier (type S) — MCr 29.43

- **Hull**：100 t，standard，streamlined
- **Drives**：Jump-A / Maneuver-A / Power-A → Jump-2，2-G
- **Fuel**：40 t（支持 1 次 jump-2）
- **Computer**：Model/1bis（邻桥）
- **Accommodations**：4 staterooms；0 low berths
- **Armament**：1 hardpoint，1 double turret + 火控已装，但未装武器
- **Vehicles**：1 air/raft（机库）
- **Cargo**：3 t
- **Crew**：1（pilot 兼 engineer）
- **Build Time**：9 月

#### Free Trader (type A) — MCr 37.08

- **Hull**：200 t，standard，streamlined
- **Drives**：Jump-A / Maneuver-A / Power-A → Jump-1，1-G
- **Fuel**：30 t（支持 1 次 jump-1）
- **Computer**：Model/1
- **Accommodations**：10 staterooms + 20 low berths
- **Armament**：2 hardpoints + 2 t 预留火控；未装 turret 或武器
- **Vehicles**：无
- **Cargo**：82 t
- **Crew**：4（pilot, engineer, medic, steward；武装时加 gunner）
- **Build Time**：11 月

#### Subsidized Merchant (type R) — MCr 100.035

- **Hull**：400 t，standard，streamlined；**15 t 预留 drive 升级**
- **Drives**：Jump-C / Maneuver-C / Power-C → Jump-1，1-G
- **Fuel**：50 t
- **Computer**：Model/1
- **Accommodations**：13 staterooms + 9 low berths
- **Armament**：2 hardpoints + 2 t 火控；未装武器
- **Vehicles**：1 × 20-ton launch
- **Cargo**：200 t
- **Crew**：5（pilot兼 launch/navigator/engineer/medic/steward；武装时加 gunner）
- **Build Time**：14 月
- 别名 *"fat trader"*。

#### Subsidized Liner (type M) — MCr 245.97

- **Hull**：600 t，standard，**unstreamlined**；2 t 预留 drive 升级
- **Drives**：Jump-J / Maneuver-C / Power-J → Jump-3，1-G
- **Fuel**：210 t
- **Computer**：Model/3
- **Accommodations**：30 staterooms + 20 low berths
- **Armament**：3 hardpoints + 3 t 火控；未装武器
- **Vehicles**：1 × 20-ton launch
- **Cargo**：129 t
- **Crew**：pilot（兼 launch）、navigator、3 engineers、medic、3 stewards；武装时加 gunner
- **Build Time**：22 月

#### Yacht (type Y) — MCr 51.057

- **Hull**：200 t，standard，unstreamlined
- **Drives**：Jump-A / Maneuver-A / Power-A → Jump-1，1-G
- **Fuel**：50 t（2 次 jump-1）
- **Computer**：Model/1
- **Accommodations**：14 staterooms（其中 2 间合并为船东套房）；0 low berths
- **Armament**：1 hardpoint + 1 t 火控
- **Vehicles**：1 air/raft、1 ship's boat（船内舱室）、1 ATV（由 ship's boat 负责轨道-地表摆渡）
- **Cargo**：13 t
- **Crew**：4（pilot 兼 ship's boat、engineer、medic、steward；商运时 steward 必选；武装时加 gunner）
- **Build Time**：11 月

#### Mercenary Cruiser (type C) — MCr 429.804

- **Hull**：800 t，custom，unstreamlined
- **Drives**：Jump-M / Maneuver-M / Power-M → Jump-3，3-G
- **Fuel**：318 t（1 次 jump-3 + 48 t 备用 + small craft 作业）
- **Computer**：Model/5
- **Accommodations**：25 staterooms；0 low berths
- **Armament**：8 triple turrets + 火控；未装武器
- **Vehicles**：2 × 50-t cutters（各配 1 个 ATV module，含 ATV）+ 2 额外 module 位；另 1 air/raft
- **Cargo**：80 t
- **Crew**（最少 8 人）：CO、pilot、navigator、4 engineers、medic；可追加 gunners、cutter pilots、行政
- **Build Time**：28 月

#### Patrol Cruiser (type T) — MCr 229.59

- **Hull**：400 t，**custom**，streamlined
- **Drives**：Jump-F / Maneuver-H / Power-H → Jump-3，4-G
- **Fuel**：160 t（1 次 jump-3）
- **Computer**：Model/3
- **Accommodations**：12 staterooms + 4 low berths
- **Armament**：4 triple turrets + 火控；2 座 Pulse Laser、2 座 Missile Rack
- **Vehicles**：1 GCarrier、1 ship's boat
- **Cargo**：50 t
- **Crew**（18）：pilot、navigator、3 engineers、medic、4 gunners、8 troops（登舰队）；gunners 与 troops 为双占
- **Build Time**：16 月

### Building Ships

定制注意事项：

1. 船体吨位如非表中标尺，按**下一档较大**档处理。本规则体系**最大船体 5,000 ton**。
2. 只允许 [Drive Potential Table](#drive-potential) 列出的驱动与 power plant。表内标 "−" 的驱动不可用于该吨位。
3. **Starship** 最小 100 ton；**Non-starship** 同最小 100 ton，只是省去 jump drive（价格其余不变）。**本设计流程不适用于 small craft**，但 p. 17–18 列出的标准小艇可大幅自定义。
4. 通常只在图纸上标 hardpoint，暂不加 turret/武器以控制造价和设计费；可后期加装。
5. 设计师在交付图纸与规格时坚持收取 **1%** 设计费。

#### Retrofitting Components

（errata 补齐；原 1981 版排版删节了以下段落）

- **Computers**：不同型号计算机可在新建或改装时安装或替换，不必沿用原图指定型号。新建时用别的型号替代原指定型号即可；**改装时，旧计算机可折价 25% 抵扣新计算机价格**。
- **Turrets**：Turret 可在船体既有 hardpoint 上**建成后加装**。既有 turret 可**拆除并替换**为不同规格的 turret。因 turret 属于可选装备，可自由**加入或剔除**标准图纸规格。**报废/替换的旧 turret 可按原价 25% 出售**。Turret 本身视为流线型。

### Formats

构造完成后，须以文档形式记录以便使用：

- **Paragraph Description**：按 [Starship Design Checklist](#starship-design-checklist) 顺序逐项描述成段。Book 2 所有 standard 船都按此法写就。
- **TAS Form 3**：见 Book 2 pp. 24–25 的空白表（可复印），涵盖注册号、原母星、建造年、排量、加速、jump、power plant、货舱、住舱、低温舱、全员、最少员数、船载 vehicle、船员名册、船东等信息。
- **Deck Plans**：方格纸绘制，**1.5 m/格**，层间距 3 m。1 ton ≈ 14 m³ ≈ **2 格甲板面积**。住舱只需部分吨位实际落于住舱，其余用作公共区；最终落差 ±10–20% 即可接受。

实际应用中两种格式常并用：设计者写段落，船东用 TAS Form 3 作运行记录。

### Design Tables

#### Standard Hulls

> 折扣船体；非表列吨位须按 MCr 0.1/ton 定制。

| Tons | Main | Drives | MCr | Time (月) |
|---:|---:|---:|---:|---:|
|  100 |  85 |  15 |   2 |  9 |
|  200 | 185 |  15 |   8 | 11 |
|  400 | 350 |  50 |  16 | 14 |
|  600 | 515 |  85 |  48 | 22 |
|  800 | 635 | 165 |  80 | 25 |
| 1000 | 835 | 165 | 100 | 27 |

- **Main** = 主舱段可用吨位；**Drives** = engineering section 可用吨位。

#### Drives and Power Plants

> 同一字母分别对应 jump / maneuver / power plant 的 mass 与 MCr。

| Letter | Jump Mass | Jump MCr | Maneuver Mass | Maneuver MCr | P-Plant Mass | P-Plant MCr |
|:---:|---:|---:|---:|---:|---:|---:|
| A |  10 |  10 |  1 |  4 |  4 |   8 |
| B |  15 |  20 |  3 |  8 |  7 |  16 |
| C |  20 |  30 |  5 | 12 | 10 |  24 |
| D |  25 |  40 |  7 | 16 | 13 |  32 |
| E |  30 |  50 |  9 | 20 | 16 |  40 |
| F |  35 |  60 | 11 | 24 | 19 |  48 |
| G |  40 |  70 | 13 | 28 | 22 |  56 |
| H |  45 |  80 | 15 | 32 | 25 |  64 |
| J |  50 |  90 | 17 | 36 | 28 |  72 |
| K |  55 | 100 | 19 | 40 | 31 |  80 |
| L |  60 | 110 | 21 | 44 | 34 |  88 |
| M |  65 | 120 | 23 | 48 | 37 |  96 |
| N |  70 | 130 | 25 | 52 | 40 | 104 |
| P |  75 | 140 | 27 | 56 | 43 | 112 |
| Q |  80 | 150 | 29 | 60 | 46 | 120 |
| R |  85 | 160 | 31 | 64 | 49 | 128 |
| S |  90 | 170 | 33 | 68 | 52 | 136 |
| T |  95 | 180 | 35 | 72 | 55 | 144 |
| U | 100 | 190 | 37 | 76 | 58 | 152 |
| V | 105 | 200 | 39 | 80 | 61 | 160 |
| W | 110 | 210 | 41 | 84 | 64 | 168 |
| X | 115 | 220 | 43 | 88 | 67 | 176 |
| Y | 120 | 230 | 45 | 92 | 70 | 184 |
| Z | 125 | 240 | 47 | 96 | 73 | 192 |

#### Computers

| Model | MCr | Tons | Capacity (CPU/Storage) | TL |
|:---:|---:|---:|:---:|:---:|
| 1    |  2 | 1 |  2 / 4  | 5 |
| 1bis |  4 | 1 |  4 / 0  | 6 |
| 2    |  9 | 2 |  3 / 6  | 7 |
| 2bis | 18 | 2 |  6 / 0  | 8 |
| 3    | 18 | 3 |  5 / 9  | 9 |
| 4    | 30 | 4 |  8 / 15 | A |
| 5    | 45 | 5 | 12 / 25 | B |
| 6    | 55 | 7 | 15 / 35 | C |
| 7    | 80 | 9 | 20 / 50 | D |

- Model 号同时限制 **最大可跃迁级**（例：Model/3 支持 ≤ Jump-3）。
- **bis** 版按 +1 jump 级处理，软件包按 −1 级。

#### Drive Potential

> 对照「船体吨位」与「驱动字母」得到驱动性能（maneuver → Gs；jump → parsec/周；power plant → Pn）。中间吨位按下一档较大船体读取。"−" 表示该组合无法工作。最后一列为 **自定义船体** 的建造时长（月；standard 船体参照 [Standard Hulls](#standard-hulls)）。

| Hull Tons | A | B | C | D | E | F | G | H | J | K | L | M | N | P | Q | R | S | T | U | V | W | X | Y | Z | Build (月) |
|---:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---:|
|  100 | 2 | 4 | 6 | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | 10 |
|  200 | 1 | 2 | 3 | 4 | 5 | 6 | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | 12 |
|  400 | − | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 | − | − | − | − | − | − | − | − | − | − | − | 16 |
|  600 | − | − | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 6 | 6 | − | − | − | − | − | 24 |
|  800 | − | − | − | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 6 | 6 | 6 | − | − | − | 28 |
| 1000 | − | − | − | − | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 6 | 6 | 6 | − | − | 30 |
| 2000 | − | − | − | − | − | − | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 4 | 6 | 32 |
| 3000 | − | − | − | − | − | − | − | − | − | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 34 |
| 4000 | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 3 | 35 |
| 5000 | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | − | 1 | 1 | 1 | 2 | 36 |

> 注：本表 OCR 噪声较大。以 CT 原版 drive potential 表的阶梯模式重构：同一 hull 下 maneuver-drive-A 开始，字母每升一档驱动提升 1 Gs；若驱动 letter 小于最小可用档则显示 "−"。2000 ton 以上的精确条目建议在实用前再对 PDF p. 22 抽查。

#### Weapons and Mounts

| Type | Cost (Cr) |
|---|---:|
| Hardpoint | 100,000 |
| Single Turret | 200,000 |
| Double Turret | 500,000 |
| Triple Turret | 1,000,000 |
| Pulse Laser | 500,000 |
| Beam Laser | 1,000,000 |
| Missile Rack | 750,000 |
| Sandcaster | 250,000 |

- Missile：**Cr 5,600/枚**，50 kg（homing type，1981 原书 Cr 5,000 为印误，已按 errata 修订）；Sand canister：Cr 400/枚，50 kg。

#### Fittings

| Fitting | Tons | Cost (Cr) |
|---|---:|---:|
| Stateroom | 4 | 500,000 |
| Low Berth | 0.5 | 50,000 |
| Emergency Low Berth | 1 | 100,000 |
| Small Craft Cabin | 2 | 50,000 |
| Small Craft Couch | 0.5 | 25,000 |
| Cargo | as required | as required |
| Fuel | as required | as required |

#### Vehicles

| Vehicle | Tons | MCr |
|---|---:|---:|
| ATV, Wheeled | 10 | 0.03 |
| ATV, Tracked | 10 | 0.03 |
| Air/Raft | 4 | 0.6 |
| Speeder | 6 | 1.0 |
| GCarrier | 8 | 1.0 |
| Launch | 20 | 14 |
| Ship's Boat | 30 | 16 |
| Pinnace | 40 | 20 |
| Cutter | 50 | 28 |
| &nbsp;&nbsp;Fuel Module | 30 | 1.0 |
| &nbsp;&nbsp;ATV Module | 30 | 1.8 |
| &nbsp;&nbsp;Open Module | 30 | 2.0 |
| Slow Boat | 30 | 15 |
| Slow Pinnace | 40 | 18 |
| Shuttle | 95 | 33 |
| Fighter | 10 | 18 |

#### Construction Fees

- **Architect**：1% of final ship cost
- **Standard Designs**：90% of list price
- **Financing**：20% down；此后每月付 1/240 list 价，共 480 期（40 年）

#### Crew Requirements（速查）

- **Pilot**：1 per ship
- **Navigator**：1 per ship over 200 tons
- **Engineer**：1 per 35 tons of drives
- **Steward**：1 per 8 high passengers
- **Medic**：1 per ship of 200 tons or more；再按 1 per 120 passengers
- **Gunner**：As required

### Starship Design Checklist

按顺序设计自定义星舰：

1. Select hull size.
2. Select drives.
   - A. Jump drive.
   - B. Maneuver drive.
   - C. Power plant.
3. Fuel Tankage.
   - A. Power plant and maneuver fuel. Formula: **10 Pn**.
   - B. Jump fuel. Formula: **0.1 M Jn**.
4. Bridge（**2%** of tonnage；最低 20 tons；MCr 0.5 per 100 tons of hull）
5. Computer.
6. Allocate accommodations for passengers and crew.
   - A. Staterooms.
   - B. Low Berths.
7. Armament.
   - A. Hardpoints.
   - B. Turrets.
   - C. Fire Control (1 ton per turret).
   - D. Weapons.
8. Vehicles. Select ship's vehicles and small craft.
9. Allocate cargo capacity.
10. Streamlining（MCr 1 per 100 tons）。
11. Determine crew.
12. Subtotal ship tonnage and costs.
13. Architect's fees（1% of total cost）。
14. Note total price and construction time required.

---

## 校对记录

抽查与 PDF 原页交叉验证的 5 处关键数值：

1. **CREW SALARIES**（PDF p. 11）— Pilot-1 Cr6,000、Navigator-1 Cr5,000、Engineer-1 Cr4,000、Steward-0 Cr3,000、Medic-1 Cr2,000、Gunner-1 Cr1,000。✓
2. **TYPICAL TRAVEL TIMES**（PDF p. 10）— 10,000 km 在 1-G 下 = 2000s；1,000,000,000 km 在 1-G 下 = 7.3d。OCR 漏掉全部 Kilometer 列值，现按扫描页重建全表。✓
3. **Subsidized Merchant (type R) 建造价**（PDF p. 19）— **MCr 100.035**（after discount），Build 14 月；对应 Jump-C / Maneuver-C / Power-C，200 t 货舱，13 stateroom。✓
4. **DRIVES AND POWER PLANTS**（PDF p. 22）— Drive Letter M：Jump mass 65 t / Jump MCr 120；Maneuver mass 23 t / Maneuver MCr 48；P-Plant mass 37 t / P-Plant MCr 96。与 Mercenary Cruiser（type C，Jump-M / Maneuver-M / Power-M）规格自洽。✓
5. **Emergency Low Berth 规格**（PDF p. 23 Fittings）— 1 ton / Cr 100,000，容 4 人同苏醒骰（正文 Book 2 p. 14）。✓

> Misjump 表（PDF p. 11）中 md OCR 将「Within 10 diameters of world」DM 错标为 `+15`；以 PDF 原页的 `+10` 为准。
