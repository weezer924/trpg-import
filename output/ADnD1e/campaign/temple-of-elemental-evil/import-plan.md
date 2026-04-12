# T1-4 The Temple of Elemental Evil — Import Plan

> **System:** AD&D 1st Edition
> **Authors:** Gary Gygax & Frank Mentzer (TSR, 1985)
> **Pages:** 146
> **Levels:** 1–8
> **Setting:** World of Greyhawk — Hommlet, Nulb, Temple of Elemental Evil
> **PDF:** `Rule Books/AD&D 1st edition/AD&D 1st Edition - T1-4 - The Temple of Elemental Evil.pdf`

---

## Module Overview

T1-4 是 AD&D 历史上最经典的超级模组之一，合并了 T1 (Village of Hommlet) 和原创的 T2-4 内容。冒险从 1 级小村庄 Hommlet 开始，逐步深入元素邪恶神殿的四层地牢和四个元素节点，最终面对恶魔女王 Zuggtmoy。

**核心结构：**
- 两个村庄（Hommlet 友善 / Nulb 敌对）
- 一个前哨地牢（Moathouse）
- 神殿遗迹地上部分（塔 + 废墟 + 主殿）
- 四层地牢（Level 1-4，规模递增）
- 四个元素节点（Air / Earth / Fire / Water，半位面）
- 附录：神祇、独有怪物、魔法物品

---

## Output File Structure

| File | Content | Required |
|------|---------|----------|
| `region.md` | 区域总览：冒险背景、Greyhawk 历史、派系、地点索引、旅行规则、主线流程 | Yes |
| `hommlet.md` | Hommlet 村庄（Areas 1-32+），含 NPC 详情、商店、教会 | Yes |
| `moathouse.md` | Moathouse 废墟（上层 + 地下层），含随机遭遇 | Yes |
| `nulb.md` | Nulb 村庄，含 NPC、商店、雇佣兵 | Yes |
| `temple-exterior.md` | 神殿地上遗迹：Broken Tower + Building Ruins + Temple 主殿 | Yes |
| `dungeon-level-1.md` | 地牢第一层（Earth Temple 区域），含随机遭遇 | Yes |
| `dungeon-level-2.md` | 地牢第二层（多元素势力区域），含随机遭遇 | Yes |
| `dungeon-level-3.md` | 地牢第三层（Greater Temple 区域），含随机遭遇 | Yes |
| `dungeon-level-4.md` | 地牢第四层（Zuggtmoy 区域），含随机遭遇 | Yes |
| `elemental-nodes.md` | 四个元素节点（Air/Earth/Fire/Water），含规则修正、居民 | Yes |
| `appendices.md` | 附录：神祇（Iuz, St. Cuthbert）、独有怪物（Zuggtmoy 等）、魔法物品 | Yes |
| `encounters.md` | 遭遇汇总：所有随机遭遇表 + 怪物数据块索引 + 固定遭遇索引 | Yes |
| `npcs.md` | NPC 索引：按地点分组（Hommlet / Nulb / Temple / Nodes） | Yes |

---

## Stat Block Format (AD&D 1e + OSE Dual Compatible)

所有 stat block 同时标注 AD&D 1e 原始数据和 OSE 兼容标记。详见 `.claude/adnd1e-campaign-import-guide.md` §3。

### Monster (内联紧凑)

```markdown
**Bugbear** ×4: AC 5 [14], HD 3+1 (15hp), Att 1 × morningstar (2-8), THAC0 16 [+3], MV 90' (30'), SV D12 W13 P14 B15 S16 (F3), ML 9, AL CE; XP 135. SA surprise on 1-3.
```

### NPC (多行结构)

```markdown
### Rufus (Human Fighter 6)
- **AC:** 1 [18] (plate mail +1 + shield)
- **HP:** 48
- **#AT:** 1, **D:** longsword +1 (1-8+3)
- **THAC0:** 14 [+5]
- **MV:** 60' (20')
- **SV:** D10 W11 P12 B13 S14 (F6)
- **AL:** LG
- **S** 17 **I** 14 **W** 11 **D** 12 **C** 16 **Ch** 13
- **Equipment:** plate mail +1, shield, longsword +1, 120 gp
```

### 转换规则速记
- **AC**：补升序 = 19 - 降序（AC 5 → AC 5 [14]，AC -2 → AC -2 [21]）
- **THAC0**：按 HD 查表补充（见 import guide §1 快查表）
- **MV**：AD&D 英寸 × 10 = 英尺，遭遇速度 = ÷3（MV 12" → 120' (40')）
- **SV**：保留 AD&D 1e 原始豁免值，格式写成 OSE 五项标记
- **ML**：AD&D 1e 不标 ML，从上下文推断或标 `ML —`

---

## Import Schedule

