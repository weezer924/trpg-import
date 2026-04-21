# Classic Traveller · Book 3 · Worlds and Adventures (Worlds + Equipment)

> 源 PDF：`Rule Books/Traveller/Classic Traveller/Classic Traveller (Facsimile 1981 edition).pdf`
> 版本：1981 年修订版，Little Black Book 3 合订复刻
> 本文件覆盖：Book 3 前半——Worlds（第 4–16 页）+ Equipment（第 17–23 页），对应 PDF 页 108–127。
> 源 md 行：3258–3935（docling OCR 生成，关键表格已对照扫描原页重建）。
> Errata：本文件已合并 Don McKinney's Consolidated Traveller Errata 中的修订（Hydrographics = 2D−7+atmosphere、Gas Giant 含往返时间、Vacc Suit 引用 Book 1 p.41），原 1981 版错误见源 PDF p.154–158。

---

## Index

- Worlds（星图生成与 UWP）
  - Star Mapping
  - World Creation
  - Technological Level
  - Referee's Notes
  - System Contents Table
  - Starport Types
  - Size / Atmosphere / Hydrographics
  - Population / Government / Law Level
  - World Generation Checklist
  - System Hex Format
  - World Data Format
  - Tech Level Table (DMs)
  - Technological Levels（装备上限对照）
  - Trade Classifications
- Equipment
  - Personal Equipment
  - Personal Devices
  - Vision Aids
  - Tools
  - Shelters
  - Food and Overhead
  - Vehicles

---

## Key Terms

| 术语 | 缩写/写法 | 说明 |
|------|-----------|------|
| Universal World Profile | UWP | 星球完整代号，格式 `Starport-Size-Atm-Hyd-Pop-Gov-Law-Tech`，例：`A788899-B` |
| Starport | A/B/C/D/E/X | 星港等级，X = 无星港 |
| Tech Level | TL | 科技等级 0–20，常见 4–15 |
| Credits | Cr | 信用币，例：`Cr500`、`Cr10,000`、`Cr1,000,000` |
| Die Modifier | DM | 骰值修正，写作 `DM +1`、`DM -4` |
| Throw | throw N+ | 目标值掷骰，掷 2D 需等于或高于 N |
| Parsec | pc | 1 hex = 1 parsec ≈ 3.26 光年 |
| Subsector | — | 8 × 10 hex 星图单位；16 个子星区（4×4）= 1 sector |
| Gas Giant | G | 气态巨星，允许 streamlined 舰船 skim 无偿燃料 |

---

## Worlds

裁判有义务在游戏开始前规划宇宙。无需一次性铺完整张星图——只需要当前使用的一小块。无裁判模式下，可由一名玩家按章节或冒险进度动态生成星球。

宇宙以 **subsector（子星区）** 为单位绘制，每个子星区是一个 8 × 10 的六角格区域。推荐 1 hex = 1 parsec（3.26 光年），因此子星区覆盖 10 pc × 8 pc。Book 3 第 13 页附 subsector grid 模板，供裁判影印使用。

16 个子星区（4 × 4 排列）组成一个 **sector**，通常是一个 Traveller 战役可支撑的最大规模。

子星区绘制分两步：

1. **Star mapping**：逐 hex 判定是否存在恒星系，并决定星港、基地、气态巨星。
2. **World mapping**：针对每个系统中最重要的星球生成基本特征。

### STAR MAPPING

使用空白 subsector grid 和骰子逐格判定系统、星港、基地。**System Hex Format** 表规定各项信息在 hex 中的排布。裁判可选择保留部分信息不填，留给玩家在冒险中自行发现。

**World Occurrence**：默认每格有 1/2 概率出现星球。逐 hex 掷 1D，结果 4、5、6 在 hex 中画圆圈，表示有星球；否则留空。

裁判可按银河区域特色整体修正：对子星区或其中某大片区域施加 DM +1 或 -1。

**Starport Type**：凡有星球者掷 2D，对照 **System Contents Table** 查 Starport 列，把结果字母标入 hex。

星港类型分布可由裁判另行设计，Traveller 的系统内容表仅给出一种参考。

**Starport Types** 表详列各级星港能力：A 级可造星际舰；E 级仅是硬地；X 无星港。几乎所有星球都视星港为治外法权区，但会严格管控进出。

**Bases**：部分系统设有海军基地、侦察兵基地或其他政府机构基地。掷骰办法见 System Contents Table 中的 Naval Base / Scout Base 列。出现基地则按 world format 在 hex 中标注相应符号。

**Gas Giants**：气态巨星允许 streamlined 舰船通过 **skimming**（跳水）免费补给——省掉燃料费、提升利润；也支持在无星港的系统里加油。Skim 一次约耗一周（含往返气态巨星的旅程；实际掠取约 8 小时），所得燃料为 unrefined。

气态巨星常见度：**掷 10+ 表示无气态巨星**。若有，则在 hex 中标注。

**System Name**：系统通常以其主星球命名，由裁判决定后写入 hex。

**Travel Zones**：多数星球视为文明或至少对旅客开放。若处于战乱、疫区或排外状态，则以旅行区分类标注，共两种：

- **Amber（琥珀）**：需谨慎访问。可能因市民仇外、政局混乱或其他潜在威胁。
- **Red（红色）**：存在重大危险——疫区隔离、战区、政府明令禁入（保护未成熟文明或稀有资源）。

**Communications Routes**：地方政府会铺设连接部分（非全部）星球的通信/商贸干线。这些干线也是客运和大货运的主要航道。裁判在子星区图上把关键星球连线——若子星区属于更大联邦或帝国，干线应延伸到子星区边缘对接外界；若是孤立社群，则航线可全部内部收束。

干线应谨慎布置，避免整个子星区全面通达：保留若干偏远角落供探险。航线以单线连接 hex 即可。

