# Mothership Character Template

> Mothership 1e 角色创建步骤 + 角色卡字段映射 + `state.yaml` schema。
> 规则出处：`rules/psg-character-creation.md`、`rules/psg-skills.md`、`rules/psg-equipment.md`、`rules/psg-checks-and-stress.md`。
> 参照角色卡：`Rule Books/OSR related/Mothership/supplyment/Character Sheet v5.11 (ZH, landscape).pdf`（v5.11 中译横版）。
> 角色术语：监守 = **Warden**（不是 GM/DM/Keeper）。

---

## 创建步骤（Warden 引导，9 步）

详见 `rules/psg-character-creation.md`，本节为速查清单。

| # | 步骤 | 投骰 / 选择 | 备注 |
|---:|---|---|---|
| 1 | 投属性 | 每项 **2d10+25** | 力量 / 速度 / 智力 / 战斗 |
| 2 | 投豁免 | 每项 **2d10+10** | 理智 / 恐惧 / 身体 |
| 3 | 选职类 + 应用调整 | 4 选 1 | 见下方[职类调整表](#职类调整) |
| 4 | 投生命值 | **1d10+10** | 损伤数上限初始 = **2**（仿生人/陆战队员 = **3**） |
| 5 | 获得起始压力 | 压力下限初始 = **2** | 当前压力 = 下限 |
| 6 | 标注职类创伤反应 | 见下方[职类创伤反应](#职类创伤反应) | 角色卡固定圈出对应文字 |
| 7 | 标注职类技能 + 选奖励技能 | 见下方[职类起始技能与奖励](#职类起始技能与奖励) | 选专家/大师必须有前置 |
| 8 | 投装备 | 行装 / 饰品 / 贴章 | 见 `rules/psg-equipment.md` 各 d10 表 |
| 9 | 投起始信用点 | **2d10×10** cr | 用于补充行装外的装备 |

---

## 职类调整

| 职类 | 属性调整 | 豁免调整 | 损伤上限 |
|---|---|---|---:|
| **陆战队员 Marine** | +10 战斗 | +10 身体, +20 恐惧 | +1（共 3） |
| **仿生人 Android** | +20 智力, **−10 任选 1 项** | +60 恐惧 | +1（共 3） |
| **科学家 Scientist** | +10 智力, +5 任选 1 项 | +30 理智 | 2 |
| **技工 Teamster** | 全部 +5 | 全部 +10 | 2 |

> 陆战队员/仿生人通过损伤上限 +1 体现"硬度"；科学家专精理智；技工万金油。

---

## 职类创伤反应

只触发本职类那条，**不影响**其他玩家的常规规则。

| 职类 | 触发条件 | 效果 |
|---|---|---|
| **陆战队员** | 你陷入惊恐时 | 所有临近友方玩家进行 1 次恐惧豁免 |
| **仿生人** | 临近友方玩家进行恐惧豁免时 | 该豁免带 **劣势 [−]** |
| **科学家** | 你理智豁免**失败**时 | 所有临近友方玩家 +1 压力 |
| **技工** | 每游戏场次一回 | 你某次惊恐检定带 **优势 [+]** |

---

## 职类起始技能与奖励

| 职类 | 起始技能（前置） | 奖励技能 |
|---|---|---|
| **陆战队员** | 军事训练, 运动 | 1 专家 **或** 2 受训 |
| **仿生人** | 语言学, 计算机, 数学 | 1 专家 **或** 2 受训 |
| **科学家** | 1 大师技能 + 该大师的 1 前置专家 + 1 前置受训 | 1 受训 |
| **技工** | 工业装备, 零重力 | 1 受训 + 1 专家 |

> 技能完整列表 + 前置链 + 加值（受训 +10 / 专家 +15 / 大师 +20）见 `rules/psg-skills.md`。

---

## 角色卡字段映射

参照 v5.11 横版角色卡，所有可写字段：

### 个人信息（Personal）
- 角色名称 (character_name)
- 性别代称 (pronouns)
- 个人笔记 (personal_notes)
- 玩家姓名 (player_name)
- 最高分 (max_score) — 死后写入名册用

### 属性（Stats，2d10+25）
- 力量 (strength) / 速度 (speed) / 智力 (intellect) / 战斗 (combat)

### 豁免（Saves，2d10+10）
- 理智 (sanity) / 恐惧 (fear) / 身体 (body)

### 职类（Class）
- class: marine | android | scientist | teamster

### 生命值与损伤（Health & Wounds）
- hp: 当前 / 上限（1d10+10）
- wounds: 当前 / 上限（marine, android = 3；scientist, teamster = 2）

> 当 hp 降至 0 以下 → 遭受 1 损伤，hp 重置为上限再扣后续超额伤害；损伤超出上限 → 死亡。详见 `rules/psg-combat.md`。

### 压力与惊恐（Stress & Panic）
- stress: 当前 / 下限（起始下限 = 2）
- panic_min: 当前下限（每次惊恐检定后可能上升）

### 技能（Skills）
- trained_skills: [...]   # 受训 +10
- expert_skills: [...]    # 专家 +15
- master_skills: [...]    # 大师 +20

### 训练中（Skill Training）
- training_in_progress: 技能名 / null
- training_time_remaining: 剩余周数 / null

### 状态（Status / Conditions）
- conditions: [...]   # 出血 / 缺氧 / 辐射病 / 受感染 等，见 `rules/psg-survival.md`

### 装备（Equipment）
- loadout: [...]   # 行装清单（每行装包含若干物品）
- trinkets: [...]  # 饰品 d100
- patches: [...]   # 贴章 d100
- armor: 名称 + AP
- weapons: [...]
- credits: 信用点（起始 2d10×10）

---

## `state.yaml` 角色字段 schema

```yaml
party:
  {pc_id}:                          # slug，如 vance / 7-of-9 / dr-elsa
    name: "Vance Calder"
    pronouns: he/him
    player_name: "Jack"             # 桌外玩家
    class: marine                   # marine | android | scientist | teamster
    max_score: 0                    # 当前最高分（属性+豁免之和峰值），死亡时录入名册

    personal_notes: |
      退役准下士。前 OCRM。手腕里有内置弹仓追踪器（不工作了）。

    # 属性（current / max；max 是创角时确定的初始值，伤害可临时降低 current）
    stats:
      strength:  {current: 38, max: 38}
      speed:     {current: 41, max: 41}
      intellect: {current: 30, max: 30}
      combat:    {current: 55, max: 55}   # +10 (marine)

    # 豁免
    saves:
      sanity: {current: 28, max: 28}
      fear:   {current: 47, max: 47}      # +20 (marine)
      body:   {current: 35, max: 35}      # +10 (marine)

    # 生命值（HP）— 1d10+10，扣到 0 以下时损伤+1 并重置
    hp: {current: 18, max: 18}

    # 损伤（Wounds）— marine/android 上限 3，scientist/teamster 上限 2
    wounds: {current: 0, max: 3}

    # 压力 / 惊恐
    stress:
      current: 2                    # 起始 = 下限
      min: 2                        # 上岸休假可降，惊恐可升
    # 注：Panic 检定 = d100 ≤ 当前压力即陷入惊恐，详见 rules/psg-checks-and-stress.md

    # 技能（按等级分桶；选专家/大师必须先有前置受训/专家）
    skills:
      trained:  ["军事训练", "运动", "驾机"]    # +10
      expert:   ["枪械"]                         # +15
      master:   []                               # +20

    # 技能训练（受训 1 周 / 专家 2 周 / 大师 4 周；上岸休假期间）
    training:
      in_progress: null              # 技能名 / null
      weeks_remaining: 0

    # 状态：出血 / 缺氧 / 辐射 / 感染 / 失血过多 / 燃烧 等（见 psg-survival.md）
    conditions: []

    # 装备
    armor:
      name: "Standard Battle Dress"
      ap: 7                          # 护甲值；超量伤害可击破
      oxygen_minutes: null           # 战斗服无；真空服 / 装甲服才有
      speed_penalty: 0
      special: ""

    weapons:
      - name: "脉冲步枪"
        damage: "2d10"
        range: "近 / 远 / 极远"
        ammo: {current: 30, magazine: 30}
        special: ""
      - name: "战斗刀"
        damage: "1d5"
        range: "邻接"
        ammo: null

    loadout:                         # 投得的行装组（含组里所有内容）
      - "Excursion 行装：信号弹 ×3, 急救包, 求生帐, ..."
    trinkets:                        # 饰品 d100（叙事道具，无机械效果）
      - "退役军牌"
    patches:                         # 贴章 d100
      - "OCRM 师徽"
    inventory: []                    # 散装物品

    credits: 130                     # 起始 2d10×10

    # 死后录入名册（roster）；死亡时 Warden 在 mission-log 里加一行 + 这里填
    death:
      cause: null
      session: null
      final_action: null
```

---

## 关键机制速查（Warden 提醒）

### 投骰
- **属性 / 豁免检定**：投 d100，**严格小于**属性即成功；≥ 属性或 ≥ 90 则失败 + **+1 压力**；00 总关键成功，99 总关键失败
- **关键 (Critical)**：个十位相同（00, 11, 22 ... 99）→ 关键成功或失败
- **优势 [+]**：投 2 次 d100，取**较低**
- **劣势 [−]**：投 2 次 d100，取**较高**
- **技能加值**：成功率提升等同于技能等级（受训 +10 / 专家 +15 / 大师 +20）
- 详见 `rules/psg-checks-and-stress.md`

### 压力 → 惊恐
- 检定**失败** → +1 压力
- **关键失败** → 进行 **惊恐检定（Panic Check）**
- Panic = **1d20** ≤ 当前压力 → 陷入惊恐，查惊恐表（仿生人改投 **2d10+压力** 查 `supplements/android-background.md` 专属表）
- 上岸休假可将压力降回下限；下限本身随经历缓慢上升

### 战斗与死亡
- HP=0 以下 → wounds +1，HP 重置为 max 后扣超额
- wounds 超过上限 → 死亡（关键失败的伤害投骰可能直接致命，查损伤表）
- 详见 `rules/psg-combat.md`

### 大气与生存
- 真空 / 有毒大气 / 缺氧 / 辐射 / 出血 / 低温 / 疲惫 / 食物 / 温度 / 医疗 全部见 `rules/psg-survival.md`
- 护甲服的 oxygen_minutes 是核心限制变量

### 经济
- 起始 2d10×10 cr → 通常勉强凑齐 1 件武器 + 1 件护甲
- 工作报酬：基础 = 受训技能数 × 500 + 专家 × 1000 + 大师 × 2000（每月）× 危险津贴 ×1-×5
- 详见 `rules/wom-campaign-design.md` § 工作应给多少钱

### 角色提升
- **没有等级 / 经验**
- 上岸休假：可将当前压力转化为豁免提升（详见 `rules/psg-port-and-crew.md`）
- 技能训练：上岸期间花周数 + 信用点学新技能
- 长期：财富 / 飞船 / 盟友 / 赛博殖装 / 知识 / 人情 才是真正的"升级"

---

## 新建 PC 流程（Warden checklist）

- [ ] 问玩家：先选职类还是先投属性？（不同顺序影响 −10 任选项的策略）
- [ ] 投 4 次 2d10+25 → 力量 / 速度 / 智力 / 战斗
- [ ] 投 3 次 2d10+10 → 理智 / 恐惧 / 身体
- [ ] 选职类 → 应用属性 / 豁免 / 损伤上限调整
- [ ] 投 1d10+10 → 生命值上限
- [ ] 标 starting stress = 2，损伤上限按职类
- [ ] 圈出本职类的创伤反应
- [ ] 标注职类起始技能 + 投奖励技能
- [ ] 投装备：行装组 + 饰品 + 贴章（d100 表见 `rules/psg-equipment.md`）
- [ ] 投信用点 2d10×10，剩余可买装备 / 武器 / 护甲
- [ ] 起个角色名、定性别代称、写一行个人笔记
- [ ] 把以上写进 `saves/{active}/state.yaml` 的 `party.{pc_id}` 节点
- [ ] 在 `mission-log.md` 记一笔："{name}（{class}）加入乘组"
- [ ] **重要**：提醒玩家这是 sci-fi horror，**死亡常态**，鼓励团队配合

---

## 角色卡 PDF 文件（Warden 备用）

| 文件 | 用途 |
|---|---|
| `Character Sheet v5.11 (ZH, landscape).pdf` | 中译横版，单页全字段（推荐打印） |
| `Character Sheet v5.11 (ZH, 2-page print).pdf` | 中译竖版双页 |
| `Character Sheet (Basic).pdf` | 英文基础版 |
| `Character Sheet (Advanced).pdf` | 英文进阶版（含飞船 / 战役额外字段） |

均位于 `Rule Books/OSR related/Mothership/supplyment/`。