| Step | Content | PDF Pages | Output File(s) | Status |
|------|---------|-----------|-----------------|--------|
| 0 | Import plan + AD&D 1e guide | — | `import-plan.md` | ✅ Done |
| 1 | Region overview + Hommlet village | p.4-20 | `region.md`, `hommlet.md` | ✅ Done |
| 2 | Moathouse | p.21-26 | `moathouse.md` | ✅ Done |
| 3 | Interlude + Nulb village | p.27-34 | `nulb.md` (+ append `region.md`) | ✅ Done |
| 4 | Temple exterior (Tower + Ruins + Temple) | p.35-42 | `temple-exterior.md` | ✅ Done |
| 5 | Dungeon Level 1 | p.43-57 | `dungeon-level-1.md` | ✅ Done |
| 6 | Dungeon Level 2 | p.58-74 | `dungeon-level-2.md` | ✅ Done |
| 7 | Dungeon Level 3 | p.75-94 | `dungeon-level-3.md` | ✅ Done |
| 8 | Dungeon Level 4 | p.95-106 | `dungeon-level-4.md` | ✅ Done |
| 9 | Elemental Nodes (Air/Earth/Fire/Water) | p.107-119 | `elemental-nodes.md` | ✅ Done |
| 10 | Appendices (Deities + Monsters + Magic Items) | p.120-128 | `appendices.md` | ✅ Done |
| 11 | Encounters + NPCs summary | — | `encounters.md`, `npcs.md` | ✅ Done |
| 12 | Cross-validation + fixes | — | all files | ✅ Done |

### Session Breakdown (建议的对话拆分)

| Session | Steps | Estimated Pages | Notes |
|---------|-------|-----------------|-------|
| 1 | 0 | — | 本对话：制定计划 |
| 2 | 1 | ~17 pages | region + hommlet (hommlet 有大量 NPC) |
| 3 | 2-3 | ~14 pages | moathouse + nulb |
| 4 | 4-5 | ~21 pages | temple exterior + dungeon L1 |
| 5 | 6 | ~17 pages | dungeon L2 (内容密集) |
| 6 | 7 | ~20 pages | dungeon L3 (最大层) |
| 7 | 8 | ~12 pages | dungeon L4 |
| 8 | 9-10 | ~21 pages | nodes + appendices |
| 9 | 11-12 | — | encounters/npcs 汇总 + 校验 |

> **总计约 9 个对话**完成全部导入。地牢层各自独立一个对话，因为房间数量多、数据密集。

---

## Factions (派系概要，用于 region.md)

| Faction | Alignment | Base | Leader | Notes |
|---------|-----------|------|--------|-------|
| Hommlet Militia | LG/NG | Hommlet | Burne & Rufus | 村庄守卫力量 |
| Church of St. Cuthbert | LG | Hommlet Area 20 | Terjon (Canon) | 善良神殿 |
| Traders / Inn | N | Hommlet Area 7, 13 | 各店主 | 商业势力 |
| Temple of Elemental Evil | CE | Temple | Zuggtmoy (被封印) | 主要敌对势力 |
| Earth Temple | NE | Dungeon L1-2 | 各层牧师 | 四元素之一 |
| Air Temple | CE | Dungeon L2 | — | 四元素之一 |
| Fire Temple | CE | Dungeon L2-3 | — | 四元素之一 |
| Water Temple | CE | Dungeon L2-3 | — | 四元素之一 |
| Iuz | CE | Behind the scenes | Iuz (demigod) | 幕后黑手 |
| Nulb Villagers | NE/CE | Nulb | 各头目 | 邪恶村庄 |

---

## Special Considerations

### 1. 双系统兼容（AD&D 1e + OSE）
- 所有 stat block 同时标注 AD&D 1e 原始数据和 OSE 兼容标记
- 数值以 PDF 原文为准，OSE 标记为附加（升序 AC、THAC0、英尺移动）
- AD&D 1e 独有数据完整保留：六项属性、SA/SD/MR、法术列表、武器速度因子等
- NPC 通常有完整六项属性 + 装备 + 法术列表

### 2. 模组体量巨大
- 146 页，比一般 B 系列模组大 3-4 倍
- 地牢四层合计约 64 页，房间数量估计 300+
- 必须严格按对话拆分，每次只做一个 step

### 3. Hommlet 村庄 NPC 密度极高
- 32+ 个建筑/地点，每个都有详细 NPC 描述
- 许多 NPC 有隐藏身份（邪恶间谍）——这些信息对 DM 至关重要
- hommlet.md 可能是最大的单个文件

### 4. OCR 质量
- 已用 pdf_extract.py 提取前 10 页，文本质量尚可
- 需要在每个 step 提取对应页码的全文再核实

### 5. Greyhawk 设定信息
- Interlude 章节包含重要的 Greyhawk 设定和秘密历史
- 这些信息归入 region.md 的 History/Background 部分