星图完成后即展示各系统在空间中的分布以及商业航道关系。

### WORLD CREATION

"世界"一词涵盖系统中一切天体——行星、卫星、以及小行星带。星系中最重要的 world 未必是行星，可能是气态巨星的卫星，也可能是小行星带内某颗 planetoid。

星球的宏观特征与其对居民、旅客的影响通过 **Starport + 六项基本特征 + 技术指数** 表达，全部以单位数字（0–9）或字母（A–Z，omit O 和 I 避免与数字混淆）编码。规则通常只给出数字范围，字母留给裁判描述特殊情况。

World Creation 仅针对系统中最重要的那颗 world；系统内其他行星由裁判按需生成。

六项基本特征各投 2D，并套用来自其他特征的 DM。六项就绪后根据 starport 与特征算出技术指数。Starport、六项基本、Tech Level 共同构成 UWP。更多附加信息（地形、星像、社会结构等）可按需补充。

首次生成时应建立一份 subsector index：星球名、hex 位置、UWP、其他关键数据。玩家可随身携带。

此外，每颗星球在裁判笔记本中至少占 1 页（最好数页），记录星球名、hex 位置、特征细节；裁判还应补录其他相关资料——同系统其他行星、恒星辐射、地形类型、独立遭遇表（见 Animal Encounters 节）、动植物、产业与农业、社会与政府、乃至星球表面地图。

以下 6 项由六次 2D 投掷决定（含 DM 套用）；完整顺序见 World Generation Checklist。

**Starports**（已在 star mapping 阶段生成）：从地图上抄录即可。

**Planetary Size (2D - 2)**：表示星球直径，单位为千英里。Book 1 据此计算重力；Book 2 用于绘制太空战微缩用行星板。

**Planetary Atmosphere (2D - 7 + size; if size 0 then atmosphere 0)**：大气类型。某些大气需佩戴防护或呼吸器。

**Hydrographic Percentage (2D - 7 + atmosphere; if size 0 then hydrographics 0; if atmosphere 0, 1, or A+, then apply DM -4)**：行星表面被海洋/液体覆盖的比例，以 10% 为单位。普通星球为水；exotic、corrosive、insidious 大气下可能是氨等其他液体。

> OCR 注：md 原文将此处写成 "if atmosphere 0, 1, or 1+"，对照 PDF 应为 "0, 1, or A+"（A+ 指 exotic、corrosive、insidious 大气）。

**Population (2D - 2)**：居民数的 10 的幂指数。例：数值 6 = 约 10⁶（一百万）居民。

**Planetary Government (2D - 7 + population)**：政府形式，从无政府到极权。Balkanization（巴尔干化）是特殊结果：全球无统一政府、几个区域政权并立，裁判应分别生成每块领地的特征。

**Law Level (2D - 7 + government)**：法律严苛程度，直接规定武器持有与使用的限制。

遇到看似矛盾或离谱的组合时，以常识为准：裁判或玩家给出合理解释，或换一种描述。

裁判也可以始终绕过随机系统，按叙事需要直接设计星球——常为奖励或折磨玩家。

### TECHNOLOGICAL LEVEL

Tech Level 基于 1D 掷骰加上 UWP 各项的修正。

查 **Tech Level Table**，把星球的 Starport、Size、Atm、Hyd、Pop、Govt 各数字分别对应到表中对应列，汇总所有 DM；掷 1D 加上总 DM，即为该星球的 Tech Level。

Tech Level 范围 0–20，常见 4–10。数值越高，工业能力越强。

Tech Level 结合 Technological Levels 表可判断星球产出商品的大致种类与品质。通常，当地人使用的是本地可制造的最佳水准；更高等级的物品可通过进口取得。警察或军方可能装备本地造不出的武器。Tech Level 也决定当地修复/维护损坏物件的能力。

Technological Levels 表留有空格，裁判或玩家在游戏中发现新物件时可自行填补。

### REFEREE'S NOTES

世界生成流程本质上是给想象力一根撬棍。即便最有创造力的裁判，面对数百颗星球也会枯竭。掷骰把随机灵感替换掉，再让裁判据此演绎具体设定。有些结果需要想象力来自圆其说——例如在小行星带里诞生 Tech 4 的文明，或一个高人口星球采用"参与式民主"。

各项特征应视为参考而非硬限。例：hydrographic = A 表示 100% 海洋，但依然会有足够大的岛屿建星港。

**Starport**：各级星港为贸易或探勘任务提供多样设施，包括燃料与造船厂。

**Bases**：侦察与海军基地是老侦察兵和老海军叙旧、找赞助人、弄过剩装备的地方。裁判也可加陆军、商队勘探与贸易、防御工事等其他基地。

**Travel Zones**：用于标记"避开"与"探索"。裁判应考虑设立旅行区的深层原因。

**World Size**：生成规则默认星球是实心球体。替代形式罕见，由裁判自行引入：

- **Rosettes（玫瑰结构）**：三颗及以上等质量世界置于正多边形顶点、以相同角速度绕共同质心旋转，可形成稳定轨道。无需中心恒星。自然发生几乎不存在。
- **Ringworlds（环世界）**：某种极强材料绕恒星旋转成带，以离心力模拟重力。半径约 9300 万英里、宽度约 100 万英里的环世界，表面积约相当于 300 万个地球。
- **Sphereworlds（球世界）**：环世界材料加上必要的重力发生器，可做成包裹恒星的球壳。半径约 9300 万英里的球壳内表面约相当于 10 亿个地球，能完全捕获恒星辐射。

**Atmosphere**：不同大气对个人装备有具体要求——

