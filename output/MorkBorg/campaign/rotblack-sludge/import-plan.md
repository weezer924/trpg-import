# Rotblack Sludge — Import Plan

> **System:** Mörk Borg
> **Source:** Rotblack Sludge — or The Shadow King's Lost Heir (Johan Nohr / Free League, introductory dungeon)
> **Raw md:** `Rule Books/Mork Borg/md files/Modules/Rotblack Sludge.md` (15 pages, 631 lines)
> **Output dir:** `output/MorkBorg/campaign/rotblack-sludge/`

---

## 1. 模组概览

- **类型**：单一地城（The Accursed Den），15 个房间，引介型冒险
- **钩子**：Shadow King 的 Seer 派 PC 营救失踪的继承人 Aldon；Seer 同时提供 d8 预言（2 真 / 2 假 / 其余真伪混杂）
- **主要反派**：Fletcher（食人术士，15 号房）vs Lesdy（绿屋操控者，11 号房）— 两大派系互相敌对
- **核心威胁**：Gutworm（隐藏于 Rotblack Sludge 黑色沼泽中的巨虫，hP 50）
- **地图结构**：15 房间，南北纵向布局；地城中部被 Rotblack Sludge 沼泽分割（房 9/12/15 临沼泽）
- **随机遭遇**：Table a（每次触发），Table b（全场景仅一次）

---

## 2. 房间/章节清单

| # | 房间 | 关键内容 | 源 md 行号 |
|---|------|---------|-----------|
| 介绍 | Hook + Seer's d8 预言 | 任务背景、Seer 预言表 | 8–36 |
| Random | Table a (d4 重复) | Dusk gnoums / Mongrels / Guards with sharpened teeth / Nesting Death | 40–93 |
| Random | Table b (一次性 d4) | Distraught spirit / Sagsobuth / Terrible silence / 石棺传送 | 94–151 |
| 索引 | The Accursed Den 房间列表 | 15 房间概览 | 153–192 |
| 1 | Entrance | 油灯、小溪、黑紫蝴蝶（食之回 d6） | 194–216 |
| 2 | Dining hall | The bearded man（不可沟通，众人入座则短暂苏醒） | 218–246 |
| 3 | Library/bedroom | 3 slumbering skeletons + Tired crystal demon（书籍 d4 触发） | 260–298 |
| 4 | Guard room | d4 crooked guards + 火炉 + d6 杂物 | 300–344 |
| 5 | Cells | 10 mad prisoners（乞怜但会扼颈） | 346–370 |
| 6 | Corridor | 大型隐藏陷坑（移画触发，落入 room 10） | 382–401 |
| 7 | Pump room | 随机遭遇 + 油泵（泥水回 d4）+ 地板舱门→room 15 | 402–421 |
| 8 | Chain room | 随机遭遇 + 挂钩链、通向 Gem/Statue/Guard | 437–464 |
| 9 | Gem room | 50 尺石柱 + 提琴骷髅 + Rotblack Sludge + **Gutworm** 数据块 | 466–499 |
| 10 | Tunnel | 压缩通道（重甲不能通过），从 pit trap 掉下 | 510–521 |
| 11 | Greenhouse | **Lesdy + 3 hosts**、玻璃房植物、营地 | 522–537 |
| 12 | Statue room | 独眼王雕像（放眼开密门）+ 地板西倾测试 | 538–566 |
| 13 | Son's room | **Aldon**（继承人，傲慢食人骨）+ bullwhip 魔物 | 568–592 |
| 14 | Debris room | 随机遭遇 + 垃圾骨堆 + 上锁门（Fletcher 钥匙） | 599–601* |
| 15 | Forge/slaughterhouse | **Fletcher** 战斗 + d4 Powers + 钥匙 + Fletcher 背景 | 599–606* |

\* 房间 14/15 的文本主要在第 15 页的 OCR 图片块（行 599–601）及后续（行 604–606）。解析时以图片块内 `----- Start of picture text -----` 到 `----- End -----` 为准。

---

## 3. 输出文件结构

参考 OSE 的 `the-hole-in-the-oak/` 布局，但 MB 数据块格式改为：
`**Name** hP X  Morale X  Armor -dY (或 No armor)  Attack d? (+ 特殊)`

| 文件 | 内容 | 必须 | 预计规模 |
|------|------|------|---------|
| `region.md` | 冒险背景、钩子、Seer 的 d8 预言表、地点索引、主线派系、探索提示 | 是 | 中 |
| `encounters.md` | Random Tables a/b、Monster Stat Block Index、Fixed Encounters by Room | 是 | 中 |
| `npcs.md` | Fletcher / Lesdy / 3 hosts / Aldon / bearded man / Tired crystal demon / Sagsobuth / Distraught spirit / Gutworm | 是 | 中 |
| `dungeon.md` | 15 房间逐个描述（Entrance → Forge/slaughterhouse），含 General Features + Rotblack Sludge 通用规则块 | 是 | 大（主文件） |

