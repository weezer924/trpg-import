# I6 Ravenloft — Import Plan

> **System:** AD&D 1st Edition
> **Authors:** Tracy & Laura Hickman (TSR, 1983)
> **Pages:** 40 (32 pages of content + maps)
> **Levels:** 5–7
> **Setting:** Barovia — Castle Ravenloft and surrounding lands
> **PDF:** `Rule Books/AD&D 1st edition/AD&D 1st Edition - I6 - Ravenloft.pdf`
> **MD:** `Rule Books/AD&D 1st edition/md files/AD&D 1st Edition - I6 - Ravenloft.md`

---

## Module Overview

I6 Ravenloft 是 AD&D 历史上最具影响力的模组之一，首创哥特恐怖风格冒险，后来衍生出整个 Ravenloft 战役设定。冒险围绕吸血鬼 Count Strahd von Zarovich 和他的城堡展开，PC 被困在 Barovia 山谷中，必须消灭 Strahd 才能离开。

**核心特色：**
- **Fortunes of Ravenloft**：冒险开始前的卡牌占卜系统，随机决定关键宝物位置、Strahd 的目标和战斗修正，每次游玩都不同
- **Strahd 作为主动敌人**：DM 必须像扮演 PC 一样扮演 Strahd，他会主动监视、袭击和操纵 PC
- **哥特恐怖氛围**：迷雾封锁、狼群巡逻、夜间袭击、精神压迫

**核心结构：**
- Strahd von Zarovich 数据和行动模式（p.3）
- Fortunes of Ravenloft 占卜系统（p.4-5）
- Barovia 户外区域（Areas A-J：道路、村庄、吉普赛营地、城堡入口）
- Castle Ravenloft 六层结构（K1-K88，约 88 个房间/区域）：
  - Courtyard (K1-K6)
  - Main Floor (K7-K24)
  - Court of the Count (K25-K34)
  - Rooms of Weeping (K35-K46)
  - Spires of Ravenloft (K47-K60)
  - Larders of Ill Omen (K61-K72)
  - Dungeon and Catacomb (K73-K88)
- 附录：独有怪物、魔法物品、Tome of Strahd

---

## Output File Structure

| File | Content | Required |
|------|---------|----------|
| `import-plan.md` | 导入计划和进度跟踪 | Yes |
| `region.md` | 区域总览：冒险背景、Barovia 地理、Fortunes 系统、随机遭遇表、旅行规则、Strahd 行动模式、DM Mechanics Reference | Yes |
| `barovia.md` | Barovia 户外（Areas A-J）：道路、村庄 (E1-E7)、吉普赛营地、城堡入口 | Yes |
| `castle-courtyard.md` | Castle Ravenloft: Courtyard (K1-K6) + Main Floor (K7-K24) | Yes |
| `castle-upper.md` | Castle Ravenloft: Court of the Count (K25-K34) + Rooms of Weeping (K35-K46) | Yes |
| `castle-spires.md` | Castle Ravenloft: Spires (K47-K60) | Yes |
| `castle-larders.md` | Castle Ravenloft: Larders of Ill Omen (K61-K72) | Yes |
| `castle-catacombs.md` | Castle Ravenloft: Dungeon & Catacomb (K73-K88)，含 40 个 crypts | Yes |
| `appendices.md` | 附录：Strahd 完整数据、独有怪物 (Strahd Zombies, Gypsies, Barovians)、魔法物品 (Sunsword, Holy Symbol, Icon, Tome)、Optional Ending | Yes |
| `encounters.md` | 遭遇汇总：随机遭遇表 (Tables 4-7) + 怪物数据块索引 + 固定遭遇索引 | Yes |
| `npcs.md` | NPC 索引：按地点分组 (Barovia / Castle) | Yes |

---

## Stat Block Format (AD&D 1e + OSE Dual Compatible)

所有 stat block 同时标注 AD&D 1e 原始数据和 OSE 兼容标记。详见 `.claude/adnd1e-campaign-import-guide.md` §3。

### Monster (内联紧凑)

```markdown
**Worg Wolf** ×4: AC 6 [13], HD 4+4 (22hp), Att 1 × bite (2-8), THAC0 15 [+4], MV 180' (60'), SV D12 W13 P14 B15 S16 (F4), ML —, AL NE; XP —.
```

### NPC (多行结构)

```markdown
### Ireena Kolyana (Human Fighter 4)
- **AC:** 10 [9]
- **HP:** 6
- **#AT:** 1, **D:** dagger (1-4)
- **THAC0:** 18 [+1]
- **MV:** 120' (40')
- **SV:** D11 W12 P13 B14 S15 (F4)
- **AL:** LG
- **S** 13 **I** 10 **W** 14 **D** 17 **Ch** 18
- **Notes:** Burgomaster's adopted daughter. Bitten twice by Strahd. Does not remember her past.
```