- 无大气、trace 大气：必须 vacc suit。
- Tainted 大气：必须 filter mask。
- Very thin 大气：必须 compressor 保证氧气。Very thin tainted 大气需 respirator/filter mask 二合一。
- Thin、standard、dense 大气：无需辅助即可呼吸。
- Exotic 大气：需氧气瓶，但不需防护服。
- Corrosive 大气：需防护服或 vacc suit。
- Insidious 大气：类似 corrosive，但 2–12 小时内穿透任何个人防护。

**Hydrographics**：真空大气的星球也可能有 > 0 的水含量——此时水以冰盖形式存在，不是自由液态水。

**Population Density** 参考（20 世纪地球）：

- 地球整体约 30 亿人（Pop 9），约 5 人/平方英里（陆地区约 16）。
- 欧洲：约 151 人/平方英里，相当于 Pop 10。
- 荷兰：约 1500 人/平方英里，相当于 Pop 11。
- 香港：约 10,000 人/平方英里，相当于 Pop 12。

**Government**：给出当地权威的大致类型，是裁判管理当地遭遇时的关键线索。

**Law Level**：星球压抑程度的指标。对照 Law Level 表可看武器限制。同时它也是玩家被当局骚扰或逮捕的掷骰目标值：`throw law level +`。

**Tech Level**：决定产品质量与精密度，指出本地常见的装备类型。

**Trade Classifications**：补充表述星球特色的额外标签（见 Trade Classifications 节）。裁判可按需自立新分类。

---

## SYSTEM CONTENTS TABLE

| Die Roll | Starport | Naval Base | Scout Base | Gas Giant | | Digit | Description (Size 列) |
|---------:|:--------:|:----------:|:----------:|:---------:|---|:-----:|------------------------|
|  2 | A | no  | no  | yes | | 0 | Asteroid / Planetoid Belt. |
|  3 | A | no  | no  | yes | | 1 | 1000 miles (1600 km). |
|  4 | A | no  | no  | yes | | 2 | 2000 miles (3200 km). |
|  5 | B | no  | no  | yes | | 3 | 3000 miles (4800 km). |
|  6 | B | no  | no  | yes | | 4 | 4000 miles (6400 km). |
|  7 | C | no  | no  | yes | | 5 | 5000 miles (8000 km). |
|  8 | C | no  | yes | yes | | 6 | 6000 miles (9600 km). |
|  9 | D | yes | yes | yes | | 7 | 7000 miles (11200 km). |
| 10 | E | yes | yes | no  | | 8 | 8000 miles (12800 km). |
| 11 | E | yes | yes | no  | | 9 | 9000 miles (14400 km). |
| 12 | X | yes | yes | no  | | A | 10000 miles (16000 km). |

每列单独投骰。

- **Scout base**：starport C 时 DM -1；starport B 时 DM -2；starport A 时 DM -3。starport E 或 X 时不投。
- **Naval base**：starport C、D、E、X 时不投。
- **Size**：大于 A 的尺寸由裁判自创。

---

## STARPORT TYPES

| Type | Description |
|:----:|-------------|
| A | Excellent quality installation. Refined fuel available. Annual maintenance overhaul available. Shipyard capable of constructing starships and non-starships present. Naval base and/or scout base may be present. |
| B | Good quality installation. Refined fuel available. Annual maintenance overhaul available. Shipyard capable of constructing non-starships present. Naval base and/or scout base may be present. |
| C | Routine quality installation. Only unrefined fuel available. Reasonable repair facilities present. Scout base may be present. |
| D | Poor quality installation. Only unrefined fuel available. No repair or shipyard facilities present. Scout base may be present. |
| E | Frontier installation. Essentially a marked spot of bedrock with no fuel, facilities, or bases present. |
| X | No starport. No provision is made for any ship landings. |

---

## ATMOSPHERE

| Digit | Description |
|:-----:|-------------|
| 0 | No atmosphere. |
| 1 | Trace. |
| 2 | Very thin, tainted. |
| 3 | Very thin. |
| 4 | Thin, tainted. |
| 5 | Thin. |
| 6 | Standard. |
| 7 | Standard, tainted. |
| 8 | Dense. |
| 9 | Dense, tainted. |
| A | Exotic. |
| B | Corrosive. |
| C | Insidious. |

Note：大气类型可能要求防护装备，具体见 Book 3 第 9 页（本文 Atmosphere 小节）。

---

## HYDROGRAPHICS

| Digit | Description |
|:-----:|-------------|
| 0 | No free standing water. Desert. |
| 1 | 10% water. |
| 2 | 20% water. |
| 3 | 30% water. |
| 4 | 40% water. |
| 5 | 50% water. |
| 6 | 60% water. |
| 7 | 70% water. |
| 8 | 80% water. |
| 9 | 90% water. |
| A | No land masses. Water World. |

---

## POPULATION

| Digit | Description |
|:-----:|-------------|
| 0 | No inhabitants. |
| 1 | Tens of inhabitants. |
| 2 | Hundreds of inhabitants. |
| 3 | Thousands of inhabitants. |
| 4 | Tens of thousands. |
| 5 | Hundreds of thousands. |
| 6 | Millions of inhabitants. |
| 7 | Tens of millions. |
| 8 | Hundreds of millions. |
| 9 | Billions of inhabitants. |
| A | Tens of billions. |

---

## GOVERNMENT