**不需要的文件**：`shops.md`（无商店，除 Sagsobuth 的一次性交易）、`quests.md`（单一主线，region.md 涵盖）。

> 地城只有 15 房间，全部放 `dungeon.md` 一个文件比拆成多文件更合理（对比 hole-in-the-oak 分 entrance-roots/etc 是因为那边有 50+ 房间、多层）。

---

## 4. Mörk Borg 数据块格式

参考 `output/MorkBorg/rules/morkborg-bestiary.md`。内联紧凑格式：

```markdown
**Monster Name** hP X  Morale X  Armor -dY  Attack d? (+ special).
```

要点：
- **hP**：直接数字（MB 无 HD）
- **Morale**：数字；不可受士气影响则写 `–`
- **Armor**：`-dY`（护甲吸收的骰子），或 `No armor`
- **Attack**：`伤害骰`，必要时加说明（如 `Bite d4: infection if Toughness dr12 failed`）
- **Special abilities / Powers**：紧随数据块后列出，如 Fletcher 的 d4 Power 表

源 md 中 "hP 4 Morale 7 No armor Knife d4" 格式需清洗为标准写法（首字母大小写、数字/骰子规范化）。

---

## 5. 导入步骤计划（每对话 1–2 章节）

| 步骤 | 对话 | 内容 | 输出文件 | 状态 |
|------|------|------|---------|------|
| 1 | 本对话 | 目录 + import-plan.md | `import-plan.md` | ✅ Done |
| 2 | 下一对话 | region.md（背景、钩子、Seer d8、地点索引、派系） | `region.md` | ⬜ |
| 3 | 下一对话 | dungeon.md 房间 1–8（Entrance → Chain room） | `dungeon.md` 前半 | ⬜ |
| 4 | 下一对话 | dungeon.md 房间 9–15（Gem room → Forge） | `dungeon.md` 后半 | ⬜ |
| 5 | 下一对话 | encounters.md（Random Tables + Stat Block Index + Fixed） | `encounters.md` | ⬜ |
| 6 | 下一对话 | npcs.md（所有 NPC）+ 跨文件校验 | `npcs.md` | ⬜ |
| 7 | 最终 | symlink：`ln -s ../dnd-rules-import/output/MorkBorg/campaign "/Users/jack/Projects/trpg-projects/Mork Borg/campaign"` | — | ⬜ |

---

## 6. 每章节检查清单（沿用 OSE guide §7.5）

- [ ] 所有房间的所有要点（bullet points）都导入
- [ ] 所有怪物数据块（hP / Morale / Armor / Attack）与原文一致
- [ ] 随机遭遇表 a/b 的触发条件准确（a 可重复、b 仅一次）
- [ ] 房间间的门/方向（east/west/north/south）与地图一致
- [ ] 关键互动触发（放眼开密门、陷坑开关、入座苏醒 bearded man、Lesdy 介绍 hosts）完整
- [ ] Gutworm 活动范围（房 9/12/15，每次游泳 d6 1–2 触发咬击）记录在 dungeon.md 通用规则块

---

## 7. MB-specific 注意事项

- **没有 THAC0 / Save 表 / XP**：MB 用 dr（difficulty rating）单一检定系统，无需 OSE 式豁免展开
- **Test 格式**：`test <Ability> dr<N>`，能力为 Toughness / Agility / Presence / Strength
- **伤害骰**：全用 d-notation（d4/d6/d8/d10），护甲减伤骰（-d2/-d4/-d6）
- **OCR 残留**：原 md 中 `hP`（小写 h）、`D4`（大写 D）、首字母大小写混乱的 heading——输出时统一为 `hP`、`d4`、正确标题大小写
- **图片块中的文本**：房 14/15 的描述被 OCR 吞到图片块里（第 15 页整页被当成一张图）；抽取时需解析 `----- Start of picture text -----` 到 `----- End -----` 之间的内容
- **Powers / scrolls**：Fletcher 的 d4 Power 表和书籍中的 "unclean scroll (see page 35)" 引用核心书，不要展开

---

## 8. 版本纯净

- 只使用原始 md（已从 Rotblack Sludge.pdf 抽取）内容
- 不从 AI 训练数据补充 MB 其他模组内容
- 规则术语（Power、dr、hP、Morale）与 `morkborg-rules.md` 保持一致
