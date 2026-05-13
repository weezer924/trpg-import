# narrative/injury-flavor: Injury Flavor（受伤描述矩阵）

> 源：自撰，基于 `Trench Crusade - Digital Rulebook v1.0.2.pdf` p.46-49（Injuries / Injury Roll Table / Bloodbath Rolls）+ `Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.68-86（Battlekit）
> 版本：v1.0.2
> **本文件用途**：给 AI 在 **Injury Roll 结算后**查的描述模板矩阵。**结算先出，描述后套**——本矩阵不能反过来影响骰子结果。
> 配套：`→ narrative/world-primer.md`（意象与短语库）/ `→ narrative/tone-guide.md`（文风允许/禁区）

## Index

- [用法](#用法)
- [核心原则：叙事始终后于规则结算](#核心原则叙事始终后于规则结算)
- [武器类别索引](#武器类别索引)
- [结果 A：1 or less — No Effect](#结果-a1-or-less--no-effect)
- [结果 B：2-6 — Minor Hit + BLOOD MARKER](#结果-b2-6--minor-hit--blood-marker)
- [结果 C：7-8 — Down + BLOOD MARKER（首次）](#结果-c7-8--down--blood-marker首次)
- [结果 D：7-8 — Down 第二次 + 2 BLOOD MARKERS](#结果-d7-8--down-第二次--2-blood-markers)
- [结果 E：9+ — Out of Action](#结果-e9--out-of-action)
- [结果 F：Bloodbath（3D6 或 DEADLY 4D6 全加）](#结果-fbloodbath3d6-或-deadly-4d6-全加)
- [跨结果适用的修辞守则](#跨结果适用的修辞守则)

---

## 用法

AI 在每次 `Injury Roll` 结算后（→ `rules/02-comprehensive-rules.md#injury-roll-table`）执行：