| Digit | Type | Description |
|:-----:|------|-------------|
| 0 | — | No government structure. In many cases, family bonds predominate. |
| 1 | Company / Corporation | Government by a company managerial elite; citizens are company employees. |
| 2 | Participating Democracy | Government by advice and consent of the citizen. |
| 3 | Self-Perpetuating Oligarchy | Government by a restricted minority, with little or no input from the masses. |
| 4 | Representative Democracy | Government by elected representatives. |
| 5 | Feudal Technocracy | Government by specific individuals for those who agree to be ruled. Relationships are based on the performance of technical activities which are mutually beneficial. |
| 6 | Captive Government | Government by an imposed leadership answerable to an outside group. A colony or conquered area. |
| 7 | Balkanization | No central ruling authority exists; rival governments compete for control. |
| 8 | Civil Service Bureaucracy | Government by agencies employing individuals selected for their expertise. |
| 9 | Impersonal Bureaucracy | Government by agencies which are insulated from the governed. |
| A | Charismatic Dictator | Government by a single leader enjoying the confidence of the citizens. |
| B | Non-Charismatic Leader | A previous charismatic dictator has been replaced by a leader through normal channels. |
| C | Charismatic Oligarchy | Government by a select group, organization, or class enjoying the overwhelming confidence of the citizenry. |
| D | Religious Dictatorship | Government by a religious organization without regard to the specific needs of the citizenry. |

---

## LAW LEVEL

| Digit | Description |
|:-----:|-------------|
| 0 | No prohibitions. |
| 1 | Body pistols undetectable by standard detectors, explosives (bombs, grenades), and poison gas prohibited. |
| 2 | Portable energy weapons (laser carbine, laser rifle) prohibited. Ship's gunnery not affected. |
| 3 | Weapons of a strict military nature (machine guns, automatic rifles) prohibited. |
| 4 | Light assault weapons (submachineguns) prohibited. |
| 5 | Personal concealable firearms (such as pistols and revolvers) prohibited. |
| 6 | Most firearms (all except shotguns) prohibited. The carrying of any type of weapon openly is discouraged. |
| 7 | Shotguns are prohibited. |
| 8 | Long bladed weapons (all but daggers) are controlled, and open possession is prohibited. |
| 9 | Possession of any weapon outside one's residence is prohibited. |

Note：Law level 同时是警察或执法人员对违规行为骚扰/逮捕的掷骰目标值。例如 law level 4 的星球上，被海关或警察拦下时躲避逮捕需 throw 4+。

---

## WORLD GENERATION CHECKLIST

1. Determine world occurrence (1D，4、5、6 标记，默认设定)。
2. 查 System Contents Table 详定系统内容：
   - A. Starport type（掷 2D）。
   - B. Naval base（掷 2D，若 starport 允许）。
   - C. Scout base（掷 2D，starport 相应 DM）。
   - D. Gas giant（throw 10+ 为无气态巨星）。
3. 命名星球。
4. 判定是否为 travel zone（amber / red）。
5. 连接通信/商贸干线。
6. 生成 UWP：
   - A. 抄录 starport。
   - B. Size: 2D - 2。
   - C. Atmosphere: 2D - 7 + size。Size 0 → atmosphere 0。
   - D. Hydrographics: 2D - 7 + atmosphere。Size 0 → hydrographics 0；atmosphere 0、1 或 A+ → DM -4。
   - E. Population: 2D - 2。
   - F. Government: 2D - 7 + population。
   - G. Law Level: 2D - 7 + government。
   - H. Tech Level: 1D + DMs from tech level table。
7. 查 Trade Classifications 为星球打标签。
8. 抄录入簿备用。

---

## SYSTEM HEX FORMAT

在 subsector grid map 上记录系统信息的标准格式如下（摘自 Book 3 第 12 页）：

**无气态巨星系统（示例左侧 hex）：**

- 左上：Naval Base（★ 星号）
- 左下：Scout Base（▲ 三角）
- 上方中央：Starport Type（字母：A/B/C/D/E/X）
- 中央：World Symbol（圆圈表示有 world；填色或附加记号表示 travel zone）
- 右上："No Gas Giant" 留空（不标 ●）
- hex 下方：System Name（本例为 "Beta"）

**有气态巨星系统（示例右侧 hex）：**

- 右上：Gas Giant Present（● 实心圆点）
- 中央：World Symbol（"no oceans" 情况写 ○，完全无水；其他情况写 ●）
- hex 下方：System Name（本例为 "Alfa"）

Travel zones 用不同填充或颜色标在 hex 上；amber 与 red 各自独立记号。

---

## WORLD DATA FORMAT

记录 universal planetary profile 时使用以下格式，确保包含 name、hex location、UPP、bases、trade classifications、travel zones、gas giant：

```
Speer    0108   C432430-8   S   Poor. Non-industrial.    R G
```

字段含义：

| 字段 | 值示例 | 说明 |
|------|--------|------|
| Name | Speer | 星球名 |
| Hex | 0108 | 列 01，行 08 |
| UPP | C432430-8 | Starport C, Size 4, Atm 3, Hyd 2, Pop 4, Gov 3, Law 0, Tech 8 |
| Bases | S | Scout base（N = Naval；N S = 两者皆有） |
| Trade | Poor. Non-industrial. | Trade classifications |
| Zones | R | R = Red（A = Amber，无记号 = 正常） |
| Gas Giant | G | G = Gas Giant Present（无记号 = 无气态巨星） |

---

## TECH LEVEL TABLE（DM 查表）

查表规则：把星球 UWP 的每一位分别对应到下表的 Starport / Size / Atm / Hyd / Pop / Govt 列，汇总全部 DM，加到 1D 骰值上即得 Tech Level。

| Digit | Starport | Size | Atm | Hyd | Pop | Govt |
|:-----:|:--------:|:----:|:---:|:---:|:---:|:----:|
| 0 |    | +2 | +1 | —  | —  | +1 |
| 1 |    | +2 | +1 | —  | +1 | —  |
| 2 |    | +1 | +1 | —  | +1 | —  |
| 3 |    | +1 | +1 | —  | +1 | —  |
| 4 |    | +1 | —  | —  | +1 | —  |
| 5 |    | —  | —  | —  | +1 | +1 |
| 6 |    | —  | —  | —  | —  | —  |
| 7 |    | —  | —  | —  | —  | —  |
| 8 |    | —  | —  | —  | —  | —  |
| 9 |    | —  | —  | +1 | +2 | —  |
| A | +6 | —  | +1 | +2 | +4 | —  |
| B | +4 |    | +1 |    |    | —  |
| C | +2 |    | +1 |    |    | —  |
| D | —  |    | +1 |    |    | -2 |
| E | —  |    | +1 |    |    | —  |
| F |    |    |    |    |    | —  |
| X | -4 |    |    |    |    |    |

