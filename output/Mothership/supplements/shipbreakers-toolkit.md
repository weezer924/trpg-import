# shipbreakers-toolkit: 拆船员工具箱

> 源：`Rule Books/OSR related/Mothership/core books/Shipbreaker's Toolkit v1.2.pdf`（英文 v1.2，44 页）
> 作者：Sean McCoy；Ships designed by Sam Wildman；编辑：Jarrett Crader；TKG 出品（2023）
> 用途：扩展 PSG / WOM 的飞船规则 — 飞船属性、舰种、升级、武器、太空旅行、飞船战斗（Megadamage / Morale）、维修维护、运营经济（公司 / 军方 / 自营 / 自由职业）。
> 写作语言：英文为主，关键术语首次出现附中文注释（参考 [glossary.md](glossary.md)）。

## Index

- [Overview 概述](#overview-概述)
- [Quick Reference Card 速查卡](#quick-reference-card-速查卡)
  - [Ship Deckplan Icons 甲板图例标符](#ship-deckplan-icons-甲板图例标符)
  - [General Travel Costs 通用旅行费用](#general-travel-costs-通用旅行费用)
  - [Fuel Costs Summary 燃料消耗汇总](#fuel-costs-summary-燃料消耗汇总)
  - [Range & Distance Reference 距离段综合表](#range--distance-reference-距离段综合表)
- [Ship Basics 飞船基础](#ship-basics-飞船基础)
  - [Transponder 应答机](#transponder-应答机)
  - [Status Report 状态报告](#status-report-状态报告)
  - [Stats & Saves 属性与豁免](#stats--saves-属性与豁免)
  - [Fuel 燃料](#fuel-燃料)
  - [Crew 乘组](#crew-乘组)
  - [Ship's Stat Checks 飞船属性检定](#ships-stat-checks-飞船属性检定)
  - [Ship Class 飞船等级](#ship-class-飞船等级)
  - [Modifying Ship Stat Checks 修正飞船属性检定](#modifying-ship-stat-checks-修正飞船属性检定)
  - [Example: Microsingularity 范例：微奇点](#example-microsingularity-范例微奇点)
- [Ships 飞船类型](#ships-飞船类型)
  - [Armored Personnel Carrier 装甲运兵车](#armored-personnel-carrier-装甲运兵车)
  - [Executive Transport 行政运输舰](#executive-transport-行政运输舰)
  - [Raider 袭掠者](#raider-袭掠者)
  - [Freighter 货运舰](#freighter-货运舰)
  - [Patrol Craft 巡逻艇](#patrol-craft-巡逻艇)
  - [Salvage Cutter 打捞快艇](#salvage-cutter-打捞快艇)
  - [Corvette 护卫舰](#corvette-护卫舰)
  - [Jumpliner 跃迁班轮](#jumpliner-跃迁班轮)
  - [Troopship 运兵舰](#troopship-运兵舰)
  - [Exploration Vessel 探索舰](#exploration-vessel-探索舰)
- [Class-0 Vessels Class-0 小型穿梭艇](#class-0-vessels-class-0-小型穿梭艇)
  - [Boarding Skiff 登舰艇](#boarding-skiff-登舰艇)
  - [Coffin Lander 棺材登陆器](#coffin-lander-棺材登陆器)
  - [Dropship 投放艇](#dropship-投放艇)
  - [Escape Pod 逃生舱](#escape-pod-逃生舱)
  - [Fighter 战斗机](#fighter-战斗机)
  - [Utility Pod 工具舱](#utility-pod-工具舱)
  - [Heavy Drop Pod (HDP) 重型投放舱](#heavy-drop-pod-hdp-重型投放舱)
- [Upgrades & Weapons 升级与武器](#upgrades--weapons-升级与武器)
  - [Minor Upgrades 小型升级](#minor-upgrades-小型升级)
  - [Major Upgrades 大型升级](#major-upgrades-大型升级)
  - [Weapons 武器系统](#weapons-武器系统)
  - [Resupply 弹药补给](#resupply-弹药补给)
- [Space Travel 太空旅行](#space-travel-太空旅行)
  - [Launching & Landing 起降](#launching--landing-起降)
  - [Booking Passage 购票搭乘](#booking-passage-购票搭乘)
  - [Interplanetary Travel 行星际旅行](#interplanetary-travel-行星际旅行)
  - [Refuel & Resupply 加油与补给](#refuel--resupply-加油与补给)
  - [Siphoning Fuel 抽吸燃料](#siphoning-fuel-抽吸燃料)
  - [Interstellar Travel 星际旅行](#interstellar-travel-星际旅行)
  - [Jump Drives 跃迁引擎](#jump-drives-跃迁引擎)
  - [Jump Points 跃迁点](#jump-points-跃迁点)
  - [Cryosleep 低温休眠](#cryosleep-低温休眠)
  - [Time Dilation 时间膨胀](#time-dilation-时间膨胀)
- [Detection & Range 探测与通信](#detection--range-探测与通信)
  - [Range 距离](#range-距离)
  - [Scanning & Sensors 扫描与传感器](#scanning--sensors-扫描与传感器)
  - [Scanning Examples 扫描结果范例](#scanning-examples-扫描结果范例)
  - [Hailing 通讯](#hailing-通讯)
  - [Transponder Info 应答机信息](#transponder-info-应答机信息)
  - [Distress Signals 求救信号](#distress-signals-求救信号)
- [Ship Combat 飞船战斗](#ship-combat-飞船战斗)
  - [Ship Rounds 飞船回合](#ship-rounds-飞船回合)
  - [What Can I Do? 我能做什么？](#what-can-i-do-我能做什么)
  - [The Movement Phase 移动阶段](#the-movement-phase-移动阶段)
  - [The Attack Phase 攻击阶段](#the-attack-phase-攻击阶段)
  - [Megadamage 兆损伤](#megadamage-兆损伤)
  - [Hull 船体](#hull-船体)
  - [Ship Class & Unwinnable Fights 等级差与必败之战](#ship-class--unwinnable-fights-等级差与必败之战)
  - [The Morale Phase 士气阶段](#the-morale-phase-士气阶段)
  - [After Battle Report 战后报告](#after-battle-report-战后报告)
  - [Example: Routine Check 范例：突发情境与 Ship Combat 切入](#example-routine-check-范例突发情境与-ship-combat-切入)
  - [Example of Play 战斗范例](#example-of-play-战斗范例)
- [Maintenance & Repairs 维修与维护](#maintenance--repairs-维修与维护)
  - [Starting Condition 初始状态](#starting-condition-初始状态)
  - [Routine Maintenance 例行维护](#routine-maintenance-例行维护)
  - [Minor Repairs 小型维修](#minor-repairs-小型维修)
  - [Major Repairs 大型维修](#major-repairs-大型维修)
  - [Maintenance Issues d100 维护故障表](#maintenance-issues-d100-维护故障表)
- [Who Pays the Bills? 谁付账？](#who-pays-the-bills-谁付账)
  - [The Company 公司](#the-company-公司)
  - [The Military 军方](#the-military-军方)
  - [Owner-Operators 自营业主](#owner-operators-自营业主)
  - [Bankruptcy Saves 破产豁免](#bankruptcy-saves-破产豁免)
  - [Freelancers 自由职业者](#freelancers-自由职业者)
  - [Expense Coverage Table 费用承担表](#expense-coverage-table-费用承担表)
- [Ship Manifest 飞船清单](#ship-manifest-飞船清单)
- [Glossary 关键术语速查](#glossary-关键术语速查)

---

## Overview 概述

> *"Whether you're crawling through the ducts of a derelict, probing the interior of an unknown vessel, or sipping day old coffee in the galley of a beat-up freighter, you spend the majority of your time in Mothership® aboard spacecraft."*

**Shipbreaker's Toolkit**（拆船员工具箱）是 Mothership 第三本核心书 — 在 PSG（玩家手册）/ WOM（监守手册）之上，给飞船一套完整的 **统计 + 经济 + 战斗** 框架：

- 飞船有自己的属性（**Thrusters / Weapons / Systems**）和回合制战斗系统。
- 每艘船都有 **Class**（等级，Class-0 到 Class-X），等级差 ≥ 2 的对决基本必败。
- 飞船战斗使用 **Megadamage（MDMG，兆损伤）** — 每点 MDMG 触发表上效果（火灾、生命维持失效、辐射泄漏等）。
- 经济侧：玩家通常 **不直接拥有飞船**，而是为公司 / 军方工作，或作为自营业主接受银行融资经营。
- 维护侧：每年一次 Maintenance Check，失败就在 **Maintenance Issues d100 表** 上滚出新故障。

核心扩展概念：

| 术语 | 中译 | 简介 |
|---|---|---|
| Hull | 船体 | 飞船的"护甲值"，吸收等级低于 Hull 的 MDMG |
| Megadamage (MDMG) | 兆损伤 | 飞船伤害单位（≥9 即销毁） |
| Hardpoint | 硬挂点 | 武器系统挂载位 |
| Range Band | 距离段 | Contact / Firing / Detection 三段 |
| Bankruptcy Save | 破产豁免 | 自营业主每年（季）滚的财务豁免 |
| Fallout | 后果 | 飞船战斗失败后的连锁后果 |
| Ship Round | 飞船回合 | 飞船战斗的时间单位（分钟到天） |

---

## Quick Reference Card 速查卡

> 源：PDF 第 2 页（封面后的速查页）。整页含 4 张参考表，AI / 监守对局中可直接查阅。

### Ship Deckplan Icons 甲板图例标符

> 全书甲板图上使用的 24 个标符 — 用于快速识别舱室类型。

| 符号 | 名称 | 用途 |
|---|---|---|
| AIRLOCK | 气闸 | 飞船与外部 / 真空环境的进出 |
| CABIN | 客舱 | 个人睡眠 / 私人空间 |
| CARGO | 货舱 | 货物存储 |
| COMMAND | 指挥舱 | 飞船控制中心 |
| COMMS | 通讯舱 | 无线电 / 远程通讯设备 |
| COMPUTER | 计算机舱 | 飞船主机 / 数据中心 |
| CRYO | 冷冻舱 | Cryopods 区 |
| DOCKING | 对接口 | 与其他飞船 / 站台对接 |
| DOOR | 舱门 | 内部隔门 |
| DUCT ACCESS | 管道入口 | 维护用通风 / 设施管道 |
| GALLEY | 厨房 | 烹饪 / 餐饮区 |
| GRAVITY | 重力发生器 | 人工重力源 |
| HANGAR | 机库 | Class-0 飞船 / 投放艇停放 |
| HARDPOINT | 硬挂点 | 武器系统挂载位 |
| JUMP DRIVE | 跃迁引擎 | 超光速引擎舱 |
| LADDERWAY | 梯井 | 垂直升降通道 |
| LIFE SUPPORT | 生命维持 | O2 / 温控 / 大气调节 |
| MAINT. | 维修 | 维护 / 工程舱 |
| MEDBAY | 医疗舱 | 医疗设施 |
| POWER | 反应堆 / 电源 | 主能源源 |
| SCANNERS | 扫描仪 | 传感器阵列 |
| TERMINAL | 终端 | 计算机终端 / 控制台 |
| UNPRESSURIZED AREA | 失压区 | 未加压舱（需太空服） |
| WARNING | 警告 | 危险区域标记 |

### General Travel Costs 通用旅行费用

> 一般化的乘客票价 — 不指明具体飞船。用于普通商业旅行。
> *注：Jumpliner 章节（[Bas-Lehman Contessa](#jumpliner-跃迁班轮)）有该型号特定的、价格更便宜的旅行费用表 — 因 Contessa 规模大；本通用表与该表 **存在 ~5x 价差**（封面速查 vs Jumpliner 详情页），属源书印刷差异，使用时按场景情境取舍。*

**Landing 着陆**

| ITEM 项目 | COST 价格 |
|---|--:|
| Shuttle Passenger Seating 穿梭艇乘客座 | 250cr |
| Cargo Space 货物空间（每加） | +1kcr |

**Interplanetary Travel 行星际旅行**

| ITEM 项目 | COST 价格 |
|---|--:|
| J0C-0 Passenger Liner Steerage Deck（仅冷冻舱位） | 2kcr |
| Second Class（公共铺位 + 冷冻舱） | 10kcr |
| First Class（私人客舱 + 冷冻舱） | 20kcr |
| Cargo Space 货物空间（每加） | +5kcr |
| Hangar Space 机库位（每加） | +20kcr |
| To distant planet 到远端行星（加） | +10kcr |
| To edge of system 到星系边缘（加） | +100kcr |

**Interstellar Travel 星际旅行**

| ITEM 项目 | COST 价格 |
|---|--:|
| J1C-III Jumpliner Steerage Deck（仅冷冻舱位） | 10kcr |
| Second Class（私人客舱 + 冷冻舱） | 20kcr |
| First Class（私人套间 + 冷冻舱） | 50kcr |
| Cargo Space 货物空间（每加） | +20kcr |
| Hangar Space 机库位（每加） | +50kcr |
| Jump-2 Ticket 二级跃迁票（加） | +10kcr |
| Jump-3 Ticket 三级跃迁票（加） | +30kcr |

### Fuel Costs Summary 燃料消耗汇总

> 各类行动消耗的燃料。

| ACTION 行动 | FUEL 燃料 |
|---|---|
| Run thrusters (Monthly) 运行推进器（每月） | **1 Fuel** |
| Evasion attempt (Contact Range) 规避（接触距） | **3 Fuel** 起 |
| Evasion attempt (Firing Range) 规避（射击距） | **2 Fuel** 起 |
| Evasion attempt (Detection Range) 规避（探测距） | **1 Fuel** 起 |
| Jump to Hyperspace 进入超空间 | **1 Warp Core** |

### Range & Distance Reference 距离段综合表

> **关键综合表** — 三个 Range Band 各维度差异（距离 / 时间 / 扫描信息 / 通讯延迟 / 战斗能力）。
> ⚠ **战斗规则隐含点**：在 Detection Range 只有 **Railgun** 能开火（其他武器射程不够）。

| RANGE | CONTACT 接触距 | FIRING 射击距 | DETECTION 探测距 |
|---|---|---|---|
| **DISTANCE 距离** | Planet to close orbit.（行星到近轨道） | Planet to moon, station, asteroid field.（行星到卫星 / 站台 / 小行星带） | Planet to distant planet.（行星到远端行星） |
| **TRAVEL TIME 旅行时间** | Minutes.（数分钟） | Hours to days.（数小时到数天） | Weeks to months.（数周到数月） |
| **SCANNERS SHOW 扫描显示** | Damage, lifeform presence, visual.（损伤、生命迹象、目视） | Transponder, class, and weapons.（应答机、等级、武器） | Vessel's size, location, and trajectory.（尺寸、位置、轨迹） |
| **HAILING LATENCY 通讯延迟** | None.（无延迟） | Minutes to hours.（数分到数小时） | Days to weeks.（数天到数周） |
| **SHIP-TO-SHIP COMBAT 飞船对飞船战斗** | **Boarding, contact/firing weapons.**（可登船 + 接触 / 射击武器） | **Firing weapons.**（仅射击武器） | **Railgun only.**（仅 Railgun） |

---

## Ship Basics 飞船基础

> 本节介绍飞船在角色卡（Ship Manifest）上的所有字段：应答机、状态报告、属性 / 豁免、燃料、乘组、属性检定、等级。

### Transponder 应答机

**Transponder** 是飞船自动广播的无线电系统，持续向外发送：

- **Ship Identifier**（飞船识别码 / 名）
- **Make & Model**（厂商与型号）
- **Jump Drive**（跃迁引擎规格）
- **Class & Type**（飞船等级与类型）

在大多数星系中，**关闭应答机是违法或高度可疑的行为**。

> 关联：[Hailing 通讯](#hailing-通讯)

### Status Report 状态报告

**Status Report** 用来追踪飞船 **Hull**（船体）的强度，以及任何 **Megadamage（MDMG）** 引起的效果。

> 关联：[Ship Combat 飞船战斗](#ship-combat-飞船战斗) / [Megadamage](#megadamage-兆损伤)

### Stats & Saves 属性与豁免

飞船有 **三个属性**，同时充当对应豁免（与 PC 的属性 / 豁免分离不同 — 飞船属性即豁免）：

| 属性 | 中译 | 类比 PC | 说明 |
|---|---|---|---|
| **Thrusters** | 推进器 | Speed | 在太空中的安全机动与加速 |
| **Weapons** | 武器 | Combat | 飞船间战斗中的目标锁定与攻击 |
| **Systems** | 系统 | Instinct | 总括项：传感器 / 计算机 / 维护 / 其他子系统 |

属性数值由飞船类型决定，可通过升级提升。

### Fuel 燃料

飞船在太空中每旅行 **一个月** 消耗 **1 单位 Fuel（燃料）**。**Warp Cores（曲率核心）** 用于通过超空间（hyperspace）跃迁。

> 关联：[Refuel & Resupply](#refuel--resupply-加油与补给) / [Siphoning Fuel](#siphoning-fuel-抽吸燃料)

### Crew 乘组

飞船的 **生命维持系统（Life Support）** 只能支持有限数量的（人类）乘组。同时记录：

- **Cryopods 数量**（冷冻舱）
- **Escape Pods 数量**（逃生舱）

— 以备需要弃船时使用。

> 关联：[Distress Signals](#distress-signals-求救信号)

### Ship's Stat Checks 飞船属性检定

飞船像其他角色一样进行属性检定。但有两条特别规则：

- **任何飞船属性检定失败时，全船所有人各得 1 点 Stress（压力）**。
- 与所有属性检定一样，**90-99** 视为失败。

> 关联：Panic（惊恐）见 [psg-checks-and-stress.md](../rules/psg-checks-and-stress.md#惊恐检定-panic-check)

### Ship Class 飞船等级

**Class（等级）** 是飞船能力的总体衡量。本书涵盖 Class-0 至 Class-V，其上还有更高等级（最高至 Class-X）。等级越高，越大、越强、越贵。

| CLASS 等级 | DESCRIPTION 描述 | EXAMPLE 范例 |
|---|---|---|
| **0** | Shuttlecraft 穿梭艇 | Shuttles, fighters, dropships（穿梭机 / 战斗机 / 投放艇） |
| **I** | Light commercial 轻型商用 | Raider, Executive Transport（袭掠者 / 行政运输舰） |
| **II** | Medium commercial 中型商用 | Freighter, Patrol Craft（货运舰 / 巡逻艇） |
| **III** | Heavy commercial 重型商用 | Salvage Cutter, Jumpliner（打捞快艇 / 跃迁班轮） |
| **IV** | Light military 轻型军用 | Corvette（护卫舰） |
| **V** | Medium military 中型军用 | Exploration Vessel, Troopship（探索舰 / 运兵舰） |

飞船等级常与 Jump Rating 缩写组合：例如 **J1C-II** = Jump-1 Class-II 飞船。

### Modifying Ship Stat Checks 修正飞船属性检定

与角色的属性检定 / 豁免一样，飞船属性检定可被 **优势 / 劣势、关键成功 / 失败、技能** 修正。

**Advantage & Disadvantage 优劣势**
飞船与普通角色一样可以获得优劣势 [+] / [−]，但优劣势的来源 **必须能影响整艘船**（而不仅是单人）。

**Critical Successes & Failures 关键成功 / 失败**
飞船关键失败时，全船所有人各做一次 **Panic Check（惊恐检定）**。

**Skills 技能**
当相关时，可以在飞船属性检定上加 Skill Bonus。**每次检定只允许一人加技能加值。**

### Example: Microsingularity 范例：微奇点

> *示范飞船属性检定如何运作 — 包含 Cryosickness（犯低温）→ 劣势、Thrusters Check + Piloting、关键失败 → 全船 Panic Check。*

WARDEN: 你们离开跃迁点，临近警报响起。
CLEO: 好，我来处理。

WARDEN: 你刚从冷冻舱出来还很虚弱（cryosickness），但你撑着到墙边终端 — 屏幕显示一个巨大的环形物体距离你们大约一周航程。
CLEO: 它就这么飘着？

WARDEN: 围着系统恒星公转，但是的。
CLEO: 我们能避开吗？

WARDEN: 问题就在这。传感器显示它正把你们吸过去。

PHIL: 像引力波牵引器？
CLEO: "电脑，发生什么了？"
WARDEN: "我们被一个未识别的微奇点（microsingularity）的引力捕获。"

CLEO: 操，好吧。我去试试看能不能用推进器飞出来。

WARDEN: 那是 Thrusters Check。
CLEO: 我能加 Piloting 吗？
WARDEN: 可以，但你犯低温所以是劣势 [−]。

CLEO: 那我吃个 Stimpak。
WARDEN: 好，划掉一支，做你的 Thrusters Check。

CLEO: 55。Critical Fail。
WARDEN: 全员 Panic Check！
PHIL: 也劣势？
WARDEN: 当然。

---

## Ships 飞船类型

> 本节列出书中提供的 8 种 Class-I 至 Class-V 飞船，每艘都给出价格（in MCR）、属性、容量与简短甲板说明。
> Class-0 小型穿梭艇见 [Class-0 Vessels](#class-0-vessels-class-0-飞船小型穿梭艇) 一节。
> 注：本书 PDF 各舰的 Thrusters / Weapons / Systems 数值嵌在装饰性图形中，部分值在 OCR 中无法可靠还原 — 下文标注为 *(see PDF spec sheet)* 处需翻原书 Ship Manifest 或 Spec Sheet 校对。

### Armored Personnel Carrier 装甲运兵车

**Make: COMOCO** | **Model: SAWTOOTH** | **Cost: 3MCR** | **Top Speed: 60 mph** | **Crew Capacity: 12**

陆战队员的移动指挥车 — 不是真正意义上的"飞船"，而是为最危险环境设计的星球地表突击载具，可承载一支陆战队小队及指挥单元，管理整场行星突击并保持与轨道指挥的通讯。

**Description 描述**：
- 可承受 **toxic** 与 **corrosive atmospheres**（有毒 / 腐蚀性大气）。
- 后部装备：**smoke grenade launcher**（烟雾弹发射器）、**flame thrower**（喷火器）、**HMG**（重机枪）、**light mortar**（轻型迫击炮，**1d10×10 DMG**）。
- 内置指挥舱配 **long-range comms**（远程通信器）与 **thermal visioning sensors**（热视成像传感器）。

### Executive Transport 行政运输舰

> **Make:** Sato GS | **Model:** Grail VI | **Class:** J2C-I（Jump-2 Class-I） | **Cost:** 350 MCR | **Length:** 90m
> *(Spec Sheet 后封面将本舰标为 J2C-II，与详情页 / Class 表的 Class-I 矛盾 — 以详情页 J2C-I 为准。)*

装备 **Jump-2 引擎**、最先进的医疗舱与宽敞客舱，是星系最受艳羡的飞船。主要用于把企业 C-Level 高管来回核心区，但也常用作 **赌船 / 微型太空赌场 / 微度假村 / 享乐主义海盗据点**。在外环（Rim）则常服务于有组织犯罪头目、贪污殖民地官员或私人军事指挥官。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 35 |
| SYSTEMS | 35 |
| WEAPONS | 5 |
| MDMG | 0 (Base 1) |
| Crew Capacity | 16 |
| Cryopods | 16 |
| Fuel Capacity | 14 |
| Escape Pods | 4 |
| Hardpoints | 0/1 |
| Upgrades | 3/3 |

**Upgrades installed**: Agar Cushioning / Cosmetic Remodel / Medbay。
**Notes**: Rest Saves relieve +1 Stress while aboard.（船上做休息豁免可额外消除 1 点 Stress。）

**Travel Costs 旅行费用**：

| ITEM 项目 | COST 价格 |
|---|--:|
| Private Suite (Interplanetary) 行星际私人套间 | 10kcr |
| Private Suite (Interstellar) 星际私人套间 | 10kcr |
| Charter (Interplanetary) 行星际包船 | 1mcr |
| Charter (Interstellar) 星际包船 | 1mcr |
| Cargo Space (per kg) 货舱（每公斤） | 50cr |
| Vessel tow (Class-II 及以下，最多 1 艘) 拖船 | 250kcr |

包船有好处：乘组通常审慎且对外环精品事物如数家珍。但缺点是显眼 — 对非 megacorp 关联人士来说就是海盗诱饵。

**Deckplan 甲板布局**（建造重舒适与速度）：

1. **Airlock**. Main entry. 主气闸 / 主入口。
2. **Life Support System**. O2, thermal control, artificial gravity. 生命维持系统。
3. **Executive Suites**. Two decks (办公空间 / 医疗舱 / 其他设施)。
4. **Docking Port and Command Module**. 对接口与指挥舱。
5. **Cryopods and Computer Module**. 冷冻舱与计算机舱。
6. **Habitat Decks**. Two decks，每甲板 6 间客舱 + 1 间 VIP 客舱（含 VIP 套间）。
7. **Reactor**. 反应堆。

**6. Habitat Decks 顶视图标注**：
- **A** Passenger Cabins with private bath. 客舱（含私人浴室）。
- **B** VIP Cabin with private bath. VIP 客舱（含私人浴室）。
- **C** VIP Suite with office, lounge and personal dining area. VIP 套间（含办公室、休息厅、私人餐厅）。

### Raider 袭掠者

> **Make:** Aava Industrial | **Model:** S5 | **Class:** J1C-I（Jump-1 Class-I） | **Cost:** 75 MCR | **Length:** 99m（船体 82m + 头部 17m）

廉价的飞船 — 几乎只是把投放艇（dropship）固定在轨道居住单元上 — **Raider** 是手头紧的公司、罪犯、海盗、赏金猎人想低空飞过雷达时的终极选择。其 **极端模块化** 让它在罪犯、海盗、赏金猎人间极为流行。

**Orbital Command 轨道指挥模块**：Raider 头部通常挂着一艘 dropship（创造一个临时指挥舱），允许乘组停靠行星，而其余飞船保持在轨。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 20 |
| SYSTEMS | 5 |
| WEAPONS | 5 |
| MDMG | 1 |
| Crew Capacity | 8 |
| Cryopods | 8 |
| Fuel Capacity | 12 |
| Escape Pods | 1 Coffin Lander |
| Hardpoints | 0/2 |
| Upgrades | 0/4 |

**Notes**: Adding a Dropship to the Raider does not increase crew capacity.（在 Raider 头部加挂 Dropship 不增加乘组容量。）

**Deckplan 甲板布局**（极端模块化，没有两艘 Raider 长得一样 — 升级和模块都可加在大型桁架上）：

1. **Airlock**. Main entry. 主气闸。
2. **Life Support and mechanical**. 生命维持与机械舱。
3. **Habitat decks**. 4 个小型圆形甲板，靠梯井贯通。
4. **Nose Port**. 可对接 Dropship、其他 Class-0 飞船、模块、甚至货物集装箱。
5. **Cryopods**. 冷冻舱。
6. **Fuel Tanks**. 仅外部访问。
7. **Engines**. Raider 引擎舱无内部进入通道，必须用 EVA（舱外活动）— 即 spacewalk — 才能进入。

### Freighter 货运舰

> **Make:** Valecore | **Model:** T9LC Platypus | **Class:** J1C-II（Jump-1 Class-II） | **Cost:** 250 MCR | **Length:** 119m

承载 50 个 20 英尺集装箱（每个约 20 吨重），**Freighter** 是星系骨干。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 25 |
| SYSTEMS | 20 |
| WEAPONS | 20 |
| MDMG | 1d5 |
| Crew Capacity | 12 |
| Cryopods | 12 |
| Fuel Capacity | 12 |
| Escape Pods | 1 |
| Hardpoints | 0/1 |
| Upgrades | 1/4 |

**Upgrades installed**: Contraband Hold（隐藏走私货舱）。
**Notes**: The Freighter's main cargo deck is large enough to serve as a makeshift hangar.（主货舱大到可改作临时机库。）

> **Sidebar — Tramp Freighters vs. Freight liners**
>
> **Tramp Freighters（流浪货船）** 没有固定路线或停靠港，只对即时需求做出响应。
> **Freight liners（班轮货船）** 走预先安排好的航线和时间表。
> 两者都按 **约 30cr/kg** 收费，无论装的是什么；但 **流浪货船可对偏远地点或危险条件加价**。
> （详见 → [Who Pays the Bills?](#who-pays-the-bills-谁付账)）

**Deckplan 甲板布局**：

1. **Airlock**. Main entry.
2. **Habitat decks**. 7 small decks（客舱 / 厨房 / 餐厅 / 后勤 / 办公 / 浴室）。
3. **Life Support System**.
4. **Command Module**.
5. **Cargo Decks**. 内部储存可携 50 个 20 英尺集装箱（每个最大 25 吨）。
6. **Cryopods**.
7. **Reactor**.

**5. Cargo Deck 货舱布局（侧视）**：A 货舱主仓 / B 货柜区 / C 通风区。

货舱集装箱：标准 **20 ft Shipping Container（最大载重 25 吨）**。

### Patrol Craft 巡逻艇

> **Make:** Arma | **Model:** Type-19 | **Class:** J0C-II（**无 Jump Drive！** Class-II） | **Cost:** 600 MCR | **Length:** 130m

太空又大又抗秩序，巡逻艇是人类企图维持秩序的微弱努力 — 一站式负责警务、海关检查、贸易禁运、求救信号响应。看你的处境，巡逻艇要么是你最坏的敌人，要么是欢迎的救星。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 30 |
| SYSTEMS | 15 |
| WEAPONS | 32 (Base 30) |
| MDMG | 1d5 |
| Crew Capacity | 12 |
| Cryopods | 12 |
| Fuel Capacity | 18 |
| Escape Pods | 3 |
| Hardpoints | 1/2 |
| Upgrades | 1/3 |

**Hardpoints installed**: Autocannon (+2)。
**Upgrades installed**: Hangar (x1 Boarding Skiff)。
**Notes**: Most Patrol Craft are fitted for their local system and are not equipped with a Jump Drive.（多数巡逻艇专为所驻系统配置，不装跃迁引擎。）

**Deckplan**（主要为军用，外置货舱，内部留有大量扩展空间）：

1. **Airlock**.
2. **Command decks**（指挥 / 计算机 / 武器库 / 医疗舱）。
3. **Weapon systems**. 4 个小圆形甲板，靠梯井贯通。
4. **Habitat decks**. 1 层军官甲板 + 1 层兵营甲板 + 1 层厨房 + 1 层浴室。
5. **Cryopods and cryobrig**（冷冻舱 + 冷冻禁闭室）。
6. **Reactor**.
7. **External Cargo**. 外置货舱，最多 8 个 20 ft 集装箱（或 200 吨）— 走私品和其他外挂货。

#### Customs Inspections 海关检查

巡逻艇定期扫描所辖系统内的飞船，标记任何可疑船只。

- 任何 **未开应答机** 飞行的飞船：**50% 几率** 被巡逻艇通讯叫停。
- 该船若开启应答机并接受问询：**50% 几率** 巡逻艇要求登船目视检查乘组与货物 — 寻找走私品，更可能是讨贿赂。
- 执行普通警务行动的巡逻艇 **Morale Check 为 [−]**（更易投降 / 撤退）。

**Boarding Party 登船队**：1d10+1 名陆战兵（Grunt）— **C:30 SMG 2d10 DMG / I:25 / W:2**。

#### Contraband 走私货物表（d10 / 1d5 集装箱装满……）

> 巡逻艇登船检查时，监守可滚此表决定查获的货物种类。

| D10 | 1D5 CONTAINERS FULL OF... |
|--:|---|
| **00** | **Exotic Wildlife**（异国野生动物）— 10% 几率为活体动物。 |
| **01** | **People**（人）：00 Indentured laborers（契约劳工）/ 01-03 Prisoners（囚犯）/ 04-06 Refugees（难民）/ 07-08 Drugs（药物 / 毒品 — 原文如此印）/ 09 Colonists (under NDA)（保密协议下的殖民者）。 |
| **02** | **Androids**（仿生人）。 |
| **03** | **Intellectual Property**（知识产权）：电影 / 漫画 / 音乐。 |
| **04** | **Cultural Property**（文化财产）：艺术品 / 色情品 / 禁书。 |
| **05** | **Weapons**（武器）：70% 民用手枪 / 29% 军用武器 / 1% 法外实验性武器。 |
| **06** | **Counterfeit**（仿冒品）：00 Food products（食品）/ 01-03 Entertainment Media（娱乐媒体）/ 04-06 Apparel, sneakers（服装、运动鞋）/ 07-08 Paperwork, designer labels（文书、设计师标签）/ 09 Jewelry & accessories（珠宝与配饰）。 |
| **07** | **Life-saving medicine, equipment, and drugs.**（救命药品、设备与药物。） |
| **08** | **Stolen goods**（赃物）：汽车 / 食物 / 奢侈品。 |
| **09** | **Hazardous Material.**（危险品。） |

### Salvage Cutter 打捞快艇

> **Make:** Sebaco | **Model:** RAS-62 | **Class:** J0C-III（**无 Jump Drive！** Class-III） | **Cost:** 200 MCR | **Length:** 140m

清理太空虚空的废船 — 一艘破船一个故事。**Salvage Cutter** 是那些喜欢虚空的安静、偶尔被纯粹恐惧打断的船员的完美载具。乘组少，常需进入久弃的废船 — 不知道是什么让它毁灭、也不知它是否还潜伏在内。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 15 |
| SYSTEMS | 20 |
| WEAPONS | 21 (Base 20) |
| MDMG | 1d5 |
| Crew Capacity | 8 |
| Cryopods | 12 |
| Fuel Capacity | 6 |
| Escape Pods | 1 |
| Hardpoints | 1/1 |
| Upgrades | 3/4 |

**Hardpoints installed**: Laser Cannon (+1)。
**Upgrades installed**: Hangar (x2 Utility Pods) / Medbay / Machine Shop。
**Notes**: The Salvage Cutter's large truss enables heavy customization.（大型桁架结构允许大量自定义改装。）

> **Sidebar — The Law of Salvage 打捞法**
>
> 任何在飞船 / 货物迷失太空时帮助回收的飞船，**有权获得与回收量成比例的奖励**。
>
> **Plunder（劫掠）**：当打捞物 **不归还** 给原主时称为"plunder（劫掠）"，一旦被发现，**会引来公司悬赏**。

**Deckplan**（兼具废品场 / 搜救舰 / 移动维修车间 / 拖船）：

1. **Airlock**.
2. **Cryo**.
3. **Habitat Decks**. 4 层客舱。
4. **Docking Port**. 可拖 Class-V 及以下任何飞船。
5. **Machine Shop and Medbay**.
6. **Command Module**.
7. **Life Support**.
8. **Exterior Hangar**.
9. **Exterior Cargo**. 最多 8 个 20 ft 集装箱。
10. **Reactor**. 仅外部访问。

#### Valuable Salvage Table 值钱打捞表（d10）

| D10 | ITEM 物品 |
|--:|---|
| 00 | **Cryopods**. 它们对某些人很值钱。 |
| 01 | **Warp Cores**. 难追踪、易自用。 |
| 02 | **Class-0 Vessels**: 原主总会出大价钱回收完整的逃生舱、投放艇、战斗机。 |
| 03 | **Cargo**: 既然值得运送，就值得收回。 |
| 04 | **Scrap**: 即便已被剥光，仍有价值。 |
| 05 | **Ore**: 你能把净亏变成净赚。 |
| 06 | *(原表此行空缺)* |
| 07 | **Data**: 研究数据 / 导航数据 / 飞船日志 / 货单。 |
| 08 | **Weapons**: 一具重型导弹发射器可以改装重用。 |
| 09 | **Upgrades**: 一个可用的医疗舱总能改作他用。 |

> *注：源表 PDF 上 d10=00 出现两次（"Cryopods" 与 "Warp Cores"）— 推测为印刷错误，应为 00 / 01。本表第 06 行原书亦空白。*

### Corvette 护卫舰

> **Make:** Gauss | **Model:** FAC-Grendel | **Class:** J1C-IV（Jump-1 Class-IV） | **Cost:** 200 MCR | **Length:** 134m

真正意义上的战舰 — 编队中最常见的护航载具。**Corvette** 装备重武器、2 架战斗机、1 艘投放艇，使其在开放空间中是致命掠食者。罪犯常会改装它以追求极致速度或火力。是你在太空中遇到的 **第一种真正令人胆寒** 的战舰。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 25 |
| SYSTEMS | 20 |
| WEAPONS | 35 (Base 30) |
| MDMG | 1d10 |
| Crew Capacity | 24 |
| Cryopods | 24 |
| Fuel Capacity | 6 |
| Escape Pods | 6 |
| Hardpoints | 2/3 |
| Upgrades | 1/4 |

**Hardpoints installed**: Light Missile Launcher (+3) / Autocannon (+2)。
**Upgrades installed**: Hangar (x2 Fighters, x1 Dropship)。
**Notes**: The Corvette deals the most MDMG tied with the Troopship.（与运兵舰并列造成最高 MDMG。）

**Deckplan**（主要为军用，外置货舱，内部留有大量扩展空间）：

1. **Airlock**. Main entry.
2. **Command module**. Targeting sensors, navigation, life support, operations.（瞄准传感器、导航、生命维持、作战。）
3. **Operations decks**. Space enough for a medbay, offices, armory, training, brig, and cryo.（足以容纳医疗舱、办公、武器库、训练区、禁闭室、冷冻舱。）
4. **Habitat decks**. 1 层军官甲板（含客舱）+ 1 层兵营甲板 + 1 层厨房与浴室合并甲板。
5. **Hangar**. Comes with x2 Fighters and x1 Dropship.（机库标配 x2 战斗机 + x1 投放艇。）
6. **Reactor**.

### Jumpliner 跃迁班轮

> **Make:** BAS-Lehman | **Model:** Contessa | **Class:** J1C-III（Jump-1 Class-III） | **Cost:** 425 MCR | **Length:** 160m

跨星系巨型客运舰。从行星际到星际，巨大的 Jumpliner 几乎能把你（和你的钱）一次性运到任何地方。

**A Typical Trip 典型一程**：大多数人一辈子也乘不上 Jumpliner。能乘上的人，先要付钱坐穿梭艇到轨道港；从那里，可能要在港等一两周等船到达、登船、装货。一旦登船，要 **2-3 周** 才到 Jump Point — 全员进冷冻舱进行超空间航行；下船后再 **2-3 周** 到目的地，然后整个过程反向重来。除了富豪或在太空工作的人，这是一辈子一次的体验 — Jumpliner 的货舱往往装着一家人的全部家产。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 25 |
| SYSTEMS | 20 (Base 15) |
| WEAPONS | 16 (Base 15) |
| MDMG | 1 |
| Crew Capacity | 100 |
| Cryopods | 800 |
| Fuel Capacity | 12 |
| Escape Pods | 50 |
| Hardpoints | 1/1 |
| Upgrades | 2/2 |

**Hardpoints installed**: Laser Defense System (+1)。
**Upgrades installed**: Agar Cushioning（仅头等舱乘客可享）/ Medbay。
**Notes**: 除已列升级外，Contessa 还有数项装饰性升级和宽敞的机库 / 货舱用于拖运其他飞船。完全意义上的豪华游船，头等舱乘客的娱乐设施齐全。

#### Travel Costs 旅行费用

**Interplanetary Travel 行星际旅行**

| ITEM 项目 | COST 价格 |
|---|--:|
| Jump-0 Class-0 Passenger Liner Steerage Deck（冷冻舱位） | 500cr |
| Second Class（公共铺位） | 1kcr |
| First Class（私人客舱） | 5kcr |
| Cargo Space 货舱（每加） | +5kcr |
| Hangar Space 机库位（每加） | +20kcr |
| To distant planet 到远端行星（加） | +10kcr |
| To edge of system 到星系边缘（加） | +100kcr |

**Interstellar Travel 星际旅行**

| ITEM 项目 | COST 价格 |
|---|--:|
| Jump-1 Class-III Jumpliner Steerage Deck（仅冷冻舱位） | 2kcr |
| Second Class：私人客舱到 Jump Point + 冷冻舱 | 5kcr |
| First Class：私人套间到 Jump Point + 冷冻舱 | 20kcr |
| Cargo Space 货舱（每加） | +20kcr |
| Hangar Space 机库位（每加） | +50kcr |
| Jump-2 Ticket 二级跃迁票（加） | +10kcr |
| Jump-3 Ticket 三级跃迁票（加） | +30kcr |

**Deckplan 甲板布局**：

1. **Primary Boarding Airlock**. Main entry.
2. **Steerage decks and cryo**.（廉价票冷冻舱位 — 大多数客在这里）
3. **Command module and operations**.
4. **Second Class Cabins**.
5. **Habitat Ring**. Meals, entertainment, First Class private suites.（生活舱环 — 餐厅、娱乐、头等舱套间）
6. **Cargo, passenger luggage, and hangar**.
7. **Reactor**.

### Troopship 运兵舰

> **Make:** Tannhäuser | **Model:** Höshö | **Class:** J3C-V（Jump-3 Class-V） | **Cost:** 2.5 BCR（25 亿信用点） | **Length:** 260m

为运送上百名陆战队员、随时投放而设计 — **Troopship** 是一艘飞行作战基地。被派去镇压整个殖民地或星球，运兵舰带着压倒性兵力。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 25 |
| SYSTEMS | 25 |
| WEAPONS | 37 (Base 30) |
| MDMG | 1d10 |
| Crew Capacity | 48 |
| Cryopods | 400 |
| Fuel Capacity | 24 |
| Escape Pods | 100 + 12 HDPs（重型投放舱） |
| Hardpoints | 3/4 |
| Upgrades | 2/5 |

**Hardpoints installed**: Light Missile Launcher (+3) / x2 Autocannon (+4)。
**Upgrades installed**: Hangar 1 (x4 Dropships) / Hangar 2 (x4 Fighters)。
**Notes**: Most of the marines awaken from cryo already ejected into their escape pods. They never see the inside of the ship.（多数陆战兵从冷冻舱中醒来时已被弹射进逃生舱 — 他们从未见过运兵舰内部。）

**Deckplan**（暴风雨前的宁静 — 400 名陆战兵藏在冷冻舱中，醒来时即降临）：

1. **Boarding Airlock**. Main entry.
2. **Operations and Command decks**.
3. **Cryo**. 冷冻舱。
4. **Cargo decks**. 可携 45 个 20 ft 集装箱。
5. **Exterior Hangar**. Comes with x4 Fighters and x4 Dropships.
6. **Life Support**.
7. **Reactor, mechanical, and utility decks**.

#### Marine Battalion (~350 Marines) 陆战营编制（约 350 兵）

- 1 × **Battalion HQ**：Colonel + 8 Officers + Synthetic Strategy Officer（合成战略官）
- 2 × **Infantry Companies**
  - 1 × **Company HQ**：Captain + 6 Officers
  - 3 × **Mechanized Infantry Platoons**
    - 1 × **Platoon HQ**：1st Lieutenant + 4 Officers
    - 3 × **Rifle Squads**
      - 2 × Fireteams per Squad
      - 4 × Marines per Fireteam
    - 2 × Weapons Squads
    - 1 × Support Squad

### Exploration Vessel 探索舰

> **Make:** Northstar Engineering Group | **Model:** Paragon | **Class:** J4C-V（Jump-4 Class-V） | **Cost:** 750 MCR | **Length:** 260m

采集样本、做行星测绘、追踪深空奇怪信号 — **Exploration Vessel** 见过一切。这并不总是一件好事。

也是 **第一波殖民舰** 的好选择：足够空间携带建材、地形改造设备、殖民者所需的所有工具。同时有 **200 个冷冻舱** — 但愿没有人在路上提前醒来，否则氧气不够分。

| Stat 属性 | Value |
|---|--:|
| THRUSTERS | 20 |
| SYSTEMS | 40 |
| WEAPONS | 27 (Base 25) |
| MDMG | 1d5 |
| Crew Capacity | 48 |
| Cryopods | 200 |
| Fuel Capacity | 120 |
| Escape Pods | 12 |
| Hardpoints | 2/2 |
| Upgrades | 4/5 |

**Hardpoints installed**: Laser Cannon (+1) / Laser Defense System (+1)。
**Upgrades installed**: Science Lab / Medbay / Deep Space Scanners / Hangar (x2 Dropships)。
**Notes**: The Exploration Vessel is a jack of all trades. It has to carry more cargo than a Freighter and be good in a fight.（万金油 — 必须比货运舰载更多货还能打。）

**Deckplan**（旋转内部甲板 + 自旋人工重力）：

1. **Airlock**.
2. **Working Crew Cryo**. 操作乘组的冷冻舱。
3. **Deep Cryo**. 长期乘客的冷冻舱。
4. **Hangar**. ×2 投放艇 / ×12 逃生舱。
5. **Cargo Decks**. 2 层货舱，每层可载 ×40 个 20 ft 集装箱。
6. **Reactor**. 曲率核心存储 + 跃迁引擎。
7. **Life Support System**. Hydroponics（水培） / 农业 / 制氧。
8. **Habitat Modules**. 乘组客舱 + 公共区。
9. **Labs and Medbay**. 实验室与医疗舱。
10. **Command Module**. 指挥舱。

---

## Upgrades & Weapons 升级与武器

每艘船能添加固定数量的升级。**升级必须在 X、B、A 级 Port（星港）安装**。下表给出 **Class-I** 飞船的标价 — 实际成本要 **乘以飞船等级**（例：Class-III 飞船买 Machine Shop = 750kcr × 3 = 2.25mcr）。

### Minor Upgrades 小型升级

| UPGRADE 升级 | COST 价格 | INST. 安装 | DESCRIPTION 描述 |
|---|--:|---|---|
| Expanded Fuel Bay | 750kcr | 3 wks. | 最大燃料容量 +12。 |
| Agar Cushioning | 600kcr | 2 wks. | 升级冷冻舱：Cryosickness 从 1 周缩短到 1d10 小时；前 10 年 Stats & Saves 不因 Cryosickness 衰减；之后每隔一年才衰减一次。 |
| Comms Jammer | 450kcr | 1 wk. | Systems Check（Firing Range）：可干扰通讯并窃听。 |
| Contraband Hold | 40kcr | 1 mo. | 小型隐藏货舱。登船队极难发现。 |
| Cosmetic Remodel | 100kcr+ | 1+ mos. | 升级船内装饰：油漆、家具、其他陈设。 |
| Cryochamber | 250kcr | 2 wks. | 增加冷冻舱数量，**最多 +24 / Ship Class**（例：Class-III 最多 +72）。 |
| Dedicated Reactor | 450kcr | 1 mo. | **Systems +10**。 |
| Emergency Systems | 1mcr | 1 mo. | 提供 1 个月的应急电力与生命维持。**用后必须更换**。 |
| Deep Space Scanners | 1mcr | 2 wks. | 所有探测能力距离段 +1（之前 Contact 能扫的，现在 Firing 就能扫到）。 |
| Habitat Module | 350kcr | 1 mo. | 最大乘组容量 **最多 +24 / Ship Class**（例：Class-IV 最多 +96）。 |
| Machine Shop | 750kcr | 3 wks. | 不返港即可修复 **最多 3 MDMG + 3 Hull**。补给：200kcr。 |
| Medbay | 250kcr | 3 wks. | 船上 Rest Save 为 [+]，其他医疗按监守裁决。 |
| Reinforced Plating | 2mcr | 1 mo. | 最大 Hull 提升至 **1**。 |
| Science Lab | 300kcr | 3 wks. | 用于详细研究、测试、实验样本。 |

### Major Upgrades 大型升级

| UPGRADE 升级 | COST 价格 | INST. 安装 | DESCRIPTION 描述 |
|---|--:|---|---|
| Adaptive Armor | 10mcr | 1 mo. | 最大 Hull 提升至 **2**。 |
| Enhanced A.I. | 10mcr | 1 wk. | **Systems +15**。 |
| Expanded Frame | 20mcr | * | 结构改造：**+5 Upgrades** 槽位。 |
| Hangar/Dronebay | 1mcr | 1 mo. | 可存放与维护 4 艘 Class-0 飞船。 |
| Hardpoint | 2mcr | 2 wks. | **+1 Hardpoint**。每多一个，价格为前一个的 3 倍。 |
| Improved Radiators | 3mcr | 3 wks. | **Thrusters +15**。 |
| Jump-1 Drive | 5mcr | 1 mo. | 标准商用跃迁引擎，允许 Jump-1 旅行。 |
| Jump-2 Drive | 20mcr | 2 mo. | 标准军用跃迁引擎，允许 Jump-2 旅行。 |
| Jump-3 Drive | 40mcr | 3 mo. | 远程尖端跃迁引擎，允许 Jump-3 旅行。 |
| Jump-4+ Drive | ??? | ??? | **极度实验性**，公开市场无售。 |
| Redundant Systems | 15mcr | 1 mo. | 允许飞船 **忽略一次任意 Megadamage 投骰**。用后必须更换。 |
| Signature Reduction | 35mcr | 1 mo. | 启用时：你的船仅可在 Firing Range 通过 Systems Check [−] 才能被探测到。使用时燃料费 / 旅行时间翻倍。**Core Space 内不起作用**。 |
| Streamlined Fuel Injectors | 50mcr | 1 mo. | 1 Fuel 可支持 2 个月空间旅行。**移动阶段下注 1 Fuel = 下注 2 Fuel**。 |
| System Overhaul | 20mcr | * | 大范围船体与系统升级。**Ship Class +1**。 |
| Targeting Sensors | 750kcr | 2 wks. | Systems Check（Firing Range）：船对船战斗中 Weapons Check 获 **[+]**。 |

> *安装时间 = Ship Class × 月（Class-II 飞船 2 个月，Class-III 飞船 3 个月，以此类推）*

### Weapons 武器系统

每装备一件武器：**+1 Hardpoint 占用 / 2 周安装时间 / 价格按船等级倍率**（同上 — 表中标价为 Class-I 飞船）。装备的武器加成会累加到 **Weapons Stat**。

| WEAPON 武器 | COST 价格 | BONUS 加值 | DESCRIPTION 描述 |
|---|--:|--:|---|
| Autocannon | 2.5mcr | +2 | Kinetic ballistic（动能弹道）武器。 |
| Electronic Countermeasures | 5mcr | +1 | 敌船 MDMG 投骰 **[−]**。 |
| Laser Cannon | 2mcr | +1 | 强力激光束 — 拆解废船、切割小行星。 |
| Laser Defense System | 1.5mcr | +1 | **忽略敌方 Missile Launcher 的 MDMG 加成**。若这是你唯一的武器，你不能攻击。 |
| Missile Launcher (Light) | 3.6mcr | +3 | — |
| Missile Launcher (Heavy) | 7mcr | +5 | **+1 MDMG**。 |
| Particle Beam | 3mcr *(原书印为 3cr，疑为印刷错)* | +1 | 敌船需 Systems Check 否则 **Radiation Level +1**。 |
| Railgun | 6.2mcr | +2 | **可在 Detection Range 开火**。 |

### Resupply 弹药补给

飞船武器一般 **入港时** 与加油同时补给。若自掏腰包：**每个武器系统补给 1mcr**。

---

## Class-0 Vessels Class-0 小型穿梭艇

**Class-0 飞船** 是 **shuttlecraft（穿梭艇）** 的统称 — 设计用于飞船间或飞船到行星表面的短距离旅行。每艘大船通常都配备若干 Class-0 载具用于登陆 / 救生 / 战术任务。

下表汇总书中给出的 6 类 Class-0 飞船 + 1 个 Escape Pod 升级（HDP）。

### Boarding Skiff 登舰艇

> **Cost:** 20 MCR | **Carrying Capacity:** 12 | **Travel Time:** 1 week

**Description**: Can attach to enemy ships when in **Contact Range** and forcibly insert a boarding party. Enemy may make a **Weapons Check to resist**.（可在 Contact Range 附着敌船并强行投放登船队；敌船可做 Weapons Check 抵抗。）

### Coffin Lander 棺材登陆器

> **Cost:** 1 MCR | **Carrying Capacity:** 4 | **Travel Time:** 2 years in cryo

**Description**: Planetary landing pod. Has a single-use launcher which can launch the command module back into orbit, but otherwise has no navigation capabilities. It stores compactly inside of a 20-foot shipping container, and is **an absolute last resort for the crew**.（行星登陆舱。有一次性发射器可把指挥舱送回轨道，除此之外无任何导航能力。可压缩放入 20 ft 集装箱内 — 是乘组的最后手段。）

### Dropship 投放艇

> **Make:** Mérida | **Model:** Arcane-1 | **Cost:** 50 MCR | **Travel Time:** 2 months
> **Crew Capacity:** **12+2**（12 名乘客 + 2 名驾驶员）— 详情页（p.9）的版本
> **Carrying Capacity:** 24（若载货则 12）— Class-0 速查页（p.29）的版本
> *注：源书 p.9 与 p.29 关于乘员数有内部矛盾。p.9 详情页明确为「12+2」，p.29 速查页为「24（载 APC / 货物时 12）」— 可按场景采用。*

**Description**: The Dropship is the standard planetary insertion vehicle built for bringing crews and platoons down to the surface of a planet, asteroid, or moon. While it has a small amount of capability in interplanetary travel, its small fuel capacity and non-existent combat capabilities make it a last resort option for an interplanetary traveller.

（行星投放载具的标准款 — 把乘组和分队送到行星 / 小行星 / 卫星表面。虽然它有少量行星际旅行能力，但燃料容量小且无战斗能力，作为行星际旅行手段是 **最后选择**。货舱足以装一个 20 ft 集装箱或一辆 APC，或额外搭载 12 名乘组。驾驶舱座 2 人。）

### Escape Pod 逃生舱

> **Cost:** 5 MCR | **Carrying Capacity:** 4 | **Travel Time:** 40 years in cryo

**Description**: Hard landings (on solid terrain) require a Body Save from all passengers or 1 Wound.（硬着陆 — 在固体地表 — 全员需做 Body Save 否则受 1 Wound。）

### Fighter 战斗机

> **Cost:** 75 MCR | **Carrying Capacity:** 2 | **Travel Time:** 1 week piloted / 6 months in cryo

**Description**: Each Fighter grants its carrier ship **+1 Weapons (max +10)**.（每架战斗机为母舰加 +1 Weapons，最多 +10。）

### Utility Pod 工具舱

> **Cost:** 2.5 MCR | **Carrying Capacity:** 2 | **Travel Time:** 1 month

**Description**: Space repair and service vehicle. Equipped with **2 robotic arms and a Laser Cutter**. Not equipped for planetary landing.（太空维修与勤务艇 — 配 2 个机械臂与 1 把激光切割器；不具备行星着陆能力。）

### Heavy Drop Pod (HDP) 重型投放舱

> **Cost:** Escape Pod base cost + **7 MCR** upgrade

**Description**: Carries up to 12, withstands hard landings, and automatically injects a Stimpak on landing.（升级后载员 12，可承受硬着陆，着陆时自动注射 Stimpak。Troopship 标配 12 个 HDP — 见 Escape Pods 列。）

---

## Space Travel 太空旅行

> 涵盖起降、买票搭乘、行星际旅行、加油、星际旅行（跃迁）。

### Launching & Landing 起降

大多数大型飞船 **不具备大气层进入能力**，必须依赖小型 Class-I 穿梭艇、投放艇、其他再入载具完成行星表面起降。

### Booking Passage 购票搭乘

不需要拥有飞船也能跨星系 — 但必须以信用点或交换支付。见 [Travel Costs Table](#executive-transport-行政运输舰)（行政运输舰一节）。

### Interplanetary Travel 行星际旅行

行星际旅行可能从 **几周**（到邻近行星）到 **数年**（到星系边缘）不等。靠飞船推进器进行，**每月 1 单位 Fuel**。燃料费 **预付** — 一旦目的地确定就支付。**改变航向也要 1 Fuel**。

**距离参照**：
- **MINUTES 分钟**：Surface to Space 地表到太空。
- **HOURS TO DAYS 数小时到数天**：To orbiting moon, station, asteroid 到环绕的卫星 / 站台 / 小行星。
- **WEEKS 数周**：To near planet or jump point 到近邻行星 / 跃迁点。
- **MONTHS 数月**：To distant planet 到远端行星 / To edge of system 到星系边缘。

### Refuel & Resupply 加油与补给

入港时加油 / 补给。**每个 Ship Class 用不同型号的 Fuel**（Class-I 船用 Class-I Fuel，Class-V 船用 Class-V Fuel）。

| FUEL TYPE 燃料类型 | COST/UNIT 单价 |
|---|--:|
| Class-I Fuel | 1kcr |
| Class-II Fuel | 2kcr |
| Class-III Fuel | 5kcr |
| Class-IV Fuel | 50kcr |
| Class-V Fuel | 100kcr |
| Warp Core | 1mcr |

### Siphoning Fuel 抽吸燃料

- 比你低 **一个等级** 的飞船的燃料：**2:1 抽吸使用**。
- 比你高 **一个等级** 的飞船的燃料：**1:2 使用**。
- **其他所有等级** 的燃料：**不兼容**。

### Interstellar Travel 星际旅行

要旅行到其他恒星系统，**必须装备 Jump Drive（跃迁引擎）**。跃迁引擎是为让飞船超光速、通过 **跃入超空间（hyperspace）** 完成大距离旅行的强力引擎。**每次跃迁消耗 1 单位 Warp Core（曲率核心）**。

### Jump Drives 跃迁引擎

按等级 1-9 评级，决定一次跃迁的距离：

- 绝大多数商用星际飞船：**Jump-1**。
- **Jump-4 及以上**：仅强大的公司 / 政府 / 军方使用。
- **Jump-9**：传说中的 **Jump-9 Colony Ships** — 没人指望它们回来。无人确知多次 Jump-9 的效果。也许它们已经回来了，只是在我们的未来千年。或者过去的某处。

### Jump Points 跃迁点

跃迁前飞船必须到达 **离邻近行星 / 站台一段安全距离的 Jump Point（跃迁点）**。从飞船当前位置到 Jump Point 通常需要 **几周**，到达后才能安全进入超空间。

### Cryosleep 低温休眠

大多数乘组在超空间中处于低温休眠 — 由仿生人监控星航计算机。那些选择在超空间中清醒的人 **报告奇怪、互相矛盾的故事**。仿生人对他们在超空间中的记忆，最好也只能形容为……令人不安。

### Time Dilation 时间膨胀

**超空间跃迁需 2d10 天**。但相对论对超光速旅行的影响 **不确定且看似随机**：

- 一支乘组从 Jump-3 航行回来，发现自己已离开数年。
- 另一支只比出发晚几秒返回。

**常规 Jump-1 贸易航线** 似乎能磨平这种混沌效应，但跑长跃迁的人 — 比如传说中的 **Jump-9 Colony Ships** — 没人指望他们回来。

> 旅行时间参照：**WEEKS** Jump Point to Destination（从跃迁出口到目的地）。

---

## Detection & Range 探测与通信

### Range 距离

飞船间相遇时，距离用 **三个 Range Bands（距离段）** 抽象表示：

- **Contact Range 接触距**：飞船相距 **几天**。可无延迟通讯。**有战斗 / 登船风险**。
- **Firing Range 射击距**：飞船相距 **数周**。通讯有延迟。**有战斗风险**。
- **Detection Range 探测距**：飞船在 **同一星系内**。通讯缓慢。**无战斗风险**。仅能探测到对方的尺寸与轨迹。

> 关联：[Ship Combat](#ship-combat-飞船战斗)

### Scanning & Sensors 扫描与传感器

飞船的扫描仪可获取敌船 / 废船 / 站台 / 行星 / 卫星 / 小行星 / 其他天体的信息。**距离越近，细节越多**（详细程度由监守裁决）。

| RANGE 距离 | INFORMATION REVEALED 信息揭示 |
|---|---|
| **DETECTION** 探测距 | Presence, trajectory, rough size, any transponder info broadcasted (with delay).（存在、轨迹、粗略尺寸、应答机广播信息 — 有延迟） |
| **FIRING** 射击距 | Trajectory, transponder info, ship class, type.（轨迹、应答机信息、飞船等级、类型） |
| **CONTACT** 接触距 | Trajectory, transponder info, ship class, type, presence of lifeforms, ship's status.（轨迹、应答机信息、飞船等级、类型、生命体存在、飞船状态） |

#### Crowded System 拥挤系统范例

> 演示 Patrol Craft 在 Firing Range 通讯巡查 — 知道你的船型与航向，但要逼近才能识别详细。

WARDEN: 离开 Waystation 大概一周后，你收到附近 Patrol Craft 的通讯：「*嗤*这里是 J0C-III 巡逻艇 Montana，你的应答机为什么关着？」

CLEO: 他们对我们了解多少？
WARDEN: 嗯，你们在 Firing Range，所以他们知道你开的是什么型号的船、朝哪个方向走。

### Scanning Examples 扫描结果范例

> 三个距离段下扫描同一艘巡逻艇 USCF *Armistice* 的呈现差异：

**RANGE: DETECTION（探测距）**
```
TRAJECTORY:   INBOUND.
              3 months, 6 days, 7 hours, 15 min until contact.
TRANSPONDER:  PENDING. 17 days until signal.
              CLASS-III VESSEL SUSPECTED.
```

**RANGE: FIRING（射击距）**
```
TRAJECTORY:   INBOUND.
              21 days, 5 hours, 42 min until contact.
CALLSIGN:     USCF Armistice    CAPTAIN: J. Ohta.
MAKE:         ARMA              MODEL:   TYPE-19.
CLASS:        J1C-III           TYPE:    PATROL CRAFT.
```

**RANGE: CONTACT（接触距）**
```
TRAJECTORY:   INBOUND.
              3 hours, 6 min until contact.
CALLSIGN:     USCF Armistice    CAPTAIN: J. Ohta.
MAKE:         ARMA              MODEL:   TYPE-19.
CLASS:        J1C-III           TYPE:    PATROL CRAFT.
LIFEFORMS:    PRESENT.
STATUS REPORT: WEAPONS OFFLINE.
```

### Hailing 通讯

跨太空通讯艰难且费时。**距离越远，发送 / 接收的延迟越大**：

| RANGE 距离 | LATENCY 延迟 |
|---|---|
| CONTACT | None.（无） |
| FIRING | Minutes to hours.（数分到数小时） |
| DETECTION | Days to weeks.（数天到数周） |
| BEYOND | Months to years, if ever.（数月到数年，甚至永远不到） |

### Transponder Info 应答机信息

应答机自动持续广播飞船信息，包括 **Callsign（呼号）、船长名、飞船类型、Class、其他**。**应答机信息受 Hailing 延迟影响** — 即使打开应答机，远距离接收方也要等延迟时间才能看到。

### Distress Signals 求救信号

偶尔你需要：把飞船切到应急电源、把全员封进冷冻舱、发送 **Distress Signal**、等待救援。这是孤注一掷 — 但有时是唯一选择。**滚 d10 查 Distress Signals Table**：

| D10 | RESPONSE TIME 响应时间 |
|--:|---|
| **0-3** | **NEVER**. The ship floats endlessly in the all consuming void of space. Thanks for playing Mothership.（永不。飞船在吞噬一切的虚空中漂浮直至永远。感谢你游玩 Mothership。） |
| **4** | **2D10 DECADES（数十年）**. Body Save [−] 否则 **所有 Stats & Saves -1d10**。 |
| **5-6** | **2D10 YEARS（数年）**. Body Save 否则 **所有 Stats & Saves -1d5**。 |
| **7-8** | **2D10 MONTHS（数月）**. 备忘：回去查公司在低温应急情况下的欠薪政策。 |
| **9** | **2D10 WEEKS（数周）**. 你是幸运儿之一。 |

---

## Ship Combat 飞船战斗

> *外面看，两艘飞船间的战斗看似缓慢、宁静；内部却像自然灾害 — 每艘船以惊人速度移动，从数小时甚至数天外用计算机瞄准武器开火。最微小的损伤就能瘫痪或摧毁整艘船，乘组死于火焰、辐射、窒息，甚至更糟。*

### Ship Rounds 飞船回合

飞船间的暴力对抗中，时间被切割为 **Ship Rounds（飞船回合）**。每个 Ship Round 由 **三个阶段** 组成：

1. **Movement Phase** 移动阶段
2. **Attack Phase** 攻击阶段
3. **Morale Phase** 士气阶段

#### How long is a ship round? 一个飞船回合多长？

每个 Ship Round 持续 **数分钟到数小时**，取决于飞船相距多远。每回合后时间恢复正常 — 你和其他玩家可以在下一回合前规划下一步动作。

- **Contact Range** 飞船：每回合间隔仅几分钟（够进行几个普通战斗回合）。
- **Firing Range** 飞船：回合间隔可能 **几小时到几天**。

### What Can I Do? 我能做什么？

**Ship-to-ship combat 假设每艘船与乘组都竭尽全力赢得对抗** — 假定他们已在采取规避机动、瞄准最佳目标、做出合理战术决策。

**你的工作是和乘组讨论：何时打、何时逃、何时谈判 / 投降。飞船负责其他。**

### The Movement Phase 移动阶段

移动阶段中，每艘船决定 **规避 / 追击 / 维持航向**，并决定 **下注多少额外 Fuel**。

#### If you're attempting to evade...规避

可下注任意数量的 Fuel，但必须 **下注至少最低值**：

| RANGE 距离 | FUEL COST 最低燃料 |
|---|--:|
| CONTACT | 3 Fuel. |
| FIRING | 2 Fuel. |
| DETECTION | 1 Fuel. |

#### If you're attempting to pursue...追击

可下注任意数量的 Fuel（甚至 0）。

#### Resolution 结算

双方亮牌后各做一次 **Thrusters (Piloting) Check**。

- **下注更多 Fuel 的一方** 获 [+]。
- **成功**：达成意图，距离段 ±1（拉近 / 拉开一段）。
- **关键成功**：即使敌方也成功你也得手。
- **关键失败**：即使敌方也失败，敌方仍得手。
- **其他结果**（双方平局）：距离不变。

#### If you're going to maintain course...维持航向

**不下注额外 Fuel**。但敌方 **不需投骰即可达成意图**（规避或追击 — 不过敌方仍要支付下注的额外 Fuel）。

### The Attack Phase 攻击阶段

移动阶段结束后，所有处于 **Firing Range 或更近** 的飞船选择目标，做 **Weapons Check**：

| 结果 | 效果 |
|---|---|
| **Critical Failure** | 该船 **+2 MDMG**（叠加敌方造成的 MDMG）。 |
| **Failure** | 该船 **+1 MDMG**（叠加敌方造成的 MDMG）。 |
| **Success** | 该船造成 MDMG。 |
| **Critical Success** | 该船造成 **双倍 MDMG**。 |

**未装备武器系统 / 武器离线** 的飞船 **不造成 MDMG**。

### Megadamage 兆损伤

**Megadamage（MDMG）** 类比角色的 Damage + Wounds 合二为一。每次飞船受到 MDMG，在 Status Report 上勾选并应用对应效果。**MDMG 累计 ≥ 9，飞船被摧毁。**

| MDMG | EFFECT 效果 |
|--:|---|
| **00** | **ALL SYSTEMS NORMAL**. 5x5. Ready to ride. 一切正常。 |
| **01** | **EMERGENCY FUEL LEAK**. Every time you spend fuel, you spend 1 more. 燃料紧急泄漏 — 每次花 Fuel 多 +1。 |
| **02** | **WEAPONS OFFLINE**. Cannot make Weapons Checks. 武器离线，无法做 Weapons Check。 |
| **03** | **NAVIGATION OFFLINE**. Cannot make Thruster Checks. **10% chance all navigation data wiped**. 导航离线，无法做 Thruster Check。10% 几率所有导航数据被清。 |
| **04** | **FIRE ON DECK**. 火势蔓延全船 — 产生 toxic atmosphere（烟雾吸入）+ highly corrosive atmosphere **10 DMG/round** 燃烧位置（详见 [psg-survival.md → 大气](../rules/psg-survival.md#大气)）。 |
| **05** | **HULL BREACH**. 全员 Body Save 否则 **+1 Wound (Explosion)**。关键失败：被猛烈吸入太空。 |
| **06** | **LIFE SUPPORT SYSTEMS OFFLINE**. 氧气限制为 **1d10 × 最大乘组容量**（详见 [psg-survival.md → 氧气](../rules/psg-survival.md#氧气)）。 |
| **07** | **RADIATION LEAK**. **每 2d10 分钟 Radiation Level +1**。 |
| **08** | **DEAD IN THE WATER**. 全部系统离线，仅应急电源。 |
| **09+** | **ABANDON SHIP!** 飞船在 1d10 分钟内毁灭。 |

### Hull 船体

**Hull**（船体）就像角色的 **Armor Points（AP）**，但用于飞船。

- 你的船 **忽略** 任何小于 Hull 的 MDMG。
- **但**：若飞船一击受到的 MDMG **≥ Hull**，**Hull 被摧毁**，飞船受到剩余 MDMG。

### Ship Class & Unwinnable Fights 等级差与必败之战

- 对 **比你低 1 等级** 的飞船：所有 Weapons Check 与 MDMG 投骰 **[+]**。
- 比你 **高 ≥ 2 等级** 的飞船：**直接对抗中假定不可战胜**，除非监守另有裁定。

### The Morale Phase 士气阶段

**任何 Ship Round 后**，**受到任何 megadamage 的敌方** 必须做一次 **Morale Check**：

- 滚 1d10。**若结果 < 当前总 megadamage**，敌方发出停火通讯并提议重新谈判。

### After Battle Report 战后报告

**任何暴力对抗结束后，若你的飞船受过 MDMG**：

- 做一次 **Systems Check**。
- **失败**：在 [Maintenance Issues 表](#maintenance-issues-d100-维护故障表) 上滚一个 Repair。
- **关键失败**：在该表上滚一个 Repair，且**用 [−]**（结果更糟）。

### Example: Routine Check 范例：突发情境与 Ship Combat 切入

> *演示日常 PC 战斗（生物袭击 + Body Save）与 Ship Combat 切入的混合场景 — Cleo 在指挥舱接到 Patrol Craft 的临检通讯，Knox 同时在气闸前与生物搏斗。*

WARDEN: 这生物像撕裂金属一样发出尖叫——「EEEEAAAAAGGHLBRGL」——口部伸出的肢体死死抓住走廊壁。
KNOX: 我冲过去把气闸门猛地关上，再把撬棍卡住，会有用吗？
WARDEN: Speed Check。同时，全船扩音器开始响起接近警报。

PHIL: 老天爷，又怎么了！
KNOX: 失败了。
WARDEN: 你把撬棍塞进去了，但卡不牢。生物又一次撞上气闸门，把门撞开把你撞翻在地。指挥舱里有人吗？
CLEO: 我在，怎么了？
WARDEN: 你接到附近一艘 Patrol Craft 的通讯：「*嗤* 这里是 J0C-III 巡逻艇 Montana，听到请回复。」
PHIL: 又来？？
CLEO: 呃，先别回。

WARDEN: Knox，这生物又一声咆哮，看样子要扑下来。你做什么？
KNOX: 操，我跑。
WARDEN: 好。但你需要做 Body Save 才能起身逃脱不被它打中。可以接受吗？
KNOX: 完全可以。

WARDEN: Cleo，又一次通讯：「未识别飞船，这里是禁区。表明身份并准备接受登船检查。」
PHIL: 我们就溜吧。
WARDEN: 当然可以，但要注意他们在 Firing Range — 你们一旦试图脱离不成功，他们仍可攻击。

KNOX: 我失败了。
WARDEN: 你起身就跑，但被它扫中受 **12 damage**，加上失败的 **+1 Stress**。
KNOX: 那是 1 个 Wound。各位！下面情况很糟！
PHIL: 我应该去帮他。我们必须走。

### Example of Play 战斗范例

> *演示一个完整 Ship Round：Movement Phase（双方下注 Fuel + Thrusters Check）→ Attack Phase（Weapons Check + MDMG 表）→ 失败的 Systems Check 触发新的 Maintenance Issue。*

CLEO: 我们试着甩开他们。
WARDEN: Firing Range 想脱离 — 最低下注 **2 Fuel**。
KNOX: 我们有多少？
CLEO: 6 Fuel。到 Adoni 还要多少？
WARDEN: 等等 — 巡逻艇下注前我先记一下……好，到 Jump Point 要 1 Fuel，到 Adoni 再 1 Fuel。
KNOX: 我们至少花 2 Fuel — 那就只剩 2 Fuel 用于规避。
CLEO: 留 1 Fuel，下 1 Fuel 试试？
WARDEN: 你下注 3 Fuel？
CLEO: 是。

WARDEN: 他们只下了 1 Fuel，所以你 [+]。Thrusters Check。
CLEO: 43 / 50。操，失败。
WARDEN: 全员 +1 Stress。巡逻艇 67，也失败 — 距离不变。Weapons Check。

CLEO: 失败。
WARDEN: 他们 26，命中！1d5 MDMG + 你失败的 1 = **3 MDMG**。**Navigation Offline**（MDMG 03）。他们没受 MDMG 所以无 Morale Phase — 但你要做 Systems Check 看有没有故障。
CLEO: 失败。
WARDEN: 全员 +1 Stress。Cleo，给我 d100 看故障。
CLEO: 43。
WARDEN: **43 — Insufficient Life Support redundancy（生命维持冗余不足）**。Minor Repair。

---

## Maintenance & Repairs 维修与维护

> *Eventually, your ship needs a tune-up, or sometimes a complete overhaul. When this happens, you'll need to get it repaired.*

### Starting Condition 初始状态

每艘船开局都有些磨损。**获得新船 / 长期加入一艘船时**：从 [Maintenance Issues d100 表](#maintenance-issues-d100-维护故障表) 滚 **1d5+1** 个 Repairs。

### Routine Maintenance 例行维护

**每年** 飞船需做一次 **Maintenance Check**（即一次 Systems Check）：

- **成功**：飞船保持当前状态。
- **失败**：在 Maintenance Issues 表上滚一次故障，全员 +1 Stress（按通常规则）。
- **关键失败**：滚 **两次**，全员做 Panic Check（按通常规则）。
- 船上有专职首席工程师（lead engineer）：监守可裁定该 check 获 [+]。

### Minor Repairs 小型维修

涵盖外观损伤、清洁、零工型工作 — 飞船在飞行中乘组就能处理。**Minor Repairs 修复用 2d10 天**。

时间紧迫或缺工具 / 资源时，监守可要求属性检定：

- **失败**：耗费更多时间与资源。
- **关键失败**：**Minor Repair 升级为 Major Repair**，必须返港修。

### Major Repairs 大型维修

涵盖大型结构 / 系统损伤，包括 **修复 MDMG 与 Hull**。**Major Repairs 只能在港维修，每个用 1d5 周**。

每点 Hull 或 Megadamage **算一次独立 Major Repair**。例：飞船 6 MDMG 归零，**最多可能要 30 周** 在港维修。

### Maintenance Issues d100 维护故障表

> 飞船一年一度的健康抽检。**00-22 = Minor Repairs**（机内可修），**23-99 = Major Repairs**（必须返港）。
> 部分条目附数值后果（如 MDMG / Stress / Save 减值）。

#### Minor Repairs（00-22）

| D100 | ISSUE 故障 |
|---:|---|
| **00** | Rancid smell permeates cabins.（客舱弥漫腐臭味） |
| **01** | Huge mess everywhere.（到处一片狼藉） |
| **02** | Staticky comms.（通讯静电杂音） |
| **03** | Faulty electrical system.（电路系统故障） |
| **04** | Loose couplings.（联接件松动） |
| **05** | Hidden (highly illegal) contraband.（隐藏的高度违禁走私品） |
| **06** | Autopilot systems down.（自动驾驶系统故障） |
| **07** | Leaking hydraulic systems.（液压系统泄漏） |
| **08** | Creaking hull.（船体咯吱作响） |
| **09** | Damaged bulkheads.（舱壁损坏） |
| **10** | Misaligned docking clamps.（对接夹具错位） |
| **11** | Viewports blocked.（舷窗堵塞） |
| **12** | Jammed exterior airlocks.（外部气闸卡死） |
| **13** | Dysfunctional gravity plating.（重力地板失灵） |
| **14** | Out of code compliance.（不合规） |
| **15** | Controls sticking.（操控杆卡涩） |
| **16** | Coolant leak.（冷却剂泄漏） |
| **17** | Miscalibrated Thruster Gimbal System.（推进器万向架系统失校） |
| **18** | Bevvy of OSHA violations.（一堆 OSHA 安全违规） |
| **19** | Blocked air vents.（通风口堵塞） |
| **20** | Emergency lighting only.（仅应急照明） |
| **21** | Internal networking issues.（内部网络故障） |
| **22** | Inaccurate data collection.（数据收集失准） |

#### Major Repairs（23-99）

| D100 | ISSUE 故障 |
|---:|---|
| **23** | **Oxygen leak**. 若船氧气低，**每天额外 -1d5 O2**。 |
| **24** | **Throttled Afterburners**：**Thrusters −2d10**。 |
| **25** | **Lemon**（劣质船）：所有 Maintenance Check 为 [−]。 |
| **26** | **Slow acceleration**：旅行时间 **+1 周**。 |
| **27** | Inaccurate navigation.（导航不准） |
| **28** | **Miscalibrated Targeting Sensors**：**Weapons −1d10**。 |
| **29** | **Faulty Cryopods**：噩梦；Cryosickness 多持续 1 周。 |
| **30** | Malfunctioning escape pods.（逃生舱故障） |
| **31** | Unable to send distress signals.（无法发送求救信号） |
| **32** | Sabotaged coolant system.（冷却系统被破坏） |
| **33** | **Death trap**：所有投骰 [−]。 |
| **34** | Worn landing struts.（着陆支柱磨损） |
| **35** | Out-of-date air filters.（空气过滤器过期） |
| **36** | Corroded pipes.（管道腐蚀） |
| **37** | Inaccurate orbital transfer navigation.（轨道转移导航不准） |
| **38** | Worn out fuel injection nozzles.（燃料喷嘴磨损） |
| **39** | Inoperative exterior lighting system.（外部照明系统失灵） |
| **40** | Defective intercom system.（对讲系统故障） |
| **41** | Inadequate waste recycling.（废物回收不足） |
| **42** | Faulty altitude control thrusters.（姿控推进器故障） |
| **43** | Insufficient Life Support redundancy.（生命维持冗余不足） |
| **44** | Delayed communication relays.（通讯中继延迟） |
| **45** | Damaged fuel lines.（燃料管线损伤） |
| **46** | Corroded exhaust manifolds.（排气歧管腐蚀） |
| **47** | Terminal displays non-functional.（终端显示器失效） |
| **48** | Check engine light won't turn off.（引擎警告灯不熄） |
| **49** | Failed backup systems.（备份系统失效） |
| **50** | Faulty door locks.（舱门锁故障） |
| **51** | Buggy communications.（通讯有 bug） |
| **52** | Infected food storage facilities.（食品储藏感染） |
| **53** | Corrupted data banks.（数据库损坏） |
| **54** | Jammed cargo bay doors.（货舱门卡死） |
| **55** | Flickering interior lights.（室内灯闪烁） |
| **56** | Failed airlock seals.（气闸密封失效） |
| **57** | **Fuel Leak**：每次花 Fuel 多 **+1 Fuel**。 |
| **58** | **Jump Bug**：**10% 几率超空间跃迁耗时 2d10 月而非 2d10 天**。 |
| **59** | **Fragile**：始终 **+1 MDMG**。 |
| **60** | Cracked heat shields.（隔热罩开裂） |
| **61** | **Outdated software**：**Systems −1d10**。 |
| **62** | **Inadequate Water Filtration**：水中有寄生虫。 |
| **63** | Malfunctioning waste management system.（废物管理系统失灵） |
| **64** | Fusion Reactors overheating.（聚变反应堆过热） |
| **65** | Failed radiation filter.（辐射过滤器失效） |
| **66** | **Radiation leak**. 整艘船处于 **Radiation Level 2**。 |
| **67** | Miscalibrated guidance system.（导引系统失校） |
| **68** | Overloaded power storage.（电力储存过载） |
| **69** | Malfunctioning sensor arrays.（传感器阵列失灵） |
| **70** | Failed Water Recovery System.（水回收系统失效） |
| **71** | Micro-meteoroid hull damage.（微陨石船体损伤） |
| **72** | Faulty Carbon Dioxide Removal Assembly.（二氧化碳清除系统故障） |
| **73** | Solar panel degradation.（太阳能板退化） |
| **74** | Computer failure from cosmic radiation.（宇宙射线导致计算机故障） |
| **75** | Overloaded circuitry.（电路过载） |
| **76** | Malfunctioning plasma thruster.（等离子推进器失灵） |
| **77** | Thermal management system failure.（热管理系统失效） |
| **78** | Intermittent electrical outages.（间歇性断电） |
| **79** | Fire suppression system out of code.（消防系统不合规） |
| **80** | Damaged floor panelling.（地板面板损坏） |
| **81** | Broken light fixture in remote corridor.（偏僻走廊灯具损坏） |
| **82** | Damaged coolant pump.（冷却泵损坏） |
| **83** | Cracked viewports.（舷窗开裂） |
| **84** | Systems overloaded with malware.（系统被恶意软件淹没） |
| **85** | Leaky fuel valve.（燃料阀泄漏） |
| **86** | Jammed exhaust vent.（排气口卡死） |
| **87** | Stuck waste disposal chute.（废物处理槽卡死） |
| **88** | Lifts non-functioning.（升降梯失效） |
| **89** | Damaged communications antenna.（通讯天线损坏） |
| **90** | **Clogged Air Filtration**：乘组容量减半。 |
| **91** | **Malfunctioning climate control**：船内恒温 **85°F（约 29°C）**。 |
| **92** | No emergency power.（无应急电源） |
| **93** | **Weak Frame**：**−1 HP, −1 Upgrade**。 |
| **94** | Toxic chemical spill.（有毒化学品泄漏） |
| **95** | **Poor scanners**：探测距离段 **−1**（要近一段才能扫到）。 |
| **96** | **Counterfit papers**：飞船是赃船，**有悬赏**。 |
| **97** | Corrupted A.I.（损坏的人工智能） |
| **98** | **Warp Cores fail 10% of the time.**（10% 跃迁失败） |
| **99** | **Rust bucket**：能出错的全出错。**乘组最低 Stress +1**。 |

> *源 PDF 该表分 6 列布局（D100 / Issue 三组并列），列间排序为：col-A 00-33 / col-B 34-66 / col-C 67-99；MAJOR REPAIRS 标头出现在 d100=23 行处。本导入按 d100 升序合并为单列以便查阅。*

---

## Who Pays the Bills? 谁付账？

> *关于飞船的一切 — 购买、维修、维护、升级 — 对普通人来说都遥不可及。能买下一艘船的人，最终都被它榨干。简言之：你不会经常自掏腰包付这些费用。那么，谁来付？*

四种角色立场：

1. **The Company** 公司
2. **The Military** 军方
3. **Owner-Operators** 自营业主
4. **Freelancers** 自由职业者

### The Company 公司

为公司工作时：**公司拥有飞船，承担所有相关费用**。你只领工资 / 完成被指派的工作。

**别想花哨的新升级** — 总部的会计员从来不爱批费用申请。

### The Military 军方

军用飞船：**任务相关的一切都由军方承担** — 你不必担心自己付不起医疗费。**与你专业相关的技能训练也由军方报销**。条件：**永远服从命令**。

### Owner-Operators 自营业主

少数飞船由小型银行联合融资 — 银行出资、然后将船租赁或与小公司联合持有。**银行垫付飞船与运营成本，并取大头利润**。作为交换，你获得：一艘船 + 在外环（Rim）经营 Raider / Freighter / Salvage Cutter / 其他小型飞船的相对自由。

### Bankruptcy Saves 破产豁免

自营业主有一个新的豁免 — **Bankruptcy Save**，**起始 2d10+10**。

每年（或监守裁定每季）做一次 Bankruptcy Save，查 **Bankruptcy Table** 决定公司财务健康状况：

| SAVE 豁免结果 | CONSEQUENCE 后果 |
|---|---|
| **CRITICAL SUCCESS** | 你赚到一小笔利润。**任选其一**：买 1 个 Major Upgrade / 修 1d5 个 Major Repair / 给每位乘组员 1d5×100kcr / Bankruptcy Save +1d10。 |
| **SUCCESS** | 你勉强糊口。**任选其一**：买 1 个 Minor Upgrade / 修 1 个 Minor Repair / 给每位乘组员 1d10×1kcr / Bankruptcy Save +1d5。 |
| **FAILURE** | **你欠无情债主 1d10mcr**。 |
| **CRITICAL FAILURE** | **公司破产，并欠下你能想象到的最坏的人一笔巨债**。 |

### Freelancers 自由职业者

自由职业者 — 自己买（或以其他方式获得）了飞船、自掏腰包付一切费用的人。**极其昂贵，你必须乞讨、易物、偷窃来凑信用点**。但好处是：你拥有外环最稀有的东西 — **自由**。

### Expense Coverage Table 费用承担表

> "P" = Provided（公司 / 军方 / 业主全额承担）；"Approved only" = 仅获批后承担；"-" = 自付。
> 注：原书表格为竖向布局（列名是身份，行是费用项目），上面的 README 引用块为读者展开为以费用为列。下表按原书结构整理。

| EXPENSE 费用项 | COMPANY 公司 | MILITARY 军方 | OWNER-OPERATORS 自营业主 | FREELANCERS 自由职业者 |
|---|---|---|---|---|
| **Salary** 薪资 | P | P | P | — |
| **Hazard Pay** 危险津贴 | Approved only. | P | Approved only. | — |
| **Jump Pay** 跃迁津贴 | Approved only. | P | Approved only. | — |
| **Room & Board** 食宿 | On ship only. | On ship and base. | On ship only. | On ship only. |
| **Refueling** 加油 | P | P | P | — |
| **Warp Cores** 曲率核心 | Approved only. | P | Approved only. | — |
| **Repairs** 维修 | Approved only. | P | — | — |
| **Upgrades** 升级 | Approved only. | Approved only. | — | — |
| **Skill Training** 技能训练 | — | Approved only. | — | — |
| **Medical Treatment** 医疗 | — | On ship and base. | — | — |
| **Equipment** 装备 | Approved only. | Approved only. | — | — |
| **Weapons** 武器 | — | P | — | — |

#### Example: Company Card 范例：公司开除

WARDEN: 你勉强返港，飞船刚进干船坞就基本散架了。地勤忙着控制损害，你到终端时收到一条消息……来自总部。

PHIL: 好极了！
KNOX: 我们应该忽略它。
WARDEN: 没问题，但你还没领到工资。

CLEO: 是 — 你好，我们能帮上什么？
WARDEN: 是 Jenkins，他暴怒。他们听说了损害，要好几个月才能修。**你们全部立即解雇**。

PHIL: 听起来对得上。
WARDEN: 另外，他们……必须通知你 — **公司已发出对你的逮捕悬赏**。
KNOX: 什么？什么罪名？
WARDEN: **损害公司财产**。

#### Example: End of the Fiscal Year 范例：年终结算

WARDEN: 那次上岸休假把我们带到年底 — Cleo，做 Maintenance Check。
KNOX: 我休假时一直在修船，所以……
WARDEN: 是 — 所以你 [+]。然后 Phil，做 Bankruptcy Save？
PHIL: 求别。
CLEO: 失败。
WARDEN: 全员 +1 Stress。Cleo，给我 d100 查故障。
CLEO: 24。
WARDEN: 看来你应该做好日常维护 — **Throttled Afterburners（−2d10 Thrusters）**。Phil，你？
PHIL: 也失败。
WARDEN: 哎呀。全员 +1 Stress。
PHIL: 我怀念因为外星人和别的鬼东西吃 Stress 的日子。
WARDEN: 看起来你们差 3mcr 才能盈利。猜猜你们欠谁？……

---

## Ship Manifest 飞船清单

> 飞船角色卡（Ship Manifest）的字段结构，便于 AI / 监守在 state.yaml 中追踪飞船状态。

```
TRANSPONDER 应答机
  Ship Identifier 飞船识别码
  Captain 船长
  Make / Model / Jump / Class / Type
    Make 制造商
    Model 型号
    Jump 跃迁等级（如 J2）
    Class 飞船等级（0-X）
    Type 类型（如 Executive Transport）

HULL POINTS 船体点
  Current / Maximum

STATS & SAVES 属性 / 豁免
  Thrusters 推进器
  Weapons 武器
  Systems 系统
  ON / OFF（在线 / 离线状态）

FUEL 燃料
  Current / Maximum

WARP CORES 曲率核心（数量）

WEAPONS 武器
  Base / Total（基础 + 装备后总值）

HARDPOINTS 硬挂点
  Installed / Maximum

MEGADAMAGE 兆损伤（已勾选条目 + 当前累计 0-9+）

UPGRADES 升级
  Installed / Maximum

CARGO 货物（清单）

CREW 乘组
  Current / Maximum
  O2 Remaining 剩余氧气

ESCAPE PODS 逃生舱（数量）
CRYOPODS 冷冻舱（数量，单格勾选 [ ]）

REPAIRS 维修
  MINOR（清单）
  MAJOR（清单）
```

**Ship Manifest 状态报告区** 0-9+ 槽位与 MDMG 对应（参见 [Megadamage](#megadamage-兆损伤) 表）。

---

## Glossary 关键术语速查

> 仅 SBT 引入或与本书强相关的术语；完整对照见 [glossary.md](glossary.md)。

| EN 原文 | ZH 译名 | 说明 |
|---|---|---|
| Hull | 船体 | 飞船 AP — 吸收 < Hull 的 MDMG；一击 ≥ Hull 时船体被毁 |
| Megadamage (MDMG) | 兆损伤 | 飞船伤害；累计 ≥ 9 即销毁 |
| Hardpoint | 硬挂点 | 武器系统槽位 |
| Range Band | 距离段 | Contact / Firing / Detection |
| Ship Round | 飞船回合 | 飞船战斗时间单位（分钟到天） |
| Movement / Attack / Morale Phase | 移动 / 攻击 / 士气阶段 | Ship Round 三阶段 |
| Bankruptcy Save | 破产豁免 | 自营业主财务豁免（2d10+10） |
| Fallout | 后果 | 飞船战斗失败的连锁后果 |
| Maintenance Check | 维护检定 | 每年一次 Systems Check；失败滚故障表 |
| Maintenance Issues Table | 维护故障表 | d100 故障表（00-22 Minor / 23-99 Major） |
| Jump Drive | 跃迁引擎 | 1-9 级，决定一次跃迁距离 |
| Jump Point | 跃迁点 | 距邻近天体安全距离的跃迁起点 |
| Warp Core | 曲率核心 | 跃迁燃料，每次跃迁消耗 1 单位 |
| Cryosickness | 犯低温 | 出冷冻舱后的虚弱状态 |
| Time Dilation | 时间膨胀 | 跃迁带来的相对论效应 |
| Class-0 / Class-V / Class-X | 等级-0 / -V / -X | 飞船尺寸 / 能力等级 |
| Hailing Latency | 通讯延迟 | 跨距离段的通讯滞后 |
| Distress Signal | 求救信号 | 应急下放出的信号；查 d10 表得响应时间 |
| Owner-Operator | 自营业主 | 银行联合融资经营的小船船东 |

---

> **导入校对要点（参 mothership-import-guide.md §5）**：
> - **覆盖范围**：已用 `Read` PDF 多模态校对全部 44 页（p.1-44）— 所有舰种 stat / Class-0 详情 / Maintenance / Travel Costs / 速查卡 / Spec Sheet 均已提取。
> - **docling OCR 系统性遗漏**：
>   - 舰种属性数值（嵌在装饰性圆圈图形中）— 全部 10 艘舰已用多模态校对补全。
>   - 速查页 p.2（Deckplan Icons / 通用 Travel Costs / Fuel Costs / Range & Distance 综合表）— 已补 [Quick Reference Card](#quick-reference-card-速查卡) 章节。
>   - Class-0 飞船详情卡（p.29）— 已补 7 类详情。
> - **d100 Maintenance Issues 表**：源 PDF 为 3 列布局（00-33 / 34-66 / 67-99），本导入合并为单列升序，**已确保 100 行完整**（00-22 Minor 23 行 + 23-99 Major 77 行）。
> - **源书内部矛盾**（已逐项加注）：
>   - Executive Transport 详情卡（p.12）J2C-I vs Spec Sheet（p.43）J2C-II — 以详情卡为准。
>   - Dropship 乘员数：详情页（p.9）"12+2" vs 速查页（p.29）"24（载货时 12）"。
>   - 通用 Travel Costs（p.2）vs Jumpliner 详情页（p.23）— 价格相差约 5 倍。
>   - Valuable Salvage 表 d10=00 重复 / 06 行空白。
>   - Contraband 表 d10=01「People」子条 07-08 印为「Drugs」与父项不符。
>   - Particle Beam 价格 "3cr" 疑应为 "3mcr"。