### 转换规则速记
- **AC**：补升序 = 19 - 降序（AC 5 → AC 5 [14]，AC -1 → AC -1 [20]）
- **THAC0**：按 HD 查表补充（见 import guide §1 快查表）
- **MV**：AD&D 英寸 × 10 = 英尺，遭遇速度 = ÷3（MV 12" → 120' (40')）
- **SV**：保留 AD&D 1e 原始豁免值，格式写成 OSE 五项标记
- **ML**：AD&D 1e 不标 ML，从上下文推断或标 `ML —`

---

## Import Schedule

| Step | Content | PDF Pages | Output File(s) | Status |
|------|---------|-----------|-----------------|--------|
| 0 | Import plan | — | `import-plan.md` | ✅ Done |
| 1 | Region overview + Fortunes system + Random encounters | p.3-6, p.12 | `region.md` | ✅ Done |
| 2 | Barovia outdoor areas (A-J) + Village (E1-E7) + Gypsy Camp | p.7-12 | `barovia.md` | ✅ Done |
| 3 | Castle Courtyard (K1-K6) + Main Floor (K7-K24) | p.12-16 | `castle-courtyard.md` | ✅ Done |
| 4 | Court of the Count (K25-K34) + Rooms of Weeping (K35-K46) | p.17-21 | `castle-upper.md` | ✅ Done |
| 5 | Spires (K47-K60) | p.21-23 | `castle-spires.md` | ✅ Done |
| 6 | Larders of Ill Omen (K61-K72) | p.22-24 | `castle-larders.md` | ✅ Done |
| 7 | Dungeon & Catacomb (K73-K88) + 40 Crypts | p.24-30 | `castle-catacombs.md` | ✅ Done |
| 8 | Appendices (monsters, treasures, Tome of Strahd, optional ending) | p.30-32 | `appendices.md` | ✅ Done |
| 9 | Encounters + NPCs summary | — | `encounters.md`, `npcs.md` | ✅ Done |
| 10 | Cross-validation + fixes | — | all files | ✅ Done |

### Session Breakdown (建议的对话拆分)

| Session | Steps | Estimated Pages | Notes |
|---------|-------|-----------------|-------|
| 1 | 0 | — | 本对话：制定计划 |
| 2 | 1-2 | ~9 pages | region + barovia（村庄 NPC 不多，可合并） |
| 3 | 3 | ~5 pages | courtyard + main floor（K7-K24 含大量房间描述） |
| 4 | 4-5 | ~6 pages | upper floors + spires |
| 5 | 6-7 | ~8 pages | larders + catacombs（catacombs 有 40 个 crypt，数据密集） |
| 6 | 8-9 | ~3 pages + 汇总 | appendices + encounters/npcs 汇总 |
| 7 | 10 | — | 校验 |

> **总计约 7 个对话**完成全部导入。模组 40 页，比 T1-4（146 页）小很多，但 Castle Ravenloft 88 个房间数据密度很高。

---

## Factions (派系概要，用于 region.md)

| Faction | Alignment | Base | Leader | Notes |
|---------|-----------|------|--------|-------|
| Strahd von Zarovich | CE | Castle Ravenloft (K86) | Strahd | 吸血鬼领主，10HD + 10th MU，主动敌人 |
| Gypsies (Vistani) | NE | Tser Pool Camp (G) | Madam Eva (C-10) | 为 Strahd 服务，可出入 Barovia |
| Barovia Villagers | NG | Village of Barovia (E) | Ismark the Lesser | 被恐怖统治，畏惧 Strahd |
| Church of Barovia | LG | Church (E6) | Donavich (C-2) | 唯一抵抗力量，每晚祈祷守护 |
| Castle Servants | CE/CN | Castle Ravenloft | Various | Cyrus Belview, Lief Lipsiege, Helga (vampire maid) |
| Castle Undead | CE/NE | Castle Ravenloft | Strahd | 各类不死生物：zombies, wraiths, spectres, vampires |
| Witches | CE | K56 (Cauldron) | — | 7 名女巫，为 Strahd 服务 |

---

## Key NPCs (主要 NPC 速查)