说明：

- "—" 表示该格对应 DM 为 0（无修正）。
- 空白表示在当前生成系统下该数字不可能出现在该列中（如数字 0–9 不会出现在 Starport 列；字母 F 仅作 Government 数字使用）。
- Starport 列仅适用于 starport 字母 A/B/C/D/E/X 的查表；其他数字列只吃 0–9（及少数情形下的 A）。
- 应用示例：UWP `A788899-?` → Starport A = +6、Size 7 = 0、Atm 8 = 0、Hyd 8 = 0、Pop 9 = +2、Govt 9 = 0，汇总 +8；掷 1D，假设 4，则 Tech Level = 4 + 8 = 12。

---

## TECHNOLOGICAL LEVELS · 装备对照表（武器 / 防具 / 重武器 / 电脑 / 通信）

| TL | Personal Weaponry | Armor | Heavy Weaponry | Computers | Communications |
|:--:|-------------------|-------|----------------|-----------|----------------|
| 0 | club, cudgel, spear | | | | runners |
| 1 | dagger, pike, sword | jack | catapault | abacus | heliograph |
| 2 | halberd, matchlock, broadsword | | cannon | | |
| 3 | foil, cutlass, flintlock blade, bayonet | | | | |
| 4 | revolver, shotgun | | artillery | adding machine | telephones |
| 5 | carbine, rifle, pistol, SMG | steel plate | sandcasters, mortars | Model/1 | radio |
| 6 | auto rifle, light machine gun | cloth | missiles, missile launchers | Model/1 bis | television |
| 7 | body pistol | mesh, flak jacket | pulse laser, grenade launcher | Model/2, hand calculator | |
| 8 | laser carbine, snub pistol | vacc suit | auto-cannon | Model/2 bis, artillery computer | |
| 9 | laser rifle | ablat | beam laser | Model/3, battle computer | |
| 10 | | reflec | | Model/4 | |
| 11 | | combat armor | | Model/5, hand computer | |
| 12 | | | | Model/6 | |
| 13 | | battle dress | | Model/7 | |
| 14 | | | | | |
| 15 | | | | | |
| *— beyond common levels —* | | | | | |
| 16 | | | disintegrators | | |
| 17 | | | | artificial intelligence | |
| 18–20 | | | | | |

## TECHNOLOGICAL LEVELS · 装备对照表（交通 / 能源）

| TL | Water | Land | Air | Space | Energy |
|:--:|-------|------|-----|-------|--------|
| 0 | canoes, rafts | carts | | | muscle |
| 1 | galleys | wagons | | | |
| 2 | | | | | wind |
| 3 | sailing ships | | hot air balloons | | water wheel |
| 4 | steamships | trains | dirigibles | | coal |
| 5 | | ground cars | fixed wing aircraft | | oil |
| 6 | submersibles | ATV, AFV | rotary wing aircraft | | fission |
| 7 | ← hovercraft → | ← hovercraft → | | non-starships | solar |
| 8 | | | air/rafts | | fusion |
| 9 | | | | drives A–D, jump drive | |
| 10 | | ← grav vehicles, grav tanks → | ← grav vehicles → | drives E–H | |
| 11 | | | | drives J–K | |
| 12 | | | grav belts | drives L–N | |
| 13 | | | | drives P–Q | |
| 14 | | | | drives R–U | |
| 15 | | | | all drives | |
| *— beyond common levels —* | | | | | |
| 16 | ← matter transport → | ← matter transport → | | | |
| 17 | | | | | anti-matter |
| 18–20 | | | | | |

说明：表格有空格代表当前规则系统下无对应物品；裁判或玩家在游戏中发现新物件时可填入。

---

## TRADE CLASSIFICATIONS

Trade classification 是对影响贸易与商务的星球属性的统称，部分分类会直接影响 Book 2 的 trade and commerce 表。

| 分类 | 限定条件 | 含义 |
|------|----------|------|
| **Agricultural** | Atm 4–9 且 Hyd 4–8 且 Pop 5–7 | 大比例经济投入农业。 |
| **Non-Agricultural** | Atm ≤ 3 且 Hyd ≤ 3 且 Pop ≥ 6 | 需大量进口食物；可能本地合成低端食品，高质食材依赖进口奢侈品。 |
| **Industrial** | Atm 0、1、2、4、7 或 9（真空/trace/tainted）且 Pop ≥ 9 | 工业基础雄厚，能大量生产成品。 |
| **Non-Industrial** | Pop ≤ 6 | 成品高度依赖进口。 |
| **Rich** | Govt 4–9 且 Atm 6 或 8 且 Pop 6–8 | 气候宜居，是多数个人愿意定居的理想之地。 |
| **Poor** | Atm 2–5 且 Hyd ≤ 3 | 欠发达、边缘地带。 |
| **Water World** | Hyd A | 完全被海洋覆盖。 |
| **Desert** | Hyd 0 | 无自由液态水。 |
| **Vacuum** | Atm 0 | 无大气。 |
| **Asteroid Belt** | Size 0 | 小行星群围绕中心恒星。 |
| **Ice-capped** | Atm 0 或 1 且 Hyd ≥ 1 | 水仅以冰盖形式存在，多为真空世界。 |
| **Subsector Capital** | 裁判指派 | 子星区中最重要的星球（若整个 sector 为单一星际政府）。 |
| **Capital** | 裁判指派 | 某个星际政府的首府；若子星区内多政府并立，每个都有自己的 capital。 |

