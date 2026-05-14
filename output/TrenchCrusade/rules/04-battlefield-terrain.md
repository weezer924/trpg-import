# rules/04-battlefield-terrain: Battlefield & Terrain

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.38（Terrain Types / Cover / Moving Into Terrain）、p.39-41（Climbing & Jumping / Falling）、p.60-67（Standard Terrain + Battlefield Archetypes）
> 版本：v1.0.2
> 关联契约：`../matches/coordinate-system.md` §7（地形 schema 单一信息源）

## Index

- [1. 范围与契约边界](#1-范围与契约边界)
- [2. 四大地形类型 Terrain Types](#2-四大地形类型-terrain-types)
- [3. Cover 关键词与触发条件](#3-cover-关键词与触发条件)
- [4. Moving Into Terrain（"in" 的判定）](#4-moving-into-terraininthe-判定)
- [5. Climbing & Jumping & Falling](#5-climbing--jumping--falling)
- [6. 标准地形 11 类（Standard Terrain）](#6-标准地形-11-类standard-terrain)
- [7. Battlefield Archetypes（战场原型）](#7-battlefield-archetypes战场原型)
- [8. 地形 yaml schema 引用](#8-地形-yaml-schema-引用)

---

## 1. 范围与契约边界

本章负责 **地形规则散文**：

- 地形如何分类、何时触发地形效果
- 模型进入 / 跨越 / 攀爬 / 跳跃 / 坠落地形的判定流程
- 战场摆放（默认 36×36 战场上 7 类地形的数量与间距规则）

**不在本章范围**（已在他处定义）：

| 概念 | 在哪定义 |
|---|---|
| 距离测量（"within X"" / "in contact"） | → `../matches/coordinate-system.md` §3 |
| Line of Sight 算法 / cover 三问 | → `../matches/coordinate-system.md` §6 |
| 地形 yaml schema 字段 | → `../matches/coordinate-system.md` §7 |
| 7 类地形完整 yaml 例 | → `../matches/coordinate-system.md` §7.3 |
| `DIFFICULT TERRAIN` / `DANGEROUS TERRAIN` / `IMPASSABLE TERRAIN` / `COVER` 关键词定义 | → `03-keywords-glossary.md` |
| Injury Roll / `INJURY DICE` 累加 | → `02-comprehensive-rules.md` |
| Risky Success Roll 判定 | → `02-comprehensive-rules.md` |

**核心原则**：所有"距离 / LOS / cover"散文复述都禁止——必须**引用** coordinate-system 对应节，避免规则漂移。

---

## 2. 四大地形类型 Terrain Types

> 来源：PDF p.38

游戏开始时双方必须就**每块地形归属哪一类**达成共识，并约定每块地形的边界，便于判定模型是否进入其中。Trench Crusade 共有 4 类地形：

| 类型 | 中文锚定 | 关键词 | 典型实例 |
|---|---|---|---|
| Open | 开阔地形 | — | 空旷地、草甸、平整路面 |
| Difficult | 崎岖地形 | `DIFFICULT TERRAIN` | rock beds（岩石堆）、swamps（泥潭）、craters（弹坑）、fallen trees（倒木）、rubble（瓦砾） |
| Dangerous | 危险地形 | `DANGEROUS TERRAIN` | barbed wire（铁丝网）、minefields（雷区）、raging fires（烈焰）、areas covered in poisonous gas（毒气区） |
| Impassable | 不可通行地形 | `IMPASSABLE TERRAIN` | cliffs（陡崖）、large monuments（大型纪念碑顶面无立足处）、pools of magma（岩浆池） |

**复合属性**：同一块地形**可以同时是 Difficult 和 Dangerous**（PDF p.38 原文：「Terrain can be both Difficult and Dangerous」）。例：泥潭里又埋了地雷。这种情况下两个 keyword 都触发。

### 2.1 Open Terrain（开阔地形）

模型可以自由穿越，无任何修正。是 Trench Crusade 战场上最常见的地形类型。

### 2.2 Difficult Terrain（崎岖地形）

进入或穿越时模型受 `DIFFICULT TERRAIN` keyword 影响（具体判定见 `03-keywords-glossary.md`）。本契约对应 yaml 字段 `movement_cost: 2`（→ `../matches/coordinate-system.md` §7.2）。

### 2.3 Dangerous Terrain（危险地形）

进入或穿越时模型受 `DANGEROUS TERRAIN` keyword 影响，可能触发 Injury Roll。本契约对应 yaml 字段 `dangerous: true`。

### 2.4 Impassable Terrain（不可通行地形）

模型**不能进入**，除非具有 `FLYING` 等可越过的 keyword（参见 PDF p.60 Landmarks 条款）。本契约对应 yaml 字段 `impassable: true`。

---

## 3. Cover 关键词与触发条件

> 来源：PDF p.38

模型 B 相对模型 A 拥有 `COVER` keyword，当且仅当**以下三个条件同时成立**（PDF 原文「三问」）：

1. **接触**：B 站在或紧贴某一块 terrain piece 上；
2. **高度**：该 terrain piece 至少 **½" 高（half-inch high）**；
3. **宽度**：该 terrain piece 至少与 B 的基座**等宽或更宽**（at least as wide as its base）；
4. **位置**：该 terrain piece 处在 A 与 B 之间，使其**部分阻挡（partially blocks）**A 与 B 之间的视线。

> **算法实现** → 见 `../matches/coordinate-system.md` §6.2 的 `target_in_cover(B)` 三问。MCP server 实现按那里的伪代码执行；本章只描述触发条件。

### 3.1 LOS 三态映射

| PDF 情景 | LOS state（→ §6） | 射击判定 |
|---|---|---|
| 视线被完全阻断 | `blocked` | 不可射击（PDF p.38 模型 A 示例：「the Line of Sight to model A is blocked by the terrain... and therefore the model cannot be seen or attacked」） |
| 部分视线 / target in cover | `partial_cover` | 可射击但 **-1 DICE**（PDF p.38 模型 B 示例：「Model B is in cover and there is only a partial line of sight to it, so attacks against the model will suffer -1 DICE penalty」） |
| 完全可见无遮蔽 | `clear` | 无修正（PDF p.38 模型 C 示例：「Model C is in the open and gains no protection from any cover」） |

> 「the bayonet does not count」（PDF p.38）：测量 LOS 时**不计算 target 的武器、手、脚、基座**。算法层把 from / to 简化为基座中心点（→ `../matches/coordinate-system.md` §6.1）。

### 3.2 与 Partial Line of Sight 的关系

`partial_cover` 出现的两种来源：

- 射线穿过 `blocks_los: partial` 的地形（如 smoke / ruins 残破墙体）；
- target 通过 §3 上面四问获得 `COVER` keyword（即"target in cover"分支）。

两者都给攻方 **-1 DICE** ranged。MCP 解析时返回 `state: partial_cover` + 阻挡物列表（→ `../matches/coordinate-system.md` §6.1）。

---

## 4. Moving Into Terrain（"in" 的判定）

> 来源：PDF p.38

PDF 原文：

> A model is said to be "in" a piece of terrain if **more than half of its base is within the boundary of that piece of terrain**.

判定流程：

1. 模型移动结束后，结算其基座占据范围；
2. 若基座面积**超过一半**落在该 terrain piece 边界内 → 模型「in」此地形；
3. 该 terrain piece 的所有 keyword（`DIFFICULT TERRAIN` / `DANGEROUS TERRAIN` / `COVER` 等）此时生效。

**数字化对应**：基座 `[w, h]` 的模型在 `pos = (x, y, z)`，其占据格集合（→ `../matches/coordinate-system.md` §5.3）中**超过 50% 的格**与 terrain 的 `bounds` 相交，即视为「in」该地形。1×1 模型简化为"基座中心点是否在 bounds 内"。

---

## 5. Climbing & Jumping & Falling

> 来源：PDF p.39-41

### 5.1 Open 判定：低矮障碍

以下地形按 **Open terrain** 处理，无需 Climb 判定：

- **Terrain up to 1" high**：高度 ≤ 1" 的任何地形（含 Linear Terrain 见 §6.5）；
- **Trench Walls up to 3" high**：高度 ≤ 3" 的战壕侧壁（见 §6.7）；
- **Ladders / ramps / ropes / stairs and other devices meant for climbing**：梯子、坡道、绳索、楼梯及任何专为攀爬设计的装置。

超过此阈值的陡面则触发 **Climbing Sheer Surfaces** 判定。

### 5.2 Climbing Sheer Surfaces（攀爬陡面）

> PDF p.39

触发条件：模型移动到陡面（如墙、超过 3" 的战壕壁、超过 1" 的 Linear Terrain）**1" 之内**时，可宣告攀爬。

流程：

1. **必须有足够移动力跨越整个表面**——模型**不能停在半墙上**（"it cannot finish the move halfway up a wall"）；
2. 到达陡面时，对该模型进行一次 **Risky Success Roll**（详见 `02-comprehensive-rules.md` Risky Success）；
3. **Success**：模型直接移到陡面顶部或底部，若有剩余移动力可继续行动；
4. **Failure**：模型**停在原地**，**激活立即结束**（Activation ends）。

### 5.3 Jumping Over Gaps（跳跃缺口）

> PDF p.40

触发条件：作为移动的一部分宣告 Jump，跨越**宽度 ≤ M/2** 的缺口。

流程：

1. 移动到缺口边缘——**移动到缺口的距离 + 跳跃距离 ≤ M**（不得超过模型的 Movement Characteristic）。**例**（PDF p.40）：`M=6` 模型可先移动 3"，再尝试跳跃宽度 ≤ 3" 的缺口；
2. 对模型进行 **Risky Success Roll**；
3. **Success**：模型落到缺口对岸，若有剩余移动力可继续行动；
4. **Failure**：模型 **Falls**（坠落，见 §5.5），激活立即结束。**坠落方向由对手选择**（"your opponent can choose which side of the gap it Falls from"）。

### 5.4 Jumping Between Ledges of Unequal Heights（跨越不等高崖）

> PDF p.40

- **从高处跳向低处**：附加适用 Jumping Down（§5.5）规则。
- **从低处跳向高处**：把**高度差加到水平距离上**计算总跳跃距离。若加和超过模型最大可移动距离，**跳跃即不可能**。

### 5.5 Jumping Down（跳下）

> PDF p.40

跳下作为移动的一部分宣告。**Jumping Down 不消耗移动力**（"the Jump Down is 'free'"）——可在任意时刻跳下。

但是：**跳下 3" 或更多** → 计为 **Falling**，必须立刻进行 Injury Roll 后再继续移动。

### 5.6 Falling（坠落）

> PDF p.41

触发条件：

- Jumping Over Gaps 失败（§5.3）；
- Jumping Down ≥ 3"（§5.5）；
- 其他规则指定（如 Diving Charge 的反向案例等）。

流程：

1. 模型从当前位置移到**正下方第一个可站立的平面**；
2. **若坠落距离 ≥ 3"**：进行一次 Injury Roll；
3. **每 3" 坠落附加 +1 `INJURY DICE`**：
   - 3-5" 坠落 → `+1 INJURY DICE`
   - 6-8" 坠落 → `+2 INJURY DICE`
   - 9-11" 坠落 → `+3 INJURY DICE`
   - 以此类推。

> **z 层换算** → 见 `../matches/coordinate-system.md` §2.3。默认 `layer_height = 3"`，因此 z 层差 1 = 3"（恰好触发 Injury Roll），z 层差 2 = 6"（`+2 INJURY DICE`）。

---

## 6. 标准地形 11 类（Standard Terrain）

> 来源：PDF p.60-63

PDF 列出 11 种"标准地形"描述（按外观/形态分类），与 §2 的 4 类（按规则归属分类）**正交**——每个标准地形在游戏开始时双方约定归入 Open/Difficult/Dangerous/Impassable 之一（PDF p.60 「sensible idea to discuss each terrain piece with your opponent to agree what type each will be treated as」）。

### 6.1 Open Terrain（开阔地形）

无遮蔽空地，最常见。模型自由穿越。

### 6.2 Landmarks（地标）

> PDF p.60

单块 **Impassable terrain**（如雕像、神龛、祭坛）。除非具有 `FLYING` keyword，否则**无法跨越**。

**剧本用途**：若 scenario 含 Marker（目标标记），双方可约定用合适的地标替代——增加沉浸感（"more interesting to know that you are fighting to capture a statue or shrine, rather than an anonymous cardboard counter"）。

### 6.3 Area Terrain（区域地形：Dangerous / Difficult / Impassable）

> PDF p.61

Area terrain 是 Dangerous / Difficult / Impassable 三类的统称。**边界协商**至关重要：

- 放在底座上；
- 用细棉线标记边界；
- 或双方简单口头约定边界。

数字化实现见 `../matches/coordinate-system.md` §7.1（`bounds` rect / `bounds_polygon`）。

### 6.4 Hills（山丘）

> PDF p.61

**尺寸建议**：宽度不超过 12"。

**规则属性**：

- **移动**：山丘**默认按 Open terrain 处理**（仅就移动而言）；
- **遮挡视线**：若山丘足够高，可阻断山丘对面模型的 LOS；
- **高地优势**：足够高度的山丘提供 **Elevated +1 DICE** ranged 加成（→ `../matches/coordinate-system.md` §3.2，要求 `(attacker.z - target.z) · layer_height ≥ 3`）。

**叠加地形**：山丘上可以再放其他地形（rocky ground / barbed wire / trenches / ruins），双方需约定这些区域如何归类。

### 6.5 Linear Terrain（线性地形）

> PDF p.62

包含墙、树篱等线性障碍。可有弯折、可拼接成长段。

**高度判定**：

- **≤ 1" 高**：按 Open terrain 跨越，无判定；
- **> 1" 高**：必须按 Climbing Sheer Surfaces 规则攀爬（§5.2）。

### 6.6 Trench Sections（战壕段）

> PDF p.62

战壕是 Trench Crusade 标志性地形（"obvious reasons"）。

**尺寸规约**：

- 长度：**4" 到 12"**（4–12 inches long）；
- 宽度：**2" 到 4"**（2–4 inches wide）；
- 可有弯折，可与其他战壕段拼接成战壕线；
- 可含十字路口（crossroads）和 T 形路口（T-junctions）。

### 6.7 战壕侧壁判定（Trench Wall）

> PDF p.62

- **侧壁 < 3" 高**：按 Open terrain 跨越；
- **侧壁 ≥ 3" 高**：必须 **Climb**（§5.2）或 **Jump Down**（§5.5）；
- 跨越战壕本身：按 **Jumping Over a Gap**（§5.3）。

战壕的 z 层数字化：`base_z: -1` + `height: 1`（顶面回到地面 z=0）。完整 yaml 见 §8。

### 6.8 Ruined Buildings（废墟建筑）

> PDF p.63

单块地形，**建议宽度不超过 12"**。

**规则属性**：

- 外墙按 **Climbing Sheer Surfaces** 攀爬（§5.2）；
- 残存楼梯/楼板按 Open terrain 处理；
- 瓦砾堆（piles of rubble）按 **Difficult terrain** 处理。

### 6.9 Corner Ruins（残角废墟）

> PDF p.63

两堵残墙拼成 L 形或 T 形，每堵墙长度 ≤ 6"。流行原因是制作简单。

**规则属性**：

- 可包含上层残存楼板，模型按 Climb 上去（§5.2）；
- 瓦砾堆按 **Difficult terrain** 处理。

### 6.10 Rivers & Streams（河流与溪流）

> PDF p.63

**布置规约**：

- **River**（河）：必须从战场一边进入，另一边离开；按 **Dangerous terrain** 处理；
- **Stream**（溪）：从一边进入，可从另一边离开或终止于沼泽/湖泊；按 **Difficult terrain** 处理；
- 两者都**必须含一处或多处过河点**（桥、浅滩）——这些过河点按 **Open terrain** 处理。

**使用限制**：只有 scenario 明确要求，或双方都同意时才使用河流/溪流。

### 6.11 Unique Terrain（独特地形）

> PDF p.64

非标准列表中的特殊地形——双方游戏前协商规则归属，"通常是个直截了当的事"。

### 6.12 Scattered Terrain（散布地形）

> PDF p.64

太小或无关紧要的地形：单棵树、箱子、标牌等。**纯装饰**。设置其他地形、移动、攻击、视线判定时**均可忽略**（"can ignore it or move it out of the way"）。

### 6.13 Intact Buildings（完好建筑）

> PDF p.64

不推荐使用。若必须使用：

- 要么约定按 **Impassable** 处理；
- 要么准备**详细的楼板平面图**（floor plan）——模型进入时切换到平面图，从那里继续移动。同时需"运用一些常识与克制"（如不让模型穿过太小的入口）。

---

## 7. Battlefield Archetypes（战场原型）

> 来源：PDF p.65-67

PDF 定义 3 种战场原型，scenario 会明确指定使用哪种。

### 7.1 通用 Setup 流程

1. **Roll-off** 决定地形布置方：双方掷骰（详见 `02-comprehensive-rules.md` Rolling Off），胜方布置整张战场地形；
2. 按原型列出的地形类型清单选择；
3. 遵守该原型的数量与摆放约束（见各小节）；
4. **8" 大件 = 2 件**：宽度或长度超过 8" 的地形片在计数时视作 2 件（"Count pieces that are more than 8" across or more than 8" long as being 2 pieces of terrain"）——三种原型都适用。

**默认战场**：本契约采用 **36×36 格（1" = 1 格）**作为入门战场（→ `../matches/coordinate-system.md` §4），与 PDF 推荐的 3'×3' 一致；可扩 48×48 用于多人或大战团。

### 7.2 No Man's Land（无人区）

> PDF p.65

战壕系统之间的死亡走廊。机枪与炮火交织、偶有废墟/弹坑/倒木/破车/弹痕累累的神龛作为掩体。**很多 No Man's Land 战斗会安排在夜间袭击**，借黑暗逃避远程火力。

**允许地形清单**：

- Trenches
- Ruined Buildings
- Ruined Corners
- Hills
- Areas of Dangerous Terrain（barbed wire / swampy ground 等）
- Areas of Difficult Terrain（craters / rubble / fallen trees 等）
- Landmarks（statues / shrines / altars 等）

**地形数量建议**：每类**至少 2 件**（"at least 2 pieces of each terrain type"）。可以多到塞满战场，也可以稀少到几乎没有，只要满足下面的间距约束。

**摆放约束**：

- 每块地形与其他地形**至少相距 3"**；
- **Trenches 仅可放置在 scenario 部署区（Deployment Zones）内**（"Trenches can only be set up if they are wholly within one of the Deployment Zones shown on the map for the scenario that is being played"）。

### 7.3 Decimated Ruins（残破废墟）

> PDF p.66

战壕之间或紧邻战壕的城镇/村庄废墟。短兵相接残酷。胜负看谁控制废墟、瓦砾堆和破车。

**允许地形清单**：

- Ruined Buildings
- Ruined Corners
- Areas of Dangerous Terrain（barbed wire / minefields 等）
- Areas of Difficult Terrain（craters / rubble 等）
- Landmarks（statues / wrecked vehicles 等）

**地形数量建议**：

- **至少 6 块 ruined buildings**；
- 其他每类**至少 2 件**；
- 8" 大件计 2 件同前。

**摆放约束**（**必须先放废墟**）：

1. 第一块 ruined building / corner 可放战场任意位置；
2. **后续每块 ruined building / corner 必须距其他 ruined building / corner 3"–9"**（"between 3" and 9" away"）；
3. 废墟摆完后再放其他地形；
4. 非废墟地形必须**距其他地形至少 3"**。

### 7.4 Trench Lines（战壕线）

> PDF p.67

战壕系统纵深数英里。深沟保护多数战士免受火力。战斗多发生在战壕内，偶有勇士冒险攀出绕侧。

**允许地形清单**：

- Trenches
- Ruined Corners
- Areas of Dangerous Terrain（barbed wire / minefields 等）
- Areas of Difficult Terrain（craters / rubble 等）
- Landmarks（statues / shrines / wrecked vehicles 等）

**地形数量建议**：

- 战壕**必须足够连接战场两边**——一个模型应能从一边进入、不离开战壕就走到对边；
- 其他每类**至少 2 件**；
- 8" 大件计 2 件同前。

**摆放约束**（**必须先放战壕**）：

1. 第一条战壕必须从战场一边进入；
2. 后续战壕必须**连接已存在的战壕**；
3. 所有战壕摆完后，应可由初始边一路经战壕走到对边；
4. 战壕摆完后再放其他地形；
5. **其他地形必须距任何战壕至少 1"**（注意：与其他原型不同，这里是 1"），且距其他非战壕地形至少 3"。

### 7.5 三原型摆放约束对照

| 原型 | 首要地形 | 首要地形间距 | 其他地形与其他地形 | 其他地形与首要 | 特殊 |
|---|---|---:|---:|---:|---|
| No Man's Land | Trenches（限部署区） | — | ≥ 3" | ≥ 3" | Trenches 不与部署区外接触 |
| Decimated Ruins | Ruined Buildings/Corners | 3"–9" | ≥ 3" | ≥ 3" | 必须 ≥ 6 块废墟 |
| Trench Lines | Trenches（连两边） | — | ≥ 3" | **≥ 1"** | 战壕必须形成连贯通路 |

---

> **PDF 省略说明**：PDF p.64 *"Trench Crusade Gaming Boards"* 一节为实体游戏板制作教程（如何用 MDF / 胶合板 / 喷漆 / foam 雕刻战壕等），对数字化对战项目无价值，本文件不收录。若需实体桌游参考，见 PDF 原文。

---

## 8. 地形 yaml schema 引用

数字化战场存档（`matches/{name}/match-state.yaml`）使用 7 类地形 yaml schema：

- **A. Trench（战壕）** → `../matches/coordinate-system.md` §7.3.A
- **B. Ruins（废墟，含 ruined building / corner）** → `../matches/coordinate-system.md` §7.3.B
- **C. Abandoned Corner（废弃角落，杂物堆）** → `../matches/coordinate-system.md` §7.3.C
- **D. Hill（山丘）** → `../matches/coordinate-system.md` §7.3.D
- **E. Dangerous Terrain（危险地形）** → `../matches/coordinate-system.md` §7.3.E
- **F. Difficult Terrain（崎岖地形）** → `../matches/coordinate-system.md` §7.3.F
- **G. Landmark（地标）** → `../matches/coordinate-system.md` §7.3.G

通用字段（`type` / `bounds` / `base_z` / `height` / `blocks_los` / `cover` / `movement_cost` / `dangerous` / `impassable` / `climbable`）定义见 `../matches/coordinate-system.md` §7.2。

**摆放校验**：MCP server 的 `validate_battlefield_setup`（v0.2 待实现）应在加载 match-state.yaml 时校验本章 §7.2–§7.4 的间距/数量约束；当前 v0.1 由布置方手动验证。

---

> **下一步**（Pass 6 起）：`rules/05-battlekit.md` 描述武器射程时直接引用 §3 short/long range，配合本章 cover -1 DICE，构成 ranged attack 的完整修正链。
