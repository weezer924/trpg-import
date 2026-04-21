# Classic Traveller — Book 2: Space Combat

> 源 PDF：`Rule Books/Traveller/Classic Traveller/Classic Traveller (Facsimile 1981 edition).pdf`
> 版本：1981 年修订版（GDW LBB 1-2-3 合订复刻）
> 对应原书页：Book 2 pp. 27–37（PDF p. 82–92）
> 本文件覆盖：Space Combat 全章（流程、移动、激光/导弹、命中定位、数据卡、损管、遭遇表、行星模板）
> Errata：本文件已合并 Don McKinney's Consolidated Traveller Errata 中的修订（Pulse Lasers / Decompression / Expendables / Starship Encounters Table）。原 1981 版错误见源 PDF p.154–158。

## Index

1. [Overview](#overview)
2. [Basic Parameters](#basic-parameters)
3. [Turn Sequence](#turn-sequence)
4. [Preparation for Play](#preparation-for-play)
5. [Movement](#movement)
6. [Gravity](#gravity)
7. [Laser Fire](#laser-fire)
   - [Pulse Lasers](#pulse-lasers-errata-insert)
8. [Laser Return Fire](#laser-return-fire)
9. [Ordnance Launch](#ordnance-launch)
   - [Reloading](#reloading)
   - [Missile Detonation](#missile-detonation)
10. [Attacker's & Defender's DMs](#attackers--defenders-dms)
11. [Hit Locations](#hit-locations)
12. [Critical Hits](#critical-hits)
13. [Ship's Data Card Example](#ships-data-card-example)
14. [Game Turn Sequence](#game-turn-sequence)
15. [Detection](#detection)
16. [Damage Definitions](#damage-definitions)
17. [Special Situations](#special-situations)
    - [Decompression](#decompression)
    - [Atmospheric Braking](#atmospheric-braking)
    - [Abandon Ship](#abandon-ship)
    - [Damage Control](#damage-control)
    - [Repair Parts](#repair-parts)
    - [Expendables (errata insert)](#expendables-errata-insert)
18. [Starship Encounters](#starship-encounters)
19. [Planetary Templates](#planetary-templates)
20. [Standard Worlds](#standard-worlds)

## Key Terms

| 缩写 | 含义 |
|---|---|
| `G` | Gravity（重力/加速度单位；1 G = 10,000 km 在 1000 秒内产生的速度变化 = 100 mm/turn） |
| `DM` | Dice Modifier（骰修正） |
| `CPU` | Computer 中可同时运行的程序容量（另见 Storage） |
| `Cr` | Credit（信用币），`MCr` = Mega-credit = 百万信用币 |
| `Pilot-n` / `Gunner-n` | Pilot/Gunnery skill 等级 |
| `Ablat` / `Reflec` | 消融/反射护甲（对激光专用） |
| `Suffix P` on ship code | 该船为海盗/可能攻击 |
| `*` on ship code | 该遭遇还伴随一个小型飞行器（small craft）遭遇 |

## Overview

When starships encounter in space, they may be forced into battle as a result of circumstance. Starship battles may be resolved by spaceship combat with miniatures in accordance with the following rules. These rules serve well in nearly all situations, from simple encounters where a free trader attempts to outrun a pirate or revenue cutter, to the complex engagements between starship squadrons of rival systems or empires.

## Basic Parameters

Starship combat uses the following scale for movement and combat resolution:

1. **Time:** Each game turn represents 1,000 seconds.
2. **Space:** A playing surface is required, representing space as a two-dimensional surface at the scale of 1:100,000,000; one millimeter equals 100 kilometers. Three meters equal one light-second. Planetary template disks may be produced to show the presence of worlds and the effects of gravity.
3. **Thrust:** Maneuver drive thrust is measured in Gs (gravities) expressed as a vector of both length and direction. While direction is variable, the length of the arrow is represented at the scale 100 mm equals 1 G (1,000 seconds acceleration at 1 G will produce a velocity change of 10,000 km, or 100 mm in scale, per turn).
4. **Units:** Starships and space vehicles are individually represented by spacecraft miniatures, or (if necessary) by counters or markers. Because spacecraft miniatures are almost certainly oversize for the scale in use, each should be marked with a spot or point to designate the exact true location of the ships in play.

## Turn Sequence

Starship miniatures battles are resolved in a series of game turns, each representing 1000 seconds elapsed time. Most battles, regardless of the number of ships or players participating, will involve only two sides. These two sides alternate player turns within a game turn. Thus, each 1000 second game turn includes two player turns, one for each combatant side. Each player turn is further divided into several phases which allow specific activity to be performed in a regular, orderly manner.

For convenience, the two sides in the battle are referred to as the **intruder** and the **native**. This terminology is intended to avoid possible confusion when one side is called the attacker but is in reality defending. Other terms could (and sometimes should) be used instead.

The sequence of the complete turn is given in the [Game Turn Sequence](#game-turn-sequence) table. Activity must be performed only in the appropriate phases of the game turn or player turn; for example, spacecraft may not move during the laser fire phase, ordnance may only be launched during the ordnance launch phase, and computers may only be reprogrammed in the computer reprogramming phase.

## Preparation for Play

Each ship involved in space combat must have a data card prepared for it. This card contains basic information about the ship, serving as a reference for the players during the course of the battle. As damage occurs, it is marked on the card to reduce the ship's abilities in later turns.

To prepare a data card, note the name and ship type on the top line of a blank 3 × 5 index card. Below the name, on succeeding lines along the left side of the card, write the six basic sections of the ship, followed by their capacities or values:

1. **M-drive** (followed by the drive letter)
2. **Power plant** (followed by the power plant letter)
3. **J-drive** (followed by the drive letter)
4. **Fuel** (followed by the fuel tonnage)
5. **Hold** (followed by the cargo hold tonnage and all vehicles carried)
6. **Bridge** (followed by the pilot expertise)

Below this data, list all turrets (numbered consecutively starting with T-1). After each turret designation, indicate the armament with which each turret is equipped, using the letters **B** (beam laser), **P** (pulse laser), **M** (missile launcher), and **S** (sandcaster). A triple turret would have up to three letters indicating the weapons installed in it, while a single turret would only have one. After the letters for the weapons, indicate the expertise of the gunner manning the turret. Also indicate the number of missiles present in each launch rack.

To the right of the card, indicate the computer model, as well as the CPU and storage capacity. Below that, indicate the computer programs which are carried on board the ship. During the game, these programs will be entered into the computer, and will be cycled from storage to CPU and back, so leave room to mark them with a pencil to indicate their status.

The data card example (below) shows how a typical type S Scout would be represented, armed with typical weaponry. Data cards must be created for all starships and non-starships. When creating cards for non-starships which were designed and built in accordance with the design rules, the above format applies. The jump drive letter designation is simply left blank. When a data card is made for small craft, the standard format is used, and appropriate items are left blank. Maneuver drives for small craft are labelled with drive letter zero. Computers and programs are listed only if they are actually installed. Weaponry is listed as all being in a single turret.

## Movement

Ships move using their maneuver drives; use of the jump drive exits a ship into interstellar space, out of the area of play. Maneuver drive uses thrust to accelerate a ship in a specific direction for a specified distance. This direction and distance is expressed as an arrow (a line in one direction) called a **vector**. Vectors determine how far, and in what direction, a ship can travel.

Each ship has a vector, which expresses that ship's velocity as a line (arrow) of a specific direction. For example, a ship might have a vector of 150 mm at 90 degrees, or of 100 mm at 277 degrees. It is possible to have a vector of 0 mm, whereupon the direction becomes irrelevant because the ship is stationary. Vectors are marked on the playing surface using string or soft wire. On some playing surfaces chalk can be used.

A ship's vector determines the direction and distance a ship will travel in the next turn, provided it is not changed by voluntary acceleration or by gravitational effects. With a vector of 150 mm at 90 degrees, a ship will travel 150 mm at 90 degrees in its next movement phase. In clear space, without gravitational influence, and without voluntary acceleration by the ship, it could travel at 150 mm per turn (direction 90 degrees) forever.

**Acceleration** involves altering a ship's vector by adding another to it; this new vector can come from thrust using the maneuver drive, or it can come from gravity. In either case, the method is the same. Vectors are added by placing them in a chain, head to tail, and drawing a new vector from the tail of the first to the head of the last.

**Figure A** illustrates simple vector addition. To add two vectors (vector 1 is 75 mm at 90 degrees, and vector 2 is 25 mm at 90 degrees), place the tail of vector 2 at the head of vector 1, and draw a line from the tail of the first to the head of the second. The result is a vector of 100 mm at 90 degrees.

**Figure B** is a more complex example of vector addition. Two vectors are at angles to each other (vector 1 is 75 mm at 90 degrees and vector 2 is 75 mm at 180 degrees). To add them, the tail of vector 2 is placed at the head of vector 1, and a new vector is drawn from the tail of vector 1 to the head of vector 2. In this case, the new length is approximately 106 mm with a direction of 135 degrees.

The important thing to note, however, is that mathematics is not required for the solution of vector problems; a new vector is generated by simply laying all required vectors on the playing surface, and connecting them as shown above.

In a player's movement phase, he or she will indicate the acceleration (new vector) desired and note any gravitational influence vector called for. They are all added to the ship's present vector. The ship then moves in the direction of its new vector, for the length of the vector. This vector then remains on the playing surface for reference during the next applicable movement phase.

Ships are restricted in the amount of acceleration which they may add to their current vector in one movement phase. Generally, a ship cannot accelerate more than **100 mm times its maneuver drive rating in Gs**. Thus, a standard design type A free trader is capable of 1-G acceleration, and cannot add more than a 100 mm vector per turn. This does not count acceleration due to gravitational influence, and does not restrict repeated acceleration in succeeding turns. While a free trader can only accelerate 100 mm per turn, after 10 turns of continuous acceleration, it would have accumulated a vector 1 meter long.

There is no restriction on the number of accelerations which may be made by a fueled ship, but the total acceleration in a turn in millimeters may not exceed 100 mm times the rating of the maneuver drive. Should the letter class of the maneuver drive (or the power plant) be reduced by combat damage, it may not exceed the revised size rating. Unused acceleration may not be saved or conserved to allow excess acceleration in following turns.

## Gravity

The section on [planetary templates](#planetary-templates) later in this chapter covers the construction of specific world disks, complete with gravitation bands which can affect movement. When the vector of a ship passes through the gravity bands of a world, the gravity may alter that vector. During the movement phase, lay out the vector of the ship to determine where it will move. If the exact midpoint of the vector lies in a gravity band, a gravity vector will be added to the course vector to create a new vector. The length of this gravity vector is equal (in millimeters) to the strength of the gravity band in Gs × 100. Thus, a vector dictated by the 0.5 G band of a world is 50 mm long. The gravity vector is parallel to a line connecting the regular course midpoint to the planetary template center. It is added to the regular course vector (along with any ordinary course change vector) during a player's movement phase.

## Laser Fire

In the laser fire phase of a player turn, the phasing player may fire laser weaponry at enemy targets. The following procedure dictates the order of actions taken by ships using laser fire. Several variables may affect this action.

**First**, the firing player selects the target at which the turrets of a single ship will fire. All lasers from one turret must fire on the same target; lasers from different turrets may fire on different targets if a multi-target program is running and allows such activity. The firing player then designates the targets for all of his ships.

**Second**, the firing player determines all applicable attack DMs and sums them to create one specific DM which he will use. Because of differences in ships, he may create one DM for each ship involved. Most attack DMs are the result of computer programs, but some may be forced by ship damage.

**Third**, the target player determines all applicable defense DMs and sums them to create a single defense DM to be used against the enemy fire. Defense DMs result from such circumstances as obscuring sand, range, or defensive programs.

**Fourth**, two dice are thrown, and that result modified by both the attack and defense DMs. If the modified result equals or exceeds **8**, a hit is achieved. The dice throw is made once for each firing laser weapon. The total number of hits is noted.

**Fifth**, each hit received is located on the target ship. Using another two dice throw for each hit, the [hit location table](#hit-locations) is consulted, and a specific effect is obtained and marked on the ship data card.

Laser fire is possible only for the phasing player, and hits are imposed on the target ship immediately. Return fire occurs in the following phase, and may be conducted only by ships which are capable of doing so after this phase.

**Shifting Fire:** Each firing ship must allocate its fire to a specific target before any ship has actually fired. Such allocation may be changed (shifted) if the target is destroyed before any weapons on the attacking ship have fired, but such a shift is subject to a DM of **-6** in addition to all other applicable DMs.

### Pulse Lasers (errata insert)

*[Merged from Don McKinney's Consolidated Errata, p.29 omission.]*

Pulse lasers are less accurate but more powerful than beam lasers. A pulse laser fires with a **DM of -1 to hit**; however, if it hits, the target suffers **two damage rolls** instead of one (i.e. roll on the hit location table twice per hit).

## Laser Return Fire

Laser return fire is conducted by those ships which have been targets for laser fire from enemy weaponry in the preceding laser fire phase. Both the **target** and **return fire** programs must be in the CPU for return fire to be performed. Laser return fire may only be directed at an enemy ship which fired at this ship. Laser return fire may be made against multiple enemy ships only if the **multi-target** program is also present.

Anti-missile fire also takes place in the laser return fire phase. It is dependent on the **anti-missile fire** program. For anti-missile fire to be performed, no target program is necessary.

## Ordnance Launch

During the ordnance launch phase, missiles or sand (or both) may be launched, provided both launch and target programs are running. In addition, lifeboats or ship's vehicles may be launched (without programs being necessary) as desired.

During the ordnance launch phase, missiles or sand which contacted a target in the preceding movement phase now explode or take effect.

Ordnance must be specified as launched during the launch phase, and only one missile or sand canister may be launched from a launch rack or sandcaster. The launched item does not actually move until the following friendly movement phase. All ordnance which is launched has the launching ship's vector, which must be taken into account.

### Reloading

Each launcher (sand or missile) has an inherent capacity for **three missiles or canisters**. This means that a triple turret with three missile launchers has a total of **9 missiles** in ready position.

When a launcher's missiles or canisters are exhausted, it may be reloaded by the turret's gunner in one turn. Reloading three launchers would take three turns. A gunner engaged in reloading is unable to fire other weaponry in the turret.

### Missile Detonation

Ordnance which impacts a target in a movement phase, and which then survives anti-missile fire, detonates in the ordnance launch phase. This detonation will inflict **1 to 6 hits** depending on the range at detonation. For each missile, throw one die. The result is the number of hits inflicted; determine each resulting hit location separately.

## Attacker's & Defender's DMs

### Attacker's DMs

| Modifier | Value |
|---|---:|
| Predict-1 | +1 |
| Predict-2 | +2 |
| Predict-3 | +2 |
| Predict-4 | +3 |
| Predict-5 | +3 |
| Gunner Interact | +gunner skill |
| Select-1 | -2 |
| Select-2 | -1 |

### Defender's DMs

| Modifier | Value |
|---|---:|
| Maneuver/Evade-1 | -¼ pilot skill |
| Maneuver/Evade-2 | -½ pilot skill |
| Maneuver/Evade-3 | -¾ pilot skill |
| Maneuver/Evade-4 | -pilot skill |
| Maneuver/Evade-5 | -pilot skill |
| Maneuver/Evade-6 | -5 |
| Auto/Evade | -2 |
| Range greater than 2500 mm | -2 |
| Range greater than 5000 mm | -5 |
| Obscuring sand (per 25 mm) | -3 |

## Hit Locations

Roll 2D and consult the appropriate column:

| 2D | Starship | Non-Starship | Small Craft |
|---:|---|---|---|
| 2 | Powerplant | Powerplant | Drive |
| 3 | Maneuver | Maneuver | Drive |
| 4 | Jump | Maneuver | Drive |
| 5 | Fuel | Fuel | Drive |
| 6 | Hull | Hull | Hull |
| 7 | Hull | Hull | Cabin |
| 8 | Hold | Hold | Computer |
| 9 | Computer | Computer | Cabin |
| 10 | Turret | Turret | Weapons |
| 11 | Turret | Turret | Weapons |
| 12 | Critical | Critical | Critical |

*If no small craft computer, treat as drive.*

## Critical Hits

Roll 1D and consult the appropriate column:

| 1D | Starship | Non-Starship | Small Craft |
|---:|---|---|---|
| 1 | Powerplant | Powerplant | Drive |
| 2 | Maneuver | Maneuver | Drive |
| 3 | Jump | Maneuver | Drive |
| 4 | Crew | Crew | Crew |
| 5 | Computer | Computer | Computer |
| 6 | Explode | Explode | Explode |

*If no small craft computer, treat as drive.*

## Ship's Data Card Example

**Suleiman (Type S Scout)**

| # | Section | Computer |
|---|---|---|
| 1 | M-Drive (A, 2G) | Model/1 |
| 2 | J-Drive (A, Jump-2) | CPU = 2 |
| 3 | Power Plant (A) | Storage = 4 |
| 4 | Fuel (40) | |
| 5 | Hold (3 tons, plus Air/Raft) | |
| 6 | Bridge (Pilot-1) | |
| T-1 | (B, M) Gunner-1 — five missiles on board | |

**Programs on board:**

| CPU / active | Storage |
|---|---|
| 1-Target | 1-Auto/Evade |
| 1-Return Fire | 2-Anti-Missile |
| 1-Launch | 1-Jump-1 |
| 1-Predict-1 | 2-Jump-2 |
| 1-Navigate | 1-Library |

*(Number prefix = CPU/Storage space required.)*

## Game Turn Sequence

### Intruder Player Turn

- **A. Intruder Movement.** The intruder moves his ships using the movement, gravity, and other applicable rules. Ordnance (missiles and sand) which he has launched in previous game turns is moved at the same time.
- **B. Intruder Laser Fire.** The intruder may fire his ships' laser weaponry at enemy targets, subject to the combat, computer, and other applicable rules. Only laser weaponry may fire in this phase.
- **C. Native Laser Return Fire.** The native may return fire with his laser weaponry at enemy ships which have fired on him, provided his return fire computer program is running during this phase, and in accordance with the computer program and combat rules. Anti-missile fire may be performed in this phase if the appropriate computer program is running.
- **D. Intruder Ordnance Launch.** The intruder may launch ordnance (missiles and/or sand) at enemy targets or on specific missions, subject to the applicable rules. Ordnance which has contacted enemy ships explodes in this phase. Lifeboats and ship's vehicles are launched in this phase.
- **E. Intruder Computer Reprogramming.** The intruder may remove computer programs from his on-board computer, and input other programs in anticipation of their use in later turns.

### Native Player Turn

- **A. Native Movement.** The native moves his ships using the movement, gravity, and other applicable rules. Ordnance (missiles and sand) which he has launched in previous game turns is moved at the same time.
- **B. Native Laser Fire.** The native may fire his ships' laser weaponry at enemy targets, subject to the combat, computer, and other applicable rules. Only laser weaponry may fire in this phase.
- **C. Intruder Laser Return Fire.** The intruder may return fire with his laser weaponry at enemy ships which have fired on him, provided his return fire computer program is running during this phase, and in accordance with the computer program and combat rules. Anti-missile fire may be performed in this phase if the appropriate computer program is running.
- **D. Native Ordnance Launch.** The native may launch ordnance (missiles and/or sand) at enemy targets or on specific missions, subject to the applicable rules. Ordnance which has contacted enemy ships explodes in this phase. Lifeboats and ship's vehicles are launched in this phase.
- **E. Native Computer Reprogramming.** The native may remove computer programs from his on-board computer, and input other programs in anticipation of their use in later turns.

### Game Turn Interphase

The end of one game turn is marked. All non-player items such as planets, worlds, and satellites move in accordance with the rules. Other miscellaneous activity may also be necessary. The game then proceeds to the movement and combat of the next game turn.

## Detection

- **Ordinary / commercial starships:** detect other ships out to a range of about **one-half light-second** (≈ 1,500 mm).
- **Military and scout starships:** detection ranges out to **two light-seconds** (6,000 mm, or 6 meters).

Ships which are maintaining **complete silence** cannot be detected at distances of greater than **half detection range**; ships in orbit around a world and also maintaining complete silence cannot be detected at distances greater than **one-eighth detection range**. Planetary masses and stars will completely conceal a ship from detection.

**Tracking:** Once a vessel has been detected, it can be tracked by anyone up to **three light-seconds** (about 9,000 mm, or 9 meters).

## Damage Definitions

Once combat results in hits against a vessel, the damage must be implemented. The precise portion of a ship affected by hits is determined from the [hit location table](#hit-locations). Separate columns are provided for starships, non-starships, and small craft. The following instructions detail the manner in which damage affects ships.

**Drives and Power Plants:** Each hit achieved on a drive or power plant reduces its letter classification by one. Thus C becomes B, X becomes W, etc. The potential of the drive or power plant is then computed based on its temporary new letter. Note that the letter rating of a power plant must equal or exceed that of a maneuver or jump drive in order for the drive to function.

A drive or power plant which is reduced to a level of the maximum drive potential table where its capabilities are marked with a dash **cannot function**, and if reduced to less than A is **destroyed**, and must be replaced rather than repaired.

**Turrets:** Each turret hit incapacitates a turret, preventing it and its weaponry from functioning. In cases where multiple hits occur on a ship with more than one turret, dice randomly to determine which turret or turrets are hit. A turret may be hit more than once, while another may not be hit at all.

**Hull:** A hull hit decompresses the ship's hull. Further hull hits have no effect.

**Hold:** A hold hit allows potential damage to items in the hold, including ship's vehicles and small craft, as well as cargo. Each hit destroys ten tons of cargo, or one vehicle, or one small craft. Dice to determine randomly which items are damaged.

**Fuel:** Each fuel hit punctures a fuel tank, and releases about 10 tons of fuel. When sufficient fuel hits have been inflicted to reduce the remaining fuel to less than is required for a jump, the vessel may not make a jump; when all fuel is accounted for, the vessel may not use its maneuver drive or fire its lasers.

**Computer:** Each hit on the computer increases its chance of malfunctioning. The basic throw for a computer to operate in any situation is **1+**, indicating extreme reliability. Each hit on the computer serves as a DM of **-1** on the throw to operate. Thus, after three hits are inflicted on the computer, a DM of -3 is applied to the throw of 1+ to operate. The throw to operate is made each time the computer is used (in combat, this is generally once per phase). A computer which does not make its throw to operate **malfunctions for the remainder of the phase**. A new throw is made at the beginning of the next phase. A computer which has received **12 hits is permanently malfunctioning**. Persons with computer expertise may apply their skill levels as DMs on the throw to operate. A computer which is not operating effectively paralyses a starship.

A computer hit on a small craft which does not have one is treated as a hit on the craft's drives instead.

**Small Craft Cabin:** A hit on a small craft cabin results in explosive decompression if depressurization has not already occurred. Additional hits have no effect. Persons in vacc suits within the craft are unaffected.

**Small Craft Weaponry:** A hit on the weaponry of a small craft destroys that weaponry. Additional hits have no effect.

**Small Craft Drive:** A hit on the drive of a small craft destroys the drive; the craft cannot maneuver, accelerate, or fire its lasers.

Hits as a result of laser fire, laser return fire, or missile detonation are located on the target vessel through the use of the hit location table. Such damage as indicated above is then marked on the ship's data card.

**Select program:** If a select program is being used to influence attacks, the firing player rolls one die for each hit inflicted. On a roll of **1 or 2**, he or she picks the hit location, specifying one of the following: maneuver, power plant, jump, fuel, hull, hold, computer, or turret. If the roll is **3 or greater**, roll hit location normally.

Damage to ships gradually wears away their capabilities, but will not generally destroy them in one shot. The exception to this is the **critical hit**. If a critical hit is achieved, then the [critical hit table](#critical-hits) is consulted with one die. The result is complete destruction or incapacitation of the indicated item. Unlike ordinary hits, the entire item is destroyed (crew is not necessarily killed, but is rendered unable to function).

## Special Situations

The following are descriptions of several special situations and how they may be handled when they arise. In addition to the specific instructions given, they also serve as a model for dealing with other special situations.

### Decompression

Starships (and other vessels) depressurize their interiors before combat whenever possible, the passengers and crew resorting to vacc suits for safety and comfort. This procedure minimizes the danger due to explosive decompression as a battle result. In some cases, selected areas may remain pressurized (perhaps the hold, for the safety of delicate cargo) while other areas are depressurized.

Any number of areas in the ship may be depressurized in the span of one turn (1,000 seconds). Repressurization requires one turn. In practice, the following parts of the ship may be individually pressure regulated: engineering section, hold, bridge, staterooms (all as one group; on some ships, in groups of four or more), turrets (individually). The pilot controls depressurization from the bridge.

Hull hits result in explosive decompression if pressure has not already been lowered. Explosive decompression kills all persons in that section unless a vacc suit is available and put on immediately. **Throw Dexterity or less** to put on a vacc suit in an emergency; apply DMs of double vacc suit skill.

> **Errata (Book 2 p.34 correction):** The vacc-suit throw is **Dexterity or less** (not 8+). The original 1981 wording made the task harder for high-Dex characters, contrary to intent.

### Atmospheric Braking

Ships passing very close to the surface of a world with a standard or dense atmosphere may slow their speed through atmospheric braking. If any portion of a ship's vector passes within **10 mm** of a world's surface, that vector is reduced by 10 mm in length.

### Abandon Ship

Should circumstances warrant, a ship may be abandoned using ship's vehicles or other methods.

- **Military vessels** (including exploratory vessels) can generally board the full passenger and crew complement of their ship's vehicles in one turn, and launch them during the ordnance phase, provided those individuals perform no other activity during the turn. If individuals are encumbered by vacc suits, each boards in the first turn on a throw of **6+**, boarding in the next turn if unsuccessful.
- **Non-military vessels** require **1D turns** to fully load all ship's vehicles. Crew members in the vehicles may elect to abandon ship without waiting for stragglers.

Individuals in vacc suits may abandon ship during the ordnance launch phase providing no other activity is performed during the player turn. Such persons may then be picked up by other ships or vessels. If no one is available to perform a rescue, then an attempt at landing on a local world is possible.

- A vacc suit can support its occupant for up to **21 one-thousand-second turns**; an additional air tank set will provide another 21 turns.
- A typical vacc suit is capable of a total of **100 mm of acceleration**.
- A foamed atmospheric reentry ablation shield (part of the vacc suit kit) can protect the individual while entering atmosphere, provided his vector, while entering atmosphere, does not exceed **75 mm**.
- Accident or mishap can occur during the process. **Throw 7+** to survive provided all else is performed properly; allow a DM of **+ vacc suit skill**.

### Damage Control

Damage inflicted on starships in combat can be repaired or controlled by crew members during the battle. Especially in the case of player characters, expertise or skill in specific fields may be used to remove or repair damage. Usually, a throw of **9+** will repair one hit of damage, with skill serving as a positive DM. **One repair attempt may be made per one-thousand-second turn.** Any part of a ship which has been completely destroyed cannot be repaired.

### Repair Parts

Most malfunctioning or damaged items in a vessel can be temporarily repaired from the stock of emergency materials in the ship's stores. Malfunctions usually occur in terms of a specific assembly (ship's computer, jump drive, etc.), and the cost of the repair is based on the cost of the original assembly.

After determining the cost of the assembly (from the component cost section of these rules), roll two dice: this indicates the cost of replacement of the item in **10% increments**; allow a DM **-2** if the repair installation will be made by ship's crew rather than a shipyard. Because the repair cost can run to 120% in some cases, complete replacement of the item is sometimes cheaper. In the case of minor malfunctions, DMs may be applied to the repair cost throw as considered appropriate. Repair parts cost of 0% is considered to be inconsequential.

### Expendables (errata insert)

*[Merged from Don McKinney's Consolidated Errata, p.34 omission — details dropped from 1981 edition.]*

Certain materials for starship (and non-starship) operation are not considered to be routine operating expenses, but nevertheless involve occasional purchases on an irregular basis, such as ammunition.

- **Missiles:** Missiles for missile launch racks are expended when they are fired; replacements must be obtained for reloading purposes when the situation warrants. A missile is of the homing type, costing **Cr5600** each. Such missiles are committed to a specific target when fired, and after launch, home towards that target until either the missile hits the target or is destroyed. Other types of missiles are possible (for example, bombs for attacks against planetary surfaces), but such require either specific alterations to ordinary missiles, or location of an arms supplier who deals in such items. Specific attributes of non-standard missiles are the realm of the referee.
- **Sand:** The abrasive particles used in the sandcaster are of a special composition, combining prismatic crystals and ablative particles, which allows interference with laser beams and pulses, as well as inflicting minor damage on ships which it touches. Ordinary sand or similar particles are not considered to be an adequate substitute. Sand must be procured from arms merchants, generally pre-packed in a sandcaster canister, weighing about 50 kilograms. Base price for a sand canister is **Cr400**.

## Starship Encounters

When a starship enters a system, there is a chance that it will encounter any one of a number of different ships going about their business. Very often, the exact encounter is the responsibility of the referee; for routine encounters, or for inspiration, the accompanying starship encounter table is provided.

The table classifies each system by the starport within it. Two dice are rolled and modified by the presence of scout or naval bases in the system. If a dash is shown on the table, then there is no encounter. The letter codes indicate the various types of standard design ships described earlier in this book. The referee should examine the specific type of ship involved and determine the precise nature of the encounter. Free traders may want to swap rumors and gossip; scouts may want information; patrol cruisers may want to inspect for smugglers.

The suffix **P** on any ship type can be construed as pirate; such a ship will probably attack, or at least try to achieve a position where it can make the attempt.

It is also possible to encounter a variety of small craft in a system. If an asterisk (**\***) appears on the table entry, a small craft has also been encountered. Roll one die and consult the standard small craft table to determine type. This encounter occurs either before or after the large ship encounter.

The referee may want to use the reaction table from the encounter section of Book 3 to determine the precise reaction of any type of ship and crew.

### Standard Starships

| Code | Ship |
|:---:|---|
| A | 200-ton Free Trader |
| C | 800-ton Mercenary Cruiser |
| M | 600-ton Subsidized Liner |
| R | 400-ton Subsidized Merchant |
| S | 100-ton Scout/Courier |
| T | 400-ton Patrol Cruiser |
| Y | 200-ton Yacht |

### Standard Small Craft

Roll 1D; DM +1 if naval base in system, DM -1 if scout base in system.

| 1D | Craft |
|---:|---|
| 0 | 20-ton Launch |
| 1 | 30-ton Ship's Boat |
| 2 | 30-ton Slow Boat |
| 3 | 40-ton Pinnace |
| 4 | 40-ton Slow Pinnace |
| 5 | 50-ton Cutter |
| 6 | 95-ton Shuttle |
| 7 | 10-ton Fighter |

### Starship Encounters Table

Roll 2D; cross-reference with system starport class.

| 2D | A | B | C | D | E | X |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2 | — | — | — | — | — | — |
| 3 | — | — | — | — | — | — |
| 4 | — | — | — | — | — | — |
| 5 | — | — | — | — | — | — |
| 6 | S | A | — | — | — | — |
| 7 | A | S | R | — | — | — |
| 8 | R | A | A | S | — | — |
| 9 | M\* | R\* | R\* | R\* | SP | S |
| 10 | Y | M | TP | A | A | TP |
| 11 | T | R | T | R | TP | CP |
| 12 | R\* | C\* | Y | M | CP | C |
| 13 | M\* | Y\* | A | Y | — | — |
| 14 | C\* | T\* | — | — | — | — |
| 15 | T\* | C\* | — | — | — | — |

**DMs:** DM +2 if naval base in system. DM +1 if scout base in system.

> **Errata (Book 2 p.35 correction):** Since naval bases can only exist in systems with class **A or B** starports, the **C and D** starport columns have **no entry** for rolls of 14 or 15 — i.e. a naval-base DM that would push the result into that range simply yields no encounter. The table above already reflects this.

## Planetary Templates

A planetary template must be constructed for each world or moon present in the scenario, showing the size of the planet itself and of its zones of various gravitational strengths. All required information may be generated using the formulae below.

- **D** — planetary size from the UPP.
- **R** — radius in millimeters (hundreds of kilometers).
- **M** — mass in Earth masses.
- **G** — gravity in Gs at various distances from the center.
- **Gₛ** — surface gravity.
- **K** — density in Earth densities (most planets have density 1).
- **L** — distance from the planetary center at which gravity equals the value of G for a planet of mass M. When G = Gₛ, L should equal R.

The planetary template is constructed in the following steps.

**Step 1.** Using the known values of D and K, compute the values of R, M, and Gₛ.

**Step 2.** Compute several values of L, for several values of G, beginning at 0.25 and increasing in increments of 0.25 until the value of G equals or exceeds Gₛ (that is, until L is equal to or less than R).

**Step 3.** Using a compass and ruler, draw concentric circles on a paper or cardboard template. Indicate the planetary surface by drawing a circle of radius R. Then draw further circles around the same center with radius equal to each value of L determined in step 2. Each circle should be labeled, and the interior of the planetary disc should be marked with the planet's name, its mass, density, Gₛ, and any other data the referee thinks useful.

### Formulae

```
R = 8D
M = K(D/8)³
Gₛ = KD/8
L = 64 × √(M/G)
```

### Example: Earth

**Step 1.** Earth has a diameter (D) of 8 and a density (K) of 1.0; thus R = 8×8 = **64 mm**, M = 1.0×(8/8)³ = **1 Earth mass**, and Gₛ = 1.0×8/8 = **1 G**.

**Step 2.** Since Gₛ = 1, it is necessary to determine L for G-values of 0.25, 0.50, and 0.75:

- At G = 0.25: L = 64 × √(1/0.25) = **128 mm**
- At G = 0.50: L = 64 × √(1/0.50) = **91 mm**
- At G = 0.75: L = 64 × √(1/0.75) = **74 mm**

**Step 3.** Four concentric circles are drawn: one of radius 64 mm for the planet's surface, and one each of radii 74, 91, and 128 mm for G-values of 0.75, 0.50, and 0.25 respectively.

### Notes of Interest

- In the scale presented for miniatures combat, there should generally be at most one world or moon of appreciable size on the average playing surface.
- The Earth's moon is 380,000 km from Earth, a scale separation of **3.8 meters**. However, a ship travelling at reasonable game speeds can cross this distance in only a few turns; it will be necessary to shift the positions of templates frequently as a battle progresses.
- A template for the sun, if anyone cared to do one, would be almost **74 meters** in radius (out to the G = 0.25 circle); the physical surface of the sun would have a radius of 7 meters.
- Asteroids, planetoids, and small moons (such as those of Mars) have no significant gravity or atmospheres, and would be essentially pinpoint-sized at this scale. The average density of an asteroid belt is about **one asteroid per 1000 square millimeters** (approximate separation: 30 mm, or 1000 asteroids per square meter). Asteroids should probably be placed on a template for ease of shifting.
- The sample planetary template (Terra, UWP `E867972-8`) shows Earth complete with gravity bands for 0.25, 0.50, and 0.75 Gs. If you construct templates for specific worlds, you may show continental outlines or other surface features, although such embellishment is purely optional.

## Standard Worlds

Template values (in millimeters) for world sizes (D) of one through ten; in all cases K is assumed to be 1. The four gas giants of the solar system are listed for reference. Columns `0.25`–`1.25` give the radius L (mm) of the gravity band at that G value; `—` means the band does not exist (G already exceeds Gₛ, or L < R).

| Size | R | M | Gₛ | 0.25 | 0.50 | 0.75 | 1.0 | 1.25 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| One | 8 | 0.002 | 0.125 | — | — | — | — | — |
| Two | 16 | 0.016 | 0.250 | 16 | — | — | — | — |
| Three | 24 | 0.053 | 0.375 | 29 | — | — | — | — |
| Four | 32 | 0.125 | 0.500 | 45 | 32 | — | — | — |
| Five | 40 | 0.244 | 0.625 | 63 | 45 | — | — | — |
| Six | 48 | 0.422 | 0.750 | 83 | 59 | 48 | — | — |
| Seven | 56 | 0.670 | 0.875 | 105 | 74 | 60 | — | — |
| Eight | 64 | 1.000 | 1.000 | 128 | 91 | 74 | 64 | — |
| Nine | 72 | 1.424 | 1.125 | 153 | 108 | 88 | 76 | — |
| Ten | 80 | 1.953 | 1.250 | 179 | 126 | 103 | 89 | 80 |
| Jupiter | 714 | 1318.7 | 2.643 | 4648 | 3287 | 2684 | 2324 | 2079\* |
| Saturn | 600 | 743.6 | 1.159 | 3490 | 2468 | 2015 | 1745 | — |
| Uranus | 254 | 14.6 | 1.11 | 489 | 346 | 282 | 246 | — |
| Neptune | 243 | 17.2 | 1.21 | 531 | 375 | 306 | 265 | — |

\* Jupiter has many further bands for which there was no room on the table. You can work them out for yourself using the formula.