1. **查规则结果**：1 or less / 2-6 / 7-8 / 9+ / Bloodbath（→ `rules/02-comprehensive-rules.md#injury-roll-table` + `#bloodbath-rolls`）。
2. **查武器类别**：本次攻击用的武器属于下方[武器类别索引](#武器类别索引)的哪一类——按攻击武器在 `→ rules/05-battlekit.md` 中的关键词归类。
3. **从对应 cell 抽 1-3 个示例句**，配上**具体的位置、模型名、武器名**改写。**不能照抄字面**；示例句是调子参考，不是台词。
4. **检查长度**：按 `→ narrative/tone-guide.md#描述长度规范` 控制句数。
5. **检查禁区**：套用前再走一次 `→ narrative/tone-guide.md#自检清单`。

调色板词汇全部从 `→ narrative/world-primer.md` 抽——`Holy Smoke` / `Wretched` / `Heretic Trooper` / `Anchorite Shrine` / `Bolt-Action Rifle` 等专有名词**保留原文**，不要汉化主名。

---

## 核心原则：叙事始终后于规则结算

`Injury Roll Table` 给出的是**事实**（PDF p.48）：

| Roll | Result |
|---:|---|
| 1 or less | No Effect |
| 2-6 | Minor Hit + 1 `BLOOD MARKER` |
| 7-8 | Down + 1 `BLOOD MARKER`（若已 Down → 2 `BLOOD MARKERS`） |
| 9+ | Out of Action |

`Bloodbath Roll`（→ `rules/02-comprehensive-rules.md#bloodbath-rolls`）：对手花 6 `BLOOD MARKERS`（目标已 Down → 3）将本次 Injury Roll 改为 3D6 全加；若武器带 `DEADLY` 则 4D6 全加。

**修辞规则**：

- ❌ 不能因为"叙事好看"把 7-8 写成"看起来像快死了"——`Down` 是**还活着**，下回合 Activate 会站起来（Movement 减半，→ `rules/02-comprehensive-rules.md#down-results`）。
- ❌ 不能因为"模型是大人物"把 9+ 写成"侥幸活下来"——`Out of Action` = 移出战场（→ `rules/02-comprehensive-rules.md#out-of-action`）。
- ❌ 不能因为某次 Bloodbath 描述写得壮观就额外伤害多模型——`Bloodbath` 仍是**一次** Injury Roll（除非 `BLAST` 武器另算）。
- ✅ 7-8 Down + 第二次 Down 触发"额外 BLOOD MARKER"时（→ `rules/02-comprehensive-rules.md#injury-roll-table`），描述可以"伤上加伤"，但**不能**升级为 Out of Action（除非骰子真的是 9+）。

---

## 武器类别索引

为避免每件武器单独写矩阵（数量爆炸），按 `→ rules/05-battlekit.md` 的关键词把武器分 **7 类**：

| 类别代号 | 名称 | 涵盖武器（示例） | 关键调色板（→ world-primer） |
|---|---|---|---|
| W1 | **远程齐射** Ranged Salvo | `Bolt-Action Rifle` / `Musket` / `Semi-Automatic Rifle` / `Automatic Rifle` / `Submachine Gun` / `Pistol` / `Automatic Pistol` / `Silenced Pistol`；步兵阵线齐射 | §1 战壕 + §5 末日 + §7 远方炮火 |
| W2 | **重型远程** Heavy Ranged | `Machine Gun` / `Heavy Shotgun` / `Sniper Rifle` / `Anti-Materiel Rifle` / `Grenade Launcher`；含 `HEAVY` / `+1 INJURY DICE` / `CRITICAL` 关键词的远程武器 | §1 战壕 + §5 末日 |
| W3 | **散弹／近距霰弹** Shotgun / Close-Range Blast | `Shotgun` / `Automatic Shotgun` / `Blunderbuss`；`SHOTGUN` / `SHRAPNEL` 关键词 | §1 战壕 + §7 废墟 |
| W4 | **圣火／神圣武器** Sacred Fire | `Flamethrower` / `Heavy Flamethrower`（用于 Faithful 一侧）+ Blessed-prefix 武器（`Blessed Sabre` / `Blessed Revolver` 等，待 Pass 8 New Antioch warband 落实）+ `Holy Smoke` 类燃烧物；通常带 `FIRE` / `IGNORE ARMOUR` 或 `BLESSED` 关键词 | §2 机械教士 + §4 教廷狂热 |
| W5 | **手雷／爆炸** Grenade / Explosive | `Frag Grenades` / `Gas Grenades` / `Incendiary Grenades` / `Molotov Cocktail` / `Satchel Charge`；`BLAST` / `IGNORE COVER` 关键词 | §1 毒气 + §3 异端军团（`Infernal Bomb`）+ §5 末日 |
| W6 | **锐器近战** Edged Melee | `Bayonet` / `Trench Knife` / `Misericordia` / `Sword/Axe` / `Trench Club` / `Flail/Scourge` | §1 战壕 + §4 教廷 / §3 异端（双向适用） |
| W7 | **重型近战** Heavy Melee | `Great Sword/Axe` / `Great Hammer/Maul` / `Anti-Tank Hammer` / `Polearm` / `Tank-Splitter Sword`（待 Pass 9）；含 `HEAVY` / `+1 INJURY DICE` / `+1 INJURY MODIFIER` 的近战武器 | §3 异端 + §2 机械教士（双向适用） |
| W8 | **异端魔法 / Goetic** Heretic Sorcery（**占位**） | 待 Pass 9 `warbands/02-heretic-legions.md` 完成后回流——Goetic Powers / `Infernal Bomb`-as-attack / heretic priest 法术 / Wretched 异能。**v0.1 阶段先用 W3 + §3 异端军团调色板代偿** | §3 异端（炉膛喉咙 / 反折关节 / 火里有惨叫）+ §6 黑圣杯（瘟疫，若适用） |

> **回流说明**：W8 异端魔法 / Goetic 的具体武器名 / 关键词需 Pass 9（`warbands/02-heretic-legions.md`）完成后回流本文件。当前 v0.1 矩阵给 W8 留占位 cell（短描述），不强求完整。

---

## 结果 A：1 or less — No Effect

> 触发：Injury Roll 修正后 ≤ 1（→ `rules/02-comprehensive-rules.md#injury-roll-table`）
> 后果：模型**未受伤**，不放 `BLOOD MARKER`
> **描述原则**：**最少**——这是"没事发生"，1 句就够，常常 0 句（AI 直接说"未命中要害"也行）。**不要把 No Effect 写成擦伤**——擦伤是 Minor Hit。

| 武器类别 | 示例（1-2 例） |
|---|---|
| **W1 远程齐射** | 「子弹钉进胸甲，被钢板吃掉了——弹头压扁在祝圣过的铆钉之间，没穿透。」 |
| **W2 重型远程** | 「狙击弹擦过 `Yeoman` 的钢盔顶——钢盔上多了一道亮金属凹痕，人没事。」 |
| **W3 散弹** | 「散弹打在战壕沿木板上，铅丸有几颗弹回胸甲——都没破。」 |
| **W4 圣火** | 「火舌掠过他的胸甲，圣油涂层冒了一秒白烟，火没贴上。」 |
| **W5 手雷** | 「`Frag Grenades` 在 4" 外炸开，弹片全打在他身后的弹坑里——他蹲得够低。」 |
| **W6 锐器近战** | 「刺刀刺到铠甲的圣徽下沿，滑开了——铠甲下的肉没被切到。」 |
| **W7 重型近战** | 「锤头砸在他的肩甲，把他甩出半步——肩甲凹了，肩膀没断。」 |
| **W8 异端魔法（占位）** | 「黑色的烟扑上他的面具玻璃，又被祝圣过的玻璃挡了回去——没穿透。」 |

---

## 结果 B：2-6 — Minor Hit + BLOOD MARKER

> 触发：Injury Roll 修正后 2-6（→ `rules/02-comprehensive-rules.md#injury-roll-table`）
> 后果：放 **1 个 `BLOOD MARKER`**；模型**继续战斗**，未 Down
> **描述原则**：**具体的擦伤 / 浅伤 / 震荡**——可见、可数、不削战斗力，但留疼。1 句即可，10-25 字（→ `tone-guide.md#描述长度规范`）。**不要软化**（"轻微擦伤" = ❌ → `tone-guide.md` PG-13 禁区）。

### W1 — 远程齐射

- 「`Bolt-Action Rifle` 的弹头擦过他的左大腿外侧，掀掉一片皮和一段裤子，肉里还嵌着布。」
- 「子弹打中胸甲左下，钢板凹进去一指节深——他咳了一声继续装弹。」
- 「弹头从耳朵上方贴头皮飞过，烫熟了一道头发——他还活着，但听不见左耳了。」
- 「子弹打在腰间皮带扣上，扣子裂了，弹芯卡进皮带——他低头看了一眼，没停下。」
- 「弹片擦过他的下颌，掀掉一块嘴唇——他往泥里啐了一口血。」

### W2 — 重型远程

- 「狙击弹擦过他的左肩——肩甲整块被切开，下面是骨头和一截白布。」
- 「`Machine Gun` 连发里有一发钉进他的小腿——小腿肌里多了一个洞，靴子里灌进血。」
- 「`Heavy Shotgun` 在长距离上散开，两颗弹丸打中他的胸甲——一颗弹回去，一颗卡进胸甲与肋骨之间。」
- 「`Anti-Materiel Rifle` 的弹片擦过他的肋下——铠甲被切出一道两寸的口子，下面渗出红色。」
- 「`Grenade Launcher` 的弹片从他左侧炸开——颊骨上多了一道开放伤口，他眨了一下眼。」

### W3 — 散弹

- 「`Shotgun` 在 6" 内开火——半数铅丸卡进胸甲，另一半擦过他的右臂袖管，掀开一片布和肉。」
- 「`Blunderbuss` 装的锈钉打中他的胳膊——三根钉穿过袖子，钉在肉里。」
- 「`Automatic Shotgun` 的连发里有几粒打中他的下巴和颈侧——颈侧渗出一道血。」

### W4 — 圣火 / 神圣武器

- 「`Flamethrower` 的火舌从他左侧扫过——铠甲表面的圣油涂层瞬间起火，他用手拍着灭，手背烫红。」
- 「`Holy Smoke` 落在他的钢铁面具上——面具表面冒白烟，玻璃眼镜片被烫出一道纹。」
- 「`Blessed Sabre` 划过他的胸前皮带——皮带断了，下面一道浅红血痕从胸口斜下。」
- 「圣火舔到 `Heretic Trooper` 的炉膛喉咙——他低吼一声，喉口的金属唇缘红了一秒，烟散开。」

### W5 — 手雷 / 爆炸

- 「`Frag Grenades` 在 5" 外炸开——一片弹片飞进他的左大腿，没穿出，伤口很整齐。」
- 「`Gas Grenades` 散开的黄绿色烟贴地爬到他脚边——他咳了三声，眼角开始流水。」
- 「`Incendiary Grenades` 的火星溅到他的肩甲——铠甲烧黑了一小块，肩膀以下的布烧着了，他拍灭。」
- 「`Molotov Cocktail` 在他身边的泥水里炸开——飞溅的油落到他的胳膊，烧出一道掌大的灼伤。」

### W6 — 锐器近战

- 「`Bayonet` 刺穿了他的肩甲缝——刀尖进了一寸，扭了一下拔出来，血顺着刀身滴下。」
- 「`Trench Knife` 划过他的颊骨——掀掉一片皮和一只耳朵的下半。」
- 「`Sword/Axe` 砍中他的胸甲右侧——铠甲裂了一道缝，里面是肋骨与一片红。」
- 「`Misericordia` 在铠甲缝里找到一个口子，扎进他的肋下——伤口很小，但他咳了血。」
- 「`Trench Club` 的钉头落在他的钢盔上——盔被砸凹一指，他眼前一黑又亮。」
- 「`Flail/Scourge` 的金属链甩过他的脸——颊骨上多了两道平行的开放伤，鼻梁裂了。」

### W7 — 重型近战

- 「`Great Sword/Axe` 的刃锋擦过他的左肩——肩甲整片被劈开，下面是锁骨上的一道红。」
- 「`Great Hammer/Maul` 砸在他的胸甲——铠甲凹陷三指深，他闷哼一声跪下一只膝盖又站起来。」
- 「`Anti-Tank Hammer` 的爆炸头在他身边炸开——肩甲被掀掉，下面的肉烧黑了一块。」
- 「`Polearm` 的尖刺穿透了他的大腿——他一拐一拐退后两步，握着伤口。」

### W8 — 异端魔法（占位）

- 「`Heretic Priest` 的咒文在他耳边响起——他鼻血开始流，但他举起圣物匣念了反咒，止住。」
- 「黑色的火星从对方的钢铁面具下喷出——他的胸甲表面被烧出一个掌印形的焦斑。」

---

## 结果 C：7-8 — Down + BLOOD MARKER（首次）

> 触发：Injury Roll 修正后 7-8（→ `rules/02-comprehensive-rules.md#injury-roll-table`）
> 后果：放 **1 个 `BLOOD MARKER`** + 标记 **Down**；本次 Activation 中被 Down 则**立即结束 Activation**；下次 Activate 时站起来，Movement 减半（→ `rules/02-comprehensive-rules.md#down-results`）
> **描述原则**：**严重伤但还活着**——他**倒在战场上**，下回合还会站起来。1-2 句，20-40 字。**不要写"昏迷"**（`Down` 不是昏迷，是**膝盖被打穿** / 胸口闷掉 / 眼里被弹片蒙住 / 肺被毒气罩住的具体伤，→ `tone-guide.md` ❌ PG-13 禁区）。

### W1 — 远程齐射

- 「`Yeoman` 在战壕沿端起 `Bolt-Action Rifle` 扣下扳机；子弹钉进 `Heretic Trooper` 的左大腿。他闷哼一声，膝盖一软，倒在泥水里。」
- 「`Bolt-Action Rifle` 的弹头穿透了他的肩甲——血一下子从肩头喷出来，他向后栽进战壕底。」
- 「`Submachine Gun` 的连发把他的右腿打成两段——他没喊，跪下，再倒下。」
- 「`Pistol` 在 6" 内开火——一发钉进他的右肺，他一口血咳到面具内壁，倒下时还在抓胸甲的圣物匣。」
- 「`Musket` 的铅球打中他的颈侧——他往前栽，钢盔砸进泥里，颈侧的血在烂泥上漫开。」
- 「`Silenced Pistol` 的两发都打中胸口——他没听见枪声，只是膝盖一软，跪下去。」

### W2 — 重型远程

- 「`Sniper Rifle` 在 30" 外咳了一声——他的左眼眶碎了，他跪在泥里，没再起来。」
- 「`Machine Gun` 的连发横扫他的腰——胸甲被打穿三处，他向侧面倒下，钢盔在泥里咣当一响。」
- 「`Anti-Materiel Rifle` 的弹头穿透他的胸甲，从背后出去——他被打得向后弹了半步，跪下，手还按在胸前的伤口。」
- 「`Heavy Shotgun` 在短距离倾倒整发——半个胸甲被打成蜂窝，他向后倒进战壕的水里。」
- 「`Grenade Launcher` 的弹片在他脚边炸开——他的左小腿被弹片切到见骨，他坐下了，再没起来。」

### W3 — 散弹

- 「`Shotgun` 在 4" 距离开火——他的胸甲被铅丸打凹一片，胸口闷得他坐进泥里。」
- 「`Automatic Shotgun` 的连发咬开他的肩——锁骨断了，半边胳膊垂着，他跪下了。」
- 「`Blunderbuss` 的锈钉和铅丸钉满他的右半身——他向右栽倒，铠甲在泥里咯吱响。」

### W4 — 圣火 / 神圣武器

- 「`Flamethrower` 的火舌罩住他的左半身——他在火里转了半圈，铠甲表面起火，跪下去用泥拍灭，跪着没起来。」
- 「`Holy Smoke` 灼穿 `Heretic Trooper` 的皮肤，像火舔到牛油——他在烟里捂着脸跪下，喉咙里发出炉膛一样的嘶声。」
- 「`Blessed Sabre` 砍中他的肩颈交界——血从盔甲缝里喷出，他跪进泥里，嘴里还在低吟。」
- 「`Heavy Flamethrower` 扫过他的下半身——他从腰部以下烧着了，向前栽倒，火还在烧。」

### W5 — 手雷 / 爆炸

- 「`Frag Grenades` 在他脚下三尺处爆开——左膝被一片弹片打穿，他向后倒进泥水里。」
- 「`Gas Grenades` 的黄绿色雾罩住他——他咳着血跪下了，眼角和鼻腔流出脓水。」
- 「`Incendiary Grenades` 在他身边炸开——铠甲烧红了，他在火里翻滚两圈，跪着没起来。」
- 「`Molotov Cocktail` 砸在他脚边——脚底的火窜上小腿，他向后倒进战壕底的水里灭火，泡在水里不动了。」
- 「`Satchel Charge` 在 5" 外炸开——他被气浪扔出去三步，铠甲背后凹进去一片，他跪着，耳朵里在流血。」

### W6 — 锐器近战

- 「`Bayonet` 刺穿他的肋间——刀尖向上扭了一下才拔出来，他咳着血跪下。」
- 「`Trench Knife` 在铠甲缝里反复找口子，最后插进他的腋下——他坐下了，握不住武器。」
- 「`Sword/Axe` 砍断了他的右臂——胳膊连着一片铠甲掉进泥里，他用左手按着断口跪在那。」
- 「`Misericordia` 钻进他的眼罩缝——刀尖进了一寸半，他向前栽倒，没出声。」
- 「`Flail/Scourge` 缠住他的脖子——铁链头甩到颊骨上，他被甩进泥里，鼻血和颊骨碎片混在一起。」
- 「`Trench Club` 的铁钉砸进他的钢盔顶——盔顶凹一指深，他眼一黑栽倒，钢盔在泥里咣咣响。」

### W7 — 重型近战

- 「`Great Sword/Axe` 斜砍 `Lieutenant` 的左肩——锁骨切断，他单膝跪下，圣物匣掉进泥水里。」
- 「`Great Hammer/Maul` 砸中他的胸甲——铠甲整片塌进去，他坐下了，咳着血。」
- 「`Anti-Tank Hammer` 的爆炸头在他胸甲爆开——他向后弹三步，倒进战壕底，铠甲背面冒着烟。」
- 「`Polearm` 穿透他的大腿——大腿被钉在地上，他试图站起来又跪下，握着腿。」
- 「`Tank-Splitter Sword` 斜砍他的胸甲——铠甲从胸口到右腰被剖开，他向前跪倒。」

### W8 — 异端魔法（占位）

- 「`Heretic Priest` 的低吟从战壕对面传来——他眼里突然流出黑色的血，跪下时还在念信经。」
- 「`Wretched` 在阴影里咯咯笑，关节反向折着扑上来——它的爪子陷进他的胸甲缝，他向后倒进泥里。」
- 「`Infernal Bomb` 在他身边炸开——火里有惨叫，火灼着他的胸甲，他在火里跪着，下半身已经烧黑。」

---

## 结果 D：7-8 — Down 第二次 + 2 BLOOD MARKERS

> 触发：Injury Roll 修正后 7-8，但模型**已经 Down**（→ `rules/02-comprehensive-rules.md#injury-roll-table`）
> 后果：放 **2 个 `BLOOD MARKERS`**（不是 1 个）；模型**仍然 Down**（不是 Out of Action）
> **描述原则**：**伤上加伤**——他还活着，但伤更重了。可以写"额外的伤口" / "气息更淡" / "面具裂得更深"。**不能**升级为 Out of Action 的描述（"他不再动"）——除非骰子真的是 9+。1-2 句。

### W1 — 远程齐射

- 「他还跪在泥里。又一发 `Bolt-Action Rifle` 弹头钉进他的背——他向前栽，胸甲蹭着泥往前滑了半尺。」
- 「他倒在水坑里，刚要撑起来，`Submachine Gun` 又是一连串——胸甲背面被打穿三处，他停下来了。」
- 「他半坐在战壕沿口，又一发 `Pistol` 弹头打中他的腿——他向侧面倒下，握不住武器。」

### W2 — 重型远程

- 「`Sniper Rifle` 第二发——他已经倒着了，弹头钉进他的胸甲，铠甲冒出一股蒸汽。他更不动了。」
- 「`Machine Gun` 又扫了一遍他倒下的位置——他的钢盔被几发打飞，露出的头还在原地。」

### W3 — 散弹

- 「`Shotgun` 在他倒下的身上倾倒整发——铠甲背面被打成蜂窝，他没了一只胳膊以下的形状。」

### W4 — 圣火 / 神圣武器

- 「`Flamethrower` 又罩了他一遍——倒着的身体被罩进火里十秒，铠甲表面起泡，他在火里翻了半圈又停下。」
- 「`Blessed Sabre` 在他倒下的颈侧又补一刀——颈侧的血漫出来，蔓延到面具下缘。」

### W5 — 手雷 / 爆炸

- 「`Frag Grenades` 第二颗炸在他身上——倒着的胸甲又被弹片钉满，他向后翻了半圈。」
- 「`Gas Grenades` 的雾继续罩着他——他在雾里咳出黑红色的水，咳到第三声没声了。」
- 「`Satchel Charge` 在他倒着的身上爆开——爆炸把他抛起半尺又落回泥里，铠甲背面凹进去一大片。」

### W6 — 锐器近战

- 「`Bayonet` 在他倒着的肋下又扎一次——刀尖向心脏方向扭了一下。他还在喘，但很浅。」
- 「`Sword/Axe` 砍中他倒着的脖子——颊骨与肩之间多了一道血。他没出声。」
- 「`Misericordia` 找到他眼罩下的缝——刀尖进了两寸半，他抽搐了一下停下。」

### W7 — 重型近战

- 「`Great Hammer/Maul` 在他倒下的胸甲上又砸一锤——胸甲塌进胸腔，他停止了挣扎站起来的动作。」
- 「`Tank-Splitter Sword` 斜砍他倒着的腰——上半身和下半身之间的铠甲被剖开，他没出声。」

### W8 — 异端魔法（占位）

- 「`Heretic Priest` 的咒文又是一道——倒着的他口里和鼻里都开始流黑血。」
- 「`Wretched` 蹲在他倒下的身上，关节反向折着，爪子陷进胸甲缝里——他抽搐着停下了。」

---

## 结果 E：9+ — Out of Action

> 触发：Injury Roll 修正后 ≥ 9（→ `rules/02-comprehensive-rules.md#injury-roll-table`）
> 后果：模型**移出战场**，本局不归（→ `rules/02-comprehensive-rules.md#out-of-action`）
> **注意**：`TOUGH` 关键词的模型**首次** 9+ 改为 Down（→ `rules/03-keywords-glossary.md#tough` / `rules/02-comprehensive-rules.md#out-of-action`）；本结果描述用于**实际触发** Out of Action 的情形。
> **描述原则**：**最重**——他**不再动了**，但**不必**写得过于戏剧化。grimdark 的死亡是平淡的、被踩进泥里的、没有遗言的。2-3 句，30-60 字。**不要内心戏 / 不要遗言 / 不要家人**（→ `tone-guide.md` ❌ 禁区）。

### W1 — 远程齐射

- 「`Bolt-Action Rifle` 的弹头从他的太阳穴入，从对侧出。钢盔里现在装的是一团红泥。他不再动。」
- 「`Submachine Gun` 的连发把他的胸甲打成蜂窝。他向后倒进泥里，圣物匣还在弹跳，他不动了。」
- 「`Pistol` 的两发都钻进他的下颌——下颌没了。他在水坑里仰躺，头盔的玻璃眼镜片碎了，里面什么都看不见了。」
- 「`Musket` 的铅球打中他的额头——额头碎了。他向后倒进战壕底，钢盔在泥里咣当响了三下。他不动了。」

### W2 — 重型远程

- 「`Sniper Rifle` 在 40" 外咳了一声。他的胸前出现一个洞，背面出现一个更大的洞。他向前栽倒在泥里。」
- 「`Anti-Materiel Rifle` 的弹头穿透了他的胸甲——胸甲背面也开了花。他飞起来落回去，胸前是一片红泥。他不动了。」
- 「`Machine Gun` 横扫他的腰——他被切成两段。两段都在泥里。」
- 「`Heavy Shotgun` 在 5" 倾倒整发——胸甲不见了，胸腔里也不见了大半。他向后栽进水坑。」
- 「`Grenade Launcher` 的弹片在他脚下炸开——他向上飞起两尺再落下，落下的时候已经没了下半身。」

### W3 — 散弹

- 「`Shotgun` 在 3" 内倾倒整发——他的脸消失了。他向后倒进战壕底，钢盔与一片红混在一起。」
- 「`Automatic Shotgun` 的连发把他的胸甲打成蜂窝——铠甲背面渗出血。他跪着没起来，然后倒下。」
- 「`Blunderbuss` 的整桶锈钉和铅丸钉满他的上半身——他向后栽倒，胸前竖着十几根钉。他不动了。」

### W4 — 圣火 / 神圣武器

- 「`Flamethrower` 罩住他的整个身体。他在火里转了一圈，倒下，火继续烧。三秒后他不再动了。」
- 「`Holy Smoke` 灼穿了 `Heretic Trooper` 的全部皮肤——他在烟里跪下，钢铁面具下传出最后一声炉膛的嘶声，然后停了。」
- 「`Blessed Sabre` 横切了他的脖子——头落进了战壕底的水里，身子保持站姿停了半秒才倒下。」
- 「`Heavy Flamethrower` 罩了他三秒——铠甲熔了一片，他不再有完整的形状。」

### W5 — 手雷 / 爆炸

- 「`Frag Grenades` 在他胸口爆开——胸前是一片红雾。他倒下时已经没了头。」
- 「`Gas Grenades` 罩住他十秒——他在雾里抽搐，停止了。脸是黄绿色的，鼻孔里漏出脓水。」
- 「`Incendiary Grenades` 把他变成一根燃烧的柱子——他在火里站了三秒，倒下时已经烧黑了。」
- 「`Molotov Cocktail` 砸碎在他的胸甲上——油泼了他整个上半身，火窜起来。他向后栽倒，火继续烧。」
- 「`Satchel Charge` 在他脚下爆开——爆炸把他抛起一人高再摔回泥里。他的腰以下消失了。」

### W6 — 锐器近战

- 「`Bayonet` 贯入肋间，向上扭了一下才拔出来。他咳了一口血到面具内壁。然后他不再呼吸。」
- 「`Sword/Axe` 砍下了他的头——头落在他自己的钢盔旁。身体跪了两秒才向前栽。」
- 「`Misericordia` 钻进他的眼罩缝——刀刃整根没入，攻击者拔出时带出一团红。他没出声。」
- 「`Trench Knife` 在他的脖子上来回切了两次——颈动脉断了，他向前栽到攻击者的脚边。」
- 「`Flail/Scourge` 把他的头骨砸开——铁链头嵌在颊骨里。他倒下时铁链还嵌着。」
- 「`Trench Club` 反复砸他的钢盔——钢盔凹成一团，里面也凹成一团。他不再有动作。」

### W7 — 重型近战

- 「`Great Sword/Axe` 斜砍过 `Lieutenant` 的左肩——刀尖从右腰下穿出。`Lieutenant` 的圣物匣掉进泥水里。他不再动了。」
- 「`Great Hammer/Maul` 砸碎了他的胸甲与胸腔——铠甲表面是平的，下面没有形状。他向后栽倒。」
- 「`Anti-Tank Hammer` 在他胸前爆开——铠甲与肉一起炸出去半个圆。他的下半身保持站姿停了一秒才倒下。」
- 「`Polearm` 从他腋下贯入，从背后出来——他被钉在原地，挣扎两秒后停下。」
- 「`Tank-Splitter Sword` 砍下他的上半身——上半身落在脚边，下半身还跪着，又过两秒才倒。」

### W8 — 异端魔法（占位）

- 「`Heretic Priest` 的咒文在他耳边响完最后一节——他的颅骨从内部炸开，血从面具的眼罩缝里喷出来。他向前栽倒。」
- 「`Wretched` 把爪子捅进他的胸甲缝——爪子在里面搅了一圈，拔出来时带出了心脏。」
- 「`Infernal Bomb` 在他脚下炸开——火里有惨叫，他被炸成几块。各块在火里继续燃烧。」

---

## 结果 F：Bloodbath（3D6 或 DEADLY 4D6 全加）

> 触发：对手花 **6 `BLOOD MARKERS`**（目标已 Down → **3** `BLOOD MARKERS`）将 Injury Roll 改为 **3D6 全加**；若武器带 `DEADLY` 关键词 → **4D6 全加**（→ `rules/02-comprehensive-rules.md#bloodbath-rolls`）
> 后果：取决于全加之后的结果——可能 9+ Out of Action、也可能 7-8 Down、也可能 2-6 Minor Hit。**Bloodbath 是"放大伤害"的赌注**，不一定 = Out of Action。但**预期值很高**：3D6 期望 = 10.5，4D6 期望 = 14。
> **描述原则**：**比平常更壮观、更彻底**——`BLOOD MARKERS` 的"伤情积累"在这一刻**兑现**。可以写"那些之前的伤口一起裂开" / "失血累积到崩溃" / "毒气积累到肺彻底糊" / "炮震叠加到大脑断电"。2-3 句，30-60 字；多模型受影响时（`BLAST` 武器）每模型 ≤ 1 句，全部 ≤ 4 句（→ `tone-guide.md#描述长度规范`）。

### W1 — 远程齐射（Bloodbath）

- 「`Heretic Trooper` 已经吃过四发——`BLOOD MARKERS` 兑现的时刻。再一发 `Bolt-Action Rifle` 弹头从他的颈侧入——之前所有伤口同时往外冒血。他向前栽，倒下时已经空了。」
- 「`Submachine Gun` 的连发在他身上找到了之前留下的每一处口子——那些口子同时炸开。他向后倒进泥里，胸前是一片红海。」

### W2 — 重型远程（Bloodbath）

- 「`Sniper Rifle` 的 `CRITICAL` 在 3D6 全加下兑现——他的头部和胸腔一起被打穿。胸前与背后各一个洞，洞之间能透光。他不动了。」
- 「`Machine Gun` 的连发在他的胸甲上找到每一个之前留下的凹痕——那些凹痕同时被打穿。胸甲背面是一片红雾。」

### W3 — 散弹（Bloodbath）

- 「`Shotgun` 在 4" 倾倒整发——之前他身上的所有 `BLOOD MARKERS` 兑现了：胸甲下面的每一块组织同时被铅丸打散。他向后倒进战壕底的水里，水变红。」

### W4 — 圣火 / 神圣武器（Bloodbath）

- 「`Flamethrower` 罩住已经焦黑的他——之前的所有焦伤一起加深。他的铠甲熔成红色的液体，沿着腿流下。他没了形状。」
- 「`Heavy Flamethrower` 在他身上烧了五秒——之前所有的灼伤现在一起穿透铠甲。他从背面也冒出火来。」

### W5 — 手雷 / 爆炸（DEADLY → 4D6 Bloodbath）

> `Satchel Charge` / `Frag Grenades` 等触发 `BLAST` 命中多模型时，Bloodbath 仍按本次 Injury Roll 单独算（每个被命中模型各掷各的）。`DEADLY` 关键词的武器进 Bloodbath 时为 **4D6 全加**。

- 「`Satchel Charge` 在三个 `Yeoman` 中间爆开——`BLAST 3"` 命中全部。第一个被气浪扔出去落地时已经没了头盔；第二个的胸甲背面凹陷一片，他向前栽倒不动了；第三个跪在原地，铠甲表面还在冒烟，他坐下了。」
- 「`Infernal Bomb` 在 4D6 Bloodbath 下兑现——他被炸成三块。各块在火里继续燃烧。火里有惨叫，惨叫持续了三秒。」（W5+W8 交界，`DEADLY` 触发，→ 待 Pass 9 回流 `Infernal Bomb` 关键词）
- 「`Gas Grenades` 罩住他已经咳了三回合的肺——肺这一秒彻底糊掉。他在雾里向前栽倒，脸是黄绿色。」

### W6 — 锐器近战（Bloodbath）

- 「`Trench Knife` 在他身上之前所有 `BLOOD MARKERS` 兑现的位置都来一刀——刀像挑选已经裂开的果皮。他倒下时身上有十几道开放伤，没有一道是新的。」
- 「`Misericordia` 在他眼罩缝里反复扎——已经流血的位置同时被找到。他停了。」

### W7 — 重型近战（Bloodbath，可能 4D6 若武器 `DEADLY`）

- 「`Anti-Tank Hammer` 的爆炸头在他胸前爆开——他身上之前的所有铠甲凹陷同时被穿透。爆炸把他抛起又落下，落下的是一团铠甲与肉的混合物。」
- 「`Tank-Splitter Sword` 斜砍他的胸甲——`BLOOD MARKERS` 兑现：胸甲从胸口到大腿根被剖开，伤口暴露的不只是肋骨。他向前跪倒，跪下又向前栽。」
- 「`Great Hammer/Maul` 砸中他的胸甲——之前他承受的所有锤击在这一锤下叠加：胸甲与胸腔同时塌成一片。他向后栽倒不再有起来的形状。」

### W8 — 异端魔法（占位，Bloodbath）

- 「`Heretic Priest` 的咒文这一段累积了之前所有的低吟——他的颅骨从内部炸开，血从面具每个缝隙喷出，铠甲下也开始渗血。他向前栽倒。」
- 「`Wretched` 蹲在他身上，关节反向折着，爪子在他的胸甲缝里搅——之前已经流血的每个口子同时裂开。他不再动。」（待 Pass 9 回流 `Wretched` 异能名）

---

## 跨结果适用的修辞守则

适用于上方矩阵所有 cell 的共通约束（与 `→ narrative/tone-guide.md` 配合阅读）：

### 1. 武器名 / 模型名 / 关键词保留英文原文

- ✅ `Bolt-Action Rifle` / `Heretic Trooper` / `Holy Smoke` / `Wretched` / `BLOOD MARKER`
- ❌ "栓动步枪"作主名 / "异端兵"作主名 / "圣烟"作主名（首次出现可加中文注释，**主名**仍用英文）
- 详见 `→ narrative/tone-guide.md#禁区` "❌ 模型名 / 武器名翻译漂移"

### 2. ALL-CAPS 关键词用反引号

- `BLOOD MARKER` / `BLESSING MARKER` / `DEADLY` / `BLAST` / `PENETRATING` / `IGNORE ARMOUR`
- 详见导入指南 §3.7.I.2

### 3. 长度按 `tone-guide.md` 规范

| 结果 | 推荐句数 / 字数 |
|---|---|
| **A. No Effect** | 0-1 句 / 5-15 字 |
| **B. Minor Hit** | 1 句 / 10-25 字 |
| **C. Down 首次** | 1-2 句 / 20-40 字 |
| **D. Down 第二次** | 1-2 句 / 20-40 字 |
| **E. Out of Action** | 2-3 句 / 30-60 字 |
| **F. Bloodbath（单模型）** | 2-3 句 / 30-60 字 |
| **F. Bloodbath（BLAST 多模型）** | 每模型 ≤ 1 句，总 ≤ 4 句 |

### 4. 不要复述规则

描述完事件后**不要**附"这意味着模型现在 Down 了" / "这次伤害绕过了铠甲"——规则结果应当作**已知**（在 match-state 里）。描述只给**感官画面**。

例外：`Out of Action` / `Down` 状态变化在描述末尾可**陈述式**带一句（"他不再动了" / "他跪下了"），与 `→ tone-guide.md` Example 5（Morale Phase 失败后陈述规则）一致。

### 5. 不要替模型加内心戏

- ❌ 「他想起教堂的钟声」 / 「他后悔没用 Blessing Marker」 / 「他在心里默念家人的名字」
- ✅ 只描述战场上**外部可见**的事实——伤口、姿势、声音、铠甲变形、液体、烟、土
- 详见 `→ narrative/tone-guide.md#禁区` "❌ 超出当前战场的剧情发展"

### 6. 不要对玩家挑衅或社交

- ❌ "嘿嘿，你的 `Yeoman` 倒下了" / "这次出招很糟糕"
- ✅ 只陈述事实：「`Yeoman` 跪在泥里」
- AI 是对手玩家，不评论玩家表现——详见 `→ narrative/tone-guide.md#AI-角色定位`

### 7. 不要软化（PG-13 禁区）

- ❌ "他受了轻微的擦伤但仍然能战斗" → 该写 `Minor Hit` 的具体感官（"弹片擦掉一块软骨"）
- ❌ "他被打晕了" → `Down` 是**具体的伤**，不是被打晕
- ✅ 让伤情的**重量**与规则结果对齐：`Minor Hit` = 看得见的浅伤；`Down` = 还活着的重伤；`Out of Action` = 死亡或濒死

### 8. 不要让叙事推翻规则

**绝对禁区**。详见 `→ narrative/tone-guide.md#核心原则` + Example 1-4：

- 骰子结果是事实，描述只能解释这个事实
- 不存在"虽然出 9+ 但叙事上他撑住了" / "虽然失败但叙事上扰乱敌方阵型"

### 9. Bloodbath 是放大不是新规则

- Bloodbath 通过**全加 3D6 / 4D6** 放大伤害——它本身**仍是**一次 Injury Roll
- 不要把 Bloodbath 写成"全军覆没"（除非 `BLAST` 命中多模型 + 各自结算后**真的**多模型 Out of Action）
- Bloodbath 触发是"对手花了 6 `BLOOD MARKERS`（已 Down 则 3）"的代价兑现，所以描述可以**叙事性地把那些累积的伤一并兑现**——但不要超出当前模型的伤情

### 10. 异端魔法 / Goetic 占位

W8 的具体武器名、关键词、伤害类型在 v0.1 **未完整确定**——Pass 9 完成 `warbands/02-heretic-legions.md` 后，回流本文件补全：

- Heretic Priest 法术列表 / Goetic Powers（如 Pass 9 包含此子系统）
- `Wretched` 异能名 / 攻击描述
- `Infernal Bomb` 是武器还是异能（影响归类 W5 还是 W8）

**当前 v0.1 阶段**：W8 cell 只给 2-3 例占位描述，AI 调用时优先用 W3 / W5 cell + `→ narrative/world-primer.md` §3 异端军团调色板代偿。
