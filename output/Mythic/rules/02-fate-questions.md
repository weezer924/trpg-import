# Fate Questions

> Source: *Mythic Game Master Emulator 2nd Edition*, Ch2, p.18-31.
> The Big Fate Question Example (Henny In Z Land, p.32-35) is in `../examples/01-henny-in-z-land.md`.

## Index

1. [Introduction](#introduction)
2. [When To Ask A Fate Question](#when-to-ask-a-fate-question)
3. [The Fate Chart](#the-fate-chart)
4. [Fate Chart (9×9 Matrix)](#fate-chart-9×9-matrix)
5. [Example Odds](#example-odds)
6. [Choosing Odds](#choosing-odds)
7. [The Chaos Factor](#the-chaos-factor)
8. [Shifting Tone](#shifting-tone)
9. [Using The Fate Chart](#using-the-fate-chart)
10. [To Answer Your Question](#to-answer-your-question)
11. [Fate Question Answers (Table)](#fate-question-answers-table)
12. [Random Events](#random-events)
13. [The Fate Check](#the-fate-check)
14. [Fate Check Modifiers (Table)](#fate-check-modifiers-table)
15. [Fate Check Answers (Table)](#fate-check-answers-table)
16. [When To Run With Expectations And When To Question Them](#when-to-run-with-expectations-and-when-to-question-them)
17. [Using Fate Questions To Replace RPG Rules](#using-fate-questions-to-replace-rpg-rules)
18. [Chaos, Events, And Exceptional Answers](#chaos-events-and-exceptional-answers)
19. [Sidebar: Asking The Right Questions](#sidebar-asking-the-right-questions)
20. [Sidebar: Chaos Factor Values](#sidebar-chaos-factor-values)
21. [Sidebar: Questionable Chaos](#sidebar-questionable-chaos)
22. [Sidebar: The Art Of Interpretation](#sidebar-the-art-of-interpretation)
23. [Sidebar: Sample Questions And Answers](#sidebar-sample-questions-and-answers)
24. [Sidebar: Using Mythic As An RPG](#sidebar-using-mythic-as-an-rpg)

---

## Introduction

*(p.18)*

Asking and answering questions is the heart of a Mythic adventure, your principal tool for learning about the game world and moving the narrative forward.

Mythic handles this process of inquiry using Fate Questions: ask a Yes/No Question, determine the Odds of the answer being Yes, consult the Fate Chart to get the percentile chance, and roll 1d100. Your roll will determine whether the answer is Yes, No, Exceptional Yes, or Exceptional No. Interpret the result within the Context of your adventure and continue playing.

All of your Questions about the adventure can be resolved in this manner. "Are there monsters in this room?" "Is the door locked?" "Is it raining today?" Anything you would ask your Game Master in a social role-playing game you can ask Mythic in a solo game.

## When To Ask A Fate Question

*(p.18)*

As you play through an adventure, you improvise the details based on what you expect your Character to experience. You can pause your improvisation at any time to test an expectation with a Fate Question; usually, you do this during a moment of narrative tension or when you're unsure of what will happen next.

*The Player Character is on a distant planetary colony, trapped in a building overrun by aggressive alien creatures. They find themself in the building's control room, where they plan to activate the blast shields on all the windows and doors in the structure. Everything seems to be functioning fine, so The Player expects the blast doors to respond, but they aren't sure. What if the aliens damaged something? The Player decides to ask the Fate Question, "Do the blast shields go up?"*

*Later in that same adventure, the PC is searching for weapons and has made their way to the colony's armory. The Player doesn't know if there are any weapons left. Maybe the original colonists cleaned out the armory when they first faced the alien invasion. Since the Player is unsure, they ask Mythic, "Are there weapons here?"*

## The Fate Chart

*(p.19)*

The Fate Chart on the following page is used to determine the percentile chances of your Fate Questions receiving a Yes answer. Along the left side are probability descriptors (Impossible, Likely, Nearly Certain, etc.), and along the bottom is the Chaos Factor.

When asking a Fate Question, decide what you think the Odds are of the answer being Yes. This is a gut decision based on the Question you're asking and the Context you're asking it in. The Fate Chart's Odds uses common language such as Likely or Impossible to judge probability.

*Let's say the Player Character is an occult investigator searching a library for tomes of magic. The Player decides to make this search into a Fate Question: "Does he find any tomes?" Maybe at this point in the adventure the PC has come across strange magic and supernatural events, and he knows that the library he's searching through once belonged to a sorcerer and occultist. Given this Context the Player assigns this Question the Odds of Likely.*

*On the other hand, maybe the original owner of the library is unknown but the Player suspects they might have been involved in magic. This Context is different from the previous one: there's less evidence that books of magic would be present. Given this Context the Player assigns the Odds of 50/50.*

## Fate Chart (9×9 Matrix)

*(p.20)*

Each cell shows three values: `<Exceptional-Yes max> / <Yes max> / <Exceptional-No min>`. An `X` means the result is not possible with those Odds at that Chaos Factor.

- Roll 1d100.
- Roll ≤ left number → **Exceptional Yes**.
- Roll ≤ middle number → **Yes**.
- Roll ≥ right number → **Exceptional No**.
- Otherwise → **No**.

|                 **Odds** |    **CF 1** |    **CF 2** |    **CF 3** |    **CF 4** |    **CF 5** |    **CF 6** |   **CF 7** |   **CF 8** |   **CF 9** |
|--------------------------|------------:|------------:|------------:|------------:|------------:|------------:|-----------:|-----------:|-----------:|
| **Certain**              |  10 / 50 / 91 |  13 / 65 / 94 |  15 / 75 / 96 |  17 / 85 / 98 |  18 / 90 / 99 |  19 / 95 / 100 |  20 / 99 / X |  20 / 99 / X |  20 / 99 / X |
| **Nearly Certain**       |   7 / 35 / 88 |  10 / 50 / 91 |  13 / 65 / 94 |  15 / 75 / 96 |  17 / 85 / 98 |  18 / 90 / 99 |  19 / 95 / 100 |  20 / 99 / X |  20 / 99 / X |
| **Very Likely**          |   5 / 25 / 86 |   7 / 35 / 88 |  10 / 50 / 91 |  13 / 65 / 94 |  15 / 75 / 96 |  17 / 85 / 98 |  18 / 90 / 99 |  19 / 95 / 100 |  20 / 99 / X |
| **Likely**               |   3 / 15 / 84 |   5 / 25 / 86 |   7 / 35 / 88 |  10 / 50 / 91 |  13 / 65 / 94 |  15 / 75 / 96 |  17 / 85 / 98 |  18 / 90 / 99 |  19 / 95 / 100 |
| **50/50**                |   2 / 10 / 83 |   3 / 15 / 84 |   5 / 25 / 86 |   7 / 35 / 88 |  10 / 50 / 91 |  13 / 65 / 94 |  15 / 75 / 96 |  17 / 85 / 98 |  18 / 90 / 99 |
| **Unlikely**             |   1 / 5 / 82 |   2 / 10 / 83 |   3 / 15 / 84 |   5 / 25 / 86 |   7 / 35 / 88 |  10 / 50 / 91 |  13 / 65 / 94 |  15 / 75 / 96 |  17 / 85 / 98 |
| **Very Unlikely**        |    X / 1 / 81 |   1 / 5 / 82 |   2 / 10 / 83 |   3 / 15 / 84 |   5 / 25 / 86 |   7 / 35 / 88 |  10 / 50 / 91 |  13 / 65 / 94 |  15 / 75 / 96 |
| **Nearly Impossible**    |    X / 1 / 81 |    X / 1 / 81 |   1 / 5 / 82 |   2 / 10 / 83 |   3 / 15 / 84 |   5 / 25 / 86 |   7 / 35 / 88 |  10 / 50 / 91 |  13 / 65 / 94 |
| **Impossible**           |    X / 1 / 81 |    X / 1 / 81 |    X / 1 / 81 |   1 / 5 / 82 |   2 / 10 / 83 |   3 / 15 / 84 |   5 / 25 / 86 |   7 / 35 / 88 |  10 / 50 / 91 |

## Example Odds

*(p.21)*

The following table gives sample narrative Contexts for each Odds value across three example Fate Questions.

| **Odds** | **Description** | **"Is the creature hostile?"** | **"Will this abandoned car start?"** | **"Does the guard help us?"** |
|---|---|---|---|---|
| **Certain** | You're as sure of this as you can be. | It's stated its intent to destroy us and looks ready to do so. | It was driven here just a moment ago. | He is an ally, pursuing the same goals as us. |
| **Nearly Certain** | You're quite sure, but there is some doubt. | We've been fighting this thing all day. | We saw the vehicle operating a few hours ago. | He's helped us before and is sympathetic to our goals. |
| **Very Likely** | It's quite likely, although far from sure. | It's armed, angry, and actively threatening. | There's signs of recent use, and it looks to be in good shape. | We're on the same team, of course he'll help. |
| **Likely** | It's slightly more likely than 50/50. | It's armed and angry. | The car appears to be in working order. | He seems to be on our side. I think? |
| **50/50** | It can go either way, or you have no idea. | It's a new encounter, we'll have to see. | We just found this vehicle. Maybe it works? | You don't know whose side he's on. Cross your fingers. |
| **Unlikely** | It's slightly less likely than 50/50. | It's unarmed and uninterested in us. | The vehicle looks a little rough. | He hasn't been too friendly. |
| **Very Unlikely** | It's quite unlikely, but possible. | It looks docile. It doesn't seem to mind our presence. | The vehicle is a mess. It looks like it hasn't moved in a while. | He's been hostile. I doubt he would risk helping us. |
| **Nearly Impossible** | There might still be a chance. | We've seen these creatures before. They've all been peaceful. | The vehicle has lots of visible damage and is a mess. | This guy is doing his job, he doesn't care about our mission. |
| **Impossible** | There's no way, unless I'm wrong about something. | These creatures have always been peaceful. This one seems tame. | This thing is a wreck. It would be a miracle if it started. | He's a true believer in our enemy. |

## Choosing Odds

*(p.19-20)*

Who determines the Odds of a Fate Question? Well, if you're playing solo, then you do. If you're playing with a GM, then they do. If you're playing with a group then the Players must all reach a consensus on how the Odds are chosen.

Your choices start in the middle at 50/50. These are the Odds to choose if you think there's roughly a 50% chance of getting a Yes answer, or if you have no idea of the probability. Odds range upward from 50/50 to Likely, Very Likely, Nearly Certain, and Certain, and downward from 50/50 to Unlikely, Very Unlikely, Nearly Impossible, and Impossible.

You may wonder at the Certain and Impossible Odds. After all, if something is impossible or certain then it's a foregone conclusion, right? Not necessarily. The Odds are based on what you think they should be at the current moment, and that opinion is based on the Context of the adventure. Allowing some wiggle room in the results of extreme Odds acknowledges that what you and your PC know about the adventure is not absolute. Something may seem certain or impossible, but unfolding events can still prove us wrong about what we thought we knew.

Extreme Odds can also become more or less likely based on the Chaos Factor. When the narrative is in high gear the impossible can become probable for the sake of keeping tension and excitement high.

## The Chaos Factor

*(p.20)*

The Chaos Factor is a value tracked throughout the adventure that represents how much control the Player Characters have over current events. The more out of control Scenes get, the higher the Chaos Factor will climb; the higher the Chaos Factor, the greater your chance of getting a Yes response to Fate Questions. The Chaos Factor also determines the frequency of Random Events and how often Scenes begin as expected.

At the start of a new adventure the Chaos Factor is set to 5. A Scene that was chaotic and out of control increases the Chaos Factor by 1 point, while a Scene in which the Player Characters were mostly in control decreases it by 1. The value cannot drop below 1 or rise above 9; results that would push it beyond those limits are ignored. We'll talk more about the ebb and flow of the Chaos Factor in the "Scenes" chapter.

The Chaos Factor has a big influence on the percentile chance of your Fate Question being a Yes. When consulting the Fate Chart, cross-reference your chosen Odds on the left of the Chart with the current Chaos Factor at the bottom. The point at which these two intersect on the Fate Chart is the chance of your Fate Question being a Yes.

*The occult investigator is searching the library for tomes of forbidden lore. The Player has determined that the Odds of finding such tomes are Likely. After all, this is the personal library of the mad mage Angus McGregor. The only reason they aren't assigning higher Odds is because the mage would probably keep his best books in a hidden location.*

*Things have been fairly calm in the last few Scenes, with the Character maintaining control for the most part, so the Chaos Factor currently sits at a value of 3. Comparing the Odds of Likely to the current Chaos Factor, the Player determines that there is a 35% chance of finding a tome of magic sitting on one of the shelves.*

## Shifting Tone

*(p.23)*

A live Game Master isn't going to maintain the same tone throughout an adventure; there are times they'll want to push more action and times they'll want to dial it back. The Chaos Factor shifts throughout your adventure to simulate a GM shifting the tempo while running a game.

Since Yes answers to Fate Questions tend to be more action oriented, they become more and more likely the higher the Chaos Factor climbs. Higher Chaos also means higher chances of Random Events and a greater likelihood that your Scenes will start in unexpected ways; these aspects of the Chaos Factor are discussed more in the "Random Events" and "Scenes" chapters, respectively.

Here's an example of how the Chaos Factor influences Fate Questions to regulate the atmosphere of a game:

*The Player Character Safrid, a high fantasy druid, has been exploring a dungeon. Safrid has handled the dungeon's various perils well so far, and the Chaos Factor has fallen to 4.*

*Suddenly, he comes across a Bog Beast, a truly terrifying creature! The battle doesn't go well, and he retreats, fleeing from the monster to relative safety. This Scene was a mess for Safrid; the PC definitely wasn't in control. The Chaos Factor goes up to 5.*

*In the following Scene, as Safrid flees, he runs afoul of a trap in the dungeon and barely escapes it with his life. Once again, this is a Scene where Safrid had difficulty dealing with trouble. The Chaos Factor goes up again to 6.*

*The higher Chaos Factor means Safrid faces greater chances of active elements during the adventure. Is there a trap in this room? Yes. Is the door locked at the end of the hall? Yes. Is the Bog Beast still chasing him? Yes. Chaotic conditions in each Scene encourage more chaotic conditions in following Scenes, creating a snowball effect where the tension slowly increases and the Chaos Factor continues to rise.*

*Eventually, Safrid gets a handle on things again. He finds a place to rest; he prepares for the Bog Beast and defeats it; he finds a potion that heals some of his wounds. The Character is facing the challenges of the adventure head-on and overcoming them. This control over the adventure reverses the rising tension, and things calm down as the Chaos Factor falls to 4, 3, and even 2.*

*The lower Chaos Factor starts to have the opposite effect from before: now that things are calm in the adventure, and the Chaos Factor is low, No answers to Fate Questions are more common. When the Character is in control, No answers tend to be negative for them. Is there treasure in the chest? No. Does he have any food left? No. Now the lower Chaos Factor is working against Safrid; this encourages the pendulum to start swinging back the other way, setting the stage for future challenges that the character may face.*

Not every Scene or Fate Question follows these assumptions exactly, but when you look at the course of an adventure as a whole they tend to hold true. The overall result is that the Chaos Factor shifts the tone of the adventure so you never get too comfortable or too sure of exactly how things are going to unfold.

## Using The Fate Chart

*(p.23)*

You have your Question, you have your Odds, you know the Chaos Factor; now it's time to consult the Fate Chart. Cross reference the determined Odds with the current Chaos Factor to get the probability of a Yes answer to your Fate Question.

You'll notice that the values in the Fate Chart are expressed with a large central number flanked by smaller numbers on both sides. The central number is the percentile chance of a Yes answer. Roll 1D100 and compare the result to this value. If you roll within the value, then the answer is Yes; if you roll above it, then the answer is No.

By rolling very low or very high you can achieve Exceptional results. The smaller numbers to the left and right of the central number represent the extreme 20% of the Yes and No ranges, giving you a 1 in 5 chance of a Yes or No answer being Exceptional. Rolling equal to or less than the left-hand number is an Exceptional Yes; rolling equal to or higher than the right-hand number is an Exceptional No. A value of "X" means an Exceptional result is not possible with those Odds.

## To Answer Your Question

*(p.23-25)*

Mythic will yield one of four responses to a Fate Question: Yes, No, Exceptional Yes, or Exceptional No. This gives you four possible paths of interpretation.

### Yes

A Yes response to a Fate Question means the answer is your Expectation of what a Yes would mean. This is the most straightforward of the possible answers and likely won't require much interpretation.

*"Is the door locked?" Yes, the door is locked. "Does the black hole begin to suck us in?" Yes, the black hole is sucking you in. "Is the gladiator armed with a sword?" Yes, he's armed with the kind of sword you'd expect.*

### No

A No response to a Fate Question means the answer is the next most Expected outcome from what a Yes would have meant. With simple Questions, a No may be the opposite of a Yes and therefore easy to interpret; a complex Question might require more interpretative legwork.

*"Is the door locked?" No, it's unlocked. "Does the black hole begin to suck us in?" No, you're fine for now. "Is the gladiator armed with a sword?" No, he's armed with a spear.*

### Exceptional Yes

An Exceptional Yes is the same as a Yes but intensified, meaning you take your Yes answer to the next logical level.

*"Is the door locked?" Yes, and it's a darn good lock. "Does the black hole begin to suck us in?" Yes, and the stressors are causing damage all across the ship. "Is the gladiator armed with a sword?" Yes, a huge greatsword.*

### Exceptional No

An Exceptional No is the opposite of a Yes answer. If that would be the same as a regular No, then it's the opposite of a Yes intensified.

*"Is the door locked?" No, in fact the door is partially open. "Does the black hole suck us in?" No, you're actually moving away from it. "Is the gladiator armed with a sword?" No, he's not armed at all.*

## Fate Question Answers (Table)

*(p.25)*

| **Answer** | **Result** |
|---|---|
| **Yes** | The answer is Yes, confirming your expectation. |
| **Exceptional Yes** | The answer is Yes, confirming your expectation and beyond. |
| **No** | The answer is No. Go with the next most expected outcome. |
| **Exceptional No** | The answer is the opposite of a Yes, or the opposite of a Yes intensified. |

## Random Events

*(p.26)*

One consequence of asking Fate Questions is inviting a Random Event to occur. When rolling d100 to answer your Question, if you get a double number (11, 22, 33, etc.), and the single value of that number (1, 2, 3, etc.) is equal to or less than the current Chaos Factor, then you've triggered a Random Event. We'll delve more into Random Events in the next chapter.

## The Fate Check

*(p.26)*

Not everyone likes looking up percentile values on a table. If you'd rather not use the Fate Chart to answer Fate Questions you can skip the Chart and use a Fate Check instead. You still roll 2d10, but this time you add the dice together instead of treating them like a percentile. This method of answering Fate Questions can be faster than using the Fate Chart and it matches the Odds fairly closely aside from a higher chance of Exceptional results.

### Adjust For Odds & Chaos Factor

Like the d100 Fate Chart, a 2d10 Fate Check is modified based on the current Chaos Factor and the Odds assigned to a Fate Question. The "Fate Check Modifiers" table on the next page breaks down how the Odds and Chaos Factor affect your roll results.

*For instance, if you asked a Fate Question with Odds of Very Likely you would apply a +2 modifier to the roll. If the Chaos Factor currently stood at 4, you would apply another modifier of -1. Adding both modifiers together gives a final modifier of +1.*

*If your next Fate Question had Odds of Nearly Impossible you would get a modifier of -4. Combined with the Chaos Factor modifier of -1 your total modifier is -5.*

### Fate Check Answers

The "Fate Check Answers" table summarizes what your roll total means. A modified total of 11 or more is a Yes answer, while a total below 11 is a No answer.

As with the Fate Chart, rolling very high or very low will give you an Exceptional answer. If the modified total falls within the 18-20 range then the answer is an Exceptional Yes; if the total falls within the 2-4 range then the answer is an Exceptional No. Your final total must fall somewhere within those ranges to count as an Exceptional result. A modified roll of 18 is an Exceptional Yes, while a modified roll of 22 is a regular Yes. This means modifiers will push your dice total toward those ranges but may also cause the total to exceed them, in which case no Exceptional result occurs.

### Random Events (in Fate Check)

Random Events are handled the same way with a Fate Check as they are with the Fate Chart. If both dice come up as the same number (11, 22, 33, etc.), and the single digit value (1, 2, 3, etc.) is equal to or less than the Chaos Factor, then you get a Random Event. As with the Fate Chart, the result that triggers an Event is still used to answer your Fate Question as well.

*Safrid the Druid has survived the Dungeon of Galzarad … so far. Now, in his travels through a deep, subterranean cavern, he's come across a rope bridge suspended over a chasm. Using a Fate Check, his Player asks the Fate Question, "Does the bridge look stable?"*

*The Player assigns this Question the Odds of Nearly Impossible (-4 modifier), and the Chaos Factor is currently 6 (+1 modifier), resulting in a final modifier of -3. This means the Player has to roll at least a 14 to receive a Yes answer.*

*The Player rolls 2d10 and gets a 3 and a 3. The rolled total is 6 with a -3 modifier for a final result of 3. That's below the target number of 11, so the answer is a No. This result also falls within the 2-4 range, making it an Exceptional No. And since a double number was rolled (3 and 3), and 3 is within the CF value of 6, this Question also results in a Random Event.*

*It looks like Safrid may be in for an interesting time trying to get across that bridge.*

## Fate Check Modifiers (Table)

*(p.27)*

| **Odds** | **Roll Modifier** |
|---|---:|
| Certain | +5 |
| Nearly Certain | +4 |
| Very Likely | +2 |
| Likely | +1 |
| 50/50 | None |
| Unlikely | -1 |
| Very Unlikely | -2 |
| Nearly Impossible | -4 |
| Impossible | -5 |

| **Chaos Factor** | **Roll Modifier** |
|---:|---:|
| 9 | +5 |
| 8 | +4 |
| 7 | +2 |
| 6 | +1 |
| 5 | None |
| 4 | -1 |
| 3 | -2 |
| 2 | -4 |
| 1 | -5 |

## Fate Check Answers (Table)

*(p.27)*

| **Roll Total (modified)** | **Fate Question Answer** |
|---:|---|
| 18-20 | Exceptional Yes |
| 11 or more | Yes |
| 10 or less | No |
| 2-4 | Exceptional No |
| Doubles, single digit ≤ CF | Random Event |

## When To Run With Expectations And When To Question Them

*(p.28)*

Fate Questions should be asked when you aren't sure whether an expectation you have is true. The more you use Mythic to create adventures the more you'll get a feel for when to ask a Fate Question and when to stick with your expectations.

If you find yourself conflicted, follow your interests, consider the Context of the adventure, and listen to your gut. Does it feel right to pose this detail as a Fate Question, or are you certain enough to take it for granted?

As your adventure progresses and develops more Context Fate Questions and their answers will get easier and easier to come up with. Much of the narrative's richness will come from details that were fleshed out by prior Fate Questions. Establishing that a certain NPC is unfriendly will shape your later expectations about that Character and might impact the Odds of future Fate Questions concerning their actions. In this way, a logical chain of events will build upon itself, shaping the structure of the adventure and spinning it into a narrative just like a Game Master would.

### Give Me More!

*(p.28-29)*

In order to keep things moving in your adventure a good rule of thumb is to try and limit yourself to no more than two Fate Questions for any one detail; that should give you enough information to reach a reasonable expectation for just about anything. If you can manage with only one Question so much the better.

*A pair of occult investigators are creeping through a graveyard at midnight, searching for the walking dead. They come across a mausoleum and inspect the entrance to see if it's been opened recently.*

*One of the Players asks, "Do we hear anything?" Mythic says Yes, but the Player doesn't have a clear expectation of what is heard.*

*"Does it sound like something scrambling inside a tomb?" No. "Does it sound like someone walking through the graveyard?" No. "Does it sound like something flying through the air?" No.*

*The Player is muscling through a run of No answers in search of a Yes, but they could have stopped after the second Question ("Does it sound like something scrambling inside a tomb?"). They already know that the investigators hear a noise that isn't coming from inside the mausoleum, so a logical expectation at this point might be that they hear something outside in the graveyard—perhaps a shuffling sound—or that they hear something too faint to identify and will have to investigate further.*

*After two Questions the Player has enough information to make a reasonable interpretation that matches their expectations.*

## Using Fate Questions To Replace RPG Rules

*(p.29)*

You can ask any Fate Question during an adventure, even one that would normally be handled with the mechanics of your chosen RPG. If you can't recall a certain rule or haven't fully learned the game, you can use Fate Questions as an on-the-spot substitute, similar to the "snap judgements" a live GM might make to save time. You can assign Odds to these Fate Questions based on the Context of the adventure and your current understanding of the RPG's rules.

*The Player is playing a post-apocalyptic game that has rules for randomly determining details about any surviving settlements the Player Character comes across. During an adventure, the PC encounters a village, but the Player can't remember the rules for generating settlements and they don't want to stop in the middle of playing to look them up.*

*They do remember that the process involves determining key factors like population size, technology level, and systems of law and order, so they take this knowledge of the RPG rules and turn it into Fate Questions: "Does the village have a decent size population?" "Do they have advanced technology?" "Is the village ordered and structured?" Once the Player has enough to go on the PC can begin to interact with the new location.*

*Later on in the adventure the PC ends up in a situation where she is at risk of drowning. The Player can't remember the rules for determining whether a character drowns, so to keep things moving they leave it up to a Fate Question: "Does the PC start to drown"? They then interpret the resulting answer and continue playing.*

## Chaos, Events, And Exceptional Answers

*(p.30-31)*

Mythic's Fate Questions are intended to guide the narrative of an adventure and the Chaos Factor is there to regulate that narrative. Questions like "Does the kingdom have harsh laws?" are narrative, story-oriented Questions; the answers to them can vary depending on the CF, and the CF varies depending on what's happened in the adventure so far. Past narrative impacts current narrative.

But when you're using Fate Questions to replace the rules of an RPG (combat "to hit" rules, recovery from damage, task resolution, etc.), what matters more than the ebb and flow of narrative tension is consistency. I suggest, in these cases, that you disregard the current CF and treat it as a value of 5. This will give those Fate Questions default, middle of the road percentiles without the Chaos Factor skewing results.

You should also consider whether to honor Exceptional results. Unless you know that the rule you're replacing has degrees of success and failure, it may be best to treat Exceptional results as regular answers.

*The Player has just picked up a new superheroes role-playing game. They understand enough of the rules to make a Character, so they decide to jump right in with a solo Mythic adventure.*

*During the first Scene, the PC finds themself in an apparently empty building. They have a power that allows them to sense when other people are nearby, but the Player can't remember the rules for how to use it. Looking it up would break the narrative tension, so the Player decides to pose it as a Fate Question instead: "Do I successfully use my power to sense if there are others nearby?"*

*The Player knows that the PC's power should be strong enough to cover the entire building (unless the building is actually bigger than it looks), so they decide that the Odds of a Yes are Nearly Certain. Since this Fate Question is replacing a rule in their chosen RPG, they ignore the current Chaos Factor of 7 and treat it as a 5. According to the Fate Chart, this gives the PC an 85% chance of successfully using their power.*

*The Player rolls and gets an 8. With the modifier from the Odds, this puts the result within the range of an Exceptional Yes. However, the Player knows that this RPG doesn't have degrees of success for this power—it either works or it doesn't—so they treat the answer like a simple Yes.*

*The power worked; the PC is psychically scanning the building for the presence of others.*

> For a reference summary of this section's rules packaged as an RPG-replacement table, see the "Fate Questions As RPG Rules" collection at p.196 (transcribed in `../tables/fate-question-answers.md` and related tables).

---

## Sidebar: Asking The Right Questions

*(p.19)*

Mythic relies on Fate Questions to construct the narrative of the adventure as you play; what you ask and how you ask it will influence your game. While it's best to phrase Fate Questions as naturally as possible, there are a few guidelines you should keep in mind.

### Action Oriented

The Chaos Factor assumes that Yes answers are typically more active than No answers, so you'll get the best results if your Fate Questions focus on active and interesting elements. "Are there zombies outside?" is better than "Is it all clear outside?"

### Guided By Expectations

It's generally best to let your Questions be guided by your expectations rather than your desires. A party of adventurers prowling down a dungeon hall might easily ask, "Do we hear anything?" but it would make little sense to ask, "Do I look down and see a Vorpal Blade of Instant Murder at my feet?" The current Context offers no logical expectation to prompt the second Question, but it does for the first.

## Sidebar: Chaos Factor Values

*(p.22)*

The Chaos Factor is a value between 1 and 9 that represents how much control the PC has over the adventure's current direction. 1 is calmest, 5 is average, 9 is most chaotic. Each completed Scene shifts it by 1 point based on whether the PC was in control; it cannot drop below 1 or rise above 9.

## Sidebar: Questionable Chaos

*(p.24)*

The Chaos Factor is a major influence on the answers to Fate Questions. While this is meant to vary the tone throughout the adventure, you can adjust the Chaos Factor's influence to suit your tastes. Check out "Choose Your Chaos Flavor" in the "Variations" chapter on page 147 for variant rules that change how much power the Chaos Factor exerts.

## Sidebar: The Art Of Interpretation

*(p.25)*

Values on the Fate Chart are expressed with a central, large number showing the percentage chance of a Yes answer. Rolling 1d100 equal to or less than this number is a Yes answer. Rolling equal to or less than the number on the left, the lower 20% of the Yes answer range, is an Exceptional Yes. Rolling above the central number is a No, and rolling equal to or above the rightmost number is an Exceptional No.

In the cutout at the top of p.25 (representing a single Fate Chart cell), a roll of 1-10 would be an Exceptional Yes, 11-50 a Yes, 51-90 a No, and 91-100 an Exceptional No.

Interpretation is an important part of the emulating process. Mythic answers your Questions, but these answers are merely prompts for you to make sense of.

Often interpretations will come easily. If the Question was, "I open the desk drawer; is there a gun inside?" then a Yes or a No will be clear. Sometimes, though, interpretations elude you, or an answer won't give you enough to interpret. If you feel like you need more information you can try to clarify the answer with another Fate Question. "Is the gun a pistol?" "Is it loaded?"

Be careful not to fall into the trap of asking for more detail than you need. A string of narrow, specific Questions can easily stall the flow of the game. Unless it's something important to the adventure it's generally best to ask a few "big picture" Questions and run with your expectations as far as you can. The goal is to gather just enough information to move things forward.

## Sidebar: Sample Questions And Answers

*(p.28)*

*"We crash land the plane in an open field as safely as possible. Did it sustain any damage?"*

- **Yes**: The plane is damaged but not in any way that can't be repaired.
- **No**: The ground was smooth enough that you were able to roll it to a stop in one piece.
- **Exceptional Yes**: The ground was rough. One of the wheels came off in a ditch and pitched us sideways, crumpling a wing as we slammed into the ground. The plane is an unflyable wreck.
- **Exceptional No**: A perfect touchdown without any damage. In fact, the plane is well-positioned for takeoff once you find fuel.

*"We succeed in breaking open the vault. Do we find the vaccine inside?"*

- **Yes**: Yes, you do.
- **No**: The vaccine isn't there.
- **Exceptional Yes**: You find several cases of the vaccine, many more than you expected.
- **Exceptional No**: You find the broken, ruined vials of the vaccine—it's been destroyed.

*"We make our way through the woods. Do we encounter anything today?"*

- **Yes**: Yes, now you have to figure out what the encounter is.
- **No**: All is peaceful.
- **Exceptional Yes**: More than one encounter. Figure out what the first one is, then once that's resolved figure out the second one.
- **Exceptional No**: All is peaceful today and tonight as well, so there's no need to check again when you make camp.

## Sidebar: Using Mythic As An RPG

*(p.29)*

So far, this section has focused on using Fate Questions to replace "spot rules" in your chosen RPG, thereby reducing the time you spend flipping pages in search of a mechanic you can't remember. You can take this further by replacing any rules you don't feel like using, or you can even forgo the rules entirely and just use Mythic. This spectrum from Mythic to mechanics lets you be flexible with how you play.

For instance, if you wanted to use a chosen RPG but felt more inspired by its setting than its actual rules, you could just take the setting and replace the mechanics with Fate Questions. But maybe there are some rules in the game you really like, such as a sanity system or a cybernetic hacking minigame. These you could port over as Fate Questions, following the tone and intent of the original rules but resolving them with Mythic instead.

You can also use this approach to learn a new RPG. Rather than reading it cover to cover, you can just start playing and replace anything you don't understand yet with Fate Questions. Then, as you learn more of the RPG, you can incorporate more and more of the game rules into your adventure.

This is another beautiful thing about solo role-playing: you have tremendous control over how you play, not just in the narrative of the adventure itself but in the meta aspect of what rules you use and how you use them.