其他可扩展分类：Prison Worlds、Exile Worlds、Preserves / Reserves 等，由裁判定义。

---

## Equipment

物理物件的种类与价格变化无穷，无法一一穷列。以下条目展示通用品质与价位的代表。

每条记录格式：**物品名 (TL) Cr价格**，后附说明。TL 指本地若要量产该物件所需的最低科技等级。价格与重量按 TL 10–15 的星际社会量产水平计；较低 TL 的同类产品更笨重、更昂贵。未注明重量的物件可方便地携带或穿戴。

该清单视为冒险者采买清单——出发前在清单上勾选装备。清单不包含武器（见 Book 1）。在 TL 足够的星球通常可自由购得；其他星球可按进口溢价取得。具体售价可能随 trade and speculation 规则上下浮动。

---

### PERSONAL EQUIPMENT

个人生存类物件：

| 物品 | TL | 价格 | 重量 | 说明 |
|------|:--:|-----:|------|------|
| Respirator | 5 | Cr100 | — | 允许在 very thin（Atm 3）大气下呼吸的小型压缩机。 |
| Filter Mask | 3 | Cr10 | — | 允许在 tainted 大气（Atm 4、7、9）下呼吸的过滤器套组。 |
| Combination | 5 | Cr150 | — | Filter mask + respirator 二合一，允许在 very thin tainted（Atm 2）下呼吸。 |
| Oxygen Tanks | 5 | Cr500 | 5 kg（两瓶，6 小时） | 压缩氧气瓶，允许在烟雾、尘埃、毒气或 exotic（Atm A）下独立呼吸。Refill: Cr20。 |
| Underwater Air Tanks | 5 | Cr800 | 5 kg（两瓶，6 小时） | 水下版氧气瓶。Refill: Cr20。 |
| Artificial Gill | 8 | Cr4,000 | 4 kg | 从水中提取氧气，水下时间不限。仅适用于 thin/standard/dense（Atm 4–9）星球。 |
| Swimming Equipment | 3 | Cr200 | — | 含泳鳍、潜水服、面镜。 |
| Protective Suit | 5 | Cr700 | 5 kg（Jack 级防护） | 抗 corrosive（Atm B）大气。重型版 Cr1400、7 kg，Cloth 级防护。 |
| Vacc Suit | 8 | Cr10,000 | — | 真空、trace、exotic、corrosive 大气穿戴；very thin 或 tainted 也可穿。含氧气瓶、短程通讯等完整设备。更多变种见 Book 1 第 41 页。 |
| Cold Weather Clothing | 1 | Cr200 | — | 御严寒。按 Jack 级防护处理。 |

---

### PERSONAL DEVICES

个人设备：

| 物品 | TL | 价格 | 重量 | 说明 |
|------|:--:|-----:|------|------|
| Short Range Communicator | 5 | Cr100 | TL 5 时 5 kg；TL 7 时 300 g | 腰挂无线电，10 km 范围（地下/水下缩短），3 频道。 |
| Medium Range Communicator | 5 | Cr200 | TL 5 时 10 kg；TL 7 时 500 g | 腰挂或背挂，最高 30 km，可接官方频道，5 频道。 |
| Long Range Communicator | 6 | Cr500 | TL 6 时 15 kg；TL 7 时 1.5 kg | 背负式，最高 500 km，可与轨道舰船通讯，10 频道。 |
| Magnetic Compass | 3 | Cr10 | — | 指示磁北（若存在）。 |
| Inertial Locator | 9 | Cr1,200 | 1.5 kg | 指示从起点出发的方向与距离。 |
| Metal Detector | 6 | Cr300 | 1 kg | 探测金属。 |
| Radiation Counter | 5 | Cr250 | 1 kg | 探测辐射及强度。 |
| Bull-Horn | 5 | Cr120 | 0.5 kg | 高声扩音，体积笨重、不便携。 |
| Hand Calculator | 7 | Cr10 | 0.1 kg | 基本数学运算。 |
| Hand Computer | 11 | Cr1,000 | 0.5 kg | 小型电脑功能；经内置无线电或其他电路可作大电脑的终端。 |
| Artificial Psionic Shield Helmet | 8 | Cr4,000 | 1 kg | 抵御灵能力量。 |
| Handcuffs | 2 | Cr25 | 0.3 kg | 高 TL 版本更轻。 |
| Wrist Watch | 4 | Cr25–Cr1,000 | — | 价格决定品质。 |

---

### VISION AIDS

视觉辅助：

| 物品 | TL | 价格 | 重量 | 说明 |
|------|:--:|-----:|------|------|
| Binoculars | 3 | Cr75 | 1 kg | 双筒望远镜。 |
| IR Goggles | 6 | Cr500 | — | 可见红外热源，画质必然失真。 |
| Light Intensifier Goggles | 7 | Cr500 | — | 只要不是全黑即可视物。 |
| Torches（火把） | 1 | Cr1 | 0.25 kg | 持续约 20 分钟。 |
| Electric Torches（手电筒） | 5 | Cr10 | 0.5 kg | 连续使用约 6 小时。 |
| Gas or Oil Lamp | 2 | Cr10 | 0.5 kg | 持续约 6 小时。 |
| Cold Light Lantern | 6 | Cr20 | 0.25 kg | 连续使用 3 天。 |

---

### TOOLS

工具套装：

