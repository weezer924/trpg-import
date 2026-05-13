# rules/00-overview: Trench Crusade v0.1 Overview & Reading Map

> 源：本项目自撰（导航 / 索引）；规则数据源 `Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` + `Warbands of Trench Crusade v1.0.2.pdf` + `Trench Crusade Rules Commentaries v1.0.2.pdf`
> 版本：v0.1 收尾（PDF v1.0.2 对齐）

## Index

- [0. 一句话总览](#0-一句话总览)
- [1. 这个项目是什么](#1-这个项目是什么)
- [2. AI 的角色定位](#2-ai-的角色定位)
- [3. v0.1 文件地图](#3-v01-文件地图)
- [4. 如何开始一局（5 步速览）](#4-如何开始一局5-步速览)
- [5. 数字化契约 — SSoT 单一信息源](#5-数字化契约--ssot-单一信息源)
- [6. v0.1 边界与已知排除](#6-v01-边界与已知排除)
- [7. 质量校验状态](#7-质量校验状态)
- [8. AI 对手运行流程（每次激活）](#8-ai-对手运行流程每次激活)
- [9. 术语速查](#9-术语速查)

---

## 0. 一句话总览

**Trench Crusade**（1914 / 战壕战 + 神圣战争 + 地狱降临的 grimdark 战棋）数字化对战项目。两方各持一个 6-10 模型的战团（warband），在 36×36 格战场上按 PDF v1.0.2 规则对战；**AI 担任对手玩家与战斗描述员**，玩家通过未来 web UI 操纵自己的战团。本目录是 v0.1（MVP）输出。

---

## 1. 这个项目是什么

| 维度 | 内容 |
|---|---|
| 游戏类型 | **战棋（skirmish wargame）**，非 TTRPG |
| 规则版本 | PDF **v1.0.2** |
| 阵营对称性 | **双方信息对等**，无 GM/Warden/Keeper |
| 项目用途 | **玩家 vs AI** 对战。AI 通过 MCP 操纵自己的战团 + 玩家通过 web UI 操纵自己的战团 + 共享同一份 `match-state.yaml` |
| v0.1 范围 | 2 个 Faction（New Antioch / Heretic Legions）+ 2 个 Scenario（Claim No Man's Land / Hunt for Heroes）+ 核心规则全套 |
| 已排除 | Campaign Rules（promotion/trauma/glory items）、其余 4 Faction、剩余 10 Scenarios、Mercenaries、扩展包（见 §6） |

**与 TTRPG 项目的关键差异**（详见 `→ ../../../.claude/trenchcrusade-import-guide.md` §0）：

- TTRPG：AI = GM / Warden / Keeper → 推剧情、布场景、扮 NPC
- TrenchCrusade：AI = **Opponent + Battle Narrator** → 按规则出招 + 给战斗结果套描述。**不推剧情**
- TTRPG：`saves/{name}/{role}-notes.md` 存私房叙事；TrenchCrusade：`matches/{name}/match-state.yaml` 存战场状态
- TTRPG：`characters/`；TrenchCrusade：`warbands/` + `matches/roster-template.md`

---

## 2. AI 的角色定位

AI 在本项目里**只做两件事**：

1. **Opponent 对手玩家**：按规则出招——查距离 / 选 ACTION / 投骰 / 接受结算
2. **Battle Narrator 战斗描述员**：在骰子结算**之后**，用 `narrative/` 调色板为结果套 1-3 句 grimdark 描述

AI **不做**：

- 不推剧情（不是 GM）
- 不调骰子（叙事永远后于规则）
- 不替玩家做决策
- 不给"任务建议"
- 不主持开放性世界（没有"你转头看到 X"——只有"骰 7+ 命中 X"）

详见 `→ ../narrative/tone-guide.md` §"AI 的角色定位"。

---

## 3. v0.1 文件地图

> 每个文件是 v0.1 完整工作的一部分。**消费者**列说明谁会读它：AI（对手 + 描述员） / 玩家（人类查规则） / MCP（机器解析 yaml） / web UI（渲染战场）。

### 3.1 规则 `rules/`

| 路径 | 一句话用途 | 主要消费者 | PDF 锚 |
|---|---|---|---|
| `rules/00-overview.md` | **本文件**。v0.1 总索引 + 阅读引导 | 新接触者 (AI / 人) | — |
| `→ ./01-core-rules.md` | 速览：三阶段回合 / 成功判定 / 移动 / 战斗 / 受伤 / 士气 | 玩家上手 / AI 快速回顾 | p.14-21 |
| `→ ./02-comprehensive-rules.md` | 详细：核心概念 / 骰子规则 / 标记 / 全部 ACTION / 战斗修正 / Injury Roll Table / Bloodbath / Morale Phase | AI 决策 / 规则查询 | p.22-51 |
| `→ ./03-keywords-glossary.md` | 关键词词典（`PENETRATING` / `CLEAVE` / `TOUGH` / `DEADLY` / `BLOOD MARKER` 等） | AI / MCP 引用 | p.52-64 |
| `→ ./04-battlefield-terrain.md` | 战场原型 + 7 类地形规则 | MCP（地形 schema 消费）/ AI | p.60-67 |
| `→ ./05-battlekit.md` | 全武器 / 装备 / 护甲数据（yaml 结构化） | AI / MCP（cost & profile） | p.68-86 |
| `→ ./08-scenarios.md` | Scenario Format 框架 + Scenario I (Claim No Man's Land) + Scenario II (Hunt for Heroes) | 玩家选剧本 / AI 知胜负条件 | p.144-157 |

> **缺位说明**：`06-campaign-rules.md` 和 `07-glory-items.md` 是 v0.2.A backlog（Campaign Rules，56 页）；v0.1 不含。文件编号留空即占位。

### 3.2 战团 `warbands/`

| 路径 | 用途 | 主要消费者 | PDF 锚 |
|---|---|---|---|
| `→ ../warbands/00-warband-keywords.md` | Warbands 合集独有的 keywords（与 `rules/03` 去重后剩余） | AI / MCP | Warbands p.15-20 |
| `→ ../warbands/01-new-antioch.md` | New Antioch 主战团 + 4 个 variants（Papal States / Éire / Alba / Abyssinia） | 玩家建团 / AI 操纵 | Warbands p.21-46 |
| `→ ../warbands/02-heretic-legions.md` | Heretic Legions 主战团 + 3 个 variants（Trench Ghosts / Knights of Avarice / Naval Raiders） | 玩家建团 / AI 操纵 | Warbands p.103-124 |

### 3.3 Errata `errata/`

| 路径 | 用途 | PDF 锚 |
|---|---|---|
| `→ ../errata/rules-commentaries.md` | 官方 FAQ / 裁决（41 条 Q&A） | Rules Commentaries v1.0.2（8p） |

### 3.4 叙事调色板 `narrative/`（**Battle Narrator 的工具箱**）

| 路径 | 用途 | 主要消费者 |
|---|---|---|
| `→ ../narrative/world-primer.md` | 7 个意象主题（战壕 / 机械教士 / 异端 / 教廷狂热 / 末日感 / 黑圣杯 / 无人区）的**调子**词汇 | AI 描述战斗时调取 |
| `→ ../narrative/tone-guide.md` | 文风指引：✅ 允许 / ❌ 禁区；AI 角色定位 | AI 自我规约 |
| `→ ../narrative/injury-flavor.md` | Injury Roll Table 6 个结果 × 武器类别的描述模板矩阵 | AI 套模板生成 |
| `→ ../narrative/event-triggers.md` | 关键事件（Charge / Bloodbath / Critical / Down / Out of Action / Morale 失败 / Bless 触发）的描述钩子 | AI 实时事件描述 |

### 3.5 战场状态 `matches/`（**MCP 的契约源**）

| 路径 | 用途 | 主要消费者 |
|---|---|---|
| `→ ../matches/coordinate-system.md` | **SSoT 单一信息源**：坐标 / 距离 / LOS / 基座 / 地形 schema / MCP 接口契约 | MCP / AI / web UI |
| `→ ../matches/match-template.yaml` | 战场状态 yaml schema 模板（battlefield + terrain + scenario + models + events） | MCP / web UI / 存档 |
| `→ ../matches/roster-template.md` | **战团构建模板**（招募流程 + 预算 + 装备槽 + cost 公式 + 两个示例 roster） | 玩家建团 |

### 3.6 Lore `lore/`（可选，AI 通常不引）

| 路径 | 用途 |
|---|---|
| `→ ../lore/timeline.md` | World in Flames 时间线（PDF p.7-13）。**与 world-primer 区别**：本文件是事件顺序，world-primer 是意象词汇。AI 在战斗中**通常不引此**，只在玩家问起时翻 |

### 3.7 参考 `_references/`（非规则，校验用）

| 路径 | 用途 |
|---|---|
| `→ ../_references/core-rules-video-transcript.md` | Core Rules 教学视频文稿。Pass 2-4 完成后用 §3 14 条 checklist 校验过 |

---

## 4. 如何开始一局（5 步速览）

| 步 | 做什么 | 引用 |
|---|---|---|
| 1 | **构建 roster**：选 faction → 选 variant（可选）→ 在 700/800 👑 预算内招募 6-10 个模型 + 装备 | `→ ../matches/roster-template.md`（招募流程 + 示例） |
| 2 | **摆地形**：选 battlefield archetype（v0.1 默认 No Man's Land）→ 摆 7 类地形（trench / ruins / hill / 等）。**模型多者**摆地形先手 | `→ ./04-battlefield-terrain.md` + `→ ../matches/coordinate-system.md §7` |
| 3 | **选 scenario**：v0.1 选 Scenario I (Claim No Man's Land) 或 II (Hunt for Heroes)。无共识 → roll-off | `→ ./08-scenarios.md` |
| 4 | **部署**：roll-off 选部署区 → 双方交替部署模型（模型多者先）→ Infiltrators 按剧本说明特殊部署 | `→ ./08-scenarios.md §1.4` |
| 5 | **开打**：每回合 Initiative Phase → Activation Phase → Morale Phase；达到剧本指定回合数后比 VP 胜负 | `→ ./02-comprehensive-rules.md` + `→ ./01-core-rules.md` |

---

## 5. 数字化契约 — SSoT 单一信息源

PDF v1.0.2 假设两人面对面用**实体卷尺测距 + 蹲下看模型视线**。数字化对战必须用数学规约替代这两个动作，否则 AI 和 MCP 没法仲裁。

**核心契约文件**：`→ ../matches/coordinate-system.md`

| 数值化对象 | SSoT 位置 | 规则散文位置 |
|---|---|---|
| 距离测量（含 charge 12" / 半射程 / cover ½"） | `coordinate-system.md §3` | rules/* 引用 |
| LOS 判定（clear / partial_cover / blocked） | `coordinate-system.md §6` | rules/02 引用 |
| Cover 三问（高 ½" / 在中间 / 模型在后） | `coordinate-system.md §6` | rules/02 引用 |
| 地形 schema（trench / ruins / hill / 等 7 类） | `coordinate-system.md §7` | rules/04 详述规则、引 schema |
| 基座占格（grid `[w, h]` vs 视觉 `base_dimensions_mm`） | `coordinate-system.md §5` | warbands/* 每单位标注 |
| MCP 接口签名（6 个） | `coordinate-system.md §8` | — |

**硬性规范**（Pass 2-12 全部遵守，本文件再次声明）：

凡涉及距离 / LOS / cover / 地形 / 基座的描述 → 引用 `coordinate-system.md`，**不复述**。这避免规则漂移与多源不一致。AI 和 MCP 在运行时**不心算**，所有空间查询走 MCP。

详细 checklist 见 `coordinate-system.md §9`。

---

## 6. v0.1 边界与已知排除

### 6.1 v0.1 含

- 2 Faction（New Antioch + Heretic Legions），含全部 variants
- 2 Scenario（I + II）
- 全部核心规则（rules/01-05）
- 全部 keywords（rules/03 + warbands/00）
- 官方 errata（41 Q&A）
- 叙事调色板 4 份
- 坐标系契约 + match-state.yaml schema
- World in Flames 时间线（lore/）

### 6.2 v0.1 不含（详见 `→ ../../../.claude/trenchcrusade-import-guide.md` §9.2）

| 类别 | 排除内容 | 计划版本 |
|---|---|---|
| Campaign Rules | Patrons / Trauma / Promotions / Reinforcements / Exploration / Quartermaster / Glory Items（PDF p.87-143） | v0.2.A |
| 其余 Factions | Trench Pilgrims / The Sultanate of the Iron Wall / The Cult of the Black Grail / The Court of the Seven-Headed Serpent | v0.2.B |
| Mercenaries | Warbands p.172-186 | v0.2.C（或 v0.1.5 若单场可用） |
| 剩余 Scenarios | III-XII（PDF p.158-197） | v0.2.D |
| 扩展包 | Prussian Stosstruppen / Sniper Priests / The Great Hunger / The Red Brigade | 未定 |
| Goetic Powers | Court of Seven-Headed Serpent 的 7 种罪恶魔法（Warbands p.154-161） | v0.2.B 子项 |

### 6.3 v0.1 单场对战的简化用法

- **VP 公式**：v0.1 单场用 scenario 自带的 VP 条目（Objective / Mark / Asset / Glorious Deed），**不用** `👑÷10、☼÷3` 之类的模型成本 VP 公式——那属 Campaign Rules。详见 `→ ./08-scenarios.md §1.7`。
- **Glory Points (☼) 简化**：单场完成 1 项 Glorious Deed = **1 VP**（非 10 VP，已与 PDF p.153/156/160 对齐）。战后不结算 ☼ / EXP / Promotion Pool。
- **Mercenaries / Glory Items**：v0.1 单场默认**不允许花 ☼ 招募**（这两类是 v0.2 内容）。双方可协商。

---

## 7. 质量校验状态

v0.1 全部 Pass 完成后已通过以下校验：

| 校验项 | 文件 / 来源 | 状态 |
|---|---|---|
| 视频 transcript §3 14 条核心规则 | `→ ../_references/core-rules-video-transcript.md` | ✅ rules/01-03 已逐条核对 |
| 官方 errata 41 条 Q&A 集成到对应单位 / battlekit | `→ ../errata/rules-commentaries.md` | ✅ 关键裁决回填到 warbands/* 和 rules/02 |
| ACTION vs Attack 用词区分 | rules/02 / warbands/* | ✅ ACTION 全大写、Attack 普通用法分离 |
| Base size 阈值方向（grid `[w, h]` vs 视觉 mm） | `→ ../matches/coordinate-system.md §5` | ✅ 两层语义已厘清，warbands/* 全部标 base_size + base_dimensions_mm |
| VP 公式修正（1 VP / Deed，非 10 VP） | rules/08 §1.9 + match-template.yaml §3 注释 | ✅ 已对齐 PDF p.153/156/160 |
| 全单位 yaml profile 结构化（MCP 可解析） | warbands/01 + 02 | ✅ §3.2 模板全员套用 |
| 全武器 / 装备 yaml 结构化 | rules/05 + warbands/* unique battlekit | ✅ §3.3 模板全员套用 |
| 跨文件引用统一用相对路径 | 全 rules/ + warbands/ + narrative/ | ✅ 无硬编码绝对路径 |
| Glorious Deeds 条件因果链 | rules/08 §1.8 | ✅ PDF 两个对照例子已纳入 |
| Bloodbath 累加 4d6 / Tough 仅首次 / Blood Marker 不能修自身 injury | rules/02 + errata | ✅ 视频明确指出的 3 条已加注 |

剩余未覆盖的边界条件（已注明 `[术语待锚定]` 或 errata 中）在 v0.2 复核时回填。

---

## 8. AI 对手运行流程（每次激活）

> AI 在自己回合的每次 Activation 该做什么。**严格顺序**：查询 → 决策 → 投骰 → 套描述。

```
┌─────────────────────────────────────────────────────────────┐
│  ① 查 match-state.yaml：找出未激活的己方模型              │
│     选一个作为本次 Activation 主体                          │
├─────────────────────────────────────────────────────────────┤
│  ② 查 MCP：get_distance / get_los / is_in_range            │
│     → coordinate-system.md §8 接口                          │
│     得出可达目标、武器射程内目标、视线状态                  │
├─────────────────────────────────────────────────────────────┤
│  ③ 选 ACTION（按 rules/02 ACTION 列表）：                  │
│     Move / Charge / Retreat / Dash / Shoot / Fight /        │
│     单位 special ACTION（Hold Your Fire / Aim / Hide / ...）│
├─────────────────────────────────────────────────────────────┤
│  ④ 投骰：Success Roll (2d6 ≥ 7) / Risky Roll / Injury Roll │
│     → rules/02 + rules/03 keywords 应用 +DICE / -DICE       │
│     → 决定花 BLOOD / BLESSING MARKER 调整骰子               │
├─────────────────────────────────────────────────────────────┤
│  ⑤ 套描述：根据结果调取                                    │
│     - narrative/injury-flavor.md（Injury Roll 落点）        │
│     - narrative/event-triggers.md（Charge / Critical / Down│
│       / OoA / Bloodbath / Morale 失败 / Bless 触发）        │
│     - narrative/world-primer.md（faction-specific 意象）   │
│     生成 1-3 句 grimdark 描述                               │
├─────────────────────────────────────────────────────────────┤
│  ⑥ 更新 match-state.yaml：                                 │
│     - 模型 pos / hp / markers / activated                   │
│     - events[] 追加这次的结果 + 描述                        │
├─────────────────────────────────────────────────────────────┤
│  ⑦ 等对手玩家激活（or 触发对手的 reactive ability）        │
└─────────────────────────────────────────────────────────────┘
```

**关键约束**：

- 第 ② 步**不心算**距离 / LOS——必须调 MCP。AI 的"我估计 8" 内"是无效推理
- 第 ⑤ 步**严格在 ④ 之后**——叙事永远后于规则。AI 不能写"他打中了"再去查骰子是否 7+
- 第 ⑥ 步是事实层（state.yaml 是 SSoT），不是描述层；描述存 events[].narrative 字段，方便回放

---

## 9. 术语速查

中英术语对照、ALL-CAPS 关键词约定、不译条目（单位名 / 武器名 / faction 名）的完整列表见：

`→ ../../../.claude/trenchcrusade-import-guide.md` §3.7 — 中英术语锚定表

**最常用速查**：

| 项 | 速查位置 |
|---|---|
| 关键词词典（`PENETRATING` 等 50+ 条） | `→ ./03-keywords-glossary.md` |
| 武器 / 装备数据 | `→ ./05-battlekit.md` |
| 距离 / LOS / 基座 / 地形 schema | `→ ../matches/coordinate-system.md` |
| 战团单位 stats / cost | `→ ../warbands/01-new-antioch.md` + `→ ../warbands/02-heretic-legions.md` |
| 招募流程 + 预算 + 示例 roster | `→ ../matches/roster-template.md` |
| Injury Roll Table 描述模板 | `→ ../narrative/injury-flavor.md` |
| 关键事件描述钩子 | `→ ../narrative/event-triggers.md` |
| 官方 errata Q&A | `→ ../errata/rules-commentaries.md` |
| 时间线（lore） | `→ ../lore/timeline.md` |

---

## 跨文件引用速查（本文件外链一览）

- 项目导入指南：`→ ../../../.claude/trenchcrusade-import-guide.md`
- 规则速览 / 详细：`→ ./01-core-rules.md` · `→ ./02-comprehensive-rules.md`
- 关键词 / 地形 / 装备：`→ ./03-keywords-glossary.md` · `→ ./04-battlefield-terrain.md` · `→ ./05-battlekit.md`
- 剧本：`→ ./08-scenarios.md`
- 战团：`→ ../warbands/00-warband-keywords.md` · `→ ../warbands/01-new-antioch.md` · `→ ../warbands/02-heretic-legions.md`
- 数字化契约：`→ ../matches/coordinate-system.md` · `→ ../matches/match-template.yaml` · `→ ../matches/roster-template.md`
- 叙事调色板：`→ ../narrative/world-primer.md` · `→ ../narrative/tone-guide.md` · `→ ../narrative/injury-flavor.md` · `→ ../narrative/event-triggers.md`
- 官方 errata：`→ ../errata/rules-commentaries.md`
- Lore：`→ ../lore/timeline.md`
- 视频 transcript（校验）：`→ ../_references/core-rules-video-transcript.md`