| NPC | Location | Class/Level | AL | Key Role |
|-----|----------|-------------|-----|----------|
| Count Strahd von Zarovich | Castle (mobile) | Vampire + MU-10 | CE | 主要敌人，55hp，AC -1 |
| Ireena Kolyana | E4 → with PCs | F-4 | LG | 被 Strahd 追求的女性，Tatyana 转世 |
| Ismark the Lesser | E2 (tavern) | F-2 | LG | Burgomaster 之子，引导 PC |
| Madam Eva | G1 (tent) | C-10 | CN | 吉普赛领袖，占卜者 |
| Donavich | E6 (church) | C-2 | LG | 教堂牧师，知道 Tome of Strahd |
| Bildrath | E1 (mercantile) | F-4 | LN | 商人，10 倍价格 |
| Parriwimple | E1 | F-9 | LN | 保镖，S 18/80，50hp |
| Cyrus Belview | K62 | F-0 | CN | 城堡仆人，疯癫但无害 |
| Lief Lipsiege | K30 | F-0 | CE | 会计师，知道 Holy Symbol 位置 |
| Helga | K32 | Vampire (8+3 HD) | CE | 伪装成仆人的吸血鬼 |
| Gertruda | K42 | F-0 | NG | Mad Mary 之女，天真无邪 |

---

## Key Treasures (重要宝物)

| Treasure | Description | Location |
|----------|-------------|----------|
| Icon of Ravenloft | Silver holy artifact, +4 turn undead, heal 3d6+3/day | K15 (Chapel) |
| Holy Symbol of Ravenkind | Platinum sun medallion, +2 turn, flares vs vampires | Fortunes-determined |
| Sunsword | +2 sword (+3 vs undead, +10 dmg vs vampires) | Hilt: Fortunes; Blade: random PC |
| Tome of Strahd | Strahd's history, clues to weaknesses | Fortunes-determined |
| Treasury (K41) | 50,000 cp; 10,000 sp/gp; 1,000 pp; gems/jewels; +2 sword; 3× +3 mace | K41 |
| Deck of Many Things | In trapped chest | K78 (Brazier Room) |
| Witches' Spellbook | Worth 42,750 gp, damages non-evil | K56 |

---

## Special Considerations

### 1. Fortunes of Ravenloft 系统
- 用普通扑克牌进行占卜，决定三个关键要素：
  - **Table 1 (Places)**：关键宝物和 Strahd 可能出现的位置（10 个可能地点）
  - **Table 2 (Modifiers)**：PC 在最终战斗中的命中和 AC 修正
  - **Table 3 (Strahd's Goals)**：Strahd 的动机（4 种不同目标）
- 这个系统使模组具有很高的重玩性
- 在 region.md 中完整记录三张表格和所有结果

### 2. Strahd 作为主动敌人
- 每天 4 次（黎明、正午、黄昏、午夜）有 60% 概率知道 PC 位置
- 如果知道位置，2 小时内发动攻击
- 有 3 种预设攻击模式，每种只能用一次
- 必须在 region.md 中完整记录 Strahd 的行为规则

### 3. 双系统兼容（AD&D 1e + OSE）
- 所有 stat block 同时标注 AD&D 1e 原始数据和 OSE 兼容标记
- 数值以 PDF 原文为准，OSE 标记为附加
- AD&D 1e 独有数据完整保留：六项属性、SA/SD/MR、法术列表
- Strahd 的 MU 法术列表必须完整保留

### 4. Castle Ravenloft 房间编号
- K1-K88，但有不少子区域（K18a, K20a, K31a, K31b, K83a 等）
- 部分房间有首次进入和再次进入的不同描述（K8, K9, K10 等）
- 需要忠实保留两套描述文本

### 5. Catacombs (K84) 的复杂性
- 40 个独立 crypt，每个有墓志铭和内容物
- Crypt 14 内部扩展（15 个 wight 棺材）
- 复杂的传送陷阱系统（crypt 32, 37, 38 互相传送）
- 这是整个模组数据最密集的部分

### 6. DM Mechanics Reference（region.md 专属章节）
- 在 `region.md` 末尾设立 **DM Mechanics Reference** 章节
- 汇总所有跨区域联动机制、隐藏身份、伪装敌人、多房间陷阱链、特殊互动等
- 每条仅列机制名称 + 涉及的房间编号/文件引用，不重复正文内容
- 目的：DM 跑团前通读此章节，掌握全局"惊喜"，避免遗漏
- 此章节在 Step 9（汇总阶段）统一编写，因为需要所有房间内容完成后才能准确索引

### 7. OCR 质量
- PDF 为扫描版，OCR 质量一般
- 常见问题：数字混淆（l/1/I）、负号丢失、多栏排版错乱
- 关键数值（AC、HP、damage）需逐一与 PDF 原文核对