| 物品 | TL | 价格 | 重量 | 说明 |
|------|:--:|-----:|------|------|
| Carpentry Tool Set | 2 | Cr300 | 25 kg | 切、整形、拼装木材。箱装。 |
| Metalwork Tool Set | 4 | Cr1,500 | 50 kg | 金属加工、焊接、塑形。箱装。 |
| Chain Saw | 6 | Cr500 | 8 kg | 电/油动链锯，切伐树木。 |
| Mechanical Tool Set | 5 | Cr1,000 | 20 kg | 机械装置维修改装。箱装。 |
| Medical Kit | 7 | Cr1,000 | 10 kg | 含药品、外科用品、诊断物料，供医生使用。 |
| Electronic Tool Set | 7 | Cr2,000 | 5 kg | 电子组装与维修基础工具。箱装。 |
| Lock Pick Set | 4 | Cr10 | — | 普通锁每 15 秒投 1 次，`throw 8+` 成功。Law 8+ 星球视为违法，价格抬到 Cr100 以上。 |
| Disguise Kit | 7 | Cr1,000 | 5 kg | 临时改变个人外貌。 |

---

### SHELTERS

可携式/临时居所：

| 物品 | TL | 价格 | 尺寸 / 重量 | 说明 |
|------|:--:|-----:|-------------|------|
| Tarpaulin | 1 | Cr10 | 2 × 4 m / 2 kg | 防水帆布，可搭临时遮蔽。 |
| Tent | 2 | Cr200 | 双人用 / 3 kg | 更大更精美者价格与重量更高。 |
| Pressure Tent | 7 | Cr2,000 | 双人用 / 25 kg | 提供 standard 大气。无气闸，进出需先减压。 |
| Pre-Fabricated Cabin | 6 | Cr10,000 | 2 × 6 × 6 m / 4 tons | 6 人未加压模块化宿舍，可载于舰船货仓。 |
| Advanced Base | 8 | Cr50,000 | 2 × 6 × 6 m / 6 tons | 6 人加压模块化宿舍，含气闸与大气循环系统，可载于舰船货仓。 |

---

### FOOD AND OVERHEAD

食物与基本开销：

**日常餐饮（每人每天）：**

| 形态 | 价格 | 备注 |
|------|-----:|------|
| Restaurant meal, ordinary quality | Cr10/天 | 普通餐厅 |
| Restaurant meal, excellent quality | Cr20–Cr50/人 | 高档 |
| Travellers' Aid Society meal | Cr20 | 会员及宾客，品质优秀 |
| Groceries (home prep) | Cr5/天 | 重约 1 kg |
| Canned / Packaged ration | Cr20/天 | 重约 0.5 kg |
| Dehydrated ration | Cr25/天 | 重约 0.2 kg，需本地水 |

**长期生活（时间快进场景，每月）：**

| 等级 | 食物 | 住宿 |
|------|-----:|-----:|
| Starvation Level | Cr60 | Cr60（dismal） |
| Subsistence Level | Cr120 | Cr180（acceptable） |
| Ordinary Level | Cr200 | Cr200（good） |
| High Living | Cr600 | Cr300（excellent） |

**Starships**：舰船乘客与船员的食宿由船方提供。

---

### VEHICLES

冒险者离开星港后常需各类交通工具。以下是通用指南。

**Primitive Transportation（TL 0–3 星球）**：主要依靠驮兽、畜力车、帆船与桨船。价格视本地情况：动物与大车按数百信用币计，船只按数千到数万计。本地驮畜与坐骑来自 local encounter tables 中的驯化食草动物，通常 200 或 400 kg 量级以上。Low passage 舱位可装下最多 400 kg 的坐骑，角色可带坐骑出入星球。

**Modern Transportation** 分 6 类：Ground Cars、Hovercraft、Winged Craft、Grav Vehicles、Grav Belts、Watercraft。Grav Belt 与 Hovercraft 类各只有 1 种；其余类多种。均需驾驶技能：Grav vehicles 用 air/raft skill；ATV 与 AFV 用 ATV skill；其余用 vehicle skill（该技能须具体指派到某辆车——含 ATV 但不含 grav vehicle）。同类其他车辆以 skill -1 操作（例如 helicopter-2 可以 level-1 驾驶 fixed wing 或 primitive biplane）。

#### Ground Cars

所有轮式或履带式车辆。具 ATV skill 者可以全等级驾驶 AFV。任何角色在慢速且非危险条件下可无技能驾驶任一地面车。

裁判参考掷骰：

- `throw 11+` → 机械故障或失效（可套用驾驶员熟练度、地形、车辆年代/状况 DM）。
- `throw 11+` → 地形阻碍（或直接并入当前星球的遭遇表）。
- 超速/违规被拦：以 `law level +` 为掷骰目标值避免。

| 车辆 | TL | 价格 | 吨位 | 性能与说明 |
|------|:--:|-----:|------|------------|
| Ground Car | 5 | Cr4,000 | 2 tons | 普通自走轮式车，道路/civilized 用途。Range 1000 km，cruise 100 kph，max 150 kph，越野时最多 10 kph。燃料依本地 TL（碳氢燃料/氢/电池）。高 TL 自动驾驶，部分高文明星球禁人工驾驶。载员 5 人 + 行李。变种（敞篷、跑车、豪华、货卡、摩托、独轮、面包车等）价格各异。不加压。量产型适配特定星球，转至异类星球时易故障。 |
| All Terrain Vehicle (ATV) | 6 | Cr30,000 | 10 tons | 轮/履带式越野探勘车。Range 5000 km，路面 cruise 60 kph，max 100 kph；越野依地形，最高开阔 ≈ 路面速度，险地 ≤ 20 kph。履带版更慢但更可靠。可由舰船电力或自带小型 fusion pack 供能（需氢或水）。适应真空/insidious 大气、高低重力。驾驶 1 人；载员最多 16，全加压，含紧凑的餐/睡/起居设施（可居 8 人）。可轻装甲、可加装炮塔。 |
| Armored Fighting Vehicle (AFV) | 6 | Cr70,000 | 10 tons | 重装甲重火力版 ATV。性能、续航、燃料相似。标配炮塔（激光或其他当地武器）。乘员 3（ATV skill 1、gunnery 1、无技能 1），无载员/货运设计。 |

#### Hovercraft

