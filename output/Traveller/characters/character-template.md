# Classic Traveller — 角色创建模板

> 参照：`rules/book1-characters.md` § Character Generation
> 完整创建例子参考 Alexander Jamison 案例（book1-characters.md 第 895 行起）

## 创建步骤

1. **UPP 属性**（六项各投 2D，转十六进制）：
   - Strength (Str)
   - Dexterity (Dex)
   - Endurance (End)
   - Intelligence (Int)
   - Education (Edu)
   - Social Standing (Soc)
   - 结果写作 6 位 hex 串，如 `787C46`

2. **选择 career**：Navy / Marines / Army / Scouts / Merchants / Other。查 Enlistment throw。失败则 draft（随机抽一个服役）。

3. **每 term（4 年）**：
   - a. **Survival throw**（失败后果视裁判决定——原 1977 版为死亡，建议改为 injured/discharged）
   - b. **Commission throw**（若尚未是军官）
   - c. **Promotion throw**（若已 commissioned 且本 term 未升）
   - d. **Skill acquisition**：本 term 获得 `1 skill + (+1 若 commission 本 term) + (+1 若 promotion 本 term) + (+1 若第一 term)`。每个 skill roll 前选 Personal Development / Service Skills / Advanced Education / Advanced Education (Edu 8+ 开放) 四表之一
   - e. **Aging check**（34 岁起每 4 年一次，检 Str / Dex / End）
   - f. **Reenlistment throw**

4. **Mustering Out**：
   - 总 benefit rolls = terms served + (1 per rank achieved 到最多 3)
   - 选择 Cash Table 或 Material Benefits Table（Cash 最多抽 3 次）
   - 每 roll 可用 rank DM（见职业表）
   - 高 Soc / 特定服役 / pension 取得可能

5. **Skill 上限**（errata）：角色持有的 skill 总 **level 数 ≤ Int + Edu**（level-0 不计）

## state.yaml schema

```yaml
party:
  {character_id}:                # 如 jamison, kira, voss
    name: "Full Name"
    upp: "787C46"                # 6-位 hex
    age: 38
    terms: 5
    career: "Merchant"           # Navy / Marines / Army / Scouts / Merchants / Other / Drafted
    rank: "Captain (ret.)"       # 包含 pension 状态
    credits: 31200               # 当前 Cr
    pension: 4000                # Cr/year（若有）
    ship_shares: 0               # 拥有的 ship share 数
    skills:                      # 等级 1+ 全列；level-0 单独存 skills_level_0
      Pilot: 1
      Vacc: 1
      Streetwise: 1
      Engineering: 1
      Navigation: 1
      Medical: 1
    skills_level_0: []           # e.g. ["Brawling", "Gambling"]
    wounds:                      # CT 伤害直接进属性
      str: 0
      dex: 0
      end: 0
    gear:                        # 随身装备（独立于船上货物）
      - "Revolver"
      - "Vacc Suit-0"
    notes: ""                    # 背景、resentments、人物钩
```

## 属性 DM 速查

CT 没有统一"modifier"概念，但创角表会用 "DM +n if X ≥ threshold" 形式给 DM。典型门槛：

- **Commission / Promotion / Advanced Education**：相关属性 7+ 或 8+ → DM +1 或 +2
- **Survival**：End 或 Int 8+ → DM +2
- **Enlistment**：Int / Edu / End / Dex / Soc 某项 8+/9+ 依职业而定

具体数值必查 `rules/book1-characters.md` § 各职业 Prior Service Table。

## 创建速查（典型值）

| 元素 | 典型投掷 |
|---|---|
| UPP 六项 | 各 2D；平均 7 |
| Enlistment | 职业-specific throw，e.g. Navy 8+、Merchants 7+ |
| Survival | 职业-specific，e.g. Navy 5+、Scouts 7+ |
| Commission | 职业-specific，e.g. Army 5+、Scouts N/A（无军衔） |
| Promotion | 职业-specific |
| Reenlistment | 职业-specific，e.g. 通常 5+ 或 6+ |

## 典型完成角色（Jamison 参考）

```yaml
jamison:
  name: "Alexander Lascelles Jamison"
  upp: "787C46"
  age: 38
  terms: 5
  career: "Merchant"
  rank: "Captain (ret.)"
  credits: 31200     # errata 校正值（非原书 33,200）
  pension: 4000
  ship_shares: 30    # 30/40 年贷款已还
  skills:
    Pilot: 1
    Vacc: 1
    Streetwise: 1
    Engineering: 1
    Navigation: 1
    Medical: 1
  wounds: {str: 0, dex: 0, end: 0}
  notes: "Retired at peak by merchant service. Mild resentment. Owns a Type A Free Trader."
```
