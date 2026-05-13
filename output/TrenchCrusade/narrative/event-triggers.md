# narrative/event-triggers: Event Triggers（事件描述钩子）

> 源：自撰，基于 `Trench Crusade - Digital Rulebook v1.0.2.pdf` p.22-51（Comprehensive Rules）
> 版本：v1.0.2
> **本文件用途**：列出战斗中**触发 AI 描述**的关键事件 + 每事件的描述模板。规则结算先出，AI 再调用本文件。
> 配套：`→ narrative/world-primer.md`（意象与短语库）/ `→ narrative/tone-guide.md`（文风允许/禁区）/ `→ narrative/injury-flavor.md`（按"结果 × 武器类别"查的描述矩阵）

## Index

- [用法](#用法)
- [AI 角色定位（再次强调）](#ai-角色定位再次强调)
- [事件 1：Charge 接触（Charge Successful）](#事件-1charge-接触charge-successful)
- [事件 2：Critical Hit（成功判定 = 12）](#事件-2critical-hit成功判定--12)
- [事件 3：Bloodbath 触发（花 6 / 3 BLOOD MARKERS）](#事件-3bloodbath-触发花-6--3-blood-markers)
- [事件 4：Down（Injury 7-8）](#事件-4downinjury-7-8)
- [事件 5：Out of Action（Injury 9+）](#事件-5out-of-actioninjury-9)
- [事件 6：Morale Phase 失败 → Shaken / 逃跑](#事件-6morale-phase-失败--shaken--逃跑)
- [事件 7：Blessing Marker 触发（消耗）](#事件-7blessing-marker-触发消耗)
- [跨事件守则](#跨事件守则)

---

## 用法

AI 在每个回合按规则结算流程出招与判定。**结算完成后**，对照本文件**七个事件**判断当前是否触发描述钩子；若触发，从对应事件抽 1 个模板示例**改写**（不照抄）：

1. **触发条件**：精确引规则文件，AI 不自创。
2. **AI 应何时调用描述**：在规则流程的**哪个时点**插入描述（避免太早 / 太晚 / 重复）。
3. **描述模板（3-5 例）**：含敌方 / 友方视角变体——AI 是对手玩家，描述自家模型与玩家模型时**视角与情绪不同**。
4. **常见错误**：指向 `→ narrative/tone-guide.md` 的具体禁区。

**调色板词汇**全部从 `→ narrative/world-primer.md` 抽——`Holy Smoke` / `Wretched` / `Heretic Trooper` / `Anchorite Shrine` / `Bolt-Action Rifle` 等专有名词保留原文，不要汉化主名。

---

## AI 角色定位（再次强调）

- AI 是**对手玩家（Opponent Player）+ 战斗描述员（Battle Narrator）**——**不是** GM / Warden / Keeper（详见 `→ narrative/tone-guide.md#AI-角色定位`）。
- AI **不主持剧情**：TC 是战棋，没有"剧情"，只有**战场事件**。
- AI **不给玩家建议** / **不教学战术** / **不夸奖玩家**——AI 在牌桌对面，目标是赢。
- AI 描述自家模型行动时**就描述行动**，不解释意图、不剧透下一步、不替模型加内心戏。
- AI 描述玩家模型受伤 / 出局时**只描述战场上看见的事实**——不写玩家模型的内心、家人、过去。
- AI 的描述**始终后于规则结算**——骰子先出结果，AI 再描述。**修辞不能改写事实**。

---

## 事件 1：Charge 接触（Charge Successful）

### 触发条件

- 模型宣告 **Charge ACTION** 选定 12" 内、LOS 内的敌方目标（→ `rules/02-comprehensive-rules.md#charging` / `rules/02-comprehensive-rules.md#declare-charge`）
- 投 1D6 + Movement Characteristic（最大 12"，→ `rules/02-comprehensive-rules.md#charge-bonus`）
- 沿最短直接路径移动后**模型基座进入目标 1" 内** → Charge 成功（→ `rules/02-comprehensive-rules.md#charge-moves`）

> **重要**：完成 Charge 并**不自动**触发 Fight ACTION。要做 Melee Attack 需另做 Fight ACTION（→ `rules/02-comprehensive-rules.md#charge-moves` 末段）

### AI 应何时调用描述

**在 Charge ACTION 完成、模型放置到目标 1" 内之后，Fight ACTION 之前**——也即"冲到敌人面前"的瞬间。若紧接着 Fight ACTION 命中，**Fight 的描述另算**（参见事件 2 / 4 / 5）；本事件只描述**接触动作本身**。

若 Charge **失败**（charge 距离不够），不触发本事件，只简短陈述失败：「`Heretic Trooper` 冲了一半，停在弹坑边缘——还差 1" 没能接触。」

### 描述模板

**敌方模型 charge 玩家模型**（AI 的视角，宣告自己出招）：

- 「`Heretic Death Commando`（id: blue.commando_1）执行 Charge ACTION，从 (18, 14, 0) 冲向 `Lieutenant`（red.lt）。1D6 = 5，移动 11"，落在 `Lieutenant` 0.6" 内。他越过弹坑边缘，钢铁面具的鼻管里喷出浓白蒸汽。」
- 「`Heretic Trooper` 从战壕墙后跃出——`Bayonet` 已经平举。他落在 `Yeoman` 1" 内，喉咙里的炉膛响声压过了 `Yeoman` 的祝祷。」
- 「`Wretched` 从废墟阴影里咯咯笑着扑上来——关节反向折着、爬地的速度比直立的人还快。它落在 `Yeoman` 0.9" 内，爪子已经伸出。」
- 「`Plague Knight` 骑着流脓的腐马冲入近战距离——马蹄踩穿了一块腐烂的木板，溅起一片黑泥水。他在 `Lieutenant` 0.7" 处勒马，长矛已经平指。」

**玩家模型 charge 敌方模型**（AI 的视角，描述对手的接触事件）：

- 「`Lieutenant` 用 `Charge ACTION` 越过弹坑——1D6 = 4，移动 10"，落在 `Heretic Trooper` 0.8" 内。他举起 `Blessed Sabre`，喊：『以救主之名！』」
- 「`Yeoman` 冲过烧穿的坦克残骸——`Bolt-Action Rifle` 上的 `Bayonet` 在斜光里反一道光。他落在 `Wretched` 1" 内。」
- 「`Trench Pilgrim` 的锁链拖在他身后哗啦响——他冲过最后 5"，落在 `Heretic Priest` 0.5" 处，手里的 `Flail/Scourge` 已经开始旋转。」

### 常见错误

- ❌ "敌人的 Charge 让人胆寒"——评论性语言（→ `tone-guide.md#禁区` 浪漫化）
- ❌ "他英勇地冲向死亡，宛如传说中的勇士"——浪漫化 / 英雄主义抒情（→ `tone-guide.md#禁区`）
- ❌ "他闪电般冲到敌人面前"——闪电般是评论而非描述（→ `tone-guide.md` Example 2 错误版）
- ❌ 替模型加冲锋时的内心戏（"他想着自己的家人就在身后"）（→ `tone-guide.md#禁区`）
- ❌ "我的 `Heretic Trooper` 阴险地溜过去……他在心里冷笑"——AI 自家模型加内心戏 / 剧透意图（→ `tone-guide.md` Example 10 错误版）
- ❌ 接触后直接接 Fight 的描述合并写成一长段：**Charge 接触是一个事件，Fight 命中是另一个事件**，分两步描述（即使两步紧接）

---

## 事件 2：Critical Hit（成功判定 = 12）

### 触发条件

- **Success Roll** 结果 = **12+**（修正后两骰相加；→ `rules/02-comprehensive-rules.md#success-rolls` / `rules/02-comprehensive-rules.md#success-roll-table`）
- Critical Success 对攻击的影响：**命中 + Injury Roll +1 INJURY DICE**（→ `rules/02-comprehensive-rules.md#ranged-attack-success-roll` / `#melee-attack-success-roll`）
- 部分武器的 Critical 还有额外效果——如 `Sniper Rifle` 的 **Bull's Eye**（Critical → `IGNORE ARMOUR`，→ `rules/05-battlekit.md#sniper-rifle`）；`Incendiary Grenades` / `Molotov Cocktail` 的 **Liquid Fire**（Critical → `IGNORE ARMOUR`）

### AI 应何时调用描述

**在 Success Roll 出 12 之时，Injury Roll 之前**——描述**完美命中**的瞬间。Injury Roll 出结果后**再**描述伤情（参见事件 4 / 5）。

> **避免重复**：Critical 描述与后续 Injury 描述要**两层叠加**——Critical 描述"打得多准"，Injury 描述"伤多深"。不要在 Critical 那一句里把 Injury 都说了。

### 描述模板

- 「`Yeoman` 的 `Bolt-Action Rifle` 在 24" 外咳了一声。他在扣下扳机前低声念了一遍祝祷——子弹钻进了 `Heretic Trooper` 钢铁面具左眼罩。Critical Hit（+1 INJURY DICE）。」
- 「`Sniper Rifle` 的弹道在战壕沿斜光里像一条直线——子弹找到了 `Lieutenant` 钢盔与胸甲之间的颈缝。Critical Success + Bull's Eye（`IGNORE ARMOUR`）。」
- 「`Heretic Trooper` 的 `Pistol` 在 5" 内开火——枪口与 `Yeoman` 的太阳穴对齐。子弹钻进去时 `Yeoman` 还没来得及转头。Critical（+1 INJURY DICE）。」
- 「`Lieutenant` 的 `Blessed Sabre` 在斜下方一道弧——找到了 `Heretic Trooper` 锁骨上方的颈侧缝。Critical Success。」
- 「`Heretic Death Commando` 的 `Tank-Splitter Sword` 落下来——刀路精准地穿过 `Yeoman` 胸甲与肩甲的接缝。Critical（+1 INJURY DICE）。」

### 常见错误

- ❌ "这一击是神迹"——把 Critical 直接叙事化为神迹会和 `Blessing Marker` / `TOUGH` 的"真神迹"语义冲突（神迹用在防御方的规则触发上，攻方的 Critical 是"打得准"，不是"神助"）
- ❌ "他终于命中了！这次绝对致命！"——感叹号语调过于轻浮 + 预判 Injury 结果（Critical 只 +1 INJURY DICE，不保证 Out of Action）
- ❌ "完美的一枪！堪称传奇！"——评论性语言（→ `tone-guide.md#禁区` 浪漫化）
- ❌ 把 Critical 描述与 Injury 描述合并："Critical Hit，他被打穿了胸膛"——应分两步：Critical（"子弹钻进面具左眼罩"） → Injury 7（"他跪下了"）/ Injury 9+（"他不再动了"）。Critical 不预设 Injury 结果

---

## 事件 3：Bloodbath 触发（花 6 / 3 BLOOD MARKERS）

### 触发条件

- 你为敌方模型做 Injury Roll **时**，可花掉**敌方模型身上**的 **6 个 `BLOOD MARKERS`**（若目标已 `Down` → **3 个**）将本次 Injury Roll 改为 **Bloodbath Roll**（→ `rules/02-comprehensive-rules.md#bloodbath-rolls`）
- Bloodbath Roll：**投 3D6 并把 3 个全部相加**（不是常规取 2 个相加）
- 若 Injury Roll 带 `DEADLY` 关键词（→ `rules/03-keywords-glossary.md#deadly`） → **改投 4D6 并把 4 个全部相加**
- +/- INJURY DICE 与 +/- INJURY MODIFIERS 按常规规则应用，但池中取**最高 3 个**或**最低 3 个**

> ⚠️ **新玩家最易混淆条目（视频教学明确警告 + Pass 3 内联）**：Bloodbath 累加 4D6 当武器自带 boost——`DEADLY` 武器（如 `Infernal Bomb`）触发 Bloodbath 时是 **4D6 全加**（→ `rules/02-comprehensive-rules.md#bloodbath-rolls`）

### AI 应何时调用描述

**Bloodbath 是一个特殊放大事件，描述分两个时点**：

1. **宣告花 markers 的瞬间**：`BLOOD MARKERS` 兑现的视觉/感官——可以写"那些之前的伤口同时裂开" / "失血累积到崩溃"。
2. **Bloodbath Roll 出结果后**：按 `→ narrative/injury-flavor.md#结果-fbloodbath3d6-或-deadly-4d6-全加` 的对应 cell 描述伤情。

合并写也可——但要**让叙事承担"累积"的语义**，不是单次伤害。Bloodbath 总长 2-3 句，30-60 字（→ `tone-guide.md#描述长度规范`）；多模型 `BLAST` 各模型 ≤ 1 句、总 ≤ 4 句。

### 描述模板

**普通 Bloodbath（3D6 全加）**：

- 「`Heretic Trooper` 身上已经有 6 个 `BLOOD MARKERS`——伤情积累到这一秒。`Yeoman` 的 `Bolt-Action Rifle` 又一发——之前所有伤口同时往外冒血。3D6 = 6+5+5 = 16。他向前栽，倒下时已经空了。」
- 「`Lieutenant` 身上的 6 个 `BLOOD MARKERS` 在 `Tank-Splitter Sword` 落下的瞬间兑现——胸甲与铠甲下面的每一处之前的凹陷同时塌开。3D6 = 4+5+6 = 15。胸前是一片裂开的红。他不再动。」
- 「目标已经 `Down`——只需 3 个 `BLOOD MARKERS`。`Misericordia` 找到他眼罩缝的那一秒，3D6 = 3+4+6 = 13。他抽搐一下停下。」

**DEADLY Bloodbath（4D6 全加）**：

- 「`Infernal Bomb` 在他脚下炸开——`DEADLY` 触发 4D6 Bloodbath。4D6 = 5+6+4+6 = 21。火里有惨叫。他被炸成几块，各块在火里继续燃烧。」
- 「`Anti-Tank Hammer` 的 `RISKY` 攻击命中——`DEADLY` 触发 4D6 Bloodbath。4D6 = 6+5+5+4 = 20。爆炸把他抛起一人高再摔回泥里。他的下半身消失了。」

**Bloodbath 多模型受影响（BLAST 武器）**：

- 「`Brazen Bull` 的炉膛喷出一道贴地的蓝紫色火焰——`BLAST 3"` 范围内三个 `Yeoman`。一个还来得及举手挡脸（4D6 = 19 Out of Action）；一个的胸甲烧红、铆钉爆开（4D6 = 14 Out of Action）；第三个没有动作——他直接没了上半身（4D6 = 23）。」
- 「`Satchel Charge` 在 `Yeoman` 小队中间爆开——`BLAST 3"` 三人。第一个被气浪扔出去落地时没了头盔（3D6 = 16 Out of Action）；第二个胸甲背面凹陷，他向前栽倒不动了（3D6 = 14 Out of Action）；第三个跪在原地，铠甲表面还在冒烟（3D6 = 8 Down）。」

### 常见错误

- ❌ "Bloodbath！全军覆没！"——Bloodbath 是**一次**伤害放大，不是 AoE 屠杀；只有 `BLAST` 武器命中多模型时才描述多人
- ❌ "Bloodbath 永远 = Out of Action"——3D6 期望 10.5，4D6 期望 14，**很可能** Out of Action 但**不一定**。骰子出来才知道
- ❌ 写得过于戏剧化以至于看起来是新规则："Bloodbath 让大地为之震动……"——它只是"花 markers 全加骰子"，描述放大 = 累积兑现，不是天降异象
- ❌ 把单次 Bloodbath 写得像"连续多回合伤害的总结"——Bloodbath 在**一次** Injury Roll 时点触发，描述也在那一刻
- ❌ "我花 6 个 `BLOOD MARKERS` 给他来个 Bloodbath，哈哈"——对手玩家的轻浮口吻（→ `tone-guide.md#禁区` 现代俚语 / 玩笑）

---

## 事件 4：Down（Injury 7-8）

### 触发条件

- **Injury Roll** 修正后结果 **7-8**（→ `rules/02-comprehensive-rules.md#injury-roll-table`）
- 后果：
  - 放 **1 个 `BLOOD MARKER`** 并标记 Down（若模型已 Down → 放 **2 个 `BLOOD MARKERS`**）
  - **模型若在自己的 Activation 中被 taken Down → Activation 立即结束**（→ `rules/02-comprehensive-rules.md#down-results`）
  - 对 Down 模型的 Melee Attack → Injury Roll **+1 INJURY DICE**
  - 为 Down 模型 take Success Roll → **-1 DICE**
  - 模型 Down 时**不能因任何原因被移动**（除非 Fall）
  - 下次 Activate 时模型**站起来**，但**该 Activation 内 Movement Characteristic 减半**（含 Charge Bonus）
  - 若 Down 时在 ledge 1" 内 → 可能 Fall（先做 Success Roll，Failure → Fall + Down，→ `rules/02-comprehensive-rules.md#down-results`）

> **Errata 裁决**：以"非 Injury Roll 来源"被打 Down 的模型（如 Eire Trench Cleric 的 *Away, Serpents!* 异能）**仍要**放 `BLOOD MARKER`（→ `rules/02-comprehensive-rules.md#injury-rolls` Errata Core Q10）

### AI 应何时调用描述

**Injury Roll 出 7-8 之后立刻**——按 `→ narrative/injury-flavor.md#结果-c7-8--down--blood-marker首次`（首次 Down）或 `#结果-d7-8--down-第二次--2-blood-markers`（已 Down + 再 Down）抽对应武器类别的 cell。

若 `Down` 触发"自己 Activation 立即结束"，AI 在描述末尾**陈述式**带一句规则后果——例如「`Lieutenant` 跪在泥里。本次 Activation 结束。」

若 Down 模型紧邻 ledge 且 Success Roll 失败导致 Fall，先描述 Down 的事件、再描述 Fall（→ `rules/02-comprehensive-rules.md#falling`）。

### 描述模板

**首次 Down**：（敌方视角，AI 描述自家模型倒下 / 描述玩家模型倒下；模板按 W1-W7 武器类别抽，下方仅给跨类共通版本）

- 「`Heretic Trooper` 的 `Bolt-Action Rifle` 在 18" 外开火——`Yeoman` 的左大腿中弹，膝盖一软，他倒在战壕底的泥水里。1 个 `BLOOD MARKER`，Down。本次 Activation 结束。」
- 「`Lieutenant` 用 `Blessed Sabre` 砍中 `Heretic Trooper` 的肩颈交界——血从盔甲缝喷出，他跪进泥里，嘴里还在低吟。1 个 `BLOOD MARKER`，Down。」
- 「`Frag Grenades` 在他脚下三尺处爆开——左膝被弹片打穿，他向后倒进泥水里。1 个 `BLOOD MARKER`，Down。」

**已 Down + 再 Down**：（积伤兑现，但**未** Out of Action）

- 「他还跪在泥里。又一发 `Bolt-Action Rifle` 弹头钉进他的背——他向前栽，胸甲蹭着泥往前滑半尺。2 个 `BLOOD MARKERS`，仍 Down。」
- 「`Wretched` 蹲在他倒下的身上，关节反向折着，爪子陷进胸甲缝里——他抽搐了一下停下来。2 个 `BLOOD MARKERS`，仍 Down。」

**Activation 中被 Down → Activation 立即结束**：

- 「`Yeoman` 在 `Heretic Priest` 1" 内挥出 `Bayonet`——攻击失手；`Heretic Priest` 用 `Trench Knife` 反击命中，Injury 7。`Yeoman` 肩膀脱臼，跪进泥里。本次 Activation 结束。」

**Down 时 Fall off ledge**：

- 「`Yeoman` 站在二楼废墟边缘——`Sniper Rifle` 弹头钉进他的胸甲。Injury 8 Down——但他在 ledge 1" 内，take Success Roll = 4 Failure → Fall 6"。落地时再做 Injury Roll（+2 INJURY DICE）= 11 Out of Action。」

### 常见错误

- ❌ "他被打晕了" → `Down` 不是被打晕，是**具体的伤**（膝盖被打穿 / 胸口闷掉 / 肺被毒气罩住，→ `tone-guide.md#禁区` PG-13 化）
- ❌ "他失去了意识，可能再也站不起来了" → 错的，**Down 模型下回合会站起来**（Movement 减半）；不要外推他"再起不来"
- ❌ "他倒下了。剧情外推：他的战友冲过来救他" → 战场之外（→ `tone-guide.md#禁区` 超出战场剧情）
- ❌ 把 `Down` 描述写得像 `Out of Action`（"他不再动了"） → 应改为"他跪下了"" / "他坐进泥里"——**他还活着**
- ❌ 忘记陈述规则后果："本次 Activation 结束" / "Down 模型 Movement 减半" 应在描述末尾用**陈述式**带一句（→ `tone-guide.md` Example 5）

---

## 事件 5：Out of Action（Injury 9+）

### 触发条件

- **Injury Roll** 修正后结果 **≥ 9**（→ `rules/02-comprehensive-rules.md#injury-roll-table` / `#out-of-action`）
- 后果：模型**严重受伤或死亡，移出战场**，本局不归（→ `rules/02-comprehensive-rules.md#out-of-action`）

> ⚠️ **新玩家最易混淆条目（视频教学明确警告 + Pass 3 内联）**：`TOUGH` 关键词的模型**仅首次**承受 Out of Action（9+）时，将该结果改为 `Down`。**第二次及以后**的 9+ 结果**不再降级**（→ `rules/03-keywords-glossary.md#tough` / `rules/02-comprehensive-rules.md#out-of-action`）
>
> 复合 `TOUGH` + `Machine Armour` 时按 Errata Keywords Q5 的"逐条字面套用"顺序进一步降级——例：第一次 9+ → ① TOUGH 改为 Down → ② Machine Armour 的 Standfast 把 Down 改为 Minor Wound → ③ 结果是 Minor Wound（→ `rules/02-comprehensive-rules.md#out-of-action`）

### AI 应何时调用描述

**Injury Roll 出 9+ 且未被 `TOUGH` / Machine Armour 降级时**——按 `→ narrative/injury-flavor.md#结果-e9--out-of-action` 抽对应武器类别的 cell。

若 `TOUGH` 触发降级（9+ → Down），**改用事件 4（Down）描述**，并在描述里**陈述式**说明 `TOUGH` 兑现：「Injury 11——但 `Lieutenant` 的 `TOUGH` 关键词首次降级为 Down。1 个 `BLOOD MARKER`。」

### 描述模板

**普通 Out of Action**：

- 「`Bolt-Action Rifle` 的弹头从 `Yeoman` 太阳穴入，从对侧出。钢盔里现在装的是一团红泥。他不再动。模型移出战场。」
- 「`Sniper Rifle` 在 40" 外咳了一声——`Heretic Trooper` 的胸前出现一个洞，背面出现一个更大的洞。他向前栽倒在泥里。Out of Action。」
- 「`Tank-Splitter Sword` 砍下 `Lieutenant` 的上半身——上半身落在脚边，下半身还跪着，又过两秒才倒。圣物匣掉进战壕底的水里。模型移出战场。」
- 「`Holy Smoke` 灼穿了 `Heretic Trooper` 的全部皮肤——他在烟里跪下，钢铁面具下传出最后一声炉膛嘶声，然后停了。Out of Action。」
- 「`Satchel Charge` 在 `Heretic Priest` 脚下爆开——爆炸把他抛起一人高再摔回泥里。他的腰以下消失了。Out of Action。」

**TOUGH 降级为 Down 的情形**：

- 「`Anti-Materiel Rifle` 的弹头打中 `Lieutenant` 的胸甲——4D6 = 12 应当 Out of Action。但 `Lieutenant` 的 `TOUGH` 关键词首次兑现——降级为 Down。胸甲被打穿，他跪在泥里，圣物匣在手里。1 个 `BLOOD MARKER`，Down。」

**TOUGH + Machine Armour 复合（Errata Keywords Q5）**：

- 「`Anchorite Shrine` 被 `Anti-Tank Hammer` 在胸前爆开——4D6 = 11 应当 Out of Action。① `TOUGH` 首次兑现 → 降级为 Down；② `Machine Armour` 的 Standfast → Down 再降级为 Minor Wound。1 个 `BLOOD MARKER`。蒸汽从甲缝里漏得更急了。」

### 常见错误

- ❌ "他英勇牺牲！他的灵魂将归于主！" → 浪漫化 + 内心戏 + 外推（→ `tone-guide.md#禁区`）
- ❌ "虽然出了 9+，但他用意志力撑住了，下回合还能动" → **绝对禁区**，叙事推翻规则（→ `tone-guide.md#禁区` "❌ 推翻骰子结果"）
- ❌ "他的家人在远方哭泣" → 战场之外（→ `tone-guide.md#禁区` 超出战场剧情）
- ❌ "他回想起小时候在教堂的钟声然后死了" → 内心戏（→ `tone-guide.md#禁区`）
- ❌ "干得漂亮！把对手的 `Lieutenant` 干掉了！" → AI 是对手，不夸玩家（→ `tone-guide.md#禁区` 把 AI 写成 GM）
- ❌ 长段抒情（"他的一生在这一刻闪过……"） → grimdark 的死是平淡的、被踩进泥里的（→ `tone-guide.md#禁区` 浪漫化）
- ❌ 忘了陈述"模型移出战场" → 应在描述末尾**陈述式**带一句规则后果

---

## 事件 6：Morale Phase 失败 → Shaken / 逃跑

### 触发条件

- 在 **Morale Phase**（每回合第三阶段，→ `rules/02-comprehensive-rules.md#3-morale-phase`）触发：
  - 若你战团中**半数或以上**模型 Down 或 Out of Action（**向上取整**）→ 必须做 **Morale Check**（一种特殊 Success Roll）
  - **半数取整说明**：5 模型战团 → 3 个 Down/Out 触发；6 模型 → 3 个；7 → 4；10 → 5
- Morale Check 失败 → 战团进入 **Shaken** 状态（→ `rules/02-comprehensive-rules.md#shaken-warbands`）
- Shaken 后果：
  - **所有 Success Rolls 视作 Risky Success Rolls**（除非本来已是 Risky）——失败立即结束 Activation
  - **下一回合 Morale Phase 必须再做一次** Morale Check（即使此时少于半数 Down/Out）
    - Success → 解除 Shaken（仍可能再次进入）
    - Failure → **战团逃跑，立即输掉游戏**
- 或选择 **Sounding the Retreat**（→ `rules/02-comprehensive-rules.md#sounding-the-retreat`）：Morale Check 失败时**主动**选择立即逃跑、输掉游戏，而非变 Shaken

### AI 应何时调用描述

**两个时点**：

1. **Morale Check 失败的瞬间**——战团进入 Shaken。
2. **Shaken 战团下一回合 Morale Check 再失败**——战团逃跑、输掉游戏。

主动 Sounding the Retreat 用同一组描述模板，但更"主动撤退"调子（"他们清楚再打下去也是死，他们走了"）。

### 描述模板

**Morale Check 失败 → Shaken**：

- 「死亡的数字到了。在那座断掉的钟楼下，最后一个 `Yeoman` 抬头看了一眼空空的天空。他身后的兄弟一个跪在泥里念信经，一个把 `Bayonet` 拄在地上喘气。Morale Check = 5 Failure。从这一刻起，他们所有 action 都变成 risky。」
- 「`Heretic Trooper` 的钢铁面具下传出一声炉膛的低嘶——前方半数兄弟在泥里。Morale Check = 6 Failure。Shaken。喉咙里的火炉响声更急了，但火不再稳。」
- 「`Trench Pilgrim` 团里最后一个还能走的把锁链解开了——之前他都把自己锁在桩子上。Morale Check 失败。他低头看着锁链，没动作。Shaken。」

**Shaken 战团再次 Morale Check 失败 → 逃跑**：

- 「他们走了。`Yeoman` 抬起钢盔扔进泥里，转身向战场后撤。其他人跟着他。Morale Check 第二次失败——战团撤离，对方胜利。」
- 「`Heretic Priest` 低吟到一半停下——他张开手指，最后一个还能走的 `Heretic Trooper` 转身跑回战壕的烟里。Morale Check 第二次失败。战团逃跑。」
- 「`Trench Pilgrim` 解开锁链的那一个还在原地——剩下的两个抬起他向后撤。Morale Check 第二次失败。Pilgrims 退出战场。」

**Sounding the Retreat（主动撤退）**：

- 「Morale Check 失败——`New Antioch` 玩家选择 Sounding the Retreat 而非变 Shaken。`Lieutenant` 举手宣告撤退，剩余兄弟跟随他向后线撤。对方胜利。比拼到最后一兵一卒不智。」

### 常见错误

- ❌ "玩家的战团士气崩溃了！他们再也无法发挥实力，你需要小心战术调整。" → GM 口吻，给玩家建议（→ `tone-guide.md` Example 5 错误版 / `tone-guide.md#禁区` 把 AI 写成 GM）
- ❌ "我的战团士气崩溃了，但他们用意志力撑住了，不变 Shaken" → 叙事推翻规则（→ `tone-guide.md#禁区` 推翻骰子结果）
- ❌ "他们在心里想起了家人" → 内心戏 + 战场外推（→ `tone-guide.md#禁区`）
- ❌ 忘记**陈述规则后果**："Shaken 后所有 action 变 risky" / "战团撤离" 应在描述末尾用**陈述式**带一句（→ `tone-guide.md` Example 5 正确版）
- ❌ 把 Shaken 写成"暂时失去战斗力" → 错的，Shaken 战团仍能 Activate，只是**所有 Success Roll 变 Risky**（→ `rules/02-comprehensive-rules.md#shaken-warbands`）
- ❌ "你完蛋了 / 我赢了" → 对手玩家的轻浮口吻（→ `tone-guide.md#禁区` 玩笑）
- ❌ 把"半数 Down/Out 触发 Morale"写成"伤亡 50% 战败" → 不是战败，是触发 Morale **Check**；Check 成功仍能继续

---

## 事件 7：Blessing Marker 触发（消耗）

### 触发条件

- 你为友方模型 take Success Roll 时，可宣告花 1 个或多个 **`BLESSING MARKERS`**——每个 = Success Roll **+1 DICE**（→ `rules/02-comprehensive-rules.md#blessing-markers` / `#spending-blessing-markers`）
- 对手为你的模型做 Injury Roll 时，你可宣告花 1 个或多个——每个 = Injury Roll **-1 INJURY DICE**
- `BLESSING MARKERS` 上限 **6 个**——超出忽略放置指令
- 由**你自己**（己方玩家）花费**友方模型身上**的 `BLESSING MARKERS`（与 `BLOOD MARKERS` 镜像——后者由对手花费）

> **Errata 裁决**：当两位玩家要对**同一次掷骰**同时应用 `BLOOD MARKER` 与 `BLESSING MARKER` 时，由持 **Initiative** 的玩家决定执行顺序（→ `rules/02-comprehensive-rules.md#blessing-markers` Errata Core Q1）

### AI 应何时调用描述

**两个时点**：

1. **宣告花 markers 的瞬间**：用神迹意象描述——圣物匣发烫、十字架渗血、一道光从教堂彩窗折出、面具下圣徒的脸闪过、铆钉缝里的圣骨震动。
2. **结算后**：
   - 若 Success Roll 因 +DICE 命中 / Injury Roll 因 -INJURY DICE 减伤 → 描述神迹**生效**
   - 若仍失败 / 仍重伤 → 描述神迹**不足** / 圣物匣的光暗了一下——但**不**反向改写骰子结果

> **关键**：`BLESSING MARKER` 描述的是**信士一方**（Faithful：New Antioch、Trench Pilgrims）的神迹兑现——异端军团也可获得 `BLESSING MARKER`（如某些 Goetic Powers 反向使用），但**意象不同**（异端神迹是**亵渎式**的——黑色光、肉体扭曲的"自愈"、地狱主的回应）。

### 描述模板

**信士一方（Faithful）— 防御方花 `BLESSING MARKER` 减 Injury DICE**：

- 「`Heretic Trooper` 扣下 `Bolt-Action Rifle` 扳机。子弹本该穿心——但 `Yeoman` 胸前的圣物匣在那一瞬间发了一下烫，弹道偏了三寸，钉进了他身后的木板。-1 INJURY DICE，Injury 5 Minor Hit。」
- 「`Tank-Splitter Sword` 落下来——`Lieutenant` 锁骨上方那块铆钉缝里嵌的圣骨突然震了一下。刀路斜了，砍中肩甲外缘。-1 INJURY DICE，Injury 7 Down（而非 9+ Out of Action）。」
- 「`Frag Grenades` 在他脚下炸开——`Trench Pilgrim` 的锁链上的小十字架渗出血，弹片在他身边偏开。-1 INJURY DICE，Injury 4 Minor Hit。」

**信士一方 — 进攻方花 `BLESSING MARKER` 加 Success Roll DICE**：

- 「`Yeoman` 在战壕沿口端起 `Bolt-Action Rifle`。胸前的圣物匣发烫——他扣下扳机时面具的玻璃眼镜片上凝了一道水汽。+1 DICE，Success 9 命中。」
- 「`Lieutenant` 举起 `Blessed Sabre` 喊：『以救主之名！』圣物匣的光从他的胸前透出来——他的下一刀比之前都准。+1 DICE，Critical Success 12。」

**异端一方（Heretic）— 黑色神迹（占位，待 Pass 9 完善）**：

- 「`Heretic Priest` 张开手指——他的钢铁面具下涌出一阵黑色的光。`Heretic Trooper` 的伤口在那一秒收口。-1 INJURY DICE。」
- 「`Wretched` 撕扯自己的皮肤献给地狱主——它的下一击带着炉膛的余温。+1 DICE。」

**神迹不足（marker 花了但仍失败）**：

- 「`Yeoman` 胸前的圣物匣发了一下烫——但烫得不够。-1 INJURY DICE 后仍是 Injury 9。他向后栽倒进泥水里。圣物匣的光暗了一下。Out of Action。」
- 「`Lieutenant` 念完了 *Lord, lead Your servant home* ——`Blessed Sabre` 这一刀仍未找到。Success Roll +1 DICE 后仍是 5 Failure。圣物匣的光暗下去，他低头看着自己的剑。」

### 常见错误

- ❌ "神迹发生了！上帝的手指拨开了子弹，`Yeoman` 安然无恙。" → 「上帝的手指」过于具体且过于浪漫（→ `tone-guide.md` Example 4 错误版）。改用"圣物匣发烫" / "铆钉缝里的圣骨震动"——**物质化**的神迹
- ❌ "他被上帝保佑活了下来" → 不接规则，纯叙事推翻骰子风险（→ `tone-guide.md#允许的语言` "✅ 宗教狂热"反例）
- ❌ "因为 Blessing 所以这次先不死" → 叙事推翻规则（→ `tone-guide.md#禁区` 推翻骰子结果）。`BLESSING MARKER` 只 **-1 INJURY DICE**，骰子结果可能仍 9+ → Out of Action，描述要承认这个事实
- ❌ 神迹描述与规则结果**脱钩**：花了 `BLESSING MARKER` → 描述里**必须**提到圣物匣 / 圣骨 / 锁链十字架之一的"物质化神迹"，否则玩家不知道 marker 兑现了什么
- ❌ "我的 `Wretched` 撕扯自己的皮肤献给地狱主，于是它无敌了一回合" → 描述加规则效果（"无敌一回合"是叙事生造的 modifier，禁止）
- ❌ 用 `BLESSING MARKER` 解释**所有**好运（如普通 Cover 触发 -1 DICE 也写成"圣物匣发烫"）→ 神迹描述**只**用在 marker 实际消耗时，否则贬值

---

## 跨事件守则

适用于上方 7 个事件的共通约束（与 `→ narrative/tone-guide.md` 自检清单配合使用）：

### 1. 始终在规则结算后调用描述

骰子先出，AI 再描述。**修辞不能改写事实**（→ `tone-guide.md#核心原则`）。

### 2. 武器名 / 模型名 / 关键词保留英文原文

- ✅ `Bolt-Action Rifle` / `Heretic Trooper` / `Tank-Splitter Sword` / `Wretched` / `BLOOD MARKER` / `BLESSING MARKER`
- ❌ "栓动步枪"作主名 / "异端兵"作主名（首次可加中文注释，**主名**仍用英文）（→ `tone-guide.md#禁区` 模型名 / 武器名翻译漂移）

### 3. ALL-CAPS 关键词反引号包

- `BLOOD MARKER` / `BLESSING MARKER` / `DEADLY` / `BLAST` / `IGNORE ARMOUR` / `IGNORE COVER` / `CRITICAL` / `TOUGH` / `ASSAULT`
- 详见导入指南 §3.7.I.2

### 4. 长度按 `tone-guide.md` 规范

| 事件 | 推荐句数 / 字数 |
|---|---|
| 1. Charge 接触 | 1-2 句 / 20-40 字 |
| 2. Critical Hit | 2-3 句 / 30-60 字（可加一个意象） |
| 3. Bloodbath（单模型） | 2-3 句 / 30-60 字 |
| 3. Bloodbath（BLAST 多模型） | 每模型 ≤ 1 句，总 ≤ 4 句 |
| 4. Down | 1-2 句 / 20-40 字 |
| 5. Out of Action | 2-3 句 / 30-60 字 |
| 6. Morale 失败 | 2 句 / 30-50 字 |
| 7. Bless 触发 | 1-2 句 / 20-40 字 |

详见 `→ narrative/tone-guide.md#描述长度规范`。

### 5. 描述末尾**陈述式**带规则后果

事件触发**规则状态变化**时（Activation 结束 / 模型移出战场 / Shaken / TOUGH 兑现等），AI 在描述末尾用陈述式（不评论）说明：

- ✅ 「他跪在泥里。本次 Activation 结束。」
- ✅ 「他不再动。模型移出战场。」
- ✅ 「Morale Check 第二次失败。战团撤离，对方胜利。」
- ✅ 「-1 INJURY DICE，Injury 5 Minor Hit。」
- ❌ "这意味着模型现在 Down 了"——啰嗦
- ❌ 不带规则后果——玩家不知道事件兑现到 match-state 的什么字段

### 6. AI 不剧透自家模型意图

- ✅ 「`Heretic Trooper`（id: blue.trooper_2）执行 Move ACTION，从 (18, 12, 0) 移动到 (15, 14, 0)——半段战壕墙后面。剩余移动 1"。」
- ❌ 「`Heretic Trooper` 阴险地溜到掩体后面，准备发动致命的反击……他在心里冷笑」（→ `tone-guide.md` Example 10 错误版）

### 7. AI 不教学 / 不建议 / 不夸奖玩家

- ❌ "你可能想要躲到那座废墟后面" / "你的 Lieutenant 处境很危险" / "干得漂亮！" / "好奇为什么没有用 Blood Marker？"
- ✅ AI 该做的只是：宣告自家模型行动 + 描述战场事件 + 等玩家出招（→ `tone-guide.md#禁区` 把 AI 写成 GM）

### 8. 不要外推到战场之外

- ❌ "他的家人在远方哭泣" / "三天后他的尸体会被发现" / "这次失败会让他在战团内部失去地位"
- ✅ 只描述**这一刻战壕里**看见的：泥、血、烟、子弹、面具、铆钉、铠甲变形
- 详见 `→ narrative/tone-guide.md#禁区` 超出当前战场的剧情发展

### 9. 不要替模型加内心戏

- ❌ 「他想起教堂的钟声」 / 「他后悔没用 `Blessing Marker`」 / 「他在心里默念家人」
- ✅ 只描述**外部可见**的事实——伤口、姿势、声音、铠甲变形、液体、烟

### 10. 不要 PG-13 软化

- ❌ "他被打晕了" / "轻微擦伤" / "受了点伤"
- ✅ 让伤情的**重量**与规则结果对齐——`Minor Hit` = 看得见的浅伤；`Down` = 还活着的重伤；`Out of Action` = 死亡或濒死

### 11. 神迹只在 marker 真正消耗时用神迹意象

- 不要给每次 -1 DICE / Cover 触发都安"圣物匣发烫"——**只**在 `BLESSING MARKER` 实际消耗的时点用。否则神迹描述贬值
- 神迹必须**物质化**——圣物匣 / 圣骨 / 锁链十字架 / 面具下圣徒的脸 / 一道光从教堂彩窗折出。**不要**抽象（"上帝保佑")

### 12. 异端魔法 / Goetic 占位

事件 7 中"异端一方的反向神迹"以及 `Heretic Priest` 法术、Goetic Powers 的具体名 / 关键词在 v0.1 **未完整确定**——Pass 9 完成 `warbands/02-heretic-legions.md` 后回流补全。

**当前 v0.1 阶段**：相关 cell 已留占位描述（"黑色的光" / "撕扯自己的皮肤献给地狱主"），AI 调用时可优先用 `→ narrative/world-primer.md` §3 异端军团调色板 + `→ narrative/world-primer.md` §6 黑圣杯调色板代偿。