气垫车（1–3 m 飞行高度）。仅 Atm 4+ 可用。

| 车辆 | TL | 价格 | 吨位 | 性能与说明 |
|------|:--:|-----:|------|------------|
| Hovercraft | 6 | Cr200,000 | 8 tons | Cruise 60 kph，burst max 150 kph。续航 2000 km。陆/水通行，但破碎地形、悬崖、风暴不利。驾驶 1 人；载员最多 15，货 3 tons。一般不装甲不武装。 |

#### Winged Craft（有翼航空器）

固定翼或旋翼。仅 Atm 4+ 可用。TL 5 起有动力航空器；TL 0 即可造无动力滑翔机，TL 3 常见。

定期维护：`throw 11+` 为故障门槛，每漏检一次加 DM +1。

| 车辆 | TL | 价格 | 吨位 | 性能与说明 |
|------|:--:|-----:|------|------------|
| Primitive Biplane Aircraft | 5 | Cr20,000 | 1 ton | 早期小型双翼机。Cruise 150 kph，burst max 200 kph，续航 3 小时。化学燃料。乘员 1 + 乘客 1 + 货 100 kg。 |
| Fixed Wing Aircraft | 6 | Cr1,000,000 | 5 tons | 双喷气单翼货运机。Cruise 600 kph，max 700 kph，续航 3600 km / 6 小时。航空煤油。乘员 2（仅 1 需飞行技能），载员 6 + 货 5 tons。翼展/机长 ≈ 15 m。水上、武装、加大、更快等变种可得。 |
| Helicopter | 6 | Cr100,000 | 1 ton | 单引擎旋翼机，VTOL 能力。Cruise 200 kph，max 250 kph，续航 600 km。乘员 1，载员 7 + 货 500 kg。 |

#### Grav Vehicles

高科技社会的主力交通工具。TL 10+ 之后其他类别除少数特殊场合外几乎绝迹。所有 grav vehicles 操控特性近似，具 air/raft skill 者可驾驶任意 grav vehicle。Speeder 是例外：在 cruise 速附近时驾驶以 `air/raft skill -1` 判定；若以 air/raft 同级低速飞行则无惩罚。Grav vehicles 在任何环境下均可工作，且皆能（最终）达到轨道。

| 车辆 | TL | 价格 | 吨位 | 性能与说明 |
|------|:--:|-----:|------|------------|
| Air/Raft | 8 | Cr600,000 | 4 tons | 轻型反重力车，使用 null-grav 模块实现升力与推进。Cruise 100 kph（极易受风影响），max 约 120 kph。可入轨道，所需小时数 = UPP 的 Size 数字；乘员需 vacc suit；不可行星际飞行。星面范围/续航几乎不限，每约 10 周回舰船补能。载员 4 + 货 4 tons。不加压，通常敞篷。 |
| GCarrier | 8 | Cr1,000,000 | 8 tons | 封闭式军/准军用 grav 车。air/raft 同级性能，附炮位与装甲尾门。乘员 1（air/raft skill）+ 炮手 1（若武装）。载员 14（含驾驶与炮手）+ 货 2 tons（或每少 1 名乘员换 250 kg 货，例如仅带驾驶、炮手两人可带 5 tons 货）。 |
| Speeder | 8 | Cr1,000,000 | 6 tons | 流线型高速 grav 车。Cruise 1000 kph，max 1200 kph，续航几乎无限，每约 10 周从舰船补能。乘员 1（`air/raft -1`）+ 乘客 1 + 货 100 kg。可 1 小时内入轨道。 |
| Grav Belt | 12 | Cr100,000 | 工作时可忽略；关机 10 kg | 个人反重力装置，单个 null-grav 模块加人身挂具。速度与续航近似 air/raft。 |

#### Water Vehicles

≤ 50 tons 排水量的水上艇只需 1 名受训船员；更大吨位及所有舰船需数名训练船员。

| 车辆 | TL | 价格 | 吨位 | 性能与说明 |
|------|:--:|-----:|------|------------|
| Small Steamship | 4 | Cr60,000 | 100 tons | 型号多样，多可持续 30 kph。燃料为基本可燃物。船员 5 + 载员 10 + 货 50 tons。 |
| Motor Boat | 5 | Cr60,000 | 60 tons | 高级水翼小艇。Cruise 60 kph，burst 100 kph。燃料依本地能源（碳氢或电池）。船员 3 + 载员 8 + 货 10 tons。 |
| Submersible | 6 | Cr2,000,000 | 500 tons | 水下舰艇，规避水面气象。大水量星球（尤其 Hyd A）中往返水下穹顶城市的主力。水下 cruise 40 kph，水面约半。续航不限，依本地能源补给。船员 5 + 载员 10 + 货 30 tons。 |

---

## 校对注记（Errata）

以下几处 OCR 与原 PDF 对照后做了修正：

1. **Hydrographic 生成公式**：docling OCR 产出 "if atmosphere 0, 1, or 1+, then apply DM -4"，依 PDF 应为 "0, 1, or A+"。
2. **System Contents Table**：OCR 把 starport 列与 size 列粘连，已按 PDF 第 10 页重建成两个独立表格。
3. **Tech Level Table (DMs)**：OCR 把 Digit 与 Starport 列错位、-4/+6 错行。依 PDF 第 12 页重建，关键要点：
   - Row `9`：Hyd +1、Pop +2。
   - Row `A`：Starport +6、Atm +1、Hyd +2、Pop +4。
   - Row `D`：Govt -2。
   - Row `X`：Starport -4。
4. **Technological Levels 两张表**：OCR 把列对齐完全打乱，按 PDF 第 14–15 页重建。
5. **Hovercraft 价格**：OCR 遗失整条定义起始，依 PDF 第 22 页补全为 `Hovercraft (6) Cr200,000, 8 tons`。
