# errata/rules-commentaries: 官方 Rules Commentaries / FAQ

> 源：`Rule Books/Trench Crusade/Trench Crusade Rules Commentaries v1.0.2.pdf`（整本 8 页）
> 版本：v1.0.2
> 性质：官方 FAQ / 裁决，回答常见规则疑问；与主规则书并列权威，遇冲突以本文件为准
>
> **使用约定**：每条裁决都给出
> - **原条目引用**：PDF 页码 + 涉及主规则书章节
> - **Q（问）**：原文翻译
> - **A（答）**：原文翻译（不扩展、不解释、不修正官方语义）
> - **→ 跨文件引用**（如适用）：指向 `rules/*` `warbands/*` 对应章节，便于 v0.1 完工后回引（部分目标文件 Pass 2-9 尚未完成时为占位）

## Index

- [Core & Comprehensive Rules](#core--comprehensive-rules)
  - [Q1 — BLOOD 与 BLESSING MARKER 应用顺序](#q1--blood-与-blessing-marker-应用顺序)
  - [Q2 — Move / Charge / Retreat 是同一种 ACTION 吗？](#q2--move--charge--retreat-是同一种-action-吗)
  - [Q3 — 无法移动的模型能否宣告 Retreat ACTION？](#q3--无法移动的模型能否宣告-retreat-action)
  - [Q4 — Jumping Over a Gap 的 free movement 如何计算？](#q4--jumping-over-a-gap-的-free-movement-如何计算)
  - [Q5 — 射入混战时 1-3 误伤友军，能否选 LOS 外的友军？](#q5--射入混战时-1-3-误伤友军能否选-los-外的友军)
  - [Q6 — INJURY DICE / INJURY MODIFIER "for a model" 的方向](#q6--injury-dice--injury-modifier-for-a-model-的方向)
  - [Q7 — 模型能否穿过窗户或狭缝？](#q7--模型能否穿过窗户或狭缝)
  - [Q8 — 所有 ACTION 都要做 Success Roll 吗？](#q8--所有-action-都要做-success-roll-吗)
  - [Q9 — 非攻击来源的 Injury Roll 由谁掷骰、谁花标记？](#q9--非攻击来源的-injury-roll-由谁掷骰谁花标记)
  - [Q10 — 非 Injury Roll 来源的 Down 是否放 BLOOD MARKER？](#q10--非-injury-roll-来源的-down-是否放-blood-marker)
- [Keyword Questions](#keyword-questions)
  - [Q1 — 能否将 BLAST 目标点设在模型基座之下？](#q1--能否将-blast-目标点设在模型基座之下)
  - [Q2 — FIRETEAM 中先单独激活、再以小队激活第二个模型？](#q2--fireteam-中先单独激活再以小队激活第二个模型)
  - [Q3 — IGNORE ARMOUR / IGNORE (MODIFIER) 是否同时忽略其特殊规则？](#q3--ignore-armour--ignore-modifier-是否同时忽略其特殊规则)
  - [Q4 — PISTOL 关键词武器在近战时是否享有弹药效果？](#q4--pistol-关键词武器在近战时是否享有弹药效果)
  - [Q5 — TOUGH 与其他防 Down 规则的叠加顺序](#q5--tough-与其他防-down-规则的叠加顺序)
  - [Q6 — BLAST 半径从目标模型何处量？](#q6--blast-半径从目标模型何处量)
  - [Q7 — LOS 到点（point）的判定细节](#q7--los-到点point的判定细节)
  - [Q8 — 手雷扔到战壕沿或台阶时谁被波及？](#q8--手雷扔到战壕沿或台阶时谁被波及)
  - [Q9 — BLAST 经接触链是否波及更远模型？](#q9--blast-经接触链是否波及更远模型)
  - [Q10 — SKIRMISHER 移出 LOS 后仍可被 Charge 吗？](#q10--skirmisher-移出-los-后仍可被-charge-吗)
- [Battlekit Questions](#battlekit-questions)
  - [BK Q1 — Standard Battlekit / Glory Item 章节为何不列 stipulation？](#bk-q1--standard-battlekit--glory-item-章节为何不列-stipulation)
  - [BK Q2 — STRONG 模型能否将 Shovel 作单手近战武器？](#bk-q2--strong-模型能否将-shovel-作单手近战武器)
- [Starting A Warband Questions](#starting-a-warband-questions)
  - [SW Q1 — 跨派系采购是否携带原 stipulation？](#sw-q1--跨派系采购是否携带原-stipulation)
  - [SW Q2 — Pistol / Halberd-Gun 双类型武器是否双占名额？](#sw-q2--pistol--halberd-gun-双类型武器是否双占名额)
  - [SW Q3 — 持盾时能否同时携 1H 近战 + 1H 远程？](#sw-q3--持盾时能否同时携-1h-近战--1h-远程)
- [Faction Lists Questions](#faction-lists-questions)
  - [Trench Pilgrims Q1 — Broken on the Wheel 致死可否作 Martyr Penitent 复活？](#trench-pilgrims-q1--broken-on-the-wheel-致死可否作-martyr-penitent-复活)
  - [Heretic Legions Q1 — Knights of Avarice 的 Goetic Warlock 双重招募](#heretic-legions-q1--knights-of-avarice-的-goetic-warlock-双重招募)
  - [Heretic Legions Q2 — Death Commando 的 Stealth Generator 对 Blast 的效力](#heretic-legions-q2--death-commando-的-stealth-generator-对-blast-的效力)
  - [Black Grail Q1 — Lord of Tumours 无武器或持盾时能否 Crushing Blows？](#black-grail-q1--lord-of-tumours-无武器或持盾时能否-crushing-blows)
  - [The Court Q1 — Sorcerer 同激活中 Cast Spell + Shoot 两次远程攻击？](#the-court-q1--sorcerer-同激活中-cast-spell--shoot-两次远程攻击)
  - [The Court Q2 — Black Heart 一次激活内可多次使用吗？](#the-court-q2--black-heart-一次激活内可多次使用吗)
  - [The Court Q3 — Slavemaster 是否能命令敌方 Yoke Fiend 自杀？](#the-court-q3--slavemaster-是否能命令敌方-yoke-fiend-自杀)
- [Mercenary Questions](#mercenary-questions)
  - [Merc Q1 — Mercy Dog 能否拖动 Downed 模型？](#merc-q1--mercy-dog-能否拖动-downed-模型)
- [Campaign Questions](#campaign-questions)
  - [Camp Q1 — Promotion Roll / Promotion Dice 是否强制？](#camp-q1--promotion-roll--promotion-dice-是否强制)
  - [Camp Q2 — Gunslinger 与双自动手枪的攻击次数](#camp-q2--gunslinger-与双自动手枪的攻击次数)
  - [Camp Q3 — Trench Dog 是否计入 Maximum Field Strength？](#camp-q3--trench-dog-是否计入-maximum-field-strength)
  - [Camp Q4 — Skill 的 Limit 增益是否惠及 Variant Warband 模型？](#camp-q4--skill-的-limit-增益是否惠及-variant-warband-模型)
  - [Camp Q5 — Exploration & Looting 中两表选择的时点](#camp-q5--exploration--looting-中两表选择的时点)
  - [Camp Q6 — Gunslinger + 双 Pistol 中途换近战武器的 Off-Hand 处理](#camp-q6--gunslinger--双-pistol-中途换近战武器的-off-hand-处理)
  - [Camp Q7 — Point Blank Skill 适用哪些修正？](#camp-q7--point-blank-skill-适用哪些修正)
  - [Camp Q8 — Campaign Rules 中的 Glory Item 是否算 Battlekit？](#camp-q8--campaign-rules-中的-glory-item-是否算-battlekit)
  - [Camp Q9 — 费 ☼ 的 Armoury 物品在 Exploration Table 是否算 Glory Item？](#camp-q9--费--的-armoury-物品在-exploration-table-是否算-glory-item)
- [Scenarios Questions](#scenarios-questions)
  - [Scn Q1 — IGNORE LONG RANGE / IGNORE COVER 能完成 "Long Range + Cover" 的 Glorious Deed 吗？](#scn-q1--ignore-long-range--ignore-cover-能完成-long-range--cover-的-glorious-deed-吗)
  - [Scn Q2 — Armoured Train 的 King of the Hill 双方同时完成如何裁决？](#scn-q2--armoured-train-的-king-of-the-hill-双方同时完成如何裁决)
- [Miscellaneous Questions](#miscellaneous-questions)
  - [Misc Q1 — 30×60mm 等非正方基座如何应用 Base size 阈值？](#misc-q1--3060mm-等非正方基座如何应用-base-size-阈值)
  - [Misc Q2 — "Friendly models within X""是否包含自己？](#misc-q2--friendly-models-within-x是否包含自己)
  - [Misc Q3 — 模型上挂"装饰性 battlekit"如何裁决？](#misc-q3--模型上挂装饰性-battlekit如何裁决)
  - [Misc Q4 — Corrupt Merchants / Weapon Collections 能否买多份同款？](#misc-q4--corrupt-merchants--weapon-collections-能否买多份同款)
  - [Misc Q5 — 必须用 3'×3' 桌面吗？4'×4' 行不行？](#misc-q5--必须用-33-桌面吗44-行不行)
  - [Misc Q6 — Glory Items 能否在单场 one-off 中使用？](#misc-q6--glory-items-能否在单场-one-off-中使用)
  - [Misc Q7 — 模型对自己有 LOS 吗？](#misc-q7--模型对自己有-los-吗)

---

## 前言

> 以下 Rules Commentaries 回答关于规则的常见问题（即"frequently asked questions" / FAQ）。如果你对规则的预期运作方式有疑问，多半能在下文找到答案。若仍未解决，请将问题发送到 trenchcrusade.com/contact。若该问题尚未被回答，下次更新 Rules Commentaries 时将会补入。
>
> — Rules Commentaries v1.0.2，p.2

---

## Core & Comprehensive Rules

> 原条目所属：主规则书 Core Rules + Comprehensive Rules 章节
> → `rules/01-core-rules.md` · `rules/02-comprehensive-rules.md`

### Q1 — BLOOD 与 BLESSING MARKER 应用顺序

**RULES Q1**（PDF p.2，引主规则书 p.32）：当两位玩家要对同一次掷骰应用 `BLOOD MARKER` 与 `BLESSING MARKER` 时，先后顺序如何确定？

**A**：如果两件事同时发生，则由持有 **Initiative**（先手 / 主动权）的玩家决定它们的执行顺序。（参见 Trench Crusade Digital Rulebook 第 32 页。）

→ `rules/02-comprehensive-rules.md#initiative` · `rules/02-comprehensive-rules.md#blood-marker` · `rules/02-comprehensive-rules.md#blessing-marker`（占位，Pass 3 待写）

---

### Q2 — Move / Charge / Retreat 是同一种 ACTION 吗？

**RULES Q2**（PDF p.2）："Move 或 Charge 或 Retreat" 算单一 ACTION，还是各自不同的 ACTION 类型（Move ACTION / Charge ACTION / Retreat ACTION）？若是后者，同一次激活中模型能否取其中两个？

**A**：它们是不同类型的 ACTION：一个 Move ACTION、一个 Charge ACTION、一个 Retreat ACTION。**然而，模型在同一次 Activation 中不能取其中超过一个**。如果你想让模型移动两次以上，必须改用 Dash ACTION。

→ `rules/02-comprehensive-rules.md#movement-actions`（占位，Pass 3）

---

### Q3 — 无法移动的模型能否宣告 Retreat ACTION？

**RULES Q3**（PDF p.2）：模型即便无法移动，是否仍可宣告 Retreat ACTION？

**A**：可以。然而，**即便模型无法移动，它仍如同已 Retreat 一样会受到攻击**（除非另有说明）。

→ `rules/02-comprehensive-rules.md#retreat-action`（占位）

---

### Q4 — Jumping Over a Gap 的 free movement 如何计算？

**RULES Q4**（PDF p.2）：跳越缝隙（Jumping Over a Gap）后被放到对岸的处理是怎样的？Movement Characteristic 为 6" 的模型能否先移动 3"，再跳 3"？

**A**：任何为将模型放到缝隙另一侧所需的移动都视为"**free** movement"（自由移动），**只要"到缝隙前的移动 + 缝隙本身的距离"之和 ≤ 模型的 Movement Characteristic**。例如：Movement Characteristic 为 6" 的模型可以先移动 3" 再跳 3"，把模型与其基座放到对岸所需的额外移动是"free"的。

→ `rules/02-comprehensive-rules.md#jumping-over-a-gap`（占位）

---

### Q5 — 射入混战时 1-3 误伤友军，能否选 LOS 外的友军？

**RULES Q5**（PDF p.2）：当我射入一场含多个友方模型的混战，并掷出 1-3 致使必须以友军为目标时，能否挑选该混战中、但**不在射击模型 Line of Sight 内**的友军？

**A**：不能。**你只能挑选可作为该攻击模型目标的友军**——即对攻击模型可见、且在所用武器射程内的友军。如果没有这样的友军，攻击作废。

→ `rules/02-comprehensive-rules.md#shooting-into-combat` · LOS 判定见 `matches/coordinate-system.md` §6

---

### Q6 — INJURY DICE / INJURY MODIFIER "for a model" 的方向

**RULES Q6**（PDF p.2）：有时能力或特殊规则会说 INJURY DICE 或 INJURY MODIFIER "for a model" 适用。例如 Lion of Jabir 的 *Artificial Life* 写："Add -1 INJURY DICE to Injury Rolls for a Lion of Jabir"。该修正是适用于**对该模型**做的 Injury Roll，还是适用于**该模型发动攻击导致**的 Injury Roll？

**A**：适用于**对该模型**做的 Injury Roll。**不**适用于该模型发动的攻击所产生的 Injury Roll。

→ `rules/02-comprehensive-rules.md#injury-roll` · `rules/03-keywords-glossary.md`（INJURY DICE / INJURY MODIFIER 词条，占位）

---

### Q7 — 模型能否穿过窗户或狭缝？

**RULES Q7**（PDF p.3）：模型能否穿越建筑窗户或一般狭缝？

**A**：模型**不能**穿越任何小于其基座尺寸的空间（如窗户、走廊、地形件之间的缝）。如果模型基座两维不等（如 30mm × 60mm），判定能否穿越某空间时**取较小一维**。

→ `matches/coordinate-system.md` §5（base size）· `rules/04-battlefield-terrain.md`（占位，Pass 5）

---

### Q8 — 所有 ACTION 都要做 Success Roll 吗？

**RULES Q8**（PDF p.3）：所有 ACTION 都要做 Success Roll 或 Risky Success Roll 吗？

**A**：不是。**需要 Success Roll 的 ACTION 在该 ACTION 的规则正文中明确说明**（如果是 Dash / Shoot / Fight 等通用 ACTION，则在 Comprehensive Rules 段说明）。

→ `rules/02-comprehensive-rules.md#success-rolls`（占位）

---

### Q9 — 非攻击来源的 Injury Roll 由谁掷骰、谁花标记？

**RULES Q9**（PDF p.3）：当模型因非攻击来源（如某些异能效果）承受 Injury Roll 时，由谁掷骰，又由谁花 `BLOOD` / `BLESSING MARKER`？

**A**：**你始终为敌方模型掷 Injury Roll，并花掉敌方模型身上的 BLOOD / INFECTION MARKER，以及花掉友方模型身上的 BLESSING MARKER**。同样地，对手始终为你的模型掷 Injury Roll，花你模型身上的 BLOOD / INFECTION MARKER，并花他自己模型上的 BLESSING MARKER。

→ `rules/02-comprehensive-rules.md#injury-roll`（占位）· `rules/03-keywords-glossary.md` 中 `INFECTION MARKER` 词条

---

### Q10 — 非 Injury Roll 来源的 Down 是否放 BLOOD MARKER？

**RULES Q10**（PDF p.3）：以非 Injury Roll 之外的方式被打 Down 的模型（如 Eire Trench Cleric 的 *Away, Serpents!* 异能），是否在其旁边放置 `BLOOD MARKER`？

**A**：是。"**被打 Down**（taken Down）"与"受到 Injury Table 的 Down 结果"是同义的。

→ `rules/02-comprehensive-rules.md#injury-results-down`（占位）

---

## Keyword Questions

> 原条目所属：主规则书 Keywords / Glossary 章节
> → `rules/03-keywords-glossary.md`

### Q1 — 能否将 BLAST 目标点设在模型基座之下？

**KEYWORDS Q1**（PDF p.3）：能否用 `BLAST` 武器以某模型基座下方的点作为目标？

**A**：不能。**你只能以战场上、攻击模型 Line of Sight 内**的点作为目标——而到模型基座下方地面的 LoS 被该模型的基座阻挡。

→ `rules/03-keywords-glossary.md#blast` · LOS 判定见 `matches/coordinate-system.md` §6

---

### Q2 — FIRETEAM 中先单独激活、再以小队激活第二个模型？

**KEYWORDS Q2**（PDF p.3）：如果我把 `FIRETEAM` 中的一个模型作为个体激活，能否随后在该回合内将第二个模型作为 `FIRETEAM` 激活——从而让先激活的那个模型获得第二次激活？

**A**：不能。

→ `rules/03-keywords-glossary.md#fireteam`

---

### Q3 — IGNORE ARMOUR / IGNORE (MODIFIER) 是否同时忽略其特殊规则？

**KEYWORDS Q3**（PDF p.3）：`IGNORE ARMOUR` 或 `IGNORE (MODIFIER)` 一类的关键词，是否也会忽略该 Armour 或该修正来源所授予的**特殊规则或异能**？

**A**：不会。

→ `rules/03-keywords-glossary.md#ignore-armour` · `rules/03-keywords-glossary.md#ignore-modifier`

---

### Q4 — PISTOL 关键词武器在近战时是否享有弹药效果？

**KEYWORDS Q4**（PDF p.3）：带 `PISTOL` 关键词的武器若加装了弹药效果（如 Incendiary Ammunition、Armour-Piercing Bullets 等），在近战中使用时是否享有该弹药的加成？

**A**：是。

→ `rules/03-keywords-glossary.md#pistol` · `rules/05-battlekit.md`（弹药条目，占位 Pass 6）

---

### Q5 — TOUGH 与其他防 Down 规则的叠加顺序

**KEYWORDS Q5**（PDF p.4）：`TOUGH` 关键词与其他"防止模型被打 Down"的规则如何交互？

**A**：**按字面顺序、逐条依次套用**（rules as written, applied one after the other in the order they occur）。例：拥有 `TOUGH` 关键词、身穿 Machine Armour 的 Lieutenant 在本场中**第一次**被 Out of Action：

1. `TOUGH` 将首次的 Out of Action 结果改写为 **Down** 结果。
2. Machine Armour 的 **Standfast** 规则又将 Down 结果改写为 **Minor Wound** 结果。
3. 因此该 Lieutenant 既不出局也不倒下，而是 Minor Wound。
4. **再次**被 Out of Action 时，因 `TOUGH` 仅改写首次 Injury 结果，模型即被 Out of Action。

→ `rules/03-keywords-glossary.md#tough` · `rules/05-battlekit.md`（Machine Armour / Standfast，占位）

---

### Q6 — BLAST 半径从目标模型何处量？

**KEYWORDS Q6**（PDF p.4）：用 `BLAST` 关键词武器以敌方模型为目标时，blast radius 在目标模型上从何处测量？

**A**：从**模型基座的中心**测量。注意：若攻击发生 scatter 并最终落在另一模型的基座上，此时 blast radius 从**攻击 scatter 到的那个新模型基座上的具体落点**测量（**不是**该新模型基座的中心）。

→ `rules/03-keywords-glossary.md#blast` · `rules/03-keywords-glossary.md#scatter`

---

### Q7 — LOS 到点（point）的判定细节

**KEYWORDS Q7**（PDF p.4）：当我检测对战场上某点或某地形件上某点的 Line of Sight 时，能看到该 1mm × 1mm 点的**任何部分**即算 LOS，还是必须看到点的**中心**？该点的高度算多少？

**A**：**能看到该点的任何部分**即算 LOS。**该点视作 1mm 高**。

→ `matches/coordinate-system.md` §6（LOS 判定）

---

### Q8 — 手雷扔到战壕沿或台阶时谁被波及？

**KEYWORDS Q8**（PDF p.4）：若我把手雷扔到战壕的沿口（lip）或台阶（ledge）上，爆炸是否会击中**位于战壕内或台阶下方**的模型？

**A**：**会击中"对目标点拥有 Line of Sight、且基座位于该手雷 blast radius 内"的任何模型**。在 PDF p.4 所附示例图中：模型 A 会被手雷击中，**模型 B 不会**——因其基座不在攻击的 blast radius 之内。

→ `rules/03-keywords-glossary.md#blast` · `matches/coordinate-system.md` §6 · 战壕地形见 `matches/coordinate-system.md` §7.3 A（Trench）

---

### Q9 — BLAST 经接触链是否波及更远模型？

**KEYWORDS Q9**（PDF p.4）：模型 A 同时与敌方模型 X 和 Y 接触。敌方模型 X 被 `BLAST` 命中，A 和 Y 不在该攻击的 blast radius 内。我知道 A 会被攻击命中——因为 A 与 B 接触\*——但 Y 是否也因与 A 接触而被命中？
<sup>*PDF 原文如此（应为 "with model X"，疑为笔误，但官方文本未更正）</sup>

**A**：不会。

→ `rules/03-keywords-glossary.md#blast`

---

### Q10 — SKIRMISHER 移出 LOS 后仍可被 Charge 吗？

**KEYWORDS Q10**（PDF p.4）：如果带 `SKIRMISHER` 关键词的模型移出了冲锋模型的 Line of Sight，我是否仍能 Charge 它？

**A**：可以。

→ `rules/03-keywords-glossary.md#skirmisher` · `rules/02-comprehensive-rules.md#charge-action`

---

## Battlekit Questions

> 原条目所属：主规则书 Battlekit 章节
> → `rules/05-battlekit.md`

### BK Q1 — Standard Battlekit / Glory Item 章节为何不列 stipulation？

**BATTLEKIT Q1**（PDF p.5）：为什么 Standard Battlekit 和 Glory Item 章节的 battlekit 条目里没列 stipulation（如 Bayonet Lug、Shield-Combo 等），而当它们出现在 Faction Lists 中时却有？这是失误吗？

**A**：不是。Standard Battlekit 和 Glory Item 章节中的 battlekit 可被多个 Warband 使用，**且不同 Warband 的 stipulation 可能不同**。因此，规则书的 Standard Battlekit 和 Glory Item 两章**故意不列 stipulation**。例：New Antioch 部队精修刺刀战术，其 Shotgun 享有 Bayonet Lug stipulation；而 The Court of the Seven-Headed Serpent 不屑于刺刀那等凡俗手段、偏好更奥术或残忍的近战武器，其 Shotgun 即**不**带 Bayonet Lug stipulation。

→ `rules/05-battlekit.md`（Standard Battlekit 与 Glory Item 章节说明，占位）· `warbands/01-new-antioch.md`（Pass 8）

---

### BK Q2 — STRONG 模型能否将 Shovel 作单手近战武器？

**BATTLEKIT Q2**（PDF p.5）：拥有 `STRONG` 关键词的模型能否将 Shovel 当 1-Handed Melee Weapon 使用？

**A**：可以。

→ `rules/03-keywords-glossary.md#strong` · `rules/05-battlekit.md`（Shovel 条目）

---

## Starting A Warband Questions

> 原条目所属：主规则书 Starting A Warband 章节（战团构建）
> → `matches/roster-template.md`（Pass 13）· `rules/05-battlekit.md`

### SW Q1 — 跨派系采购是否携带原 stipulation？

**STARTING A WARBAND Q1**（PDF p.5）：当我拥有"允许从其他派系 Armoury Table 采购 Battlekit"的特殊规则时，那些 battlekit 是否仍携带其他 Armoury Table 中列出的 stipulation（如 `ELITE only`、`Shield Combo`、`Limit: 1` 等）？

**A**：是。**从某 Armoury Table 采购的 Battlekit 始终带其列出的 stipulation**，除非另有说明。

→ `matches/roster-template.md`（Pass 13）

---

### SW Q2 — Pistol / Halberd-Gun 双类型武器是否双占名额？

**STARTING A WARBAND Q2**（PDF p.5）：像 Pistol 或 Halberd-Gun 这种双类型武器，是否同时占用 Ranged 与 Melee 名额？

**A**：不。**武器只占用其在 Armoury Table 上被采购的同类型名额**。例如：Pistol 算一把 1-handed Ranged Weapon；Halberd-Gun 算一把 2-Handed Melee Weapon。

→ `rules/05-battlekit.md`（Pistol / Halberd-Gun 条目）· `matches/roster-template.md`

---

### SW Q3 — 持盾时能否同时携 1H 近战 + 1H 远程？

**STARTING A WARBAND Q3**（PDF p.5）：如果我装备了 Shield，能否同时携带一把 1-Handed Melee Weapon **和**一把 1-Handed Ranged Weapon？

**A**：可以。

→ `rules/05-battlekit.md`（Shield-Combo / 装备槽规则）· `matches/roster-template.md`

---

## Faction Lists Questions

> 原条目所属：Warbands of Trench Crusade（各派系条目）
> → `warbands/*`

### Trench Pilgrims Q1 — Broken on the Wheel 致死可否作 Martyr Penitent 复活？

**TRENCH PILGRIMS Q1**（PDF p.5）：我能否将因 *Broken on the Wheel* 而死的 Trench Pilgrim 作为 Martyr Penitent 复活？

**A**：不能。**虽然其牺牲的事迹本身已是奖赏，但他们尚未赢得殉道之名**（they have not earned their martyrdom）。

→ `warbands/03-trench-pilgrims.md`（v0.2，暂未导入）

---

### Heretic Legions Q1 — Knights of Avarice 的 Goetic Warlock 双重招募

**HERETIC LEGIONS Q1**（PDF p.6）：Knights of Avarice Warband 允许以 👑 招募 Goetic Warlock Mercenary 的特殊规则，是否就阻止我以 ☼（Glory）再招募一名 Goetic Warlock 作为 Mercenary？

**A**：不阻止。**该规则的意义是：允许 Knights of Avarice Warband 拥有两名 Goetic Warlock**。

→ `warbands/02-heretic-legions.md`（Knights of Avarice 变体条目，Pass 9）

---

### Heretic Legions Q2 — Death Commando 的 Stealth Generator 对 Blast 的效力

**HERETIC LEGIONS Q2**（PDF p.6）：Death Commando 的 *Stealth Generator* 异能是否影响 Blast 攻击？

**A**：**仅在攻击直接以 Death Commando 为目标时生效**。对以地面某点为目标的 Blast 无效。

→ `warbands/02-heretic-legions.md`（Heretic Death Commando 条目，Pass 9）

---

### Black Grail Q1 — Lord of Tumours 无武器或持盾时能否 Crushing Blows？

**BLACK GRAIL Q1**（PDF p.6）：Lord of Tumours 在**没有 Melee Weapon** 和/或**持盾**时，能否做 *Crushing Blows* 攻击？

**A**：两种情形**均可**。

→ `warbands/04-black-grail.md`（v0.2，暂未导入）

---

### The Court Q1 — Sorcerer 同激活中 Cast Spell + Shoot 两次远程攻击？

**THE COURT Q1**（PDF p.6）：我的 Sorcerer 能否做 Cast Spell ACTION 来使用 *Burning Inferno* 远程攻击，再在同一次 Activation 中做 Shoot ACTION 做另一次远程攻击？

**A**：可以。**Ranged（和 Melee）Attack 不是 ACTION**——只有 ACTION 才被限定为"每次激活同类型仅一次"（除非另有说明）。

→ `rules/02-comprehensive-rules.md#actions-vs-attacks`（占位）· `warbands/05-court-of-seven-headed-serpent.md`（v0.2，暂未导入）

---

### The Court Q2 — Black Heart 一次激活内可多次使用吗？

**THE COURT Q2**（PDF p.6）：Greed 系 Goetic Power *Black Heart* 是否可在同一次 Activation 中多次使用？

**A**：不可——**同一次 Activation 中同一法术只能施展一次**。但你**可以**在自己 Activation 之外、每当你做 Success Roll 或 Risky Success Roll 时使用 *Black Heart*。

→ `warbands/05-court-of-seven-headed-serpent.md`（v0.2）

---

### The Court Q3 — Slavemaster 是否能命令敌方 Yoke Fiend 自杀？

**THE COURT Q3**（PDF p.6）：友方模型若拥有 *Slavemaster* 法术，能否用它对自己 18" 内的**敌方 Yoke Fiend** 下达 Carry out Commands？若可以，是否能用此机制以 *Sacrifice Command* 命令敌方 Yoke Fiend 自杀？

**A**：可以。

→ `warbands/05-court-of-seven-headed-serpent.md`（v0.2）

---

## Mercenary Questions

> 原条目所属：Warbands of Trench Crusade — Mercenaries 章节
> → `warbands/`（Mercenaries，v0.2）

### Merc Q1 — Mercy Dog 能否拖动 Downed 模型？

**MERCENARIES Q1**（PDF p.6）：Mercy Dog 能否拖动 Downed 模型？

**A**：可以。**规则明确指出 Mercy Dog 可以移动一个 Down 状态的模型**。

→ `warbands/`（Mercenaries — Mercy Dog 条目，v0.2 暂未导入）

---

## Campaign Questions

> 原条目所属：主规则书 Campaign Rules 章节（v0.2 暂未导入）
> → `rules/06-campaign-rules.md`（v0.2，占位）· `rules/07-glory-items.md`（v0.2，占位）

### Camp Q1 — Promotion Roll / Promotion Dice 是否强制？

**CAMPAIGNS Q1**（PDF p.6）：必须做 Promotion Roll 和 / 或分配 Promotion Dice 吗？

**A**：必须。**当你的 Patron 或 High Command 认定应当晋升你战团中的成员时，拒绝晋升将是不明智之举**。

→ `rules/06-campaign-rules.md#promotions`（占位）

---

### Camp Q2 — Gunslinger 与双自动手枪的攻击次数

**CAMPAIGNS Q2**（PDF p.7）：Campaign Rules 之 Ranged Skills 表中的 *Gunslinger* 技能，是否允许携带一对自动手枪的模型用每把手枪各做两次攻击？

**A**：是。**先用第一把手枪依其 `AUTOMATIC 2` 关键词连续做两次攻击；再用 *Gunslinger* 技能让第二把手枪也连续做两次攻击**。

→ `rules/06-campaign-rules.md#gunslinger`（占位）· `rules/03-keywords-glossary.md#automatic`

---

### Camp Q3 — Trench Dog 是否计入 Maximum Field Strength？

**CAMPAIGNS Q3**（PDF p.7）：Trench Dog 是否计入战团的 Maximum Field Strength？

**A**：是。**它仅在 Morale Check 判定中不计为战团内的模型**。

→ `rules/06-campaign-rules.md#field-strength` · `rules/02-comprehensive-rules.md#morale-phase`

---

### Camp Q4 — Skill 的 Limit 增益是否惠及 Variant Warband 模型？

**CAMPAIGNS Q4**（PDF p.7）：那些"提升战团内某些模型可携之物 Limit"的 Skill（如 Logistical Skills、Sultan's Favour），是否也适用于 Variant Warband（如 Expeditionary Forces of Abyssinia 中的 Holy Warriors）的相应模型？

**A**：是。

→ `rules/06-campaign-rules.md#skills`（占位）

---

### Camp Q5 — Exploration & Looting 中两表选择的时点

**CAMPAIGNS Q5**（PDF p.7）：当 Warband 在 Exploration & Looting Step 中可在两张不同 Exploration Table 间选择时，是在掷骰**之前**还是**之后**选？

**A**：**之前**。

→ `rules/06-campaign-rules.md#exploration-and-looting`（占位）

---

### Camp Q6 — Gunslinger + 双 Pistol 中途换近战武器的 Off-Hand 处理

**CAMPAIGNS Q6**（PDF p.7）：拥有 *Gunslinger* Skill 与两把 Pistol 的模型，在做 Fight ACTION 时能否把其中一把 Pistol 换成一把近战武器？若可以，且第二次近战攻击是用 Pistol 做的，那次攻击是否享有 `IGNORE OFF-HAND WEAPON` 关键词？

**A**：两个问题**均为是**。

→ `rules/06-campaign-rules.md#gunslinger` · `rules/03-keywords-glossary.md#ignore-off-hand-weapon`（占位）

---

### Camp Q7 — Point Blank Skill 适用哪些修正？

**CAMPAIGNS Q7**（PDF p.7）：用 *Point Blank* Skill 做出的攻击适用哪些修正？

**A**：**适用 Melee Attack 的修正**。

→ `rules/06-campaign-rules.md#point-blank`（占位）

---

### Camp Q8 — Campaign Rules 中的 Glory Item 是否算 Battlekit？

**CAMPAIGNS Q8**（PDF p.7）：Campaign Rules 章节里的 Glory Item 是否视为 Battlekit？

**A**：是。

→ `rules/07-glory-items.md`（v0.2，占位）· `rules/05-battlekit.md`

---

### Camp Q9 — 费 ☼ 的 Armoury 物品在 Exploration Table 是否算 Glory Item？

**CAMPAIGNS Q9**（PDF p.7）：那些"在 Faction List Armoury Table 中花费 Glory Points 购买"的 battlekit，或 Variant Warband 特殊规则中以 ☼ 购买的物品（如 Troop Flag、Field Shrine），在 Exploration Table 判定时是否算 Glory Item？

**A**：不算。

→ `rules/07-glory-items.md`（v0.2，占位）

---

## Scenarios Questions

> 原条目所属：主规则书 Scenarios 章节
> → `rules/08-scenarios.md`

### Scn Q1 — IGNORE LONG RANGE / IGNORE COVER 能完成 "Long Range + Cover" 的 Glorious Deed 吗？

**SCENARIOS Q1**（PDF p.7）：有些 Glorious Deed 要求"以使用了 Long Range 修正与 Cover 修正的 Ranged Attack 将敌人打成 Out of Action"。如果该攻击带 `IGNORE LONG RANGE` 或 `IGNORE COVER` 关键词，**还能**完成这些事迹吗？

**A**：不能。

→ `rules/08-scenarios.md`（Glorious Deeds 通用条款，Pass 12）· `rules/03-keywords-glossary.md#ignore-long-range` · `rules/03-keywords-glossary.md#ignore-cover`

---

### Scn Q2 — Armoured Train 的 King of the Hill 双方同时完成如何裁决？

**SCENARIOS Q2**（PDF p.7）：在 Armoured Train 剧本中，双方有可能**同时**完成 *King of the Hill* Glorious Deed。如何裁决？

**A**：**持 Initiative 的玩家决定谁先完成该事迹**（参见 Digital Rulebook 第 32 页的方框栏）。

→ `rules/08-scenarios.md`（Armoured Train，v0.2.D 暂未导入）· 参见本文件 [Core Rules Q1](#q1--blood-与-blessing-marker-应用顺序)（同时发生事件的通用裁决）

---

## Miscellaneous Questions

> 原条目所属：主规则书各处零散裁决
> → 见各条 → 跨文件引用

### Misc Q1 — 30×60mm 等非正方基座如何应用 Base size 阈值？

**MISC. Q1**（PDF p.8）：有些模型基座为 30 × 60mm。对那些"按 Base size 给予不同效果"（如小于 / 大于 40mm）的规则该如何处理？

**A**：**基座两维不等的模型（如 30 × 60mm），在所有引用 Base size 的规则中按其较大一维（如 60mm）处理**。

→ `matches/coordinate-system.md` §5（base size）· 对比 Core Rules [Q7](#q7--模型能否穿过窗户或狭缝)（穿越狭缝按**较小**一维——两条规则方向相反，按字面应用）

---

### Misc Q2 — "Friendly models within X""是否包含自己？

**MISC. Q2**（PDF p.8）：当一条规则影响"友方模型在 X" 之内"，是否也影响**拥有该规则的模型自己**？例如：Musical Instrument 的拥有者本人能否享其效果？

**A**：是。**模型视作位于自己 0" 之内**——除非另有说明。

→ `rules/02-comprehensive-rules.md#within-x-inches`（占位）

---

### Misc Q3 — 模型上挂"装饰性 battlekit"如何裁决？

**MISC. Q3**（PDF p.8）：我有些模型出于造型理由佩戴了规则不允许它使用的 battlekit——比如某模型背着一把步枪、单手握一把手枪、另一手握战壕棒。按规则字面，该模型不能使用（因为同时有 2-Handed Ranged Weapon 与 1-Handed Ranged Weapon）。如果游戏中**不**使用那把步枪，可以上场吗？若可以，是否仍需为步枪付 ducats？

**A**：**完全可以——此时 rule of cool 优先**。任何额外的 battlekit 视为**纯装饰**：你不能使用它，也不用付 ducats，且**在测量到 / 自该模型的射程或 Line of Sight 时也忽略它**。但是，**如果你这样用一个模型，必须在双方部署之前向对手说明哪些 battlekit 是装饰性的**。

→ `matches/roster-template.md`（Pass 13）· LOS / 测量见 `matches/coordinate-system.md` §3, §6

---

### Misc Q4 — Corrupt Merchants / Weapon Collections 能否买多份同款？

**MISC. Q4**（PDF p.8）：*Corrupt Merchants* 与 *Weapon Collections* 特殊规则是只允许买一份所选 battlekit，还是可以买多份同款？

**A**：**每款只能买一份**。

→ `rules/06-campaign-rules.md`（v0.2，占位）

---

### Misc Q5 — 必须用 3'×3' 桌面吗？4'×4' 行不行？

**MISC. Q5**（PDF p.8）：有人告诉我剧本必须在 3' × 3' 桌面上进行。这是不是说我自制的 4' × 4' 桌面不能用？

**A**：**不必担心**。Trench Crusade Rulebook 中的**所有剧本都能在 4' × 4' 桌面上进行**。剧本被设计为**几乎所有都可在至少 30" 跨度的台面上进行**；少数剧本需要更大区域，需要时会在剧本说明中明确指出。因此你可以使用任意尺寸的桌面，**只要其最窄一边 ≥ 30"** —— 4' × 4'、6' × 4'、甚至 10' × 5' 都可以。

→ `matches/coordinate-system.md` §4（战场默认；项目内 36×36 格 = 36" 已 ≥ 30"）· `rules/08-scenarios.md`（Pass 12）

---

### Misc Q6 — Glory Items 能否在单场 one-off 中使用？

**MISC. Q6**（PDF p.8）：能否在单场 one-off 比赛中使用 Campaign Rules 中的 Glory Items？

**A**：**按规则字面**，Glory Items 仅可在 campaign 中获取（参见 Digital Rulebook 的 Glory Items 条）。然而，**只要你和对手都同意，在 one-off 中使用任何 Glory Items 都没问题**。只要桌上各方达成一致，Trench Crusade 没有"错的玩法"。

→ `rules/07-glory-items.md`（v0.2，占位）

---

### Misc Q7 — 模型对自己有 LOS 吗？

**MISC. Q7**（PDF p.8）：模型对自己有 Line of Sight 吗？

**A**：有。

→ `matches/coordinate-system.md` §6（LOS 判定）

---

## 附录：跨文件回引索引

本文件提及但 v0.1 暂未完成的目标文件，统一占位。其他 Pass 完成后可按此清单回填反向引用。

| 跨引目标 | 状态 | 涉及本文件条目 |
|---|---|---|
| `rules/01-core-rules.md` | Pass 2 | 整章 Core Rules Q1-Q10 |
| `rules/02-comprehensive-rules.md` | Pass 3 | Core Rules Q1-Q10、Camp Q3、Misc Q2 |
| `rules/03-keywords-glossary.md` | Pass 4 | Keywords Q1-Q10、BK Q2、Camp Q2/Q6、Scn Q1 |
| `rules/04-battlefield-terrain.md` | Pass 5 | Core Rules Q7 |
| `rules/05-battlekit.md` | Pass 6 | BK Q1-Q2、SW Q1-Q3、Keywords Q4（弹药）、Camp Q8 |
| `rules/06-campaign-rules.md` | v0.2 | Camp Q1-Q9（除 Q8 → Glory Items）、Misc Q4 |
| `rules/07-glory-items.md` | v0.2 | Camp Q8-Q9、Misc Q6 |
| `rules/08-scenarios.md` | Pass 12 | Scn Q1-Q2、Misc Q5 |
| `warbands/01-new-antioch.md` | Pass 8 | BK Q1（New Antioch Shotgun 例） |
| `warbands/02-heretic-legions.md` | Pass 9 | Heretic Legions Q1-Q2 |
| `warbands/03-trench-pilgrims.md` | v0.2 | Trench Pilgrims Q1 |
| `warbands/04-black-grail.md` | v0.2 | Black Grail Q1 |
| `warbands/05-court-of-seven-headed-serpent.md` | v0.2 | The Court Q1-Q3 |
| `warbands/` Mercenaries | v0.2 | Merc Q1、Heretic Legions Q1（Goetic Warlock 雇佣） |
| `matches/coordinate-system.md` | Pass 1（完成） | Core Rules Q5/Q7、Keywords Q1/Q7/Q8、Misc Q1/Q5/Q7、Misc Q3 |
| `matches/roster-template.md` | Pass 13 | SW Q1-Q3、Misc Q3 |
