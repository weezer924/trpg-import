# Monsters

> Complete Edition fan translation, source: Sword World.txt lines 10137–15298

## Index

- [13.1 Types of Monsters](#131-types-of-monsters)
- [13.2 Monster Catalog](#132-monster-catalog)
  - [13.2.1 How to Read the Monster Catalog](#1321-how-to-read-the-monster-catalog)
  - [13.2.2 Fae](#1322-fae)
  - [13.2.3 Youma](#1323-youma)
  - [13.2.4 Spirits](#1324-spirits)
  - [13.2.5 Titans](#1325-titans)
  - [13.2.6 Mythical Beasts and Magical Beasts](#1326-mythical-beasts-and-magical-beasts)
  - [13.2.7 Animals](#1327-animals)
  - [13.2.8 Plants](#1328-plants)
  - [13.2.9 Undead](#1329-undead)
  - [13.2.10 Magical Creatures](#13210-magical-creatures)
  - [13.2.11 Daemons / Underworld Creatures](#13211-daemons--underworld-creatures)
  - [13.2.12 Humans](#13212-humans)
  - [13.2.13 Other](#13213-other)
- [13.3 Converting Character Data to Monster Data](#133-converting-character-data-to-monster-data)
- [13.4 Representing Special Monsters with Character Data](#134-representing-special-monsters-with-character-data)
- [13.5 Monster Level and Adventurer Level](#135-monster-level-and-adventurer-level)
- [13.6 Handling Monster Special Abilities](#136-handling-monster-special-abilities)

---

A life of adventure is a thrill. Even among those who provide this, monsters are by far the greatest. This chapter explains monsters, their game details, and how to handle them.

## 13.1 Types of Monsters

There are 12 types of monsters in Alecrast: fae, youma, spirits, giants, mythical beasts, magical beasts, animals, plants, undead, magical creatures, demons, humans, and others. This is based on the types set by Laverna, the famous witch of Orphan, who compiled the Natural History of Alecrast. The meaning of each type are as follows.

### Fae

Fae are a demi-human race that originally lived in the fae world, but for various reasons they came to live in this world and were unable to return to their original world. However, some races, such as high elves and fairies, still have the ability to travel between the two worlds. They are relatively friendly towards humans, but do not actively try to connect with them.

Elves, dwarves, and grassrunners are also fae, and these three races can also be player characters.

### Youma

Youma are a race of fae that have evil personalities. They may also use spirit magic or dark magic. They have a very strong hostile relationship with the fae, and of course they are not friendly with humans either. If you encounter them, there's a high probability that you'll get into a fight.

Typical examples of youma include goblins and gremlins.

### Spirits

Spirits have a will, but they can be called energy rather than living beings. They are closely related to the natural elements of earth, water, fire, wind and light, as well as darkness, and emotions and the nature of the heart, which are the functions of the mind. In addition, spirits may reside in natural creatures and objects, and above all, it seems certain that spirits are involved in the activities of life itself. Poisons, illnesses, and mental attacks are all meaningless against spirits. Also, they will not be wounded even if attacked by the spirit power they control.

Spirits that appear in the material world in response to a shaman's summoning usually return to the spirit world after fulfilling their role (when you use spirit magic). However, sometimes spirits present themselves in the material world as mad spirits. These mad spirits are extremely dangerous. They cannot adapt to the material world and will act destructively towards everything in it. A mad spirit will return to the spirit world as soon as its life points or spirit points reach 0.

Spirits can use an unlimited amount of spirit magic depending on their power. No matter how much they use it, it will not consume their mental points. However, they cannot expand the power of their spells.

Regardless of a spirit's rarity (a score related to how well-known the monster is, which will be explained later), a shaman knows all spirits. When encountering a spirit, a shaman can recognize a spirit without the need for a success roll.

Typical spirits include sylph, undine, and will-o-wisp.

### Titans

The origin of the titans is unclear. Some are said to be giant species of fae or youma, but others are clearly not. Some sages claim that, like the gods, they were born directly from the primordial titans, and that the gods were the greatest titans among them (though of course priests and theologians strongly deny this).

Their bodies are much larger than that of a human. Among the titans, some races are relatively gentle, while others are frenetic and hostile. Their strong bodies hold terrifying power, so it is best not to deal with them unless you're a very experienced adventurer.

### Mythical Beasts and Magical Beasts

Mythical beast and magical beast are general terms for monsters that have living bodies, unlike spirits or undead. These include three types: things that have existed long before humans, such as dragons, things that live like humans, and artificial creatures created through the experiments of ancient sorcerers that have turned wild. Many have a mixture of features from multiple animals.

Dragons, wyrms, wyverns, unicorns, lynx, etc. have been around since ancient times. They have a near-infinite lifespan, but leave behind very few offspring, and so are doomed to gradual decline and extinction. Some of them have high intellect, while others have become wild and have lost most of their intellect. Many of them have special abilities, like using ancient magic, or having undifferentiated spirit power (fire, ice, life, mind, etc) in their bodies (in these cases, attacks involving that spirit power have no effect on them). They are also not affected by illness or poison, and do not sleep in the normal sense of the word.

Harpies, minotaurs, centaurs, etc. were created by the gods to live in the material world around the same time as humans. These creatures have an intellect close to that of humans, and create societies and live their lives in the same way as humans. Many of them are unable to reproduce on their own and can only produce offspring with the help of humans.

Medusa, chimera, griffon, etc. are creatures created by sorcerers during the ancient kingdom period. They look like a combination of animals (as well as) humans, and are endowed with very special abilities. These mythical beasts and magical beasts created by such magic have almost no reproductive ability. However, on the other hand, they can survive on very little food. To protect themselves or to show off their power, sorcerers of the ancient kingdom period often gave them various offensive abilities and frenetic personalities, and many of these kinds of mythical and magical beasts are dangerous. Sleep is necessary for the maintenance of normal animals and humans both as individuals and a race, but some mythical beasts and magical beasts are created such that they do not need to sleep. Magic that causes sleep (such as Sleep Cloud or Sleep) has no effect on such things. Similarly, most poisons, etc. have no effect.

Creatures that have a beautiful appearance and are neutral or friendly towards humans are called mythical beasts, while those that have an ugly or unpleasant appearance and are harmful to humans are called magical beasts. However, this is rather a result of selfish value judgment by humans, and even if they are called mythical beasts, they do not seem to like interacting with humans. There are also things such as dragons that are called both mythical and magical beasts.

Examples of mythical beasts include griffons, unicorns, etc. and magical beasts include chimeras, manticores etc.

### Animals

There are animals in Forcelia too. Of course, they are basically the same animals that live in our world, but they also include those of unusual size and animals that are already extinct in our world.

### Plants

Plants are basically the same as those that live in our world, but there are also abnormal creatures that move around under the influence of magic, etc. and prey on animals and humans.

### Undead

Undead are monsters that exist and move around through forces that are the exact opposite of those of us humans and normal animals.

If the source of our life is called positive life force, then the undead's source can be called negative life force. This negative life force is sometimes called the undeath force. There are many mysteries surrounding the origin of these undead, but it's completely different from how normal animals give birth. They may be created by magical power, reborn, or infected and transformed like an illness.

They despise creatures with positive life force and also target them both as prey and for the expansion of their species. If you meet them, there is a high probability that you'll fight.

Undead are not affected by poison or illness. Many spells with mental effects are also meaningless. They do not require rest in the normal sense and can never be magically put to sleep.

### Magical Creatures

Pseudo-life forms created (or created in the past) using ancient magic. They are given temporary bodies made of various materials and run on magical power.

During the ancient kingdom period, various magical creatures were created as a challenge to the gods. The sorcerers sought to gain power as creators. The magical creatures that were created in this way basically continue to live indefinitely without needing to eat or breathe, and many of them are still around today.

There were also many failures in the production of magical creatures. Among the failures that were carelessly discarded, there are some that are still alive due to their strong life force. These are also of the magical creature type.

### Daemons / Underworld Creatures

Daemons are underworld monsters that live in a material world different from ours. In the age of the gods, they were known as terrifying slaughterers who followed the dark god Phalaris, and in the age of the ancient kingdom, they were summoned to this material world by sorcerers who were skilled in summoning magic, offering their wicked power to the sorcerers. They have a number of special abilities and wicked personalities, making them extremely dangerous. They are said to have a deep connection with the dark gods, and many are also well-versed in dark magic. Although they rarely make their presence felt in this world, those summoned during the days of the ancient kingdom still dwell in underground labyrinths and remote ruins.

Many of them seem to have a humanoid appearance, but there are many different types, such as those with horns, tails, wings, etc. Some sages claim that just as there are different races in our world, there are also different subspecies of demon. Furthermore, in the original world in which demons live-- the underworld --it's said that they form society just like humans.

There are different ranks of demons. The highest rank ones, called demon lords and archdemons, are said to have powers comparable to that of ancient giants or dragons. Below them are types called greater demons and lesser demons, and even the lowest rank Lesser Demons have powers that far exceed those of humans.

With the discovery of two similar demons (lesser demons and greater demons) called doubleburg and doppelgänger, it's become an established theory among sages that demons are born as lower rank demons and grow to become higher rank.

In the underworld where demons live, there are also animal-like creatures with low intellect. Sages say that they are comparable to the animals in our world, and claim that this is proof that there are multiple material worlds. These underworld creatures are far more dangerous than the animals of the material world, just as demons are far more dangerous than humans.

### Humans

Even among humans, there are those who are called villains. There are bandits who build strongholds in the mountains and fields and attack nearby villages and roads, and dark priests who believe in wicked gods and do evil according to their teachings.

### Other

There are also monsters in Alecrast that do not belong to any of the 12 types. Examples of this include lycanthropes and red caps, where humans become monsters due to infectious diseases.

## 13.2 Monster Catalog

### 13.2.1 How to Read the Monster Catalog

Monster data is written in the following format.

#### [ Dog ]

- Monster Level=1
- Rarity=3
- Agility=15    Movement Speed=20
- Number=One to around ten
- Frequency=Frequent
- Intellect=Animal
- Reaction=Neutral to friendly
- Attack Points=Fangs: 8 (1)    Strike Points=4
- Evasion Points=9 (2)    Defense Points=4
- Life Points／Resistance=12／7 (0)
- Mental Points／Resistance=5／7 (0)
- Special Abilities=None in particular
- Habitat=Forests, meadows, human villages
- Perception=Five senses
- Languages=None

Dogs are animals that have a very close relationship with humans. They have fur and fangs in their mouths. Dogs have been domesticated and used for a variety of purposes, such as hunting dogs, guard dogs, or simply as pet dogs. New breeds have been artificially created by the hands of humans, and there are many subspecies, ranging from small dogs that are no taller than a person's shins to large dogs that are taller than a human's waist. The data presented here is for the most commonly seen medium-sized dog, and its body height is roughly from the knee to the thigh of a human. If you want to include small or large dogs in your game, the game master should increase or decrease the scores listed here by 1 or 2 points.

Dogs have a habit of following their leaders, and humans have taken advantage of this habit to use dogs for various purposes. Dogs react to humans in a variety of ways. If they are domesticated, they will not attack humans because they consider humans to be their masters. However, special guard dogs, military dogs, etc. that have been trained to treat all but specific people as enemies will attack even humans larger than themselves. Dogs are especially aggressive towards intruders-- they also have a strong sense of territory. If it's a wild dog that's not owned by humans, it will act according to its own instincts. If they're hungry and think their opponent is weak, they may attack.

A few lines of game data are shown first, followed by a detailed explanation. The meaning of each game detail is as follows.

##### Monster Level

This is a score that corresponds to a character's adventurer level, and represents the general strength of that monster. If it's 1, it's an extremely weak monster. If it's 10, even a seasoned adventurer will have a hard time crossing swords with it.

Monster level, similar to a character's adventurer level, indicates how difficult it is for a monster to die. When a monster suffers damage from magic, etc. the damage can be reduced by this monster level score.

##### Rarity

This is a score that indicates whether the monster is famous or not. The lower this score, the more well-known the monster is. When using the sage skill's monster check ability, this rarity is the target score for a success roll.

##### Agility

Similar to agility, which is a character ability score, this represents the quickness of a monster. It's used to determine the order of actions in a combat round.

##### Movement Speed

Indicates the speed at which the monster moves. Similar to a character's agility, monsters can move up to movement speed meters per round during normal movement, or movement speed x 3 meters per round during full movement.

It's also used to determine whether a character can escape from the monster. If the monster's movement speed is greater than the character's agility, the character will not be able to escape from the monster unless they think of something.

Some monsters fly in the sky, and some travel in water or underground. For such monsters, two types of movement speed are written. The number before the slash (／) is movement speed on the ground, and the number after the slash is movement speed when performing special movements. In rare cases, there are monsters that do not move on the ground (such as those that are always floating in the air), so in these cases, the movement method is written in parentheses immediately after the movement speed.

##### Number

This is the most common number appearing when encountering that monster. Monsters that act in groups are usually encountered in large numbers, while monsters that have a strong sense of territory and really only exist alone in a certain area are unlikely to be encountered in numbers greater than one.

This data is not exact, and the game master may change the number appearing depending on the circumstances of the scenario. However, in order to do so, you will need a reason that the players can understand.

##### Frequency

This is the frequency at which the monster appears. The types in descending order of frequency are frequent, moderate, rare, and very rare. It's a bit unnatural to have rare or very rare monsters repeatedly appear in a scenario. In such cases, it would be best to provide a reason that the players can understand.

##### Intellect

Indicates the monster's degree of intellect. There are eight types: none, almost none, obeys commands, animal, low, human, high, and very high.

If it says none, that means it doesn't have intelligence, so to speak. It does not think, nor does it even have instincts. It acts only on reflex. It's similar to how a mimosa closes its leaves when touched. Spells that affect the mind have no effect on these monsters. If you were to convert it to an intelligence score, it would be 0.

If it says almost none, then it has almost no intellect. They have no advanced thinking and have almost no means of communicating their intentions. They only act on instinct. This is the intellectual standard of lower animals such as insects. If you were to convert it to intelligence, it would be 1-2. Of course, spells that affect the mind cannot be expected to have any effect.

If it says obeys commands, it's common among magical creatures created by magic, the undead, etc. If given a command-- the only ones who can give commands are those who directly created the monster or those who used magic to give the command --they will faithfully carry it out, but they cannot make their own decisions. However, they have a memory comparable to that of humans, and can answer questions accurately if asked (if commanded to answer the question). If you were to convert it to intelligence, it would be 1 for judgment ability, but around 10 for memory if they're able to remember. Since they do not act on their own judgment, spells that affect the minds are ineffective.

If it says animal, it means literally the same degree as an animal. They can distinguish their master and will follow their commands (if they're trained). Also, they have enough judgment ability to quickly run away if their life is in danger. If you were to convert it to intelligence, it would be around 3 to 5. However, they can sometimes display surprising judgment, although this is something that has been learned as an instinct. There are known stories of parent birds feigning injury to keep predators away from their nests, and predators using intimidation to lure prey to ambush spots for their mates.

If it says low, it means that while the intellect is not as high as that of humans, it is still quite high. They can also use primitive tools, words, and a very limited number of written characters. Although they're somewhat slow, they're able to make accurate judgments in normal activities. However, they're not good enough to fight using advanced tactics, and are easily fooled by simple words and tricks. If you were to convert it to intelligence, it would be around 6 to 8.

If it says human, it means an intellect that's almost the same as that of a human. They can handle tools, words, text, etc. freely. If you were to convert it to intelligence, it would be 10 to 15.

If it says high, it means that it has a greater intellect than the average human. For a human, you could even use the adjective wise. If you were to convert it to intelligence, it would be 18 to 20.

If it says very high, it means their intellect is beyond the reach of normal humans. A human with this much intellect would probably go down in history as a great genius. If you were to convert it to intelligence, it would be 24 or greater.

##### Reaction

This represents the monster's general reaction when it encounters adventurers. It can be violent, adversarial, neutral, friendly, hunger-based or command-based.

If it says violent, that means it will attack immediately. Examples include undead who have hatred for the living, and plants that act solely on reflex. Many have no concept of running away.

If it says adversarial, it means they consider adventurers (human or fae) to be their enemies. The specific actions they'll take will vary depending on the power dynamic (difference in number) between the adventurers and monsters, as well as the intelligence of the monsters. Even if the monster is adversarial, if the adventurers have the superior numbers, it will not attack immediately and may try to use trickery.

If it says neutral, it means the monster holds no special feelings of hostility nor allyship towards the adventurers. Depending on the situation, they can be your enemy or your ally. Sometimes they simply avoid interaction and disappear.

If it says friendly, it means the monster has friendly feelings towards adventurers (humans and fae). If you don't feel like they're a nuisance to you, they might provide some assistance. However, if an adventurer takes hostile action, they will naturally consider retaliation. In addition, out in the world are also monsters that get carried away, who do things that end up causing annoyance even though they mean no harm.

If it says hunger-based, it means they're basically neutral. However, for carnivorous (omnivorous) animals, it can be very dangerous when they're hungry. This is because they may attack adventurers, seeing them as food.

Command-based is often seen in magical creatures and lower grade undead that move according to the commands of others. They follow the instructions of their commander. Whether they consider adventurers to be enemies or not depends on the commands given to them.

There are several other reactions as well, but you can understand their meaning by looking at the explanation text after the data.

##### Attack Points

This represents the monster's attack method and its accuracy. The higher this score, the more likely the monster will be able to hit you with an attack. A character must make a success roll using their evasion speed as the baseline score and these attack points as the target score. If you fail, you will suffer damage (refer to Chapter 4: Weapon Combat).

Some monsters have multiple attack methods. Multiple attack points are also listed for these cases. In this case, if they're written on one line separated by a slash (／), it means that they can attack that number of times in one round. For example, Horn：12 (5)／Hoof：12 (5) means that two attacks can be made with horn and hoof. Each targeted character must make a success roll to determine whether they're able to avoid the attack.

If there are multiple attack methods, but they are written on two (or more) lines, the monster may have multiple attack methods, but can only use one of them during a round.

The numbers in parentheses next to each attack point score are used in the optional rule 16.1: Combat in Which Monsters Rolls Dice.

##### Strike Points

This represents the amount of damage dealt by the monster. If a character fails to evade their attack, these strike points become damage and reduce the character's life force. A character can reduce this damage through armor (defense rolls) and adventurer level.

Monsters that have multiple attack methods also have multiple strike points written next to them. The arrangement of attack points also carries over to strike points.

If Attack Points=Horn：12 (5)／Hoof：12 (5) is written as Strike Points=17／16, then if the horn attack hits, it'll deal 17 points of damage, and the hoof attack hits, it'll deal 16 points.

##### Evasion Points

This represents the degree to which the monster can evade attacks. In order for a character to hit a monster with an attack, they must succeed on a success roll using these evasion points as the target score and their attack power as the baseline score. If you fail, your character's attack will miss.

##### Defense Points

Just as characters can reduce damage through armor, monsters also have thick skin, shells, scales, etc. to reduce damage (some fae and youma may wear armor just like humans). This is represented by defense points. When a monster suffers damage from a character's (weapon) attack, they can reduce the damage by the amount of defense points. This is exactly the same as a character's damage reduction due to armor (defense rolls) and adventurer level.

Defense points are only effective against attacks such as weapons, etc. When struck by magic or similar attacks, defense points cannot reduce damage, monster level reduces damage instead. Whether or not a character can reduce damage through armor is the standard for deciding whether to use defense points or monster level.

Monster level, like adventurer level, prevents all damage, but a monster's defense points already include damage reduction due to monster level. Therefore, only defense points should be applied when reducing damage from weapon attacks. Monster level may not be further subtracted from it.

##### Life Points／Resistance

There are two numbers written. The number before the slash (／) is life points, and the number after is life point resistance.

Life points represents the monster's life force. When a monster suffers damage, it will lose life points. As with a character, when a monster's life points fall to 0 or less, they become disabled and, in some cases, die.

(Life point) resistance is a substitute for a character's life force resistance roll. When a character is poisoned, etc. a life force resistance roll determines whether they can avoid or reduce the effects of the poison. In the case of monsters, life point resistance is used instead. When a monster is poisoned, etc. compare its resistance score with the strength of the poison (toxicity score). If the life point resistance is greater, the monster will be safe from the effects of the poison. Where a character would make a life force resistance roll, a monster would use their life point resistance. For characters, the resistance roll is successful if the final score of the resistance roll is equal to the toxicity score, etc., but for monsters, the life point resistance must be greater than the toxicity score, etc.

The baseline score when making a judgment by rolling the dice, just like a character, is written in parenthesis next to the life point resistance.

##### Mental Points／Resistance

Mental points have the same meaning as a character's mental power. When a monster uses magic, it consumes mental points, just like a character. Monsters whose mental points are reduced to 0 (or less) by Shade magic, etc. will fall unconscious. Mental point resistance is a score that's a substitute for a character's mental power resistance roll, so when a character casts magic on a monster, this mental point resistance becomes the target score.

When a character casts a spell on a monster, they must make a success roll using their magic power as the baseline score. If the final score is equal to or greater than the monster's mental point resistance, the magic will successfully be cast. Please refer to 5.1.4.4: Procedure When an Adventurer Casts Resistible Magic on a Monster. Conversely, for a monster to resist magic, its mental point resistance must be greater than the magic's final score. A tie means the magic will successfully be cast. Please be careful about this. This is done purely for consistency, so that from the character's perspective, tied success rolls are always successful.

##### Special Abilities

Monsters may have various special abilities. Some breathe fire, and others are not affected by mental attacks. There are some that cannot be hurt by normal weapons, and require magic or magical weapons to defeat them.

When a monster has such special abilities, they are briefly expressed here. Since the amount of text would be enormous, we will avoid explaining each one individually here. When necessary, refer to the main text of the monster catalog and 13.6: Dealing with Monster Special Abilities.

##### Habitat

This is where the monster commonly lives. If you want to have the monster appear in a place other than what's shown here, you'll need a reason that the players can understand.

##### Perception

This represents the monster's sensory abilities. There are three types: five senses, pseudo, and magic.

Five senses refer to the same five senses that humans use to perceive the outside world: vision, hearing, smell, taste, and touch. In some cases, some of these senses may be missing. Illusions that deceive monsters which lack these senses will be ineffective. It may also include specialized features such as darkvision, infravision, illumination, sonar, and vibration sense.

(Darkvision) means the monster can see completely in the dark. Dwarf player characters have this ability.

(Infravision) indicates that the monster can see the heat of the target, similar to a shaman's infravision, and can perceive it even in places where there is no normal light.

(Illumination) means the monster can see as clearly as daytime even under very weak light, such as only starlight.

(Sonar) means the monster can use sound waves or ultrasonic echoes to perceive the outside world. Therefore, they have almost no restrictions on action even in the dark.

(Vibration sense) means the monster can sense vibrations in the ground and perceive things moving around it. They cannot perceive things that are flying in the air or that are not moving.

Those whose sensory abilities are pseudo have five pseudo-senses through magical means. After all, one part may be missing, or they may have special senses. In such cases, there is an organ that captures the sensation in a pseudo manner. If those organs are destroyed, the pseudo-senses will no longer be usable. For example, skeletons can use their empty eye sockets for pseudo vision. Therefore, if they're blindfolded, they won't be able to see, and they won't be able to see anything approaching from behind. Monsters whose perception is pseudo can experience illusions.

Those whose sensory abilities are magic perceive their surroundings with magical senses. These senses cannot be blocked or deceived by any means. Illusions are ineffective on monsters whose perception is magic.

##### Languages

This indicates whether the monster speaks, and if so, what kind of language it uses. Only normal languages are described, and runes (except for silent spirit) are omitted. If it says none, then the monster does not use language (those with obeys commands intellect may not speak themselves, but may understand what others are saying). For more information on language, please refer to 12.1: Rules Regarding Language.

### 13.2.2 Fae

#### [ Pixie ]

- Monster Level=1
- Rarity=12
- Agility=14    Movement Speed=4／7 (air)
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Friendly
- Attack Points=Weapon: 8 (1)    Strike Points=2
- Evasion Points=10 (3)    Defense Points=3
- Life Points／Resistance=7／8 (1)
- Mental Points／Resistance=15／9 (2)
- Special Abilities=2nd level spirit magic (Magic Intensity／Magic Power=11／4); Invisibility
- Habitat=Forests, meadows
- Languages=Fairy, silent spirit
- Perception=Five senses (infravision)

Pixies look similar to elves, but are only about 30 cm tall. They have wings on their backs reminiscent of insects. Most of them have the appearance of women, but there are also individuals that have the appearance of men. Also, for some reason, they seem to be wearing something that looks like clothes. Although they are relatively friendly towards humans, they do not actively interact with humans and rarely appear in public. Moreover, they seem to have a very close relationship with the small spirits called sprites, and have as a basic ability the power of the Invisibility spell that the sprites provide to shamans, which makes them all the more difficult to witness. They can use this ability without any restrictions, and they do not consume mental points by using this ability. However, in order to remain invisible, they need focus, and if they cannot do this, you will not be able to use Invisibility, and even if they do use it, if they lose their concentration (such as when attacking or using other magic, etc.) they will appear instantly.

They sometimes play pranks on humans. They'll whisper in your ear while remaining hidden from view, and thrust a weapon in their hand (it appears to be a needle-thin dagger) into your butt.

Combat is unlikely to occur, but when it does, pixies can use up to 2nd level spirit magic.

#### [ Fairy ]

- Monster Level=1
- Rarity=11
- Agility=18    Movement Speed=9／10 (Air)
- Number=Several    Frequency=Rare
- Intellect=Human    Reaction=Friendly to neutral
- Attack Points=Weapon: 8 (1)    Strike Points=3
- Evasion Points=10 (3)    Defense Points=3
- Life Points／Resistance=10／8 (1)
- Mental Points／Resistance=18／10 (3)
- Special Abilities=3rd level spirit magic (Magic Intensity／Magic Power=12／5)
- Habitat=Uncertain
- Languages=Fairy, silent spirit
- Perception=Five senses (infravision)

Fairies are a representative race of fae, and many of them still live in the fae world, and rarely come to the material world, the world we live in. However, there are some places in the material world that have contact with the fae world. Stories are often told of humans who inadvertently wandered into the fae world from these places.

Fairies are sometimes seen where these two worlds meet. Just as humans wander into the fae world, there are also fairies who wander from the fae world into the material world. Fairies take the form of beautiful elf women, often mostly naked or clad in thin silk garments. They are about the same height as elves, but the most prominent difference between them and elves is the beautiful wings that grow from their backs. These wings are very thin but strong, allowing them to fly, albeit at a slow speed. They may carry items such as silver daggers, etc. for self-defense, but they rarely wield them. If they really get into trouble, they will choose to use their power of spirit magic rather than weapons. As they are residents of the fae world, they have a deep connection with spirits, and use spirit magic up to 3rd level.

#### [ Pooka ]

- Monster Level=3
- Rarity=12
- Agility=18    Movement Speed=18
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Friendly
- Attack Points=Fist: 11 (4)    Strike Points=4
- Evasion Points=13 (6)    Defense Points=5
- Life Points／Resistance=10／10 (3)
- Mental Points／Resistance=8／12 (5)
- Special Abilities=3rd level spirit magic (Magic Intensity／Magic Power=12／5); Shapeshift (Animal)
- Habitat=Forests
- Languages=Fairy, silent spirit, regional
- Perception=Five senses (infravision)

The Pooka is a member of the fairy family that lives in the forest, and looks similar to a grassrunner, but is a little smarter. They're not in the habit of wearing clothes. However, they don't always wander around naked; they have the ability to transform into forest animals, and most of the time they live as animals. While transformed, they can use all of the animal's physical abilities and can also speak. However, they cannot transform into very large animals such as bears, wolves, etc. They mostly turn into foxes, fawns, rabbits, squirrels etc. This transformation cannot be detected even by using Sense Magic or Sense Aura.

They are friendly to characters they meet in the forest, and will contact them in an attempt to befriend them. However, they like mischief, and in order to surprise you, they will sometimes call out to you while disguised as an animal, hiding their appearance, etc. However, once you get in touch with them, they will help you in many ways. They will guide you through the forest and tell you where dangerous places are. In addition, they will show lifelong loyalty to a character who saves them from danger, and will act together with them. They can use spirit magic. Their shaman skill level is 3.

#### [ Featherfolk ]

- Monster Level=4
- Rarity=9
- Agility=16
- Movement Speed=10／30 (air)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Weapon: 11 (4)    Strike Points=8
- Evasion Points=12 (5)    Defense Points=7
- Life Points／Resistance=12／12 (5)
- Mental Points／Resistance=18／13 (6)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6)
- Habitat=Mountains
- Languages=Harpy, silent spirit, regional
- Perception=Five senses (infravision)

Featherfolk resemble humans, but have bird wings growing from their shoulders, allowing them to fly. Both their men and women look beautiful. They live in rugged mountainous areas, have gentle personalities and do not like fighting, but they despise harpies (furia-species). Their language and customs are similar to humans, although their level of culture is somewhat lower. However, they're not interested in gold or jewelry.

Featherfolk use swords, bows and arrows, and spears as weapons. They cannot wear heavy armor, only soft leather at most. They use spirit magic and their shaman skill level is 4. Sometimes they keep eagles and griffons for reconnaissance and self-defense purposes.

#### [ Merman ]

- Monster Level=2
- Rarity=11
- Agility=16    Movement Speed=3／20 (water)
- Number=Several to dozens
- Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Weapon: 9 (2)    Strike Points=5
- Evasion Points=10 (3)    Defense Points=4
- Life Points／Resistance=14／10 (3)
- Mental Points／Resistance=16／10 (3)
- Special Abilities=Water adaptation
- Habitat=Seas
- Languages=Merman
- Perception=Five senses (illumination)

Mermen are a race that lives under the sea, with the upper body of a human and the lower body of fish. Female mermen are called mermaids. They have an extreme fear and hatred of humans and will never try to negotiate with them. This is because over a hundred years ago, a rumor spread that eating merman flesh will give long life, so humans fought and overhunted mermen. Since then, mermen have lived at the bottom of the deep sea, avoiding humans, and their social system and customs are shrouded in mystery.

Mermen are a species that breathes underwater and cannot breathe on land. They can only act on land for up to their life points rounds (14 rounds), after which they will suffocate. They usually live in groups of about a few dozen. The group has a leader and a shaman who govern the tribe.

They use a trident as a weapon.

#### [ Mermaid Shaman ]

- Monster Level=4
- Rarity=18
- Agility=16    Movement Speed=3／20 (water)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Weapon: 10 (3)    Strike Points=7
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=12／12 (5)
- Mental Points／Resistance=18／13 (6)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6, water spirits only); Water adaptation
- Habitat=Seas
- Languages=Merman, silent spirit
- Perception=Five senses (infravision, illumination)

Merman tribes select girls with outstanding intelligence and mental power and train them as shamans from an early age. The result is a mermaid shaman. Mermaid shamans can use spirit magic up to 4th level, which is powered by water spirits (undine). There is one mermaid shaman per combat group, and her role is to assist the merman leader. Also, if the merman leader is defeated, she will take command of the battle in his place. A combat group whose leader and shaman are both defeated will either join another group or flee. When this is not possible, the mermen will fight to the death.

#### [ Merman Leader ]

- Monster Level=4
- Rarity=13
- Agility=16    Movement Speed=3／20 (water)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Weapon: 10 (3)    Strike Points=8
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=15／12 (5)
- Mental Points／Resistance=17／12 (5)
- Special Abilities=Water adaptation
- Habitat=Seas
- Languages=Merman
- Perception=Five senses (illumination)

Merman tribes select physically superior boys from an early age and give them special training. Those who receive training and grow up will become merman leaders, the head of a combat group of 10 mermen, and command those mermen in battle. Also, a particularly chosen one among them becomes the chieftain who leads the tribe.

### 13.2.3 Youma

#### [ Imp ]

- Monster Level=1
- Rarity=12
- Agility=14    Movement Speed=7／7 (air)
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Tail: 8 (1)    Strike Points=4+poison
- Evasion Points=9 (2)    Defense Points=3
- Life Points／Resistance=8／8 (1)
- Mental Points／Resistance=14／9 (2)
- Special Abilities=1st level dark magic (Magic Intensity／Magic Power=10／3); Poison (Toxicity Score 10, Paralysis, Duration=1 Hour)
- Habitat=Unknown
- Languages=Impish
- Perception=Five senses (darkvision)

Imps are small youma with brown to dark brown skin, no body hair, and a tail. Its tip is sharp like the tip of a spear, and the imp uses this tail to attack. The tail contains a paralyzing poison. Anyone who suffers damage from an imp's attack must attempt a life force resistance roll. If you fail, you've been poisoned and will be paralyzed and unable to move at the end of the next round.

The ecology of imps, such as where they live, etc. is not well understood. They are sometimes seen in large cities, and sometimes live in abandoned houses in the suburbs. They may use 1st level dark magic, and may also be the familiars of evil sorcerers (many of whom also have the dark priest skill).

The imp looks very similar to the gargoyle and its model, the zalbard. For this reason, some sages argue that imps are not youma at all, but were originally underworld creatures.

#### [ Kobold ]

- Monster Level=1
- Rarity=6
- Agility=14
- Movement Speed=8
- Number=Several to dozens
- Frequency=Frequent
- Intellect=Low
- Reaction=Adversarial
- Attack Points=Weapon or fangs: 8 (1)
- Strike Points=5
- Evasion Points=10 (3)
- Defense Points=3
- Life Points／Resistance=8／8 (1)
- Mental Points／Resistance=8／8 (1)
- Special Abilities=Silver corrosion?
- Habitat=Mountains near human villages, forests, caves
- Languages=Goblin
- Perception=Five senses (darkvision)

Kobolds are small youma with dog-like faces and tails. They have no body hair at all. They live in forests, hills, and mountains near human villages, but they are timid and rarely cause harm to human homes. However, kobolds are also known to be sneaky and will attack opponents who are outnumbered, wounded, or unable to fight, such as women and children. They usually attack with their fangs, but they may also use a piece of wood as a club (in terms of data, they are the same).

Legend has it that kobolds can corrode silver, so they are fiercely regarded as enemies by miners and dwarves.

#### [ Gremlin ]

- Monster Level=2
- Rarity=9
- Agility=17    Movement Speed=6／8 (air)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Fangs: 9 (2)    Strike Points=3
- Evasion Points=11 (4)    Defense Points=4
- Life Points／Resistance=8／9 (2)
- Mental Points／Resistance=14／10 (3)
- Special Abilities=2nd level spirit magic (Magic Intensity／Magic Power=11／4)
- Habitat=Mountains, highlands
- Languages=Impish, silent spirit
- Perception=Five senses (infravision)

A small winged youma also known as the "sky imp". Its body is dark brown and it has black wings on its back resembling those of a bat. These wings allow them to fly, but their speed is not that great. They have the power to use spirit magic up to 2nd level.

Gremlins are not aggressive, but they are treacherous and enjoy playing malicious pranks. The tragedy of the hero Grax riding Pegasus and dying in a crash due to a gremlin's prank is widely known in Alecrast. (See here)

#### [ Hobgoblin ]

- Monster Level=3
- Rarity=8
- Agility=12
- Movement Speed=8
- Number=Several
- Frequency=Normal
- Intellect=Low
- Reaction=Adversarial
- Attack Points=Weapon or fangs: 10 (3)
- Strike Points=10
- Evasion Points=11 (4)
- Defense Points=7
- Life Points／Resistance=15／11 (4)
- Mental Points／Resistance=12／11 (4)
- Special Abilities=None in particular
- Habitat=Mountains relatively far from human villages, forests, caves
- Languages=Goblin
- Perception=Five senses (darkvision)

Hobgoblins are a race of youma that are closely related to goblins, described later. They have reddish-brown skin and very little hair on their heads, but they do have thick hair all over their bodies. They are a feared monster with a physique comparable to that of a human, strong and powerful. When fighting, they use either a crude club or the fangs that protrude from their jaws. Although they have a belligerent personality, they are also surprisingly cowardly, and will run away as soon as they see that the situation is not going well.

Although they may live in a goblin village, they usually live alone or in groups of several, frequently changing locations and living relatively far from human villages.

#### [ Goblin ]

- Monster Level=2
- Rarity=5
- Agility=13    Movement Speed=8
- Number=Several to dozens
- Frequency=Frequent
- Intellect=Low    Reaction=Adversarial
- Attack Points=Weapon or fangs: 9 (2)
- Strike Points=7
- Evasion Points=10 (3)    Defense Points=5
- Life Points／Resistance=12／10 (3)
- Mental Points／Resistance=10／9 (2)
- Special Abilities=None in particular
- Habitat=Mountains near human villages, forests, caves
- Languages=Goblin
- Perception=Five senses (darkvision)

Goblins are a type of youma that live near human villages, and are extremely common monsters in Alecrast. Their height is slightly smaller than that of a human, and their skin is reddish-brown. They usually live in groups of several to several dozen in forests and hills, but they sometimes appear at people's homes and attack livestock or steal. They often use weapons (mostly small ones such as shortswords, daggers etc.) stolen from humans. In their villages, they may use kobolds and human children as slaves. They may also live with a hobgoblin who acts as their bodyguard.

#### [ Goblin Shaman ]

- Monster Level=3
- Rarity=10
- Agility=13    Movement Speed=8
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon or fang: 10 (3)
- Strike Points=8
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=12／11 (4)
- Mental Points／Resistance=15／11 (4)
- Special Abilities=3rd level spirit magic (Magic Intensity／Magic Power=12／5); 1st level dark magic (Magic Intensity／Magic Power=10／3)
- Habitat=Mountains, forests, caves
- Languages=Goblin, silent spirit, regional
- Perception=Five senses (darkvision, infravision)

Among the goblin tribe, this refers to those who are skilled in the power of spirit magic. Their physical characteristics are not much different from ordinary goblins, but they are smart and moreover, have mastered silent spirit. This is not surprising, considering that goblins are originally from the fae world. Some goblin shamans are also dark priests who can use dark magic. Goblins served the dark gods in mythical times. A goblin shaman has either a 3rd level shaman skill (magical intensity 12／magic power 5), a 1st level dark priest skill (magical intensity 10／magic power 3), or both.

#### [ Goblin Lord ]

- Monster Level=4
- Rarity=10
- Agility=12    Movement Speed=10
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon or fangs: 11 (4)
- Strike Points=11
- Evasion Points=12 (5)    Defense Points=7
- Life Points／Resistance=18／13 (6)
- Mental Points／Resistance=15／12 (5)
- Special Abilities=None in particular
- Habitat=Mountains, forests, caves
- Languages=Goblin, regional
- Perception=Five senses (darkvision)

The goblin lord, as the name suggests, is the king of the goblins. However, not all tribes have this type of lord-species, if anything they're rare. They are a greater species of goblin, so to speak, who retain a limited amount of power from the time when goblins lived in the fairy world. Although they lack magical abilities, they have bodies that are about the same size or even larger than humans and hobgoblins. It is said that there are quite a few of this goblin lord species in the Youma Forest to the east of Alecrast.

#### [ Marshman ]

- Monster Level=4
- Rarity=15    Agility=13
- Movement Speed=6／18 (water)
- Number=One to several
- Frequency=Very rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Claw：12 (5) ／Claw：12 (5)
- Strike Points=11／11
- Evasion Points=12 (5)    Defense Points=9
- Life Points／Resistance=18 (13／6)
- Mental Points／Resistance=15 (12／5)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6); Weak to fire; Weak to dehydration
- Habitat=Swamps
- Languages=Impish, regional
- Perception=Five senses (infravision)

Marshmen, also known as water imps, are youma that live in swamps. Their bodies are covered with green skin, and their backs are hard and shell-shaped. They have high intelligence comparable to humans, and also have a rudimentary social life. They are exclusionary toward other races and react aggressively to anything that enters their habitat. They seem to have a deep connection with water spirits, and use undine-type spirit magic up to 4th level.

They're weak against fire and heat, so when attacking a marshman with fire-based magic, add +10 to strike power when making the check. In addition, they are susceptible to dehydration and are nearly unable to leave the swamps where they live. If they're forced to leave and their body becomes dehydrated, they'll lose life points at the rate of 1 point every hour.

#### [ Dark Elf ]

- Monster Level=3
- Rarity=11
- Agility=19    Movement Speed=19
- Number=One to several    Frequency=Rare
- Intellect=High    Reaction=Adversarial
- Attack Points=Weapon: 9 (2)    Strike Points=6+poison
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=10／10 (3)
- Mental Points／Resistance=17／15 (8)
- Special Abilities=3rd level spirit magic (Magic Intensity／Magic Power=13／6); 1st level dark magic (Magic Intensity／Magic Power=11／4); Poison (Toxicity Score 10, Strike Power 10, Bonus Damage 3)
- Habitat=Forests far from human villages
- Languages=Elven, silent spirit, regional
- Perception=Five senses (darkvision, infravision)

In the ancient battle of the gods, the elves fought on the side of the gods of light. However, there were some who sided with the dark gods. These elves with jet-black skin are called dark elves.

They are apostles of the dark gods, and love to be despicable. Assassination using Invisibility is said to be their most special technique. The weapons they use are often coated with poison. A character who is attacked by a poisoned weapon and suffers damage must immediately make a life force resistance roll against target score 10. If you fail, you will suffer damage resulting from a strike power 10 strike roll plus +3 bonus damage. This damage is separate from the damage of the weapon itself and can be reduced by adventurer level. If you successfully resist, you will not suffer any poison damage.

Dark elves often conspire with stronger beings (such as dark priests) to plan great acts of evil. Humans also harbor strong hostility toward dark elves.

#### [ Dark Elf Leader ]

- Monster Level=6
- Rarity=11
- Agility=19    Movement Speed=19
- Number=One    Frequency=Very Rare
- Intellect=High    Reaction=Adversarial
- Attack Points=Weapon: 12 (5)
- Strike Points=9+poison
- Evasion Points=15 (8)    Defense Points=9
- Life Points／Resistance=10／13 (6)
- Mental Points／Resistance=17／18 (11)
- Special Abilities=6th level spirit magic (Magic Intensity／Magic Power=16／9); 5th level dark magic (Magic Intensity／Magic Power=15／8); Poison (Toxicity score 13, paralysis, lasts 12 hours)
- Habitat=Forests far from human villages
- Languages=Elven, silent spirit, regional
- Perception=Five senses (darkvision, infravision)

Dark Elves vary widely in their individual abilities, just like adventurers. The data listed here is based on the strength needed to lead a group of 5 to 6 people. Those who lead larger groups can be even stronger.

Leaders also often apply and use poison on their weapons. The poison they use has a higher toxicity score than the usual kind, and its effect is paralysis. If a character is poisoned and also fails a life force resistance roll (target score 13), the character will be paralyzed at the end of the next round.

### 13.2.4 Spirits

#### [ Will-O-Wisp ]

- Monster Level=2
- Rarity=12 (However, a shaman always knows)
- Agility=18    Movement Speed=20 (air)
- Number=Solo to several    Frequency=Rare
- Intellect=Almost none
- Reaction=Neutral to violent
- Attack Points=Disintegrate：Always hits
- Strike Points=Strike power 10, bonus damage 2
- Evasion Points=12 (5)    Defense Points=0
- Life Points／Resistance=1／8 (1)
- Mental Points／Resistance=ー／10 (3)
- Special Abilities=Releases energy and disintegrates; Mental attack immunity; Not affected by poison and illness
- Habitat=Near forests and swamps, or anywhere
- Languages=None
- Perception=Magic

Will-O-Wisp is a spirit of light. Its main body is a blue-white ball of light about 50 cm in diameter, and its light illuminates a space with a 5-meter radius. They are among the most unstable of spirits and have little to no semblance of intellect. When they appear as mad spirits, there are two actions they can take. First, one will float gently in front of someone and lead them deep into an endless swamp or forest. This type of will-o-wisp will not attack you directly.

The other type is one that collides directly with anything that comes into view. Will-o-wisps only target things that have a functioning mind. They will not target plants, minerals, vessels, etc. that do not have intelligence. They also will not attack low grade undead that do not have a mind. However, sleeping humans are subject to attack. Please make your judgment based on whether it has a score called mental power (points). Will-o-wisp attacks are always successful. When a Will-O-Wisp hits its target, it'll simply shatter. However, at the same time, the will-o-wisp emits a powerful shockwave. This shockwave's damage results from a strike power 10 strike roll plus bonus damage 2. Armor is ineffective against this attack, and only adventurer level can reduce the damage.

If you strike a will-o-wisp with a melee weapon (it doesn't have to be silver or magical), you can destroy it, but the attacker will also suffer damage as if they were hit by the will-o-wisp.

Will-o-wisp is the counterpart to the shade, which is described below, and when it comes into contact with a shade, it disappears without emitting any energy.

#### [ Shade ]

- Monster Level=2
- Rarity=12 (However, a shaman always knows)
- Agility=18    Movement Speed=20 (air)
- Number=One to several    Frequency=Rare
- Intellect=Almost none
- Reaction=Violent
- Attack Points=Disintegrate：Always hits
- Strike Points=Strike power 10, bonus damage 2, to mental power
- Evasion Points=12 (5)    Defense Points=0
- Life Points／Resistance=1／8 (1)
- Mental Points／Resistance=ー／10 (3)
- Special Abilities=Energy disintegration that deals damage to mind; Mental attack immunity; Not affected by poison and illness
- Habitat=Anywhere
- Languages=None
- Perception=Magic

Shade is a spirit of darkness, and also a mind spirit that controls fear. All natural light within 5 meters of its body is canceled out, leaving you in total darkness. Its body seems to be dark and spherical, but it's impossible to identify its shape because it's in the dark. Therefore, attacks against shades always suffer a -4 penalty. Since the shade itself has 12 evasion points, it's unlikely that your attacks will hit it (it'll definitely disintegrate if they do). They will always attack by ramming any being with a will that comes into their view. Its effect is exactly like a will-o-wisp attack, except that the damage is dealt to mental power instead of life force. Strike power is 10, bonus damage is 2, and only adventurer level can reduce it.

Shade is the counterpart to the aforementioned will-o-wisp, and when it comes into contact with a will-o-wisp, it disappears without emitting any energy.

#### [ Brownie ]

- Monster Level=3
- Rarity=14 (However, a shaman always knows)
- Agility=14    Movement Speed=Special
- Number=Solo to several
- Frequency=Very Rare
- Intellect=Human
- Reaction=Neutral to violent
- Attack Points=Furniture：10 (3)
- Strike Points=5 to 9
- Evasion Points=ー    Defense Points=ー
- Life Points／Resistance=ー／ー
- Mental Points／Resistance=18／12 (5)
- Special Abilities=Physical attack immunity; Mental attack immunity; Not affected by poison and illness; Teleport (Limited); Illusion
- Habitat=Old mansions
- Languages=Silent spirit, mansion residents' language
- Perception=Magic

Brownie is a spirit that appears in old mansions where people have lived for over 50 years. If the humans living in the mansion disappear or die, the brownie may turn into a mad spirit.

Mad brownies have the ability to create illusions. Some illusions are visual, while others are auditory, making their presence known through visions or strange noises.

They also have a small amount of telekinesis, and will attack unwanted intruders by hitting them with things inside the mansion. The strike points when this attack hits vary depending on what is used for the attack. A small dish would be 5 points, a knife, etc. would be 7, and a large chest of drawers would be 9.

Mad brownies also have the ability to teleport, allowing them to appear anywhere in the mansion. Also, they are fully aware of everything happening inside the mansion with their magic senses.

However, these abilities can only be manifested within the mansion, and the brownie cannot leave the mansion.

Mad Brownies are often influenced by the actions of those who lived there, and in some cases continue to faithfully reproduce those actions through illusions (and telekinesis) after the residents have left.

Brownies have no substance, and physical attacks have no effect on them at all. However, if their mental points are reduced to 0 or if the mansion they live in is destroyed, they will vanish.

#### [ Undine ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=10
- Movement Speed=6／10 (water)
- Number=Solo to several    Frequency=Rare
- Intellect=Human    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6, undine only); Enter lungs (Target score for evade and resist=12); Mental attack immunity; Normal weapon immunity; Not affected by poison and illness
- Habitat=Water
- Languages=Silent spirit
- Perception=Magic

Undine is a Water Spirit. Its body is just about 10 liters of liquid. It often takes the form of a small girl, but it can take any form as long as its weight and volume remain the same. Undine has no direct means of attack. They can stick to their opponent and make them uncomfortable, or they can wrap around their face and make them feel pain for a while, but if the opponent has the will to resist, they can easily escape. However, if anyone bathes or swims in a spring or river where this spirit resides, without realizing its presence, the mad undine will do everything it can to drown its opponent, including casting a Sink spell to take away their buoyancy or fly directly into their lungs.

Undine can cast magic sourced from the power of undine without consuming its own mental points (the spells cannot be expanded). Undine's shaman skill level should be 4.

If a target drinks even a little of an undine's body, this water spirit will enter directly into their lungs. A check for whether or not you've taken a drink is made via success roll using "adventurer level + agility bonus" as the baseline score. The target score in this case is 12. This check must be made every round until you escape from the spring or river containing the undine. However, in this case, you can obviously hold your breath. As long as you hold your breath, you don't have to worry about drinking the water. However, the undine's first attack will always be a surprise attack, so in the first round, please make a check to see whether you've swallowed the undine or not.

If a character fails the check, that means they've swallowed the undine. However, the victim can attempt to spit the undine out once swallowed. To do so, you must make a successful life force resistance roll. The target score is still 12. This check may be attempted once per round, but you cannot take any other actions while swallowing the undine. Also, you cannot spit out the undine while underwater.

The number of rounds in which you can hold your breath, or in which you can survive while swallowing an undine, is equal to your life force. Also, please refer to 10.4: Water Combat for detailed rules.

Undines do not leave their habitat, so they are not a threat as long as you can escape from the water. Of course, this attack has no meaning against things that don't breathe air (fish, undead, etc.). The same goes for characters who've had Water Breathing cast on them.

To harm an undine, as with most other spirits, magical or silver weapons are required.

#### [ Salamander ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=10    Movement Speed=6
- Number=Solo to several    Frequency=Rare
- Intellect=Low    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=Fire (Strike power 10, bonus damage 5, Magic Intensity／Magic Power=12／5); Normal weapon immunity; Mental attack immunity; Fire immunity; Not affected by poison and illness; Weak to water
- Habitat=Anywhere, provided there's fire
- Languages=Silent spirit
- Perception=Magic

Salamanders, which are spirits of fire, look like quadrupedal beasts with a body length of about 1 meter, as they are called by the name fire lizard. However, its entire body is not covered in animal skin but in flames, making it extremely dangerous as it ignites flammable materials around it. A mad salamander, as befitting of a spirit of fire, a symbol of destruction, acts with the sole purpose of burning everything to ash. Salamanders shower you in a breath of fire, which has the same effect as the 1st level spirit magic spell Fire Bolt. This fire always hits, but an adventurer can attempt to resist just the same way they would against magic. A Salamander's fire breath ability should be treated as shaman skill level 4, magic intensity 12 (magic power 5). Even when the Salamander breathes out this fiery breath, it does not consume a single mental point.

Salamanders are spirits, so their temporary bodies are, so to speak, a modified form of their spirit power, so they cannot be attacked by normal weapons. Iron can obstruct the workings of a spirit, but it cannot be used as a means to extinguish it. To damage a Salamander, you need a magic or magically-imbued weapon, or a silver weapon. Also, when a person using the spirit magic Water Screen is attacked by a salamander, after the normal effect, 2 points of damage will be dealt to the salamander (the salamander cannot reduce this damage), then the magic's effect will vanish. You can also deal damage to a Salamander by pouring water on it. The damage is 1 point per liter of water. A salamander cannot reduce this damage either. Conversely, fire attacks have no effect on salamanders.

#### [ Sandman ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=18
- Movement Speed=16／6 (air)
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Violent
- Attack Points=Arm：12 (5)    Strike Points=5
- Evasion Points=14 (7)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6, sandman only); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness; Teleport
- Habitat=Anywhere
- Languages=Silent spirit
- Perception=Magic

Sandman is a mind spirit that controls sleep. Its figure is that of a small, completely naked child, with no features that would indicate gender.

A mad sandman indiscriminately uses Sleep spells to try to put others to sleep. No matter how much Sleep it uses, a sandman does not consume any mental points. A sandman can instantly appear wherever there's a working mind, and during combat, it can perform actions while teleporting.

To wound a sandman, you need magic or a silver weapon.

#### [ Sylph ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=10    Movement Speed=18 (air)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=Wind cutter (Strike power 10, bonus damage 6, Magic Intensity／Magic Power=13／6); 4th level spirit magic (Magic Intensity／Magic Power=13／6, sylph only); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness
- Habitat=Anywhere
- Languages=Silent spirit
- Perception=Magic

Sylph is a spirit of wind. It appears as a naked elf woman. Its pale upper body is translucent, but from the waist down it is completely invisible and nothing can be seen. Sylph does not have normal methods of attack, but by entangling itself with its target, it can cause a powerful wind cutter attack. This attack cannot be evaded. Wind cutter is treated as strike power 10 damage magic. Its magic intensity is 13 (magic power 6). Sylphs also use spirit magic that is sourced from the power of the wind. Their shaman skill level is 4. However, spirit points are not consumed even if they use wind cutter attacks or spirit magic. To harm a sylph, you need a magical or silver weapon.

#### [ Sprite ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=18    Movement Speed=16
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Violent
- Attack Points=Fangs：11 (4)    Strike Points=7
- Evasion Points=14 (7)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=Transparent; Make others transparent (resist target score=13); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness
- Habitat=Anywhere
- Languages=Silent spirit
- Perception=Magic

Sprites are said to be the spirits that control the emotion of shame (the function of the mind). A mad sprite remains invisible and attacks nearby creatures with its fangs. Because it's invisible, its appearance cannot be identified, but it is said to resemble a leprechaun, etc. When attacking a mad sprite, a -4 modifier will be imposed. Also, you cannot cast magic on mad sprites.

Mad sprites have the ability to make others invisible. When a mad sprite performs this attack, the target must make a mental power resistance roll (target score 13). If you fail, you will become invisible. Those who have become invisible cannot see themselves either. For this reason, a -2 modifier will be imposed on all physical action checks. This invisibility cannot be removed unless you use Dispel Magic, etc. or defeat the mad sprite.

To harm a sprite, it must be a silver or magic weapon.

#### [ Gnome ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=10
- Movement Speed=6 (ground)／10 (underground)
- Number=One to several    Frequency=Rare
- Intellect=Low    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=Stone (Strike power 20, bonus damage 5, Magic Intensity／Magic Power=12／5); 4th level spirit magic (Magic Intensity／Magic Power=12／5, gnome only); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness
- Habitat=Anywhere
- Languages=Silent spirit
- Perception=Magic

Gnome is the spirit of earth. Its appearance resembles that of a dwarf, but its skin is gray and at first glance looks like a rock. They can move 10 meters per round underground. Then, they suddenly appear above ground and attack by throwing stones at you. A gnome can disappear into the ground, move underground, and reappear above ground all in one round. However, the gnome cannot take any other actions during the round in which this action was chosen. A gnome's stones will always hit their target. Treat it as strike power 20 damage magic (magic intensity／magic power=12／5). They also use spirit magic that is sourced from the power of the earth. Its shaman skill level is 4. They do not consume mental points even when they throw stones or use spirit magic.

To harm a gnome, you need a magical or a silver weapon.

#### [ Frau ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=10    Movement Speed=18 (air)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=Cold (Strike power 10, bonus damage 6, Magic Intensity／Magic Power=13／6); 4th level spirit magic (Magic Intensity／Magic Power=13／6, frau only); Normal weapon immunity; Mental attack immunity; Cold immunity; Not affected by poison and illness
- Habitat=Cold regions
- Languages=Silent spirit
- Perception=Magic

Frau is a spirit of ice and looks very similar to a sylph. Its whole body is pure white, as if covered in frost, becoming more transparent towards the lower half of the body. Therefore, its legs are not visible at all. Its eyes are also pure white. Frau only appear in areas with snow and ice.

A mad frau attacks by blowing cold air while it flies through the air. Treat this cold air as strike power 10 damage magic (magic intensity／magic power=13／6). Against a frau itself, cold-based magic is completely meaningless. Also, when attacking with a weapon, you will only be able to deal damage if it's a magical or a silver weapon.

#### [ Leprechaun ]

- Monster Level=4
- Rarity=12 (However, a shaman always knows)
- Agility=18    Movement Speed=16／6 (air)
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Violent
- Attack Points=Fangs：11 (4)    Strike Points=7
- Evasion Points=14 (7)    Defense Points=6
- Life Points／Resistance=10／11 (4)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6, leprechaun only); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness; Teleport
- Habitat=Anywhere
- Languages=Silent spirit
- Perception=Magic

Leprechauns are mind spirits who control chaos. Its appearance is that of a completely naked imp, with no features that indicate its gender. In addition to normal movement, they can also perform teleportation. They cannot take any other actions during the round in which this action was chosen The teleportation destination is within the leprechaun's view. Leprechauns are spirits, but in this world they have a complete form, and will attack by biting. Other than that, they also attack (confuse) you with spells such as Confusion and Forget. Their shaman skill level is 4. To harm a leprechaun, you need a magical or silver weapon.

#### [ Dryad ]

- Monster Level=5
- Rarity=12 (However, a shaman always knows)
- Agility=19    Movement Speed=19
- Number=One    Frequency=Very Rare
- Intellect=Human    Reaction=Violent
- Attack Points=Barehanded：12 (5)    Strike Points=6
- Evasion Points=14 (7)    Defense Points=7
- Life Points／Resistance=10／12 (5)
- Mental Points／Resistance=20／14 (7)
- Special Abilities=Charm (Resist target score=14); 5th level spirit magic (Magic Intensity／Magic Power=14／7, dryad only); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness
- Habitat=Woods
- Languages=Silent spirit
- Perception=Magic

Dryads are plant spirits. They usually reside in trees, but a shaman can summon them anywhere there are plants. Their figure is that of a completely naked elf woman, with long green hair wrapped around her entire body. Their skin is also green.

A mad dryad uses the spirit magic "Charm" to cause division among allies, and tries to block their opponent's movements with "Binding". Using these spells does not consume any of the dryad's mental points.

If magic cannot be cast on the target, the dryad will attack barehanded.

To harm a dryad, it must be a magical or silver weapon.

#### [ Mad Spirit of Life ]

- Monster Level=6
- Rarity=12 (However, a shaman always knows)
- Agility=16    Movement Speed=16
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=13 (6)    Defense Points=8
- Life Points／Resistance=15／14 (7)
- Mental Points／Resistance=25／16 (9)
- Special Abilities=Age shift (Resist target score=15); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness
- Habitat=Anywhere
- Languages=Silent spirit
- Perception=Magic

The mad spirit of life appears in the form of a shining white horse. The sages believe this suggests a connection with unicorns. The mad spirit of life does not attack physically. However, its reckless power has a major impact on the lives around it.

Each round, the mad spirit of life attempts to pour excessive life spirit power into a single target. Those affected by it suffer the effects of (physical) age shifting. The target must make a mental power resistance roll (target score 15). If you fail, roll 2D. If the roll is 8 or greater, you will age by roll-7 years. If the roll is 6 or less, you will become younger by 7-roll years. If the roll is exactly 7, no age change will occur. Regarding the results of aging and de-aging, please refer to 18.2: Guidelines for Adventurer Age and Ability Score Changes and use the game master's discretion.

To harm a mad spirit of life, it must be a magical or silver weapon.

#### [ Valkyrie ]

- Monster Level=6
- Rarity=12 (However, a shaman always knows)
- Agility=14
- Movement Speed=14／30 (air)
- Number=One
- Frequency=Very Rare
- Intellect=Human
- Reaction=Adversarial
- Attack Points=ー
- Strike Points=ー
- Evasion Points=14 (7)
- Defense Points=8
- Life Points／Resistance=15／14 (7)
- Mental Points／Resistance=25／16 (9)
- Special Abilities=6th level spirit magic (Magic Intensity／Magic Power=15／8, valkyrie only); Normal weapon immunity; Mental attack immunity; Not affected by poison and illness
- Habitat=Anywhere
- Languages=Silent spirit
- Perception=Magic

Valkyrie is a mind spirit. It governs the courage of men who fight. Her appearance is that of a human woman clad in shining white armor, and her noble appearance is said to fascinate all men. However, a mad valkyrie is extremely cruel and terrifying. They attack from above, casting the spell Valkyrie Javelin where sword attacks can't reach. They will also cast a Fanaticism spell to provoke you. Casting these spells does not consume spirit points. To harm a valkyrie, you need magical or silver weapons.

### 13.2.5 Titans

#### [ Yeti ]

- Monster Level=5
- Rarity=14    Agility=10
- Movement Speed=15
- Number=One to several
- Frequency=Very Rare
- Intellect=Low    Reaction=Hunger-based
- Attack Points=Claw：13 (6)／Claw：13 (6)
- Strike Points=13／13
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=21／14 (7)
- Mental Points／Resistance=14／13 (6)
- Special Abilities=Strong to cold; Snow adaptation; Weak to fire
- Habitat=Cold regions, high mountains (snow never melts)
- Languages=Giant
- Perception=Five senses

The yeti is a titan, about two and a half meters tall, that is rarely seen in cold, snowy regions, and its body is covered in thick white fur. Its ecology is not very clear. They are not very ferocious and do not actively attack humans, but they do seem to attack when they're hungry-- in cold areas with deep snow, it's not uncommon for them to be hungry and unable to find prey.

Characters cannot move freely in deep snow areas such as those where the yeti lives. When fighting in these locations, your attack and evasion will suffer a -2 penalty, and your movement speed will be halved. However, the yeti itself is adapted to snow and does not suffer this penalty.

The yeti is strong against cold, and cold-based attacks must be made with a -10 reduction to strike power during the check. Conversely, it is weak against fire, so if it's a fire-based attack, the check can be made with +10 to strike power.

#### [ Ogre ]

- Monster Level=5
- Rarity=10
- Agility=10    Movement Speed=15
- Number=One to several    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Weapon or arm：13 (6)
- Strike Points=12
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=21／14 (7)
- Mental Points／Resistance=10／12 (5)
- Special Abilities=None in particular
- Habitat=Forests and hills near human villages
- Languages=Giant
- Perception=Five senses (darkvision)

Ogres, also known as jikininki, are ferocious, carnivorous titans who, as their name suggests, particularly enjoy human flesh. Their body color is reddish-brown, and their face is reminiscent of primitive humans (of our world). They have sharp canine teeth that allow them to tear and eat raw meat. Although they are on the smaller side of the titans, their height is well over 2 meters, and they have strong bodies to match. Of course, their strength is also considerable. They mainly fight with huge clubs made from thick tree branches, but even without using such a thing, their thick arms alone are enough to pose a threat. Numerically, there is no difference in the strength of an ogre even if it does not have a weapon.

They usually live alone, or sometimes in groups of several, in forests and hills near human villages, and attack their favorite food: humans. If targeted by them, a small village, etc. would surely be no match for them. In some cases, all the residents of one village have to abandon their homes and land and migrate.

#### [ Spriggan ]

- Monster Level=5
- Rarity=12
- Agility=18    Movement Speed=20
- Number=One    Frequency=Very Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points (Titan)=Fangs：12 (5)／Claw：13 (6)／Claw：13 (6)
- Strike Points=14／13／13
- Attack Points (Child)=Fist：12 (5)
- Strike Points=7
- Evasion Points=13 (6)    Defense Points=8
- Life Points／Resistance=22／14 (7)
- Mental Points／Resistance=18／14 (7)
- Special Abilities=Shapeshift (Human Child); 2nd level dark magic (Magic Intensity／Magic Power=11／4)
- Habitat=Mountains near human villages, hills, forests, human villages
- Languages=Giant, regional
- Perception=Five senses

Spriggans are evil titans who enjoy eating raw meat. They usually live in mountains, hills, forests, etc. but sometimes they come to human villages in search of their favorite food, human flesh. When entering a human village, spriggan transforms into a human child between the ages of 4 and 10. The transformation is so ingenious that there's nothing that hints at the spriggan's true identity, nor can it be detected by Sense Magic or Sense Aura. The form that a Spriggan can take after transforming is fixed for each individual (its apparent age cannot be changed either). Therefore, a spriggan cannot take the form of a specific child. Once their true identity is discovered, they won't be able to fool the same opponent again.

If given the chance (such as when they're alone with a human who believes they're a normal child), a spriggan will revert to their true form (an ugly, 3-meter-tall titan with fangs bared and claws out) to attack their target. The transformation is instantaneous. If the target is unaware of the spriggan's true identity, this is a surprise attack. The target may not take any actions for one round and will suffer a -4 penalty to evasion. Spriggans quickly devour the flesh of those they kill. If they are not hungry, they will not attack people unless they have a specific reason to do so (such as because they suspect their true identity, etc.).

A spriggan can use its considerable strength even in its child form. However, if they attempt to attack others while still in their child form, their attack ability will be significantly reduced. Please use the (child) section of the data.

Spriggans are apostles of the dark gods and can use up to 2nd level dark magic.

#### [ Troll ]

- Monster Level=6
- Rarity=11
- Agility=12    Movement Speed=24
- Number=One to several    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Arm：14 (7)    Strike Points=13
- Evasion Points=13 (6)    Defense Points=11
- Life Points／Resistance=21／15 (8)
- Mental Points／Resistance=14／14 (7)
- Special Abilities=Camouflage (Sense target score=13)
- Habitat=Caves, hills
- Languages=Giant
- Perception=Five senses (darkvision)

Trolls are titans with rock-like skin. They have very low intellect and rarely use tools. They live in caves and hills, and do not appear in forests or meadows. Due to this and their rugged, rock-like appearance, some sages believe that they may have some kind of connection with earth spirits, but it's not clear whether this is true. In any case, it's certain that they're terrifying monsters with enormous strength.

Although they're about 3 meters long, they walk with their backs bent, probably because they live in caves. They also have arms so long that their fingertips just barely touch the ground. Their body color is the same as a rock surface, and if you are careless, you may mistake one for a huge rock. To notice their presence, you must succeed on a success roll against target score 13 using ranger skill level + intelligence bonus as the baseline score. If you fail, the troll can make a surprise attack. A character caught by surprise cannot take any actions for one round, and suffers a -4 penalty to evasion for that round.

A troll's skin is not only similar in color, but also has a hardness comparable to that of rock. It will not be affected by just any half-hearted attack, etc. They have the physical strength to match their body size, and when they attack, they strike with their rock-like arms. That single blow has terrifying destructive power that can kill a person in an instant.

#### [ Hecatoncheir ]

- Monster Level=7
- Rarity=15
- Agility=7    Movement Speed=15
- Number=One    Frequency=Very Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Weapon or arms (6 times)：15 (8)
- Strike Points=15 x 6
- Evasion Points=13 (6)    Defense Points=11
- Life Points／Resistance=28／17 (10)
- Mental Points／Resistance=14／15 (8)
- Special Abilities=4th level holy magic (Magic Intensity／Magic Power=13／6) rarely
- Habitat=Underground ruins
- Languages=Giant
- Perception=Five senses (darkvision)

Hecatoncheir are a subspecies of titan, reaching nearly 4 meters tall. Although they're called the hundred-handed titan, they actually have only 12 arms. Six of these are used in combat. They can aim at different targets in one round, or focus on hitting one target. Some of them carry weapons, but even without such things, their thick arms are enough to pose a threat to humans (and fae).

Hecatoncheir protect the treasure and secrets of the ancient kingdom in deep underground labyrinths, and rarely appear above ground. Their intellect is on par with humans, and they're not necessarily evil. There are also hecatoncheir who serve the gods. They possess the 4th level priest skill.

#### [ Giant ]

Among the titans, the race called Giants in particular, unlike those that are merely large fae and youma (such as trolls, etc.), are one of the ancient races like dragons and gods, who are claimed to have originated from the primordial titans. Their appearance is similar to that of a human, but their physique is twice that of a human, at least 5 meters tall, and some over 10 meters. Giants are divided into several subspecies depending on where they live. There are differences in skin color and hair color, and each has a different personality. Some of them live alone, but they also live in groups of a few to about ten, and female giants and baby giants can sometimes be seen.

#### [ Hill Giant ]

- Monster Level=8
- Rarity=12
- Agility=8    Movement Speed=16
- Number=One to several
- Frequency=Very Rare
- Intellect=Low    Reaction=Neutral
- Attack Points=Arm：16 (9)    Strike Points=17
- Evasion Points=13 (6)    Defense Points=12
- Life Points／Resistance=35／19 (12)
- Mental Points／Resistance=16／16 (9)
- Special Abilities=None in particular
- Habitat=Hills, mountains
- Languages=Giant
- Perception=Five senses

These giants, about 5 meters tall, live in hills and mountains, and have golden or light brown hair on their heads and bodies. They have a gentle personality, so even if you meet them, they will not attack you unless there's some reason to do so.

#### [ Forest Giant ]

- Monster Level=10
- Rarity=12
- Agility=10    Movement Speed=20
- Number=One to several
- Frequency=Very Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Arm：18 (11)    Strike Points=19
- Evasion Points=15 (8)    Defense Points=14
- Life Points／Resistance=40／22 (15)
- Mental Points／Resistance=14／18 (11)
- Special Abilities=None in particular
- Habitat=Forest
- Languages=Giant
- Perception=Five senses

This giant makes the forest its home, and has darker hair on its head and body than a hill giant. It's about 5 meters tall. They have a very ferocious personality and will attack any animal that comes into view, in an attempt to eat them. Of course, humans are no exception.

#### [ Fire Giant ]

- Monster Level=11
- Rarity=12
- Agility=9    Movement Speed=20
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Arm：19 (12)    Strike Points=21
- Evasion Points=16 (9)    Defense Points=15
- Life Points／Resistance=45／24 (17)
- Mental Points／Resistance=15／19 (12)
- Special Abilities=7th level spirit magic (Magic Intensity／Magic Power=16／9, fire spirits only); Fire immunity
- Habitat=Mountains near human villages, hills
- Languages=Giant, silent spirit
- Perception=Five senses (infravision)

A fire giant is a titan about 7 meters tall, with reddish-brown skin. They have rich heads of hair, the color of which ranges from jet black to deep crimson, depending on the individual. They also have body hair of the same color as the hair on their heads, but it's not all over their bodies.

Fire giants are ferocious creatures that will attack anything that enters their territory without mercy. Since they often live near human villages, they are greatly feared by humans.

Fire giants have a deep connection with the spirit power of fire, and can use spirit magic sourced from the power of fire spirits (salamander, etc.) up to 7th level. Also, they will not suffer any damage at all from fire.

#### [ Frost Giant ]

- Monster Level=13
- Rarity=13
- Agility=8    Movement Speed=19
- Number=One to several
- Frequency=Very Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Arm：21 (14)    Strike Points=23
- Evasion Points=18 (11)    Defense Points=17
- Life Points／Resistance=50／27 (20)
- Mental Points／Resistance=16／21 (14)
- Special Abilities=8th level spirit magic (Magic Intensity／Magic Power=17／10, ice spirits only); Cold immunity; Snow adaptation
- Habitat=Cold regions
- Languages=Giant, silent spirit
- Perception=Five senses (infravision)

Frost giants are titans that live in cold regions and are covered in white hair all over their bodies. They are among the largest of the titans, reaching over 10 meters tall. Yet, they have relatively gentle personalities and will not attack humans unless they do something particularly unjust. However, they live a closed life and do not like when their territory is invaded. If you're open to communication, they'll simply give you a warning and ask you to leave their territory. If you can't communicate, they may threaten you.

Frost giants have a deep connection with the spirit power of ice, and can use spirit magic sourced from the power of ice spirits (frau, fenrir) up to 8th level. Also, they will not suffer any damage at all from cold-type attacks.

#### [ Cyclops ]

- Monster Level=15
- Rarity=10
- Agility=6    Movement Speed=18
- Number=One to several
- Frequency=Very Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Arm：23 (16)    Strike Points=26
- Evasion Points=20 (13)    Defense Points=19
- Life Points／Resistance=60／31 (24)
- Mental Points／Resistance=20／24 (17)
- Special Abilities=None in particular
- Habitat=Secluded seasides
- Languages=Giant
- Perception=Five senses

Cyclops are the largest of all titans, reaching over 10 meters in height. They have only one eye and no hair on their heads. The top of their heads are hard and pointed like a horn. They're almost naked, but they do wear a loincloth. They have brownish skin and brown bristles on their chest and limbs. They live on secluded seashores. Sometimes they live alone, but sometimes they live in groups of several. They never leave their homes, and there are usually no humans living nearby. They will attack anyone who invades their territory without mercy.

### 13.2.6 Mythical Beasts and Magical Beasts

#### [ Satyr ]

- Monster Level=3
- Rarity=14    Agility=15
- Movement Speed=15
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Horns：9 (2)    Strike Points=9
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=12／11 (4)
- Mental Points／Resistance=18／12 (5)
- Special Abilities=Manipulate emotions with a flute (Resist target score=10)
- Habitat=Forests
- Languages=Regional
- Perception=Five senses

Satyrs are a forest-dwelling race with the upper body of a hairy human, pointed ears, short horns sprouting from their heads, and the lower body of a goat. Their staple food is nuts and berries, they have gentle personalities, they're fond of alcohol, music, and women, and they love festivities. They don't like fighting and will run away if danger approaches. Female satyrs are called she-satyrs.

They always carry a flute and can manipulate human emotions with their melodies. Humans who hear the satyr's flute may suddenly become frightened and run away, get excited and start dancing, or become lewd and start taking off their clothes. To resist this, you must succeed on a mental power resistance roll against target score 10.

#### [ Ceiling Hanger ]

- Monster Level=3
- Rarity=14
- Agility=12    Movement Speed=6
- Frequency=Rare    Number=One
- Intellect=Low    Reaction=Adversarial
- Attack Points=Right arm：11 (4)／Left arm：10 (3)
- Strike Points=Special／5    Evasion Points=10 (3)
- Defense Points=5
- Life Points／Resistance=14 (11／4)
- Mental Points／Resistance=11 (10／3)
- Special Abilities=Surprise attack (Sense target score=12); Strangle; Sleepless
- Habitat=Underground labyrinths
- Languages=None
- Perception=Five senses

A ceiling hanger is a magical beast with arms of different sizes on its left and right sides. Its lower body is made of a glue-like substance that expands and contracts, and it's usually about 1 meter long. By sticking with this lower body, a ceiling hanger can also move along walls and ceilings. When attacking prey, this lower body stretches, reaching a length of 6 meters. Its body color is gray, but like a chameleon, it has the ability to assimilate into the color of its surroundings.

Ceiling hangers primarily attack sleeping prey, but when hungry they may attack active prey as well. In addition to its protective color, it also stretches its body out from the ceiling in an instant to attack, so it has a high potential for surprise attacks. Rangers have a chance to notice this surprise attack with their sense danger ability. To do so, you must succeed on a success toll against target score 12 using ranger skill level + intelligence bonus as the baseline score. Failure will result in a surprise attack and the targeted character will suffer a -4 penalty to evasion.

A ceiling hanger's right hand has an extremely enlarged thumb, while conversely, the other four fingers are integrated into a scissor shape, allowing it to strangle its prey. When a ceiling hanger catches its prey, it will pull them up to the ceiling on the next round and attempt to choke the opponent to death. At the same time, the left arm makes a normal attack (strike) on the prey. A hanging character cannot breathe, nor even cast spells. Also, evading the left arm's attack incurs a -2 penalty.

Strangling has strike power 0 and bonus damage 6 when making a damage check. Non-metal armor and ring mail have no effect against this damage, and points can only be reduced by adventurer level. Characters wearing metal armor (other than ring mail) will not suffer any damage. Regardless of damage or armor, once character's life force rounds have elapsed, the character will suffocate and fall unconscious (life force 0). From then on, in each round, a death check must be made when applying damage (even if it's 0).

Ceiling hangers with prey suspended from the ceiling cannot be reached by melee weapons, so it'll be extremely difficult to provide support to a suspended character.

#### [ Harpy ]

Harpies are carnivorous creatures with the head and chest of a human female, and the rest of its body is that of a bird. Harpies have two races, deela and furia.

#### [ Deela ]

- Monster Level=3
- Rarity=13
- Agility=16    Movement Speed=6／30 (air)
- Number=Several    Frequency=Moderate
- Intellect=Human    Reaction=Neutral
- Attack Points=Talons：11 (4)    Strike Points=6
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=9／10 (3)
- Mental Points／Resistance=12／11 (4)
- Special Abilities=Charm by singing (Resist target score=10)
- Habitat=Coasts
- Languages=Harpy, regional
- Perception=Five senses

Deelas live on the coast, are beautiful, and can speak. They are neutral toward humans. Deelas mate with human males and lay eggs. At this time, deelas use the ability to charm by singing. Anyone who hears a deela's song must make a mental power resistance roll against target score 10. If you fail, you will be charmed and must do what the deela tells you to do.

#### [ Deela King ]

- Monster Level=3
- Rarity=18
- Agility=16    Movement Speed=6／30 (air)
- Number=One    Frequency=Very Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Talons：11 (4)    Strike Points=9
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=15／11 (4)
- Mental Points／Resistance=12／11 (4)
- Special Abilities=None in particular
- Habitat=Coasts
- Languages=Harpy, regional
- Perception=Five senses

Usually, only female individuals are born among harpies. However, very rarely a male is born. A flock blessed with a male can produce offspring without the use of a human male, so that male is made their king. In such groups, they do not try to charm humans and avoid interaction as much as possible, because they do not need to use humans and do not want their king's existence to be known.

Male harpies, which are rare, are slightly larger than the usual females. They also do not have the ability to charm by singing.

#### [ Furia ]

- Monster Level=3
- Rarity=13
- Agility=16    Movement Speed=6／30 (air)
- Number=Several    Frequency=Moderate
- Intellect=Low    Reaction=Adversarial
- Attack Points=Talons：11 (4)    Strike Points=7
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=10／10 (3)
- Mental Points／Resistance=8／10 (3)
- Special Abilities=None in particular
- Habitat=Mountains
- Languages=Harpy
- Perception=Five senses

Furia live in mountainous areas, are ugly, have low intellect, and are always aggressive. Furia mate with male eagles and may be encountered along with them. They have no special abilities.

#### [ Hippocampus ]

- Monster Level=3
- Rarity=12
- Agility=14    Movement Speed=8／20 (water)
- Number=One to dozens
- Frequency=Rare    Intellect=Animal
- Reaction=Neutral
- Attack Points=Leg：11 (4)    Strike Points=9
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=20／12 (5)
- Mental Points／Resistance=10／10 (3)
- Special Abilities=Water adaptation
- Habitat=Seas
- Languages=None
- Perception=Five senses (illumination)

It's a horse that lives in the sea, the lower half of its body is that of a fish. Its front legs have fins instead of hooves, and it has no hind legs. They can move around quickly underwater, but once on land they suffer a -4 penalty to attack and evasion.

Mermen have tamed the hippocampus and use them as riding horses.

#### [ Medusa ]

- Monster Level=3
- Rarity=12
- Agility=14    Movement Speed=14
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Snakes (all engaged)：10 (3)
- Strike Points=7+poison
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=14／11 (4)
- Mental Points／Resistance=18／12 (5)
- Special Abilities=Petrify (Resist target score=10); Poison (Toxicity score 10, strike power 10, bonus damage 3); Not affected by poison and illness; Sleepless
- Habitat=Ruins, underground labyrinths
- Languages=Regional
- Perception=Five senses (darkvision)

Medusa is a magical beast that takes the form of a human woman, with dozens of snakes growing out of her head instead of hair, and a face with the magical power to petrify humans. They dwell mainly in ruins and underground labyrinths, and find wicked pleasure in turning visitors into stone statues. Anyone who encounters a medusa must succeed on a mental power resistance roll against target score 10 or they will instantly be turned into a stone statue. You can avoid being petrified by fighting with your eyes closed or your face turned away, but in such a state you will suffer a -4 penalty to your attack power and evasion speed. Also, you cannot cast magic on the medusa in these states. Mirrors do not reflect a medusa's magic. Therefore, you can fight while looking at a medusa's reflection in a mirror. In this case, the penalty to attack power and evasion speed is only -2. Conversely, holding a mirror up to a medusa is completely ineffective.

A medusa uses the snakes on her head to attack. A medusa has countless snakes (hair), and anyone who engages with a medusa in melee is exposed to these snakes' attacks. The snakes are poisonous, and anyone dealt damage by the snakes' attacks must immediately make a life force resistance roll against target score 10. If you fail, you immediately suffer damage resulting from a strike power 10 strike roll plus bonus damage 3. This damage can be reduced by adventurer level. If the resistance roll is successful, no poison damage is sustained.

Even if a medusa is killed, the magical power remains in her head for a while. It is possible to put the severed head of a Medusa in a bag, then show it to an enemy in combat to turn them to stone, but it must be used carefully, as there is a risk of it turning your allies to stone as well. The magical power in the head will disappear in about one week.

#### [ Androscorpio ]

- Monster Level=4
- Rarity=14
- Agility=17    Movement Speed=17
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon：11 (4)／Tail：11 (4)
- Strike Points=10／12+poison
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=17／12 (5)
- Mental Points／Resistance=18／13 (6)
- Special Abilities=3rd level spirit magic (Magic Intensity／Magic Power=12／5); Poison (Toxicity score 11, illusion, lasts 1 hour)
- Habitat=Deserts
- Languages=Regional, silent spirit
- Perception=Five senses (infravision)

Androscorpio is a mythical beast that lives in the desert, with the upper body of a handsome young man and the lower body of a brightly colored scorpion. Like humans, there are good androscorpios, and there are evil androscorpios. They can use spirit magic, and their shaman skill level is 3.

In combat, an androscorpio uses a sword in his hand, but he can also attack with his tail at the same time. The stinger at the tip of his tail contains a hallucinogenic poison (toxicity score 11). Those wounded by a tail attack and fail a life force resistance roll will experience hallucinations starting on the next round. The enemy's appearance can change, or it can appear as multiple. This symptom lasts for one hour, during which time the victim suffers a -4 penalty on all success rolls.

#### [ Centaur ]

- Monster Level=4
- Rarity=9
- Agility=14    Movement Speed=30
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Human    Reaction=Neutral
- Attack Points=Spear：10 (3)／Heel：10 (3)
- Strike Points=12／12
- Attack Points=Bow：11 (4)
- Strike Points=12
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=19／13 (6)
- Mental Points／Resistance=13／12 (5)
- Special Abilities=4th level ancient magic (Magic Intensity／Magic Power=13／6) rarely
- Habitat=Meadows
- Languages=Centaurian
- Perception=Five senses

Centaurs are a meadow-dwelling race that are human from the waist up and horse from the waist down. They do not have permanent homes, but live as hunters while traveling in groups, and their language and lifestyle are similar to those of humans, though their culture is somewhat less advanced.

They do not have a permanent place of residence and live a hunting lifestyle while traveling in groups, and although their level of culture is somewhat low, their language and lifestyle are similar to those of humans. They are not interested in money, but aside from that, if you bring them a suitable gift, you may be able to form a friendship.

They use bows and arrows or spears as weapons. In melee combat, a centaur can attack a single target with the weapon in its hand and its heel at the same time.

It is said that there are very rare centaurs who have very advanced knowledge and can use magic.

#### [ Cockatrice ]

- Monster Level=4
- Rarity=15
- Agility=11    Movement Speed=10
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Neutral
- Attack Points=Beak：11 (4)
- Strike Points=9+petrify
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=16／12 (5)
- Mental Points／Resistance=8／11 (4)
- Special Abilities=Petrify (Resist target score=11); Not affected by poison and illness; Sleepless
- Habitat=Wilderness
- Languages=None
- Perception=Five senses

A cockatrice is a flightless bird about the size of a human with the legs and tail of a lizard. Its beak has the ability to petrify living creatures, and anyone hit by a cockatrice (regardless of whether they're dealt damage or not) must make a life force resistance roll against target score 11. If you fail, you will instantly turn to stone.

Cockatrices mainly live in the wilderness and feed on an herb called henruda. It's the only plant that does not turn to stone when touched by a cockatrice's beak. If you find and eat henruda in advance, you can neutralize the cockatrice's magical power and prevent being petrified. This herb is also effective against medusa and basilisk, but its drawback is that it cannot be stored and its effect only lasts for one day.

#### [ Scylla ]

- Monster Level=4
- Rarity=13
- Agility=12
- Movement Speed=12／12 (water)
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Fangs (6 times)：11 (4)
- Strike Points=12
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=18／13 (6)
- Mental Points／Resistance=15／12 (5)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6); Not affected by poison and illness; Sleepless
- Habitat=Water
- Languages=Regional, silent spirit
- Perception=Five senses (infravision)

Scylla is a beautiful woman from the waist up, but six serpent heads and 12 octopus tentacles grow from her lower body. They are amphibious and can move freely on land, but mainly prefer to live in water. Their personality is extremely wicked, often luring men with only their upper bodies above the water, then dragging them underwater to kill them.

When in combat, a scylla can attack different targets at the same time with its six heads. However, she can only attack a single target three times in one round. Scylla can also use spirit magic. Her shaman skill level is 4 and her magic intensity is 13 (magic power 6).

#### [ Chimera ]

- Monster Level=5
- Rarity=13
- Agility=12    Movement Speed=12
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Fangs：12 (5)／Snake's fangs：12 (5)
- Strike Points=15／13+poison
- Evasion Points=12 (5)    Defense Points=9
- Life Points／Resistance=24／15 (8)
- Mental Points／Resistance=18／14 (7)
- Special Abilities=5th level dark magic (Magic Intensity／Magic Power=14／7); Poison (Toxicity score 12, speech impediment, lasts 1 day); Not affected by poison and illness; Sleepless
- Habitat=Mountain recesses
- Languages=None
- Perception=Five senses (darkvision)

A chimera has a black lion for the front half of its body and a demonic black goat for the rear half. Its tail is a snake and a goat's head grows out of its back. Known to be extremely ferocious, they are impossible to defeat except by the very bravest. Fortunately, they live deep in the mountains, their fertility is weak due to their unnatural composition, and their numbers are small, so they're rarely encountered.

In combat, a Chimera can attack two targets at the same time, using its lion fangs and the snake fangs at the tip of its tail. It cannot attack the same target twice in one turn. The snake's fangs contain a neurotoxin that paralyzes the speech center, rendering those affected unable to speak or cast spells for one day. The black goat head on its back can also cast dark magic up to 5th level.

#### [ Twintail Cat ]

- Monster Level=5
- Rarity=13    Agility=18
- Movement Speed=15
- Number=One
- Frequency=Rare (Kaios Island)／Very Rare (Other)
- Intellect=High    Reaction=Neutral
- Attack Points=Fangs：12 (5)／Claw：13(6)／Claw：13 (6)
- Strike Points=8／7／7
- Evasion Points=15 (8)    Defense Points=8
- Life Points／Resistance=12／13 (6)
- Mental Points／Resistance=20／14 (7)
- Special Abilities=5th level ancient magic (Magic Intensity／Magic Power=15／8); 5th level spirit magic (Magic Intensity／Magic Power=15／8); Mental attack immunity; Not affected by poison and illness
- Habitat=Meadows, provided it's Kaios Island (Islands of Azarn) mostly
- Languages=Regional, fairy, low ancient, silent spirit
- Perception=Five senses (illumination, infravision)

Twintailed cats look like normal black cats, except for the fact that they have two tails. However, it is a true mythical beast that has an intellect greater than humans and can also use magic. They will occasionally meddle with humans on a whim, but rarely engage beyond light teasing. They believe that straightforward thinking is extremely dangerous. Therefore, when they communicate something, they say it in a mysterious way, as if they are trying to bewilder the person they're talking to. Although extremely rare, friendships may form between humans and twintail cats. If this happens, they will never betray their friends.

They can use ancient magic and spirit magic, but they are especially fond of illusions and magic that affects the mind. Twintail Cats may have rare magical items related to these kinds of magic.

Twintail cats are the rulers and protectors of the cats of Kaios Island (the Islands of Azarn). All cats follow their commands. However, they rarely give commands, as they value the spirit of self-reliance that is characteristic of the cat family. When a situation beyond their control arises, they skillfully guide and encourage other races to act voluntarily in accordance with their goals. Also, magical beasts do not follow their orders.

#### [ Telchines ]

- Monster Level=5
- Rarity=14
- Agility=12
- Movement Speed=10／10 (water)
- Number=One    Frequency=Very Rare
- Intellect=High    Reaction=Neutral
- Attack Points=Weapon：11 (4)／Tail：12 (5)
- Strike Points=12／11
- Evasion Points=12 (5)    Defense Points=8
- Life Points／Resistance=16／13 (6)
- Mental Points／Resistance=20／14 (7)
- Special Abilities=5th level ancient magic (Magic Intensity／Magic Power=15／8); Water adaptation
- Habitat=Secluded coasts
- Languages=Merman, low ancient
- Perception=Five senses (illumination)

Telchines has the upper body of a human male, but his lower body has two large snake tails instead of legs. They live quietly on the coast, far from human villages, and their ecology is shrouded in mystery. Just like humans, there are good telchines and there are evil telchines. All of them have deep knowledge of ancient magic and poisons, and can also cast ancient magic.

When in danger, telchines will use a Shape Change spell to take on the form of a giant or an ugly beast to intimidate their opponents. When fighting in its true form, it uses a trident in its hand along with its two tails.

#### [ Hippogriff ]

- Monster Level=5
- Rarity=13
- Agility=15
- Movement Speed=10／40 (air)
- Number=One    Frequency=Rare
- Intellect=Low    Reaction=Neutral
- Attack Points=Talon：13 (6)／Talon：13 (6)／Beak：12 (5)
- Strike Points=13／13／12
- Evasion Points=12 (5)    Defense Points=8
- Life Points／Resistance=22／14 (7)
- Mental Points／Resistance=10／12 (5)
- Special Abilities=None in particular
- Habitat=Meadows
- Languages=None
- Perception=Five senses

The hippogriff is said to have been born after a griffon attacked a mare. A flying mythical beast, the front half of its body is an eagle and the back half is a horse. They live in grasslands and feed on small herbivores. Despite their appearance, they're not very ferocious and will not attack humans unless they are very hungry. If you catch one as a child and tame it, you can even use it as a riding horse.

#### [ Pegasus ]

- Monster Level=5
- Rarity=10
- Agility=12
- Movement Speed=30／40 (air)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Heel：11 (4)    Strike Points=13
- Evasion Points=12 (5)    Defense Points=8
- Life Points／Resistance=20／14 (7)
- Mental Points／Resistance=15／13 (6)
- Special Abilities=Not affected by poison and illness
- Habitat=Steep mountains, meadows
- Languages=None
- Perception=Five senses

Pegasus is a winged white horse that can fly. In the wild, Pegasus live on steep mountains and come down to the meadows at the foot of the mountains to feed on grass. Although it's difficult to capture a pegasus alive, it's even more difficult to tame. This is because pegasus are proud animals, even more so than humans, and would rather die than be enslaved. However, if a human is recognized as a true hero, a pegasus will willingly let them ride on its back.

#### [ Head Displacer ]

- Monster Level=5
- Rarity=15
- Agility=18    Movement Speed=18 (air)
- Frequency=Very Rare    Number=One
- Intellect=Human    Reaction=Adversarial
- Attack Points=Tentacles (strangle) x 4：12 (5)／Fangs：12 (5)
- Strike Points=8 x 4／10
- Evasion Points=15 (8)    Defense Points=7
- Life Points／Resistance=18 (14／7)
- Mental Points／Resistance=15 (13／6)
- Special Abilities=5th level dark magic (Magic Intensity／Magic Power=14／7) rarely; Strangling; Not affected by poison and illness; Sleepless
- Habitat=Underground labyrinths, ruins
- Languages=Low ancient
- Perception=Five senses (darkvision)

Head displacers have the ability to devour large numbers of humans without being noticed. It is said among the sages that they may have been created primarily for attacking castles during war.

The head displacer looks like a severed human head with four vermillion tentacles growing out of its neck. When it remains alone, it moves by floating in the air. When it finds prey (humans), it'll first attack with its tentacles. The tentacles are usually about 15 cm long, but can extend up to 4 meters. If a tentacle attack hits, resolve it as strangling. If all 4 tentacles entangle its opponent, it'll also attack with its fangs. If the opponent becomes disabled, it'll devour their head and place itself in the head's position. It'll then embed its tentacles inside its prey's body and begin to act as if it were a living person. Then it'll aim to catch new prey by surprise and attack it. A head displacer itself has the ability to speak low ancient, but cannot use any of its host's (?) skills. Its movements are awkward, and naturally, after several days since its prey was slain, the body will begin to decompose and a putrid odor will linger in the air.

If a character is in danger of a surprise attack by a head displacer, a character with the ranger skill may be able to notice it due to their sense danger ability. Make a success roll against target score 15 using ranger skill level + intelligence bonus as the baseline score, and if you succeed, you'll be able to sense it, but if you fail, you'll be hit by the surprise attack. If the tentacles are not clear, those with the sage skill cannot use the monster check ability.

If the head displacer's tentacles have entangled your character, refer to the rules for grappling to attack them.

A head displacer may use dark magic on very rare occasions. Its magic intensity is 14 (magic power 7).

#### [ Lamia ]

- Monster Level=5
- Rarity=15
- Agility=9    Movement Speed=12
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Strangle：13 (6)    Strike Points=11
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=20／14 (7)
- Mental Points／Resistance=16／13 (6)
- Special Abilities=4th level ancient magic (Magic Intensity／Magic Power=13／6); Needs bloodsucking to maintain life points
- Habitat=Human villages
- Languages=Regional, low ancient
- Perception=Five senses

A lamia is a large snake with the upper body of a beautiful woman and a rainbow-colored lower body, 7 to 8 meters long. Although she is well versed in ancient magic, she doesn't really like to use spells that attack her enemies directly, mainly using illusions and transformations to bewitch them.

Lamia cannot survive without sucking fresh blood from young humans, so they often use a Shape Change spell to disguise themselves as human girls, deceive young people into becoming their lovers, and then secretly suck their blood in the middle of the night. Whenever they suck blood, they must return to their original form. A lamia that does not suck blood at least once per day will lose 1 life point, and if she does not suck blood for 20 days, she will starve to death. Those who have their blood sucked will lose life points, and the lamia will recover that same amount of life points. Usually only 1 point worth of blood is needed per day. With this amount of damage, a healthy young person will only feel mild fatigue and should recover quickly. There are some who have been living with lamia for years without even realizing it.

Lamia are not necessarily wicked, and some of them seem to be kind-hearted. Since they cannot survive without depending on humans, they usually live quietly in villages and towns, and you're unlikely to encounter them outdoors or in labyrinths.

#### [ Lizardman ]

Lizardmen are broadly sorted into two types: noble and slave.

The overwhelming majority are slaves. Slaves have low intellect and cannot use magic. Most lizardman villages consist of only slaves, with populations ranging from about 20 to 50. These communities do not have a very complex social life and are unproductive, simply catching and eating fish from nearby lakes and rivers. The only reason they form groups is for protection from foreign enemies and for ease of reproduction.

Nobles are far superior to slaves in both physique and intellect, and they can also use magic (dragon roar magic). The mixed community of noble lizardmen is rarely seen by humans, so the exact facts are unknown, but it is said to be several times the size of the slave-only community and have a great difference in function.

The magic used by noble lizardmen is said to be dragon roar magic. Although the Witch of Orphan Laverna assumed that the lizardman family was closely related to dragons and avoided premature classification, it was precisely because of this reason that later sages classified them as a type of mythical or magical beast.

#### [ Slave (Lizardman) ]

- Monster Level=8
- Rarity=10
- Agility=18
- Movement Speed=10／10 (water)
- Number=Several to dozens
- Frequency=Rare
- Intellect=Low    Reaction=Neutral
- Attack Points=Weapon:10 (3)    Strike Points=7
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=16／10 (3)
- Mental Points／Resistance=10／9 (2)
- Special Abilities=Water adaptation
- Habitat=Lakes, river coasts
- Languages=Lizardman
- Perception=Five senses (illumination)

#### [ Noble (Lizardman) ]

- Monster Level=5
- Rarity=15
- Agility=14
- Movement Speed=10／10 (water)
- Number=One to several
- Frequency=Very Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Weapon: 13 (6)    Strike Points=10
- Evasion Points=14 (7)    Defense Points=10
- Life Points／Resistance=20／14 (7)
- Mental Points／Resistance=14／13 (6)
- Special Abilities=5th level dragon roar magic (Magic Intensity／Magic Power=14／7); Water adaptation
- Habitat=Swamps
- Languages=Lizardman
- Perception=Five senses (darkvision)

The noble lizardman is a far superior species to the slave lizardman. The data given here is for what's said to be average, but there are great individual differences, and some are said to have dragon roar magic ability of nearly 10th level.

#### [ Griffon ]

- Monster Level=6
- Rarity=12
- Agility=14
- Movement Speed=6／40 (air)
- Number=One to several    Frequency=Rare
- Intellect=Animal    Reaction=Neutral
- Attack Points=Talon：14 (7)／Talon：14 (7)／Beak：13 (6)
- Strike Points=15／15／15
- Evasion Points=13 (6)    Defense Points=10
- Life Points／Resistance=26／16 (9)
- Mental Points／Resistance=14／14 (7)
- Special Abilities=None in particular
- Habitat=Steep mountains
- Languages=None
- Perception=Five senses

The griffon is a magical beast with the body of a lion, the head of an eagle, and the wings of an eagle, and it can fly. They have a strange habit of collecting shiny things, and a large amount of gold, silver, and jewels are stored in a griffon's cave on the cliff. They mainly feed on small animals and do not attack humans unnecessarily, but if an adventurer is ostentatiously wearing jewelry, they may attack in order to steal it.

#### [ Manticore ]

- Monster Level=6
- Rarity=12
- Agility=10    Movement Speed=21
- Number=One    Frequency=Rare
- Intellect=High    Reaction=Hostile
- Attack Points=Fangs：13 (6)／Needle：13 (6)
- Strike Points=15／17+poison
- Evasion Points=12 (5)    Defense Points=10
- Life Points／Resistance=23／15 (8)
- Mental Points／Resistance=18／15 (8)
- Special Abilities=5th level dark magic (Magic Intensity／Magic Power=15／8); Poison (Toxicity score 13, death in 1 hour); Not affected by poison and illness; Sleepless
- Habitat=Deserts, Underground labyrinths
- Languages=Low ancient
- Perception=Five senses (darkvision)

A manticore has the body of a lion, the tail of a scorpion, the wings of a bat, and the face of an old man. They have an extremely long life span and accumulate a great deal of knowledge. While the sphinx is the guardian of true knowledge, the manticore is said to be the guardian of wicked knowledge. Many are followers of Phalaris, and their dark priest skill is 5th level.

In combat, a manticore can attack separate targets at the same time with its lion fangs and scorpion tail (it can also attack the same target twice). The stinger at the tip of its tail is highly poisonous. Those dealt damage by the tail attack must make a life force resistance roll against target score 13. Those who fail will become paralyzed and draw their last breath after one hour.

#### [ Minotaur ]

- Monster Level=6
- Rarity=12
- Agility=10    Movement Speed=15
- Number=One    Frequency=Moderate
- Intellect=Low    Reaction=Adversarial
- Attack Points=Two-handed ax: 13 (6)
- Strike Points=16
- Attack Points=Strangle：15 (8)
- Strike Points=14
- Evasion Points=12 (5)    Defense Points=10
- Life Points／Resistance=25／16 (9)
- Mental Points／Resistance=10／13 (6)
- Special Abilities=Strangling
- Habitat=Caves, underground labyrinths
- Languages=Minotaur
- Perception=Five senses (darkvision)

The minotaur, with a strong human body and the head of a bull, is an extremely brutal creature. They are carnivorous, especially fond of human flesh, and when they are hungry, they will sometimes come out and attack nearby villages. To prevent such calamities, rural villages will often hold rituals in which young girls are sacrificed to the minotaur. If the minotaur is hungry, it'll eat the sacrifice immediately, but if it has other food, it'll keep her alive for a while and use her for other pleasures. With that being said, all minotaurs are male, so they must use human women to produce offspring.

Minotaurs primarily use a giant ax as a weapon, but when fighting barehanded, they will attempt to strangle their opponent to death with both arms. For more information, please refer to strangling under 13.6: Handling Monster Special Abilities.

#### [ Unicorn ]

- Monster Level=6
- Rarity=10
- Agility=15    Movement Speed=30
- Number=One to several
- Frequency=Very Rare
- Intellect=High    Reaction=Neutral to friendly
- Attack Points=Horn：12 (5)／Heel：12 (5)
- Strike Points=17／16
- Evasion Points=13 (6)    Defense Points=9
- Life Points／Resistance=25／16 (9)
- Mental Points／Resistance=20／15 (8)
- Special Abilities=6th level spirit magic (Magic Intensity／Magic Power=16／9); 10th level healing-type spirit magic (Magic Intensity／Magic Power=20／13); Not affected by poison and illness
- Habitat=Deep in the woods, rarely seen outside Unicorn Woods
- Languages=Silent spirit
- Perception=Five senses (infravision)

A unicorn looks like a white horse with a long spiral horn growing from its head.

Unicorns have high intellect and can communicate in silent spirit, but will only trust human (or elf or half-elf) virgin girls. Even in the unfortunate case of a fight, a unicorn will not do anything that would harm a human maiden. However, if anyone other than the maiden tries to touch it, the unicorn will issue a warning, and if you still do not listen, it'll get angry and attack.

Unicorns are said to be deeply connected to the unknown spirit of life. They have an unlimited life span and are never affected by illness or poison.

A unicorn's horn has great healing abilities, allowing them to use magic related to the spirit of life, such as Healing and Restore Health. At this time, their shaman skill is 10th level. Unicorns can also use spirit magic unrelated to the spirit of life, but at this time their shaman skill is only 6th level. If a unicorn runs out of mental points, its horn will wear out and crumble away, leaving not a trace behind.

A unicorn's horn can be cut off, allowing others to use magic related to the spirit of life. For this reason, unicorn horns are sometimes traded as magical items. The user does not have to be a shaman or a woman, and may also wear metal armor. A horn has a reserve of mental points equal to the unicorn's mental points when cut off x 10, and when you use magic, the base mental power cost of each is directly subtracted from this mental point reserve. If magic power is required, calculate it as 10. The reserve mental points cannot be recovered, and once they are used up, the horn will wear out and crumble away.

If a unicorn loses its horn due to overuse of magic or it being cut off, it will never grow back again. They will no longer be able to use magic at all, and will be affected by illness, poison, etc. Eventually they will reach the end of their life span and die.

Currently, unicorns are known to live in large numbers in the Unicorn Woods of Ramliearth, but they are almost extinct outside of that area. Ramliearth has deployed a forest guard regiment and is working as an entire nation to protect these mythical beasts. In addition, the group of druids who protect the forest also have great power, keeping it out of reach of potential poachers.

#### [ Lynx ]

- Monster Level=6
- Rarity=12
- Agility=19    Movement Speed=20
- Number=One    Frequency=Very Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：13 (6)／Claw：14 (7)／Claw：14 (7)
- Strike Points=15／14／14
- Evasion Points=14 (7)    Defense Points=10
- Life Points／Resistance=22／15 (8)
- Mental Points／Resistance=16／14 (7)
- Special Abilities=Clairvoyance (within 100 meters); Not affected by poison and illness
- Habitat=Countryside, woods
- Languages=None
- Perception=Five senses (illumination)

A lynx is a large cat-like creature about 3 meters long that lives in mountains and forests. Its body fur shines yellow to gold in color. Although carnivorous, they mainly feed on small animals and will not attack human-sized creatures unless they are extremely hungry.

Rather, it is humans who hunt the lynx. This is because the lynx has a small amber stone called lignia stone in its body, and this stone is a cure-all for illnesses that affect the mind.

However, the lynx has a sharp clairvoyance ability, and if something approaches within a 100 meter radius, it can quickly spot it, even if it's lurking in the shadows. Therefore, it's very difficult to approach a lynx without being noticed.

#### [ Sphinx ]

- Monster Level=7
- Rarity=12
- Agility=14
- Movement Speed=18／30 (air)
- Number=One    Frequency=Very Rare
- Intellect=High    Reaction=Neutral
- Attack Points=Claw：15 (8)／Claw：15 (8)
- Strike Points=16／16
- Evasion Points=14 (7)    Defense Points=11
- Life Points／Resistance=24／17 (10)
- Mental Points/Resistance=20／16 (9)
- Special Abilities=5th level ancient magic (Magic Intensity／Magic Power=15／8); Tell riddles; Not affected by poison and illness; Sleepless
- Habitat=Ruins, underground labyrinths
- Languages=Regional, low ancient
- Perception=Five senses (darkvision)

The sphinx has the body of a lion with the wings of an eagle and a beautiful human-like face. They have an extremely long lifespan and have accumulated a great deal of knowledge. Although they can cast ancient magic, they will not use magic recklessly or challenge you to a fight unless something really bad happens.

The sphinx is said to be a mythical beast created by the sorcerers of the ancient kingdom to protect true knowledge, and to prevent lost ancient magic spell books and valuable magical items from falling into the hands of fools. If approached in a friendly manner, the sphinx may play a game of riddles to determine the intelligence of their opponent. The sphinx will only reveal its secrets to those it deems to be truly wise and right-minded.

#### [ Wyvern ]

- Monster Level=7
- Rarity=10
- Agility=18
- Movement Speed=8／35 (air)
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Neutral
- Attack Points=Fangs：14 (7)／Talon：15 (8)／Talon：15 (8)／Tail：14 (7)
- Strike Points=17／16／16／16+poison
- Evasion Points=13 (6)    Defense Points=11
- Life Points／Resistance=25／17 (10)
- Special Abilities=Poison (Toxicity score 14, strike power 20, bonus damage 7)
- Habitat=Deserts, forests, mountains, etc.
- Languages=None
- Perception=Five senses (illumination)

Wyverns are said to be one of the subspecies of dragons. They are over 10 meters long and use their large wings to fly, but they have no front legs. Since they don't choose where they live, they are feared throughout Alecrast. Unlike dragons, they have low intellect, so they cannot cast spells, nor can they breathe fire.

Wyverns have highly poisonous stingers at the tips of their tails. Anyone dealt damage by a wyvern's tail attack must immediately make a life force resistance roll against target score 14. If you fail, the poison deals damage resulting from a strike power 20 strike roll plus bonus damage 7. If you succeed, the strike power will only be 10. This damage can be reduced by adventurer level.

#### [ Basilisk ]

- Monster Level=8
- Rarity=9
- Agility=12    Movement Speed=10
- Number=Solo    Frequency=Very Rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Fangs：15 (8)    Strike Points=18
- Evasion Points=14 (7)    Defense Points=12
- Life Points／Resistance=25／18 (11)
- Mental Points／Resistance=12／16 (9)
- Special Abilities=Gaze (Resist target score=15, petrifying, once every 2 rounds); Poison blood (Toxicity score 15, strike power 10, bonus damage 8); Not affected by poison and illness; Sleepless
- Habitat=Deserts
- Languages=None
- Perception=Five senses

A basilisk is a large lizard, about 10 meters long, with a chicken's comb on its head and eight legs. In normal combat, it'll try to bite its enemy to death with its fangs, but if it realizes that it's at a disadvantage, it'll attack with its petrifying gaze.

Its gaze can only be used once every two rounds, cannot be used at the same time as its fangs, and can only aim at one target. Those gazed at by the basilisk must succeed on a mental power resistance roll against target score 15, or they will instantly turn to stone.

You can attempt to use a large mirror (at least the size of a small shield) to catch the basilisk's gaze and reflect it back to turn the basilisk into stone. In that case, if a character attains a final score of 19 or greater on a resistance roll against petrification, they will be able to reflect it back at the basilisk. If this happens, the basilisk will automatically be petrified.

Basilisks also have a powerful poison in their blood. Weapons that deal damage to a basilisk will be soaked with the blood and become highly poisonous. Anyone holding a weapon with basilisk blood on it must make a life force resistance roll against target score 15 each round, and if they fail, they will suffer damage resulting from a strike power 10 strike roll plus bonus damage 8. If the resistance roll is successful, the strike force becomes 0. This damage can only be reduced by adventurer level.

#### [ Small Basilisk ]

- Monster Level=5
- Rarity=10
- Agility=12    Movement Speed=7
- Number=One    Frequency=Very Rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Fangs：12 (5)    Strike Points=13
- Evasion Points=13 (6)    Defense Points=9
- Life Points／Resistance=19／14 (7)
- Mental Points／Resistance=9／12 (5)
- Special Ability=Gaze (Resist target score=15, petrifying, once every 2 rounds); Poison blood (Toxicity score 15, strike power 10, bonus damage 8); Not affected by poison and illness; Sleepless
- Habitat=Deserts
- Languages=None
- Perception=Five senses

This is a small species of basilisk. Although they're small, their petrifying gaze and poisonous blood are just as powerful as those of the larger species.

#### [ Sea Dragon ]

- Monster Level=8
- Rarity=18
- Agility=13    Movement Speed=8／14 (air)
- Number=One    Frequency=Very Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：15 (8)／Tail：15 (8)／Strangle：17 (10)
- Strike Points=19／18／17
- Evasion Points=14 (7)    Defense Points=12
- Life Points／Resistance=35／19 (12)
- Mental Points／Resistance=12／16 (9)
- Special Abilities=Strangling; Water adaptation
- Habitat=Seas
- Languages=None
- Perception=Five senses (darkvision)

It is said that the sea monster, the sea dragon, is a creature that evolved from a dragon to adapt to living in the water, but this is not known for sure. Its face looks like that of a dragon, but its body is long and slender and has no wings, making it more like a snake. At a total of 30 meters long, it is feared by sailors along with the giant octopus (p. 228).

A sea dragon can attack with its fangs and tail, and at the same time, it can also wrap its long body around its opponent and perform a strangling attack. Even a large ship can sink within minutes if it's ensnared by a sea dragon.

#### [ Wyrm ]

- Monster Level=8
- Rarity=18
- Agility=12    Movement Speed=35 (air)
- Number=One    Frequency=Very Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Fangs：15 (8)／Tail：15 (8)
- Strike Points=18／17
- Evasion Points=14 (7)    Defense Points=11
- Life Points／Resistance=25／18 (11)
- Mental Points／Resistance=16／16 (9)
- Special Abilities=None in particular
- Habitat=Steep mountains that humans can't pass through
- Languages=Lizardman
- Perception=Five senses (illumination)

A wyrm has the appearance of a large snake, with a body over 15 meters long, and bat-like wings. Its head resembles that of a dragon or wyvern, but it has no legs at all. They have human-like intellect and can speak lizardman, but they do not have the ability to use magic.

Wyrms are highly territorial, and when other wyrms or giant creatures enter their territory, which is a radius of about 20 kilometers, they will immediately try to drive them out or they may approach them to eat them as food.

#### [ Buckbaird ]

- Monster Level=9
- Rarity=15
- Agility=11    Movement Speed=15 (air)
- Number=One    Frequency=Very Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Ram：17 (10)
- Strike Points=18
- Evasion Points=16 (9)    Defense Points=12
- Life Points／Resistance=27／19 (12)
- Mental Points／Resistance=17／17 (10)
- Special Abilities=Ray (Resist target score=16, one of paralysis／hypnosis／freeze／brainwashing／metal destruction); Not affected by poison and illness; Sleepless
- Habitat=Underground labyrinths, ruins
- Languages=Low ancient
- Perception=Pseudo

Among the Magical Beasts created by the sorcerers of the ancient kingdom, buckbairds are especially bizarre. It's a giant eyeball about one and a half meters in diameter, covered in long black hair, and it somehow floats in the air. There seem to be several subspecies, and some have been seen with antennae and short limbs. They are only found in underground labyrinths, but what they eat and how they reproduce is a complete mystery.

In combat, a buckbaird uses five different types of rays. The game master should roll 1D to determine which ray the buckbaird fires (or if it attempts to ram). The ray can only affect one target. Those targeted by the ray will be unaffected if they succeed on a mental power resistance roll against target score 16, but will be seriously affected if they fail. This ray cannot affect the buckbaird itself, even if it's reflected using a mirror, etc.

1. **Paralysis Ray** — You will be paralyzed for 6 rounds.
2. **Hypnosis Ray** — You will fall asleep. This is considered natural sleep.
3. **Freeze Ray** — You will freeze instantly and enter a state of suspended animation. Treat this the same way as the spirit magic Ice Coffin.
4. **Brainwashing Ray** — You will think the buckbaird is your ally and attack your allies. This effect lasts 18 rounds. Treat this the same way as magic that belongs to mind.
5. **Metal Destruction Ray** — Destroys metal weapons and armor you are wearing. Magical weapons and armor are not affected. This ray cannot be resisted.
6. **No firing** — It will attack without firing a ray.

#### [ Hydra ]

- Monster Level=10
- Rarity=13
- Agility=9
- Movement Speed=12／20 (water)
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Fangs： 17 (10) x 9
- Strike Points=20 x 9
- Evasion Points=15 (8)    Defense Points=14
- Life Points／Resistance=54／25 (18)
- Mental Points／Resistance=10／17 (10)
- Special Abilities=Head regenerate; Water adaptation
- Habitat=Lakes, rivers
- Languages=None
- Perception=Five senses (illumination)

The hydra is a terrifying serpent with nine heads and a total length of 10 meters. They mainly live in lakes and rivers, but can also act on land without penalty. In combat, a hydra attacks with its nine heads. At this time, it can attack a single target 9 times, or aim at different targets.

If you attack a hydra with a bladed weapon and deal 6 or more points of damage (20 or more if defense points are taken into account) in one blow, you will have cut off one head, and the hydra's number of attacks will be reduced by 1. A severed head will grow back after 5 rounds, restoring the number of attacks, and also recovering 6 life points. However, if a head is dealt fire or electric damage immediately after it falls off, that head will not regenerate. Once its life points reach 0, its heads will no longer regenerate.

#### [ Humbaba ]

- Monster Level=10
- Rarity=15
- Agility=10    Movement Speed=10
- Number=One    Frequency=Very Rare
- Intellect=High    Reaction=Adversarial
- Attack Points=Arm：18 (11)    Strike Points=17
- Evasion Points=16 (9)    Defense Points=18
- Life Points／Resistance=21／19 (12)
- Mental Points／Resistance=21／19 (12)
- Special Abilities=Gaze (Resist target score=17, petrifying, once every 3 rounds); Fire breath that covers one person (Resist target score=17, strike power 20, bonus damage 10 as well as illness／Intensity 7, once every 3 rounds); Fire immunity; Not affected by poison and illness; Sleepless
- Habitat=Forests
- Languages=Low ancient
- Perception=Five senses

The humbaba is a strange creature created by the sorcerers of the ancient kingdom, along with the buckbaird. It looks like a giant with one eye and one leg, and is over 2 meters tall. Its body color ranges from green to yellow, with a head of long hair of the same color growing in all directions like a lion's mane.

A humbaba will fire a terrifying petrification ray from its one eye, once every 3 rounds. Those struck by this gaze must make a mental power resistance roll against target score 17. If you fail, you will instantly turn to stone. Even if this ray is reflected off a mirror, etc. it cannot affect the humbaba.

A humbaba can also spit fire from its large mouth, which takes up half of its face, once every 3 rounds. The fire is large enough to cover one person, and those hit by the fire will suffer damage resulting from a strike power 20 strike roll plus bonus damage 10. However, if you succeed on a mental power resistance roll against target score 17, the strike power becomes 10. This damage can only be reduced by adventurer level and magical defense. The humbaba's fire deals damage and at the same time causes a terrible disease. Anyone who suffers even 1 point of damage from the humbaba's fire has a chance of contracting a dreadful illness called humbaba curse. You must roll 2D and if you don't roll a 7 or greater, you will become infected.

Please refer here for details on this disease.

A humbaba cannot use gaze, fire, and normal attacks at the same time. Only one of these attacks can be performed per round.

#### [ Roc ]

- Monster Level=12
- Rarity=13
- Agility=10
- Movement Speed=10／40 (air)
- Number=One    Frequency=Very Rare
- Intellect=Animal    Reaction=Neutral
- Attack Points=Beak：19 (12)／Talons：20 (13)
- Strike Points=22／22
- Evasion Points=17 (10)    Defense Points=16
- Life Points／Resistance=40／24 (17)
- Mental Points／Resistance=20／21 (14)
- Special Abilities=Capture
- Habitat=Rarely seen on the distant southern islands of Alecrast
- Languages=None
- Perception=Five senses

The most feared beast second only to the dragon, the roc is a gigantic bird resembling an eagle, with a wingspan of 20 meters. Once every few years, they may be swept close to the continent by the wind, and are the subject of gossip among sailors.

A roc's talons alone are over 1 meter long, and it can lift and carry human-sized animals with one foot, or a cow or horse with both feet. Those hit by a roc's talon attacks will be grabbed by the talons, lifted into the air, and carried to its nest. Besides roc infants, its nest is said to be full of treasure. Like the griffon, it may have a habit of collecting shiny objects.

Rock eggs can measure up to 2 meters in diameter, making even newborn infants larger than humans. Here is the data of an infant for your reference.

#### [ Roc Infant ]

- Monster Level=3
- Rarity=13
- Agility=6    Movement Speed=6
- Number=One to several
- Frequency=Very Rare
- Intellect=Animal    Reaction=Neutral
- Attack Points=Beak：10 (3)    Strike Points=10
- Evasion Points=9 (2)    Defense Points=6
- Life Points／Resistance=20／12 (5)
- Mental Points／Resistance=8／10 (3)
- Special Abilities=None in particular
- Habitat=Rarely seen on the distant southern islands of Alecrast
- Languages=None
- Perception=Five Senses

#### [ Dragon ]

There are three main types of dragons in Forcelia: ancient dragons (drakes), elder dragons, and lesser dragons.

All of these dragons are similar in appearance. Their entire body is covered with hard scales, and the color of these scales varies depending on the individual. They have a snake-like head and tail, with horns and spikes growing along their spine. Their legs are thick and sturdy, for bipedal walking on the ground. By contrast, their hands are slender, but they can move them dexterously. They have bat-like wings on their backs. These wings are comparatively small for their body size.

The 30 meter long drake, feared as a god slayer monster, and also a master of a variety of magic, is nowhere to be seen in Forcelia today. It is said that there is no way for a human to ever take on a drake. Even the elder and lesser species, which are weaker than drakes, are far too powerful enemies for humans to face, and those who defeat these dragons are hailed as dragon slayer heroes.

#### [ Lesser Dragon ]

- Monster Level=10
- Rarity=10
- Agility=10
- Movement Speed=10／30 (air)
- Number=One    Frequency=Very Rare
- Intellect=Low    Reaction=Neutral
- Attack Points=Fangs：17 (10)／Talon：18 (11)／Talon：18 (11)／Tail：17 (10)
- Strike Points=22／21／21／21
- Evasion Points=15 (8)    Defense Points=15
- Life Points／Resistance=50／24 (17)
- Mental Points／Resistance=20／19 (12)
- Special Abilities=Fire breath in a 20 meter forward radius (Resist target score=17, strike power 20, bonus damage 10); Roar of fear (Resist target score=17); Fire immunity; Not affected by poison and illness; Sleepless
- Habitat=Mountains, caves, other
- Languages=Lizardman
- Perception=Five senses (darkvision)

Lesser dragons are about 15 meters long. They have low intellect, and do not use magic. There is an outlook that they are like giant beasts, living according to instinct rather than thought.

Lesser dragons have the ability to breathe fire, and are also resistant to fire. The lesser dragon's flames spread out in a semicircle, with a 20 meter forward radius. Those within range must make a mental power resistance roll against target score 17. If you fail, you'll suffer damage resulting from a strike power 20 strike roll plus 10 points of bonus damage. The use of fire is at the dragon's discretion, and there is no limit to the number of times it can use it, but it cannot make physical attacks with fangs or claws on the same round in which it uses fire.

A dragon's roar also brings intense fear to those who hear it. Anyone who hears the dragon's roar must make a mental power resistance roll against target score 17. If you fail, determine the effect using Table 5-5: Fears. Treat this the same as magic that belongs to mind. A dragon cannot breathe fire or attack with their fangs or claws on the same round in which it roars.

Dragons may take long periods of rest called dormant season, but they do not require sleep in the normal sense of the word and cannot be put to sleep by magic.

#### [ Elder Dragon ]

- Monster Level=15
- Rarity=10
- Agility=10
- Movement Speed=10／30 (air)
- Number=One    Frequency=Very Rare
- Intellect=High    Reaction=Neutral
- Attack Points=Fangs：22 (15)／Talon：23 (16)／Talon：23 (16)／Tail：22 (15)
- Strike Points=28／27／27／27
- Evasion Points=20 (13)    Defense Points=21
- Life Points／Resistance=70／32 (25)
- Mental Points／Resistance=30／26 (19)
- Special Abilities=10th level ancient magic (Magic Intensity／Magic Power=20／13); 10th level dragon roar magic (Magic Intensity／Magic Power=20／13); Fire breath in a 30 meter forward radius (Resist target score=22, strike power 30, bonus damage 15); Roar of fear (Resist target score=22); Fire immunity; Not affected by poison and illness; Sleepless
- Habitat=Mountains, caves, other
- Languages=Lizardman, low ancient
- Perception=Five senses (darkvision)

Elder dragons are about 20 meters long. Unlike lesser dragons, they have high intellect and sometimes use ancient magic. Some sages claim that this is based on the lost dragon roar, and should not be called ancient magic, although the results are the same. Furthermore, they can also use dragon roar magic that uses the lost dragon roar (though they possess most of their abilities without using magic).

Elder dragons also have the ability to breathe fire. Elder-species' fire spreads in a 30-meter forward radius, and those who fail a mental power resistance roll against target score 22 will suffer damage resulting from a strike power 30 strike roll plus bonus damage 15. They also have the roar ability which causes fear. The target score to resist is 22.

Like lesser-species, elder-species can only use one of fire, roar, or physical attack (or magic) in one round.

### 13.2.7 Animals (partial)

#### [ Wolf ]

- Monster Level=1
- Rarity=5
- Agility=16    Movement Speed=24
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：8 (1)    Strike Points=5
- Evasion Points=9 (2)    Defense Points=4
- Life Points／Resistance=14／9 (2)
- Mental Points／Resistance=6／8 (1)
- Special Abilities=None in particular
- Habitat=Woods, meadows, near human villages
- Languages=None
- Perception=Five senses (illumination)

Wolves are carnivorous and usually act in packs of several to several dozen. They are also nocturnal, which means their activity is limited to the night. They systematically attack unsuspecting animals that are separated from their herd. They do not attempt to fight opponents that are stronger or outnumber them, and will immediately run away if they find themselves at a disadvantage.

Rarely, wolf cubs are captured and sometimes domesticated as hunting dogs. Such wolves have greater morals than normal ones, and will fight to the death to protect their masters.

#### [ Giant Rat ]

- Monster Level=1
- Rarity=6
- Agility=18    Movement Speed=20
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Animal    Reaction=Neutral
- Attack Points=Fangs：8 (1)／Claw：9 (2)／Claw：9 (2)
- Strike Points=4／3／3
- Evasion Points=10 (3)    Defense Points=4
- Life Points／Resistance=9／8 (1)
- Mental Points／Resistance=7／8 (1)
- Special Abilities=Disease (Intensity 5)
- Habitat=Underground tunnels, caves, ruins
- Languages=None
- Perception=Five senses (illumination)

A giant rat is a huge rodent, about 1 meter long. However, they are intelligent and dexterous, and thus can stand on their hind legs and use simple tools. They are omnivorous, and usually live in groups. They are timid by nature and will not attack unless you seriously provoke them or invade their burrow without them knowing. Even on the rare occasion that they do attack you, they will quickly run away if you wound them, and you can easily drive them away with fire.

Adventurers wounded by a giant rat's fangs or claws are at risk of contracting an illness. You must roll 2D again. If you roll a 4 or less, you will contract rat disease. Please refer to here for rat disease details.

#### [ Hanger Leg ]

- Monster Level=1
- Rarity=13
- Agility=18    Movement Speed=8
- Number=One. However, eggs are often found in groups
- Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Needle: 8 (1)    Strike Points=6
- Evasion Points=11 (4)    Defense Points=4
- Life Points／Resistance=8／8 (1)
- Mental Points／Resistance=8／8 (1)
- Special Abilities=Parasitism (Resist target score=8)
- Habitat=Forests
- Languages=None
- Perception=Five senses

This headless octopus-like creature is a vicious parasite that lives by taking over the bodies of large animals, and has no visible distinction between male and female. Its body is only 20 cm long, but its supple legs, which also serve as tentacles, are equipped with countless suckers, and can stretch to over 1 meter when extended. Also, its jumping power and strangling power are not something to be underestimated. It can easily jump up to 3 meters, and once it attaches itself to a creature's head, it won't come off even if a giant pulls at it.

Then, needles extended from the tips of the legs are embedded into the opponent's brain. In addition to absorbing nourishing blood from the blood vessels, the needles also have the function of paralyzing the opponent's brain and controlling their nervous system. The victim must make a life force resistance roll against target score 8, and if they fail, their body is taken from them regardless of their will. If your armor and adventurer level prevent you from suffering substantial damage, the needles will not pass through to your head and you will not need to make a resistance roll. However, once the attack hits, the hanger leg will now be lodged in the victim's head, so all subsequent attacks will automatically succeed.

A hanger leg that is lodged in a head cannot be removed by force. If other allies want to help, they must attack and be prepared to hit their own ally. Please refer to Attacks and Magic Against Grapplers.

A hanger leg can freely use the body of the victim it's taken over. However, even if its opponent has human intellect, it cannot speak their languages, nor can it take their knowledge and experience as its own. Of course, using magic is out of the question. Nevertheless, all motor functions and physiological abilities are at the will of the parasite.

When a hanger leg attaches itself to an adventurer, it cannot use that person's skills or adventurer level as is. Although it can perform the corresponding actions, the final score will be the result of rolling the dice as if it did not have any skills, plus 1 point bonus from the parasite's adaptive ability.

An unfortunate victim of a hanger leg's possession will lose all senses, unable to see or hear anything, and furthermore, will be unable to think. Naturally, you cannot escape on your own, but once killed, the parasite leaves the host's body. Conversely, if the host dies, it'll attempt to possess the nearest living creature.

Also, when death is near, the hanger leg will form several balls under the flesh hardened with secretion and lay small eggs. These eggs will hatch and grow inside the balls, and when they grow up, they will form a cocoon and sleep until a host creature approaches. Then, when the long-awaited opportunity arrives, they are quick to pounce on such an unwary creature.

Fortunately, however, they rarely attach themselves to humans, usually preferring to possess animals and livestock.

#### [ Eagle ]

- Monster Level=2
- Rarity=6
- Agility=18    Movement Speed=8／30 (air)
- Number=One to several    Frequency=Rare
- Intellect=Animal
- Reaction=Hunger-based
- Attack Points=Beak：9 (2)／Talons：10 (3)
- Strike Points=5／5
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=16／10 (3)
- Mental Points／Resistance=7／9 (2)
- Special Abilities=Opponent's attack is -2
- Habitat=Mountains
- Languages=None
- Perception=Five senses

Eagles are large, carnivorous birds. They attack their opponents from the air with their claws and beak. When an adventurer attacks an eagle, they will suffer a -2 penalty to their attack because it's airborne. An eagle can grab and carry away a medium-sized animal, such as a dog.

In some regions, eagles and hawks are tamed and used for hunting. They are very proud creatures by nature and are reluctant to get used to humans, but once one opens up to you, they will serve you for the rest of their lives.

#### [ Giant Centipede ]

- Monster Level=2
- Rarity=7
- Agility=10    Movement Speed=12
- Number=One to several
- Frequency=Moderate
- Intellect=Almost none    Reaction=Neutral
- Attack Points=Fangs：9 (2)    Strike Points=6+poison
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=16／10 (3)
- Mental Points／Resistance=5／8 (1)
- Special Abilities=Poison (Toxicity score 9, motor function decline=success roll-2); Mental attack immunity
- Habitat=Damp, gloomy places such as deep forests, jungles, caves, ruins, etc.
- Languages=None
- Perception=Five senses

The giant centipede is an abnormally developed giant bug, with a body length that ranges from about 30 cm to 1 meter. Their long and narrow, multi-segmented bodies are lined with dozens of legs, which they use to twist and crawl along, attacking and feeding on those who get in their way.

A giant centipede's fangs are poisonous. An adventurer bitten by a giant centipede must make a life force resistance roll against target score 9. If you fail, your motor nerves will be affected, and will suffer a -2 penalty on all success rolls. The effects of this poison last for 3 days.

#### [ Giant Lizard ]

- Monster Level=2
- Rarity=8
- Agility=13    Movement Speed=13
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：9 (2)／Claw：10 (3)／Claw：10 (3)
- Strike Points=8／7／7
- Evasion Points=9 (2)    Defense Points=6
- Life Points／Resistance=14／10 (3)
- Mental Points／Resistance=9／9 (2)
- Special Abilities=None in particular
- Habitat=Jungles, deserts, wastelands, watersides
- Languages=None
- Perception=Five senses

The giant lizard is a huge reptile with a body length of just over 2 meters. They're carnivorous and not very ferocious, and will only attack when they're hungry.

#### [ Giant Wasp ]

- Monster Level=2
- Rarity=10
- Agility=16    Movement Speed=5／18 (air)
- Number=One    Frequency=Moderate
- Intellect=Almost none
- Reaction=Neutral, aggressive during spawning season
- Attack Points=Stinger：9 (2)    Strike Points=7+poison
- Evasion Points=10 (3)    Defense Points=4
- Life Points／Resistance=8／9 (2)
- Mental Points／Resistance=6／9 (2)
- Special Abilities=Poison (Toxicity score 12, paralysis); Mental attack immunity
- Habitat=Warm Forests
- Languages=None
- Perception=Five senses

This is a wasp about 1 meter long, with a black body and a red band on its belly. They do not build hives like honeybees, and will not attack you unless you attack them. However, during the autumn spawning season, the females become ferocious. This is because they have to attack animals to lay their eggs.

A giant wasp's stinger is poisonous (toxicity score 12). Those dealt damage by a wasp's attack must succeed on a life force resistance roll, or else the poison will paralyze their bodies, leaving them in a state of suspended animation. This state of suspended animation lasts semi-permanently. A giant wasp will drag paralyzed prey to its burrow, lay eggs inside them, then hide the entrance to the burrow with dead leaves, etc. Wasp larvae grow by feeding on the flesh and organs of their prey.

#### [ Horse ]

##### Warhorse

- Monster Level=2
- Rarity=5
- Agility=12    Movement Speed=30
- Number=Depends on the situation
- Frequency=Moderate
- Intellect=Animal    Reaction=Depends on the rider
- Attack Points=Heel：8 (1)    Strike Points=10
- Evasion Points=9 (2)    Defense Points=5
- Life Points／Resistance=18／11 (4)
- Mental Points／Resistance=10／9 (2)
- Special Abilities=None in particular
- Habitat=Human villages
- Languages=None
- Perception=Five senses

This is a riding horse trained to follow the will of its rider, even in battle. It can attack at the same time as the rider, unless the rider performs a lance charge. The rider basically holds the reins with one hand, and a weapon with the other. This means you can't use shields or two-handed weapons.

To fight on horseback, you must make a success roll against target score 7 each round using adventurer level + dexterity bonus as the baseline score. If you attempt to control your horse without using the reins, you will suffer a -4 penalty to your final score.

#### [ Wardog ]

- Monster Level=3
- Rarity=10
- Agility=16    Movement Speed=24
- Number=Depends on the situation    Frequency=Rare
- Intellect=Animal    Reaction=Depends on the user
- Attack Points=Fangs：10 (3)    Strike Points=10
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=16／11 (4)
- Mental Points／Resistance=10／10 (3)
- Special Abilities=None in particular
- Habitat=Human villages
- Languages=None
- Perception=Five senses

A wardog is a breed of dog that has been bred through crossbreeding, specially trained for combat, and is a specialty of the kingdom of Azarnia (the Azarn Islands). They're characterized by entirely black bodies, pointed ears and snout, almost no tail, and a slender physique. They can fight more than equally against normal soldiers, even if their opponents are well armed. No matter how unfavorable the situation becomes, they will not run away unless commanded to do so. A wardog never barks unless commanded to do so in advance.

#### [ Killer Shark ]

- Monster Level=3
- Rarity=8
- Agility=16    Movement Speed=24 (water)
- Number=One to several
- Frequency=Moderate
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：10 (3)    Strike Points=13
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=25／13 (6)
- Mental Points／Resistance=6／10 (3)
- Special Abilities=Water adaptation
- Habitat=Seas
- Languages=None
- Perception=Five senses

Killer Sharks belong to the so-called man-eating shark family, but they are particularly large, ferocious, and cunning. They're about 5 meters long, and will attack anything that moves in the sea, chomping it to pieces with the sharp fangs in their huge mouths. Killer sharks will continue to grow as long as they live. The data listed here is for an average adult shark. For older ones, set the monster level to 4 and apply +1 to each score. Some young killer sharks have a monster level of 2. Apply -1 to each score.

#### [ Crocodile ]

- Monster Level=3
- Rarity=6
- Agility=12    Movement Speed=6／12 (water)
- Number=One to several    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Large jaws：10 (3)／Tail：10 (3)
- Strike Points=12／10
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=20／12 (5)
- Mental Points／Resistance=6／10 (3)
- Special Abilities=Strangling with large jaws; Water adaptation
- Habitat=Wetlands such as jungles, swamps, etc.
- Languages=None
- Perception=Five senses

Crocodiles are large carnivorous reptiles. Their standard body length is 1.5 meters, but larger ones can exceed 3 meters. Such giant crocodiles are also called alligators. They are ferocious by nature and will attack indiscriminately if they are hungry. Attacks with their large jaws are powerful, and once they bite an opponent, they will not let go and continue to deal damage. Please resolve this as strangling. After biting down on their prey this way, crocodiles like to drag them underwater to eat it.

A crocodile's tail is also a powerful weapon, but it cannot attack the same target with its jaws and tail at the same time.

#### [ Giant Scorpion ]

- Monster Level=3
- Rarity=8
- Agility=12    Movement Speed=14
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Almost none    Reaction=Violent
- Attack Points=Pincer：11 (4)／Pincer：11 (4)／Needle：10 (3)
- Strike Points=9／9／12+poison
- Evasion Points=10 (3)    Defense Points=7
- Life Points／Resistance=18／12 (5)
- Mental Points／Resistance=5／9 (2)
- Special Abilities=Poison (Toxicity score 10, death after 1 Hour); Mental attack immunity
- Habitat=Deserts, wastelands
- Languages=None
- Perception=Five senses

The giant scorpion is a huge scorpion with a body length of over 3 meters. Their personality is ferocious, moreover, they're carnivorous, always hungry and when any moving thing comes into view, they'll attack it immediately.

When in combat, a giant scorpion can use the pincers on its arms and the barb on its tail to attack different targets (of course, it can also concentrate its attacks on a single target). The barb on the tip of its tail is a stinger that secretes a deadly poison (toxicity score 10), and those stung must make a life force resistance roll. If you fail, your whole body will become paralyzed after an hour, then you will draw your last breath.

#### [ Giant Mantis ]

- Monster Level=3
- Rarity=13
- Agility=18
- Movement Speed=18／20 (air)
- Number=One    Frequency=Rare
- Intellect=Almost none
- Reaction=Hunger-based
- Attack Points=Sickle：10 (3)／Sickle：10 (3)
- Strike Points=8／8
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=14／11 (4)
- Mental Points／Resistance=7／10 (3)
- Special Abilities=Strangling with sickles (1D: 1-3 right arm, 4-6 left arm); Mental attack immunity
- Habitat=Remote Deserts and Wastelands
- Languages=None
- Perception=Five senses

This is a praying mantis about the size of a human, with quick movements, it unleashes two sickles to kill and eat animals. It is also able to fly over a distance of several tens of meters.

When attacking a human, a giant mantis will use its sickles to capture their arms and attempt to block their movement. Anyone hit by a giant mantis's attack will have one arm trapped. You must roll the dice to determine which arm is trapped. Roll 1D, and if it's 1-3, it'll be the right arm, but if it's 4-6 it'll be the left arm. Ancient magic cannot be used while one arm is trapped. Also, on subsequent rounds, you cannot escape from the giant mantis, so your evasion points will be -4. In order to escape from a sickle that's trapped your arm, you must succeed on a resistance roll against target score 10 (or attack points from when the attack hits, if using optional rules) using adventurer level + strength bonus as the baseline score. If you cannot escape, you will suffer 8 points of damage from strangling. This damage can be reduced by armor and adventurer level.

On the other hand, while capturing a human's arm with one sickle, a giant mantis can only use its other sickle to attack, and since it cannot move freely, its evasion points will be reduced by -2.

#### [ Scarlet Vulture ]

- Monster Level=3
- Rarity=10
- Agility=15
- Movement Speed=10／30 (air)
- Number=One to several
- Frequency=Moderate
- Intellect=Animal
- Reaction=Hunger-based
- Attack Points=Beak：10 (3)／Talons：11 (4)
- Strike Points=6／6
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=15／11 (4)
- Mental Points／Resistance=9／10 (3)
- Special Abilities=Capture; Opponent's attack is -2
- Habitat=Mountains, meadows
- Languages=None
- Perception=Five senses (darkvision)

The scarlet vulture is a large carnivorous bird, with a wingspan of up to 4 meters while both wings are spread. It is so called because its wings and the top of its head are bright red. Although it is a member of the vulture family, so to speak, it regularly eats live meat, rather than dead meat. It can lift anything from small animals such as dogs, cats, etc. to things the size of a human child into the air. It tries to kill its prey by dropping it from a high altitude, or by pecking what it catches with its beak. The scarlet vulture has strong legs, and can move quite freely on the ground.

Those hit by a scarlet vulture's claw attack, if they're of a suitable size (a grassrunner is of a suitable size), will be lifted into the air. If the Scarlet Vulture's claw attack hits an object of a suitable size (the Grass Runner is a "reasonable size"), it will be lifted into the air. Those who are caught, even if not lifted into the air, will suffer a -2 penalty to evasion speed against the beak attack.

This bird can see things even at night. At this time, its eyes reflect a small amount of light, and glow red.

To attack scarlet vulture while in the air, you must suffer a -2 penalty to attack power.

#### [ Tiger ]

- Monster Level=3
- Rarity=6
- Agility=21    Movement Speed=25
- Number=One to several    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fang：10 (3)／Claw：11 (4)／Claw：11 (4)
- Strike Points=11／10／10
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=20／12 (5)
- Mental Points／Resistance=7／10 (3)
- Special Abilities=None in particular
- Habitat=Deep in forests
- Languages=None
- Perception=Five senses (illumination)

Tigers are fierce, carnivorous beasts that usually act alone. Despite their large size, they possess the graceful and flexible movements characteristic of the cat family, and are among the strongest of all ordinary animals. If they're hungry, they may also attack humans.

It is said that once a tiger learns the taste of human flesh, it becomes a man-eating tiger, which aggressively attacks humans.

#### [ Bat ]

There are many different types of bats in Forcelia. Some of these bats are not very strong, but have characteristics that make them dangerous monsters. Here we will introduce three of them.

##### Bat

- Monster Level=1
- Rarity=5
- Agility=18    Movement Speed=10
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Animal    Reaction=Neutral
- Attack Points=Fangs：8 (1)    Strike Points=3
- Evasion Points=11 (4)    Defense Points=3
- Life Points／Resistance=7／8 (1)
- Mental Points／Resistance=6／8 (1)
- Special Abilities=Disease (Intensity 6); Opponent's attack is -2
- Habitat=Places sunlight does not reach, such as caves, etc.
- Languages=None
- Perception=Five senses (sonar)

They often sleep hanging from the ceiling of their caves during the day, and are mainly active at night. They are sensitive to light, and if an adventurer with a light carelessly enters the nest, they may blindly attack in groups.

When attacking a bat, you'll suffer a -2 penalty due to the bat's keen perception, plus the fact that it's flying in the air.

Those bitten by a bat-- those whose life force has been dealt damage by a bat's attack --are at risk of contracting a fever. Roll 2D again. If you roll a 5 or less, you'll be infected with bat fever. Please refer to here for details on bat fever.

##### Vampire Bat

- Monster Level=2
- Rarity=10
- Agility=19    Movement Speed=20
- Number=One to several    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：9 (2)    Strike Points=5
- Evasion Points=10 (3)    Defense Points=4
- Life Points／Resistance=11／9 (2)
- Mental Points／Resistance=6／9 (2)
- Special Abilities=Bloodsuck (Strike power 10, bonus damage 2); Opponent's attack is -2
- Habitat=Places sunlight does not reach, such as caves, etc.
- Languages=None
- Perception=Five senses (sonar)

A vampire bat is a giant bloodsucking bat with a wingspan of about 2 meters. However, it prefers to suck the blood of living creatures rather than eat their meat. Once a fang attack hits, it will attach itself to its opponent and begin bloodsucking starting on the next round. Make a strike power 10 plus bonus damage 2 check. This damage can only be reduced by adventurer level. Assume this state is a grapple as in the optional rules. Therefore, in order for the possessed opponent to attack the vampire bat in question, they will need a melee weapon that can be used at close range, such as a dagger. Also, to detach the vampire bat, you must make a resistance roll using adventurer level + strength bonus as the baseline score. At this time, the vampire bat's attack points become the target score. Furthermore, if you attack a vampire bat that's attached to a living creature, there is also a risk of accidentally hitting an ally.

Attacks made against a vampire bat while it's in the air suffer a penalty of 2 due to the bat's keen perception plus the fact that it is flying.

##### Giant Bat

- Monster Level=3
- Rarity=9
- Agility=18    Movement Speed=20
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：10 (3)／Talon：10 (3)／Talon：10 (3)
- Strike Points=6／6／6
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=11／10 (3)
- Mental Points／Resistance=6／10 (3)
- Special Abilities=Capture; Opponent's attack is -2
- Habitat=Places sunlight does not reach, such as caves, etc.
- Languages=None
- Perception=Five senses (sonar)

A giant bat is a massive bat, with a wingspan of 3 meters across. They are completely nocturnal creatures, flying around forests and wastelands to hunt at night. They're omnivorous and mainly catch and eat small animals, but when they're starving they may also attack livestock and humans. When attacking prey, they act in groups, quickly descending from above, and scratching with their sharp talons.

A giant bat can capture and carry away a small human. If hit by both claws at the same time, a victim adventurer must make a resistance roll using the giant bat's attack points (or if using optional rules, the attack's final score, whichever is higher) as the target score and adventurer level + strength bonus as the baseline score, to prevent being carried away. If you succeed, you'll be able to escape before the giant bat flies too high, but if you fail, you'll be taken straight to its nesting hole. You can try to resist again while being carried, but you'll have to be prepared to suffer falling damage.

#### [ Bear ]

There are several types of bears, but here we will introduce the grizzly, which is the representative type in Forcelia.

##### Grizzly

- Monster Level=3
- Rarity=6
- Agility=14    Movement Speed=21
- Number=One to several    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：10 (3)／Claw：11 (4)／Claw：11 (4)
- Strike Points=12／11／11
- Attack Points=Fangs：10 (3)／Bind：11 (4)
- Strike Points=12／10
- Evasion Points=10 (3)    Defense Points=7
- Life Points／Resistance=22／12 (5)
- Mental Points／Resistance=7／10 (3)
- Special Abilities=Strangling
- Habitat=Forests
- Languages=None
- Perception=Five senses

Grizzlies are generally solitary, except when a mother bear is with her cubs. They are omnivores and are said to eat anything they can fit into their mouths. They're about 3 meters tall, but some giant grizzlies can reach 4 meters. Moreover, they're classified as one of the most terrifying animals due to their super strength and agility that you wouldn't expect from their physique.

Usually it tries to avoid humans on its own accord, but if it and a human bump into one another, or if it's hungry, then things are different. Also, a mother bear with her cubs will do everything in her power to protect them, so travelers should avoid approaching groups of bears carelessly. At this time, it's useless to play dead. This is because they also eat dead meat. It is also said that once a grizzly bear has learned the taste of human flesh, it'll attack humans more frequently.

A bear's special attack is a bear hug. This is a technique in which it holds its opponent in its thick arms, squeezing them. Treat this as strangling. Bears use this attack depending on the situation. When surrounded by multiple opponents, it'll choose to swing its arms around and try to mow down anything it happens to hit, but if there are fewer opponents, it'll approach for a bear hug. If a bear hug attack hits, the adventurer will be held by the bear.

A bear that captures an opponent in a bear hug will both strangle and bite the opponent at the same time. During this attack, a bear gains a +4 bonus to attack points. In this state, the bear cannot attack other opponents.

#### [ Lion ]

The lion is a carnivorous beast of prey, as its popular moniker "king of the beasts" suggests. They usually live in small family groups consisting of one male with a fine mane and several females. Males and females differ slightly in strength. In most cases, it is the female lion who fights and hunts. The male lion's primary role is to intimidate its prey and lead it to where the females are waiting.

Lions usually don't try to come close to human villages. However, lions sometimes attack humans if they're starving or if they've tasted human flesh.

##### Female Lion

- Monster Level=3
- Rarity=5
- Agility=22    Movement Speed=27
- Number=Several    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：10 (3)／Claw：11 (4)／Claw：11 (4)
- Strike Points=11／10／10
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=18／12 (5)
- Mental Points／Resistance=8／10 (3)
- Special Abilities=None in particular
- Habitat=Meadows, wastelands
- Languages=None
- Perception=Five senses (illumination)

##### Male Lion

- Monster Level=3
- Rarity=5
- Agility=18    Movement Speed=25
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：10 (3)／Claw：11 (4)／Claw：11 (4)
- Strike Points=11／10／10
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=20／12 (5)
- Mental Points／Resistance=8／10 (3)
- Special Abilities=None in particular
- Habitat=Meadows, wastelands
- Languages=None
- Perception=Five senses (illumination)

#### [ Giant Slug ]

- Monster Level=4
- Rarity=12
- Agility=6    Movement Speed=5
- Number=One    Frequency=Rare
- Intellect=Almost none
- Reaction=Hunger-based
- Attack Points=Ram：12 (5)
- Strike Points=11
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=19／13 (6)
- Mental Points／Resistance=6／11 (4)
- Special Abilities=Crush (14 damage next round); Weak to Salt
- Habitat=Damp underground labyrinths, marshlands
- Languages=None
- Perception=Five senses

This is a slug with a body length of about 5 meters. It moves very slowly, knocking down everything in its path, and grinding it all up with its jagged belly lined with bumps.

Those hit by a giant slug attack will be dealt damage and knocked down at the same time. On the next round, the slug will pass over your body, dealing you 14 points of damage. No actions can be taken while the slug is passing over. This damage can be reduced by armor.

You can put a large amount of salt (at least 500 kg) on a giant slug to dehydrate it and put it into suspended animation, but salt alone will not kill it.

#### [ Toad ]

There are many types of frogs in Alecrast, but most are small and harmless. However, there are some that are dangerous, such as the following two types.

##### Poison Toad

- Monster Level=1
- Rarity=7
- Agility=8    Movement Speed=8／10 (water)
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Animal    Reaction=Neutral
- Attack Points=ー    Strike Points=ー
- Evasion Points=9 (2)    Defense Points=3
- Life Points／Resistance=7／8 (1)
- Mental Points／Resistance=2／7 (0)
- Special Abilities=Poison body surface (Toxicity score 9, blind)
- Habitat=Lakes
- Languages=None
- Perception=Five senses

This is a toad about 50 cm long. Since they feed on fish and insects, they rarely attack humans, but if they're attacked or startled, they'll try to protect themselves by spewing venom from the secretory glands in their heads.

Anyone within 3 meters of a poison toad when it spews its venom must succeed on a life force resistance roll against target score 9. If you fail, the poison will get into your eyes and you will lose your vision. It'll recover naturally after 3 days, but it can also be cured with the holy magic Cure Poison. Even if you succeed on the resistance roll, your skin will be irritated and itchy for a while.

##### Giant Toad

- Monster Level=4
- Rarity=11
- Agility=8    Movement Speed=10／16 (water)
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Tongue：10 (3)    Strike Points=7
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=21／13 (6)
- Mental Points／Resistance=6／11 (4)
- Special Abilities=Wrap tongue around (strangling) and swallow whole
- Habitat=Wetlands such as lakes, riverbanks, etc.
- Languages=None
- Perception=Five senses

This is a huge toad with a body length of 3 meters. It extends its 5 meter long tongue and entangles its prey, and if it's a human-sized animal, it will swallow it whole.

Attacks by a giant toad are treated as strangling. If the prey can't escape within 3 rounds, the toad will pull it in on the next round and swallow it whole.

If someone becomes entangled in a Toad's tongue, the other party members can attempt to sever it with a bladed weapon. A toad's tongue has 4 defense points, and can be severed if it's dealt a total of 7 or more points of damage. At this time, there is a risk of hurting your ally. For more information, please refer to how to handle grapples. With his tongue severed, a toad will run away.

Those who are swallowed whole will continue to suffer strike power 10 damage plus bonus damage 4 each round spent inside the toad's belly. This damage cannot be prevented by armor and can only be reduced by adventurer level. Resistance rolls are also not possible. If you have a dagger, shortsword, or similar bladed weapon, you can use it to slice through the toad's belly and attempt to escape. You must make the attack at a -4 penalty, and if you hit, the damage check is made as normal, and if the toad dies, you can escape.

Alternatively, someone else could kill the toad, then cut its belly open and rescue the victim before they're digested. In that case, if you deal more damage than the toad's remaining life points, that same damage (before it's reduced by the toad's defense points) is also dealt to the victim inside its belly at the same time.

#### [ Ant ]

Ordinary ants are unlikely to pose a threat to adventurers. However, Alecrast is home to giant ants, which are larger and more dangerous than humans.

##### Giant Ant

- Monster Level=3
- Rarity=8
- Agility=16    Movement Speed=15
- Number=Several to around ten
- Frequency=Moderate
- Intellect=Almost none    Reaction=Violent
- Attack Points=Fangs：10 (3)    Strike Points=8
- Evasion Points=10 (3)    Defense Points=8
- Life Points／Resistance=24／13 (6)
- Mental Points／Resistance=6／10 (3)
- Special Abilities=Mental attack immunity
- Habitat=Caves, ruins
- Languages=None
- Perception=Five senses

Giant ants are giant omnivorous ants that are just over 2 meters long. Although their bodies are gigantic, their nature is no different from that of ordinary ants. Although they have almost no intellect, that makes them fearless and a troublesome opponent to deal with. They are extremely voracious creatures, and will attack anything that moves, thinking it's food. Its shiny black carapace is as strong as plate armor, and its attacks with its sharp fangs are not to be underestimated. In Alecrast, it's said that not a single blade of grass remains after a giant ant has passed by.

##### Giant Ant Infant

- Monster Level=3
- Rarity=8
- Agility=10    Movement Speed=8
- Number=Several to around ten
- Frequency=Rare
- Intellect=Almost none    Reaction=Violent
- Attack Points=Fangs：10 (3)    Strike Points=8
- Evasion Points=9 (2)    Defense Points=5
- Life Points／Resistance=20／12 (5)
- Mental Points／Resistance=6／10 (3)
- Special Abilities=Mental attack immunity
- Habitat=Caves, ruins
- Languages=None
- Perception=Five senses

A giant ant larva. It looks like a normal ant larva made many times larger. These larvae are always hungry, and will attack any creature other than their own kind that approaches to feed.

##### Giant Ant Soldier

- Monster Level=4
- Rarity=10
- Agility=16    Movement Speed=16
- Number=Several    Frequency=Moderate
- Intellect=Almost none    Reaction=Violent
- Attack Points=Fangs：11 (4)／Claw：12 (5)／Claw：12 (5)
- Strike Points=14+poison／13／13
- Evasion Points=11 (4)    Defense Points=9
- Life Points／Resistance=25／14 (7)
- Mental Points／Resistance=6／11 (4)
- Special Abilities=Poison (Toxicity score 10, strike power 10, bonus damage 4); Mental attack immunity
- Habitat=Caves, ruins
- Languages=None
- Perception=Five senses

Giant ant soldiers are soldier ants that are raised on a special diet to protect the giant ant queen. It doesn't look much different from a regular giant ant, but its jaws are even more massive and strong. In addition, a soldier's fangs secrete a highly toxic acid. Anyone hit by a giant ant soldier will have their wound burned by the acid and, in addition to normal damage, must make a life force resistance roll, which if they fail, they will suffer damage resulting from a strike power 10 strike roll plus bonus damage 4. This damage can only be reduced by adventurer level. If the fangs cannot penetrate armor, damage from the acid will not be dealt. Whether the acid is capable of destroying armor, etc. is up to each game master's decision. Usually, it's easier to progress through the game if you don't think about it. By the way, all giant ant soldiers are female.

##### Giant Ant Queen

- Monster Level=5
- Rarity=10
- Agility=16    Movement Speed=5
- Number=One    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Fangs：12 (5)    Strike Points=16
- Evasion Points=12 (5)    Defense Points=8
- Life Points／Resistance=35／16 (9)
- Mental Points／Resistance=15／13 (6)
- Special Abilities=Entangling; Command
- Habitat=Caves, ruins
- Languages=None
- Perception=Five senses

The giant ant queen is the queen of all giant ants. Her head and chest are almost the same as those of a normal giant ant, but her white abdomen is full of eggs and bloated. Therefore, her body length can reach over 10 meters.

A giant ant queen is always protected by giant ant soldiers, but she also has her own means of attack. Giant ant queens can spit out mucus from their mouths that's used to alter the food they feed to their young. Those hit by this mucus will be deprived of their bodily freedom. If you're hit by the mucus, you won't suffer damage, but you will become more and more entangled. While entangled in the mucus, attack and evasion suffer a -4 penalty, and ancient magic and spirit magic cannot be used. You can escape from the mucus by succeeding on a success roll against target score 12 using adventurer level + strength bonus as the baseline score. However, if you're unable to escape, the target score for the success roll required to escape increases by 2 points each time you're hit by the mucus, increasing to 14, 16…… and so on. If the target score is 13 or more above the baseline score, the prey will be completely entangled and unable to move.

A giant ant queen has some intellect. With a certain scent (pheromone), she can command other giant ants, devise some strategy, and make them fight. Once a giant ant queen is defeated, the giant ants under its command will begin to attack everything around them indiscriminately (they will not attack each other).

#### [ Ape ]

Forcelia is home to many different types of monkeys, from small apes that live in groups to giant apes that grow to abnormal sizes. Here, we will introduce four types of different sizes.

##### Small Ape

- Monster Level=1
- Rarity=5
- Agility=13    Movement Speed=13
- Number=Several to around ten
- Frequency=Moderate    Intellect=Low
- Reaction=Neutral
- Attack Points=Claws：9 (2)    Strike Points=3
- Evasion Points=9 (2)    Defense Points=4
- Life Points／Resistance=12／9 (2)
- Mental Points／Resistance=10／8 (1)
- Special Abilities=None in particular
- Habitat=Forests and mountains near human villages
- Languages=None
- Perception=Five senses

Small apes are omnivorous and usually live in groups of several to around ten. In large groups, the number may swell to several dozen, centered around a strong male leader (boss ape). They are generally docile and do not attack humans, but in rare cases when faced with severe hunger or the need to protect their group, they may display hostile behavior. Furthermore, once they do fight, they fight together in groups and display considerable bravery, especially while the leader is still alive. They also have high intellect for an animal, so in that sense you should not let your guard down.

Small apes live in most parts of Forcelia. There are many breeds, and although the differences in physique and body fur are too countless to mention, they generally share similar characteristics.

##### Boss Ape

- Monster Level=2
- Rarity=5
- Agility=13    Movement Speed=13
- Number=One    Frequency=Moderate
- Intellect=Low    Reaction=Neutral
- Attack Points=Fangs：10 (3)    Strike Points=5
- Evasion Points=10 (3)    Defense Points=5
- Life Points／Resistance=14／10 (3)
- Mental Points／Resistance=10／9 (2)
- Special Abilities=None in particular
- Habitat=Forests and mountains near human villages
- Languages=None
- Perception=Five senses

This is the boss ape that leads a group of small apes, and only males can become one.

##### Gorilla

- Monster Level=2
- Rarity=    Agility=12    Movement Speed=16
- Number=One to several    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Arm：10 (3)／Arm：10 (3)
- Strike Points=8／8
- Attack Points=Strangling：10 (3)
- Strike Points=7
- Evasion Points=9 (2)    Defense Points=5
- Life Points／Resistance=18／11 (4)
- Mental Points／Resistance=10／9 (2)
- Special Abilities=Strangling
- Habitat=Jungles
- Languages=None
- Perception=Five senses

Gorillas are apes larger than humans, are omnivorous, and do not form large groups. Those in Alecrast have ferocious personalities and prefer to attack creatures smaller than themselves.

Gorillas attack by swinging their brawny arms around, but if an opponent is smaller than itself, it will grab it with both arms and try to strangle it to death. This attack method is resolved using the rules for strangling.

##### Mutant Big Ape

- Monster Level=5
- Rarity=11
- Agility=12
- Movement Speed=20
- Number=One
- Frequency=Very Rare
- Intellect=Low
- Reaction=Adversarial
- Attack Points=Arm：13 (6)／Arm：13 (6)
- Strike Points=13／13
- Attack Points=Strangling：13 (6)
- Strike Points=12
- Evasion Points=11 (4)
- Defense Points=9
- Life Points／Resistance=24／15 (8)
- Mental Points／Resistance=10／12 (5)
- Special Abilities=Strangling
- Habitat=Jungles
- Languages=None
- Perception=Five senses

The mutant big ape is a mutant species of gorilla, a ferocious giant ape that can in fact reach up to 5 meters in height. They have a ferocious personality similar to that of a gorilla, and will attack anything they see. Like gorillas, they fight by flailing their arms and, in some cases, trying to strangle their opponent to death.

#### [ Giant Antlion ]

##### Larva

- Monster Level=5
- Rarity=14
- Agility=7    Movement Speed=10／10 (underground)
- Number=One    Frequency=Very Rare
- Intellect=Almost none    Reaction=Violent
- Attack Points=Large jaws：12 (5)    Strike Points=14
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=20／14 (7)
- Mental Points／Resistance=10／12 (5)
- Special Abilities=Capture with large jaws; Bloodsuck (Strike power 10, bonus damage 5); Surprise attack (Sense target score=16); Mental attack immunity
- Habitat=Deserts (Khan Desert only)
- Languages=None
- Perception=Five senses

The giant antlion is a creature about 3 meters long total, with most of the front half of its body occupied by its large jaws, a cone-shaped tail on the back half of its body, and three pairs of spatula-shaped legs that bend forward at the joints, making it suitable for burrowing underground. This creature usually lurks in shallow underground areas. When a creature passes directly above it, the giant antlion will sense its footsteps and suddenly dive further underground (with its tail). As a result, a large cone-shaped hole with a 2 meter radius and a 3 meter depth opens up at the feet of the unfortunate prey, into which the prey will fall. The footing inside this sand pit is extremely poor, so it's impossible to escape on your own using normal methods (climbing). In addition, a character's attack and evasion suffer a -4 penalty.

The giant antlion will attempt to bite down on its fallen prey with its large jaws. If it manages to bite, it'll hold its grip firmly in place then stab its mouth which is a hollow needle into the prey's body and suck out the body's fluids (this attack will hit automatically). Escaping from a giant antlion's large jaws requires a success roll using adventurer level + strength bonus as the baseline score. Damage due to bloodsucking is strike power 10 plus bonus damage 5, and cannot be reduced by armor.

Those with the ranger skill may be able to sense an attack from this dangerous creature with their sense danger ability. Make a success roll against target score 16, using ranger skill level + intelligence bonus as the baseline score. If you succeed, you'll be able to sense the hole just before it opens under your feet and jump to the side.

##### Imago

- Monster Level=5
- Rarity=14
- Agility=18    Movement Speed=10／30 (air)
- Number=One    Frequency=Very Rare
- Intellect=Low    Reaction=Neutral
- Attack Points=Arms：13 (6)    Strike Points=7
- Evasion Points=13 (6)    Defense Points=7
- Life Points／Resistance=15／13 (6)
- Mental Points／Resistance=10／12 (5)
- Special Abilities=None in particular
- Habitat=Deserts (Kahn Desert only)
- Languages=None
- Perception=Five senses

Adult giant antlions look very similar to humans, and are about the same height. They have a slender build and don't wear any clothes, but their gender can't be known. They have long blond hair that reaches down to their waist, and 2 antennae growing from their head. On their back, they have dragonfly-like wings that are 3 meters across, reminiscent of a fairy. Their wings are decorated with a pattern of dazzling blue light. They spend most of their lives in the sand as ugly larvae, and once every 100 years, when the desert becomes green again, they emerge above ground and become adults. An adult has a very short lifespan, and dies after just a few days.

#### [ Giant Crab ]

- Monster Level=5
- Rarity=12
- Agility=10    Movement Speed=10／10 (water)
- Number=One    Frequency=Rare
- Intellect=Almost none    Reaction=Hunger-based
- Attack Points=Large pincer：13 (6)／Pincer：13 (6)
- Strike Points=13／12
- Evasion Points=11 (4)    Defense Points=10
- Life Points／Resistance=20／14 (7)
- Mental Points／Resistance=7／12 (5)
- Special Abilities=Right pincer strangling; Water Adaptation
- Habitat=Warm coastal areas
- Languages=None
- Perception=Five senses

This is a huge crab with a shell that's about 2 meters wide. They usually live in the water, but sometimes search for food on land. Its weapons are its two large pincers, but the right pincer is considerably larger than the left one, and can grasp anything the size of a human torso.

Anyone hit by the right pincer of a giant crab will be caught by the pincer. This is resolved as strangling. While a giant crab is holding one person with its right pincer, it can attack another target with its left.

#### [ Worm ]

Huge and dangerous caterpillar-like creatures can sometimes be seen in Forcelia. These creatures, worms, are known to exist in several subspecies over a fairly wide range.

##### Sea Worm

- Monster Level=5
- Rarity=14
- Agility=10    Movement Speed=5／5 (water)
- Number=One to several
- Intellect=Animal
- Reaction=Hunger-based, becomes ferocious when exposed to strong light
- Attack Points=Acid：12 (5)
- Strike Points=See description
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=15／13 (6)
- Mental Points／Resistance=5／11 (4)
- Special Abilities=Acid (Strike power 10, bonus damage 5); Water adaptation
- Habitat=Deep seas
- Languages=None
- Perception=Five senses

The sea worm is a gigantic, disgusting, grub-like monster that's over 3 meters long. Its long, thick body is covered with a thick rubbery membrane and has many segments lined up in a row. Additionally, there are a large number of whip-like tentacles growing around the circular feeding mouth at the tip of its body. It is also completely omnivorous, digesting and eating anything the tentacles can catch and fit in its mouth. For this reason, they have glands in their bodies that secrete powerful digestive juices, and when in combat, they spit acidic liquid from their mouths, showering it on their opponents. Acid damage cannot be reduced by armor. Whether acid causes damage to armor (e.g., reducing defense by 1 point per exposure) is the game master's choice. Usually, it'll be easier to play the game if you don't let it affect you. Although they live in the deep sea, sea worms are sensitive to light, and will appear in shallow water when attracted by light. When they sense strong light, they'll become ferocious and continue to fight blindly until the light is completely cut off.

A sea worm will emerge from the water and directly attack whoever is holding the light. If the adventurers are quick-witted enough to turn off the light, the monster will return to the tide pool.

##### Rock Worm

- Monster Level=5
- Rarity=10
- Agility=5    Movement Speed=12／10 (underground)
- Number=One to several    Frequency=Rare
- Intellect=Animal
- Reaction=Neutral, becomes ferocious when exposed to strong light
- Attack Points=Acid：13 (6)
- Strike Points=See description
- Evasion Points=10 (3)    Defense Points=10
- Life Points／Resistance=28／15 (8)
- Mental Points／Resistance=9／13 (5)
- Special Abilities=Acid (Strike power 10, bonus damage 5)
- Habitat=Underground
- Languages=None
- Perception=Five senses

The rock worm is a member of the worm family that lives underground and looks like a giant earthworm, 5 meters long total. They feed on soil like normal earthworms, but they also eat rocks without hesitation. To do this, they secrete strong acidic digestive juices from their mouths. Similar to its relative, the sea worm, it has an extreme dislike of light. Therefore, if you come across one in an underground passage and are holding a torch or lantern, they will attack you. The attack is made using digestive juices from its mouth. This digestive juice deals strike power 10 damage plus bonus damage 5. Armor cannot reduce it.

They will not approach gold or silver, perhaps because they cannot digest them with their digestive juices. Therefore, they do not appear near veins of precious metals.

##### Sand Worm

- Monster Level=6
- Rarity=15
- Agility=10    Movement Speed=10／20 (underground)
- Number=One to several    Frequency=Rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Mouth：13 (6)    Strike Points=14
- Evasion Points=11 (4)    Defense Points=9
- Life Points／Resistance=30／17 (10)
- Mental Points／Resistance=5／12 (5)
- Special Abilities=None in particular
- Habitat=Deserts
- Languages=None
- Perception=Five senses

Sand worms are giant carnivorous worms. They usually burrow underground, but are always hungry, so when other creatures pass by on the ground, they leap out to attack them for food.

Sand worms have no growth limit and will continue to grow indefinitely. The data presented here is for a typical adult around 3 years old, and about 10 meters long. If it's a small larva, its scores will be low, and if it lives for more than 10 years and reaches a length of nearly 20 meters, it will become an even more formidable enemy.

#### [ Giant Seal ]

Giant Seals are creatures that live in the frozen seas of the north. They dive under the ice to feed on fish, so they're usually found near large ice cracks. Giant seals can also use their fins to advance over ice fields, but they do not eat land animals, so they won't attack you unless you attack them or invade their territory. They are polygamous, with one king gathering a hundred or more females to form a kingdom.

Giant seal hides are ideal material for making leather armor, so fishermen in the northern seas hunt them on large ice-sailing ships using ballistas (extra-large crane-quin crossbows). One average-sized male seal yields enough hide for around 150 people. Including the price of meat, fat (used for fuel, etc.) and tusks, the average income for one animal is 10,000 gamels.

When in combat on ice, characters suffer a -2 penalty to attack and evasion due to poor footing. This means that the characters must be equipped with ice-proof shoes, etc., otherwise combat actions, etc. will be almost impossible.

If a character falls prone due to being hit by a giant seal, they will slide about 10 meters on the ice as they are.

##### Female

- Monster Level=5
- Rarity=10
- Agility=10    Movement Speed=10／17 (water)
- Number=Several to over a hundred    Frequency=Moderate
- Intellect=Animal    Reaction=Neutral
- Attack Points=Ram：13 (6)    Strike Points=12
- Evasion Points=11 (4)    Defense Points=9
- Life Points／Resistance=20／14 (7)
- Mental Points／Resistance=10／12 (5)
- Special Abilities=Ice adaptation; Water adaptation; Strong to cold
- Habitat=Ice fields
- Languages=None
- Perception=Five senses

Female giant seals are slightly smaller than males, measuring 6 to 7 meters long and do not have tusks. Although young females may wander alone, they usually belong to a kingdom. Fishermen never choose to hunt females, out of fear that seal numbers will decline.

##### Male

- Monster Level=6
- Rarity=10
- Agility=10    Movement Speed=10／16 (water)
- Number=One    Frequency=Moderate
- Intellect=Animal    Reaction=Neutral
- Attack Points=Ram：14 (7)    Strike Points=15
- Evasion Points=12 (5)    Defense Points=10
- Life Points／Resistance=24／16 (9)
- Mental Points／Resistance=10／13 (6)
- Special Abilities=Ice adaptation; Water adaptation; Strong to cold
- Habitat=Ice fields
- Languages=None
- Perception=Five senses

Male giant seals are 7 to 8 meters long and have large tusks. When they reach a certain age, they fight their father, the king, for ownership of the females. Most are defeated in combat and driven from their kingdom, leaving them to wander aimlessly across the ice fields. Fishermen hunt them.

Only the strongest of the males can win their battle, and become the new king. The king commands at least a hundred females, and fights bravely against any intruders in his kingdom. The king has 1-2 more strike points than a regular male, and 30 more life points. It is said that there are several of these giant seal kingdoms in the frozen seas of the north.

##### Golden Wanderer

- Monster Level=6
- Rarity=12
- Agility=10    Movement Speed=10／16 (water)
- Number=One    Frequency=Very rare
- Intellect=Animal    Reaction=Neutral
- Attack Points=Ram：14 (7)    Strike Points=15
- Evasion Points=12 (5)    Defense Points=10
- Life Points／Resistance=30／17 (10)
- Mental Points／Resistance=10／13 (6)
- Special Abilities=Ice adaptation; Water adaptation; Strong to cold
- Habitat=Ice fields
- Languages=None
- Perception=Five senses

Among giant seals, one in every thousand males may be born with a mutation that results in golden skin. Although these mutants are larger than normal males, they're incapable of reproduction, so they never become kings and invariably roam the ice fields. This rare seal is called the golden wanderer, and its skin can sell for tens of times more than the skin of a normal seal. A fisherman who catches a golden wanderer is highly respected by their peers.

#### [ Snake ]

There are many different types of snakes in Forcelia. Here we will introduce four types of potentially dangerous monsters.

##### Viper

- Monster Level=2
- Rarity=7
- Agility=12    Movement Speed=12
- Number=One    Frequency=Moderate
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：9 (2)    Strike Points=7+poison
- Evasion Points=10 (3)    Defense Points=5
- Life Points／Resistance=12／10 (3)
- Mental Points／Resistance=5／8 (1)
- Special Abilities=Poison (Toxicity score 9, death in 1 hour)
- Habitat=Woods, deserts, other
- Languages=None
- Perception=Five senses

A viper is a poisonous snake about 2 meters long. They attack indiscriminately if they are hungry, making them the most feared among travelers in Alecrast. Its fangs are poisonous, and those bitten must succeed on a life force resistance roll against target score 9 or die from the poison after one hour.

##### Python

- Monster Level=4
- Rarity=8
- Agility=9    Movement Speed=12
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Strangle：12 (5)    Strike Points=10
- Evasion Points=9 (2)    Defense Points=8
- Life Points／Resistance=20／13 (6)
- Mental Points／Resistance=8／11 (4)
- Special Abilities=Strangling
- Habitat=Forests, meadows
- Languages=None
- Perception=Five senses

A python is a giant snake that can reach up to 10 meters in length. When it attacks its prey, it entangles it with its body and tries to strangle it to death. This attack resolves as strangling. They are not poisonous.

##### Hypnopython

- Monster Level=4
- Rarity=12
- Agility=9    Movement Speed=12
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Fangs：11 (4)    Strike Points=8
- Evasion Points=9 (2)    Defense Points=7
- Life Points／Resistance=18／13 (6)
- Mental Points／Resistance=10／11 (4)
- Special Abilities=Hypnotism (Resist target score=11)
- Habitat=Meadows, underground labyrinths, caves
- Languages=None
- Perception=Five senses

This is a python with a body length of 8 meters. In combat, they dance by twisting their bodies, attempting to hypnotize their foes with their movements. Those who see a Hypnopython's dance must succeed on a mental power resistance roll against target score 11, or they will be hypnotized, unable to move or think. This hypnotic state lasts as long as the hypnopython dances within your view, so if there's no one around to help you, you will be swallowed by the python without resistance. A python can attack and evade without penalty while dancing.

Treat hypnotism the same as magic that belongs to mind. You can also stop it by blindfolding the target to prevent them from seeing the dance, or by forcing the hypnopython to stop dancing. If the python takes damage, it'll stop dancing for one round, allowing those affected by the dance to return to their senses. However, starting on the next round, they will begin dancing again.

##### Sea Serpent

- Monster Level=6
- Rarity=12
- Agility=11    Movement Speed=9／20 (water)
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Strangle：14 (7)    Strike Points=13
- Evasion Points=11 (4)    Defense Points=9
- Life Points／Resistance=23／15 (8)
- Mental Points／Resistance=10／13 (6)
- Special Abilities=Strangling; Water adaptation
- Habitat=Rock crevices and caves in reef areas
- Languages=None
- Perception=Five senses

The sea serpent is a giant snake that often lives among reefs, and its whole body is covered with hard scales. Their body length starts at 10 meters, but it's said that some can reach over 20 meters.

#### [ Spider ]

Alecrast is home to the following dangerous spiders.

##### Giant Spider

- Monster Level=1
- Rarity=6
- Agility=12    Movement Speed=10
- Number=One to several    Frequency=Moderate
- Intellect=Almost none    Reaction=Hunger-based
- Attack Points=Fangs：8 (1)    Strike Points=6
- Attack Points=String：7 (0)    Strike Points=Special
- Evasion Points=9 (2)    Defense Points=3
- Life Points／Resistance=10／8 (1)
- Mental Points／Resistance=1／7 (0)
- Special Abilities=Capture with string; Mental attack immunity
- Habitat=Forests, underground labyrinths
- Languages=None
- Perception=Five senses (Vibration sense)

Giant spiders are large spiders with a body length of about 50 cm. They usually feed on small animals such as rabbits, but if they can't stand their hunger they may attack larger creatures than themselves such as humans, etc. They do not build webs, nor are they poisonous.

Giant spiders attack their prey by shooting sticky string at it. If hit by the string attack, an adventurer will become entangled and lose their freedom of movement. Escaping from this should be resolved the same way as strangling. The giant spider will bite the opponent with its fangs and attempt to suck out their fluids. An entangled opponent suffers a -4 penalty to evasion speed (points).

##### Giant Tarantula

- Monster Level=4
- Rarity=12
- Agility=14    Movement Speed=14
- Number=One    Frequency=Rare
- Intellect=Almost none    Reaction=Hunger-based
- Attack Points=Fangs：11 (4)    Strike Points=8+poison
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=17／12 (5)
- Mental Points／Resistance=5／10 (3)
- Special Abilities=Poison (Toxicity score 12, Dance=-4 to attack and evasion, 1 damage every 10 minutes, lasts for 1 hour); Mental attack immunity
- Habitat=Deserts, meadows
- Languages=None
- Perception=Five senses

This is a hairy spider with legs up to 2 meters long, and does not build webs.

A giant tarantula's fangs contain a poison (toxicity score 12) that affects motor nerves. Those who are dealt damage by these fangs, and fail a life force resistance roll, will begin to dance violently. While dancing, you'll suffer a -4 penalty on attack and evasion, and cannot use ancient magic or spirit magic. If the poison is not removed using the holy magic Cure Poison, etc. the victim will continue dancing for one hour, losing 1 point of life force every 10 minutes due to fatigue. This damage cannot be reduced by adventurer level.

##### Giant Webspinner

- Monster Level=6
- Rarity=12
- Agility=14    Movement Speed=14
- Number=One    Frequency=Rare
- Intellect=Almost none    Reaction=Violent
- Attack Points=Fangs：13 (6)    Strike Points=16
- Attack Points=String：14 (7)    Strike Points=Special
- Evasion Points=13 (6)    Defense Points=8
- Life Points／Resistance=25／16 (9)
- Mental Points／Resistance=8／13 (6)
- Special Abilities=Capture with web (Sense and escape target score=13); Entangling with string; Mental attack immunity
- Habitat=Deep inside dark forests, large rooms in underground labyrinths
- Languages=None
- Perception=Five senses (Vibration sense, no vision)

This is a huge spider, 3 meters long with legs that are 4 meters long. They build their nests in their habitat with sturdy webs several cm thick. They usually stay in one corner of the nest, but if an intruder gets caught in their web, they will attack. They will not attack anyone who has not touched their web.

To safely pass through a giant webspinner's nest without touching the surrounding webs, you must succeed on a success roll against target score 13 using adventurer level + agility bonus as the baseline score. If you fail, you will get caught in the web and attract the attention of the giant webspinner. The web is highly sticky, so much that it entangles the body, and anyone caught in it will suffer a -4 penalty to their attack and evasion, and will be unable to use ancient magic. To shake free from the web, you must succeed on a success roll against target score 13 using adventurer level + strength bonus (for monsters, use monster level) as the baseline score.

When a giant webspinner is hungry, it'll suddenly bite you with its fangs. When it's not, it'll emit a large amount of string from its abdomen and use its legs to try to entangle its prey. Those hit by a giant webspinner's string will not suffer any damage, but they will become more and more entangled in the string. Therefore, the target score of the success roll required to shake free from the web also increases by 2 points, to 15, 17…… etc. If the target score is 13 or more above than the baseline value, the prey will be completely enwrapped and unable to move. This allows a giant webspinner to hang its prey alive but deprived of freedom in its nest, then eat it whenever it wants.

A giant web spinner's webs are not affected by fire or acid.

#### [ Octopus ]

An octopus is a sea-dwelling mollusk that uses its eight tentacles to entangle and strangle its prey to death. On rare occasions, they may come ashore, in which case they suffer a -4 penalty to hit and evasion.

There are many different types of octopus, but most of them are small and harmless. Here we will only explain the two dangerous types known as killer and giant.

##### Killer Octopus

- Monster Level=3
- Rarity=13
- Agility=12    Movement Speed=3／15 (water)
- Number=One    Frequency=Moderate
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Strangle：10 (3)    Strike Points=8
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=17／11 (4)
- Mental Points/Resistance=6／10 (3)
- Special Abilities=Strangling; Water adaptation
- Habitat=Sunken ships, underwater ruins
- Languages=None
- Perception=Five senses

The killer octopus is an aggressive octopus with tentacles up to 2 meters long. They kill and eat large fish, but they also attack human swimmers.

A killer octopus will use all of its tentacles to attack one target, constricting the opponent with its entire body. Please follow the rules for strangling.

##### Giant Octopus

- Monster Level=7
- Rarity=12
- Agility=10    Movement Speed=5／20 (water)
- Number=One    Frequency=Very Rare
- Intellect=Animal    Reaction=Hunger-based
- Attack Points=Strangle (8 times)：16 (9)    Strike Points=16
- Evasion Points=12 (5)    Defense Points=9
- Life Points／Resistance=50／21 (14)
- Mental Points／Resistance=10／14 (7)
- Special Abilities=Strangling
- Habitat=Seas
- Languages=None
- Perception=Five senses

The giant octopus is almost legendary, feared by fishermen and sailors as the devil of the sea. Its tentacles, which are up to 10 meters long, can entangle boats and sink them.

A giant octopus can use each of its eight tentacles to perform a strangling attack on separate targets. If you deal 5 or more points of damage (14 or more points of damage if defense points are taken into account) to a giant octopus with a bladed weapon, you'll have cut off one of its tentacles, and the octopus' number of attacks will be reduced by one.

### 13.2.8 Plants

#### [ Creeping Tree ]

- Monster Level=2
- Rarity=10
- Agility=11    Movement Speed=12
- Number=One    Frequency=Rare
- Intellect=None    Reaction=Violent
- Attack Points=Tentacles：9 (2)    Strike Points=5
- Evasion Points=8 (1)    Defense Points=6
- Life Points／Resistance=25／12 (5)
- Mental Points／Resistance=ー／10 (3)
- Special Abilities=Strangling; Mental attack immunity; Weak to fire
- Habitat=Forests, meadows, human villages rarely
- Languages=None
- Perception=Magic

Creeping trees do not have roots underground, but move around on the ground using their roots like imitation toes. They then use their tentacle-like branches to prey on animals that approach. Tentacle attacks are resolved the same way as strangling. When it stands still, it looks like an old oak tree covered in vines.

Since it is a plant, it is weak against fire attacks, and when using spells such as Fire Weapon and Fire Bolt, you gain a +10 bonus to the usual strike power of spells. However, they do not have human-like minds, so spells that cause mental effects have no effect at all.

#### [ Ethnoa ]

- Monster Level=3
- Rarity=18
- Agility=14    Movement Speed=0
- Number=One to several    Frequency=Rare
- Intellect=None    Reaction=Violent
- Attack Points=Tentacles：9 (2)    Strike Points=5
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=19／12 (5)
- Mental Points／Resistance=ー／11 (4)
- Special Abilities=Capture with tentacles; Digest (Swallow whole); Mental attack immunity; Weak to fire
- Habitat=Woods
- Languages=None
- Perception=Magic

An ethnoa is a plant about 3 meters tall, with six tentacles and a large, open-mouthed pouch. Each tentacle is about 4 meters long, and will wrap around anything that comes near, and throw it into the pouch. The pouch contains a strong acid, which dissolves its prey. An ethnoa can attack using all six tentacles at the same time, but it can use only two against a single target. If an adventurer is hit by an ethnoa's tentacles, they will suffer damage and also become entangled in the tentacles. On the next round, you must make a resistance roll using adventurer level + strength bonus as the baseline score and the ethnoa's attack points (or the final score from when the attack hits) as the target score. If you fail, the poor adventurer is thrown into the pouch that makes up the bulk of the body. If you're unfortunate enough to be entangled by two tentacles, you must make two resistance rolls and succeed on both.

Those thrown into the pouch will suffer strike power 10 damage plus bonus damage 3 each round, starting on the next round. Against this acid damage, only adventurer level helps damage reduction, and armor defense power is completely ineffective.

While the victim is still conscious, they can attack from within using a dagger, shortsword, or similar small bladed weapon. This attack suffers a -4 penalty to hit. However, the damage dealt is as per the normal rules. The victim cannot escape from inside unless the ethnoa dies.

There may be cases where the property of former victims remains undigested inside the ethnoa's pouch. It's a low probability for these treasures to remain, but their value is usually around 100 to 1000 gamels per creature.

#### [ Killer Creeper ]

- Monster Level=3
- Rarity=12
- Agility=5    Movement Speed=0
- Number=One    Frequency=Rare
- Intellect=None    Reaction=Violent
- Attack Points=Vine：10 (3)    Strike Points=7
- Evasion Points=9 (2)    Defense Points=6
- Life Points／Resistance=30／14 (7)
- Mental Points／Resistance=ー／11 (4)
- Special Abilities=Strangling; Mental attack immunity; Weak to fire
- Habitat=Woods
- Languages=None
- Perception=Magic

A killer creeper is a vine. This vine can crawl on the ground and if there are trees, etc. it can attach itself to them and grow. A single vine may grow over a radius of several tens of meters.

If an animal, etc. steps into a killer creeper thicket, the killer creeper will attack them by entangling its vines around them. It'll then strangle the animal to death. The corpse is eventually returned to the soil to provide nourishment for the killer creeper.

If a ranger or sage succeeds on a success roll against target score 12 using ranger／sage skill level + intelligence bonus as the baseline score, they will be able to see the killer creeper's true identity before it approaches, and thus avoid the encounter (this is considered a use of plant and animal check and monster check). If they fail, the adventurer will have stepped into the killer creeper without realizing it. This is always a surprise attack, so for one round, only the killer creeper can attack. The adventurer's evasion will suffer a -4 penalty.

A killer creeper attacks by entangling with its vines. There is an immeasurable number of these vines, but only three vines can attack a single target at the same time. If the killer creeper's attack hits, the vines will entangle the target. Entangled vines automatically deal damage in subsequent rounds without requiring a hit check. Also, characters who are entangled in the vines will suffer a penalty on attack and evasion from then on. If you're entangled in one, this is -2, and if you're entangled in two or more, it's -4.

A character entangled in two or more vines cannot use ancient magic or spirit magic, because they're unable to move. However, holy magic can be used freely.

A character entangled in vines can also attempt to pull the entangled vines off instead of making a normal attack. Make a success roll using adventurer level + strength bonus as the baseline score and the killer creeper's attack points (10, or the final score from when the attack hit) as the target score. If successful, you can pull off the vines. If entangled in multiple vines, you must make separate checks for each. When you pull the vines off, 1 point of damage per vine is dealt to the killer creeper's life points.

#### [ Mandrake ]

- Monster Level=5
- Rarity=16
- Agility=8    Movement Speed=8
- Number=One to several    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Barehanded：12 (5)    Strike Points=7
- Evasion Points=12 (5)    Defense Points=7
- Life Points／Resistance=14／13 (6)
- Mental Points／Resistance=12／13 (6)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=12／5, gnome, dryad only); Scream (Resist target score=12, once per day); Mental attack immunity; Weak to fire
- Habitat=Forests
- Languages=Silent spirit
- Perception=Five senses (infravision)

A mandrake is a plant with human-shaped roots, and when it's young, it grows underground like a normal plant, but in the seventh year after its seeds are sown, it crawls out from the soil and begins walking around the forest. It looks like an even uglier version of a goblin, with long leaves growing out of its head instead of hair. Despite being plants, they have some intellect and can use spirit magic sourced from the power of dryad and gnome.

When a mandrake is hurt, it makes a terrifying scream. A Mandrake can only scream once per day. Anyone who hears this at close range without first wearing earplugs must make a mental power resistance roll against target score 12. If you fail, you cannot attack or cast spells for one full round, and you suffer a -4 penalty to evasion. At this time, if you roll double ones on your resistance roll, you will immediately go insane and become disabled.

Additionally, those who fail the resistance roll must make another one, this time a life force resistance roll against target score 12. If you fail, you will lose your hearing. At this time, if you roll double ones on the resistance roll, your life force will instantly become zero.

Young Mandrake root is prized as an ingredient for sedatives, stimulants, and poisons. For this reason, humans often find and dig up young mandrakes. Young mandrakes scream like their parents, but they're small and unable to move or cast spells, making them easy to kill. Therefore, mandrakes deeply hate humans.

#### [ Alraune ]

- Monster Level=6
- Rarity=16
- Agility=14    Movement Speed=14
- Number=One    Frequency=Very Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Barehanded：13 (6)    Strike Points=8
- Evasion Points=14 (7)    Defense Points=8
- Life Points／Resistance=14／14 (7)
- Mental Points／Resistance=18／15 (8)
- Special Abilities=4th level spirit magic (Magic Intensity／Magic Power=13／6, gnome, dryad only); Scream (Resist target score=13, once per day); Mental attack immunity
- Habitat=Human villages
- Languages=Silent spirit
- Perception=Five senses (infravision)

If you feed a young mandrake root with human blood and nurture it, it will grow to look exactly like a human. This is called an alraune. They cannot grow with the blood of fae, youma, etc. Alraune look exactly like humans, and can speak and think like humans, but when they are wounded, a thick, red mucus oozes out of them. When hurt, it'll let out a scream with the same effect as that of a mandrake's. The target score for resisting an alraune's scream is 13.

Alraune are also naturally able to use spirit magic, which is sourced from the power of dryad and gnome.

It is said that the appearance and personality of an alraune will resemble that of the first human who gave it blood. If raised with the blood of a ruthless criminal, a ruthless alraune will be born. Since alraune are an artificial variety, they have no fertility. Also, they do not have a weakness to fire, which is the weakness of plant-type monsters.

#### [ Bloody Petal ]

This plant, which has huge red flowers that resemble the color of human blood, is called blood flower, but is sometimes also called man-eating flower, which more clearly describes its characteristics.

This plant can grow up to about 10 meters in height. The stem has 2 to 5 bud-shaped flowers about 1 meter in diameter. When a creature such as a human, etc. approaches, the folded flower stalks extend out and the buds open to envelop their prey. The flower stalks grow to about 10 meters long.

##### Flower

- Monster Level=6
- Rarity=11
- Agility=10    Movement Speed=0
- Number=One    Frequency=Very Rare
- Intellect=None    Reaction=Adversarial
- Attack Points=Flower：11 (4)    Strike Points=7
- Evasion Points=13 (6)    Defense Points=8
- Life Points／Resistance=1／12 (5)
- Mental Points／Resistance=ー／14 (7)
- Special Abilities=Strangling; Mental attack immunity; Weak to fire
- Habitat=Forests
- Languages=None
- Perception=Magic

This flower's attack strangles the character and deals damage. When the prey dies, the flower reverts back to a bud and finishes absorbing nutrients in about one week. If the prey escapes with all their might, the flower becomes torn and unusable, and will eventually wither.

##### Body

- Monster Level=6
- Rarity=11
- Agility=10    Movement Speed=0
- Number=One    Frequency=Very Rare
- Intellect=None    Reaction=Adversarial
- Attack Points=ー    Strike Points=ー
- Evasion Points=11 (4)    Defense Points=9
- Life Points／Resistance=20／15 (8)
- Mental Points／Resistance=ー／14 (7)
- Special Abilities=Mental attack immunity; Weak to fire
- Habitat=Forests
- Languages=None
- Perception=Magic

Adventurers can also attack the body. If the body's life points reach 0, the flower will also cease activity.

#### [ Fungus ]

- Monster Level=8
- Rarity=15
- Agility=7    Movement Speed=7
- Number=One to several    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Barehanded：15 (8)    Strike Points=11
- Evasion Points=15 (8)    Defense Points=10
- Life Points／Resistance=17／16 (9)
- Mental Points／Resistance=9／15 (8)
- Special Abilities=Toxic spores (Toxicity score 16, illusions as well as turning into a fungus)
- Habitat=Damp, dark places
- Languages=Regional
- Perception=Pseudo

A fungus is a mass of mushrooms shaped like a human, or rather, a human whose entire body is covered in mushrooms. They quietly lurk in forests, etc. killing animals and humans that pass by, and absorbing nutrients from the corpses. They cannot survive for long in dry or sunny areas.

Fungus release toxic spores (toxicity score 16) when injured. While fighting a fungus, anyone within a 5 meter radius may inhale the spores. After combat, they must make a life force resistance roll against target score 16, and those who fail will then have mushrooms growing all over their bodies after 24 hours. No matter how many you cut off, there will be no end. Gradually, your sense of humanity will fade and you'll begin to suffer from hallucinations. To cure this, use the holy magic Cure Poison or the spirit magic Restore Health. When the spell is cast, if the caster's final score is 16 or greater, it will be healed.

If one week elapses without treatment, the character will turn into a fungus. Those who have completely become a fungus cannot be cured with the holy magic Cure Poison nor the spirit magic Restore Health. They can only be restored to their original state by using the holy magic Refresh.

### 13.2.9 Undead

#### [ Buau Zombie ]

- Monster Level=Based on previous
- Rarity=16
- Agility=Half of previous    Movement Speed=Half of previous
- Number=Several to dozens    Frequency=Rare
- Intellect=Low    Reaction=Command-based
- Attack Points=／Strike Points／Evasion Points／Defense Points=Based on previous
- Life Points／Resistance=Based on previous／Based on previous
- Mental Points／Resistance=ー／Based on previous
- Special Abilities=Retains previous abilities; Mental attack immunity; Not affected by poison and illness; Damage from healing magic
- Habitat=Various
- Languages=Based on previous
- Perception=Pseudo

These are undead created by the lost spell Create Buau Zombie. Unlike normal zombies, they possess intellect, albeit low, and can make independent decisions and follow the commands of their creator. Therefore, they will do their best to obey even abstract commands (for example, sneak into a house and steal something, etc.). They can also use tools such as weapons, armor, etc..

Unlike zombies, they decay slowly and can work for decades to centuries. Strength and life force are kept at their original scores, but dexterity, agility, and intelligence are reduced to half of what their scores were before death, and mental power is completely lost. All magic and bard skill spellsong abilities cannot be used once you become a buau zombie. Attack, defense, etc. are performed at their previous level (fighter, thief, etc.). Game masters should be aware of changes due to ability scores (reduced dexterity and agility). Monster level is the same as their previous adventurer level.

Buau zombies are mindless beings, so spells that cause mental effects on them are ineffective.

#### [ Skeleton ]

- Monster Level=1
- Rarity=10
- Agility=14    Movement Speed=14
- Number=Several to dozens    Frequency=Frequent
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Weapon：8 (1)    Strike Points=4
- Evasion Points=9 (2)    Defense Points=3
- Life Points／Resistance=7／8 (1)
- Mental Points／Resistance=ー／9 (2)
- Special Abilities=Bladed weapons cannot critical; Mental Attack Immunity; Not affected by poison and illness; Damage from healing magic
- Habitat=Ruins
- Languages=None
- Perception=Pseudo

A skeleton, as the name suggests, is a moving skeleton, created by ancient magic or dark magic. Its weapon is usually the one it used before its death. Typically this is a one-handed sword with a shield. In most cases, however, its armor will be worn out and unusable. Due to their characteristic lack of flesh, bladed weapons cannot deal additional critical damage to skeletons. Also, since they have no intelligence, magic that produces mental effects will not work on them.

#### [ Zombie ]

- Monster Level=1
- Rarity=9
- Agility=7    Movement Speed=7
- Number=Several to dozens    Frequency=Frequent
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Barehanded：8 (1)    Strike Points=4
- Evasion Points=8 (1)    Defense Points=3
- Life Points／Resistance=19／10 (3)
- Mental Points／Resistance=ー／9 (2)
- Special Abilities=Mental attack immunity; Not affected by poison and illness; Damage from healing magic
- Habitat=Ruins
- Languages=None
- Perception=Pseudo

Zombies, along with skeletons, are representative undead, and are created from corpses by ancient magic and dark magic. However, unlike skeletons, they do not use weapons or armor. Since they have no intelligence, mental attacks have no effect at all.

#### [ Ash ]

- Monster Level=2
- Rarity=11
- Agility=9    Movement Speed=8
- Number=Several    Frequency=Moderate
- Intellect=Almost none    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=ー    Defense Points=ー
- Life Points／Resistance=7／9 (2)
- Mental Points／Resistance=ー／10 (3)
- Special Abilities=Wrap (Evasion target score=10, strike power 10, bonus damage 2); Mental attack immunity; Weapon immunity; Fire immunity; Not affected by poison and illness; Damage from healing magic
- Habitat=Ruins
- Languages=None
- Perception=Magic

An ash is an undead created from the ashes of a burned corpse using ancient magic and dark magic. It's usually spread out on the ground like sand, but if something living approaches it, it will suddenly fly up as if blown by the wind, take the form of a human, and attack. Due to the ash's physical characteristics, attacks with weapons, etc. cannot be used at all. Also, since it's already been burned once, fire has no effect on it at all. It's possible to damage an ash's life points with damage magic other than fire-type. Also, since it does not have a mind, attacks that affect the mind are also ineffective.

An ash's attacks also do not deal direct damage. The Ash wraps itself around the target creature and attacks it. The target of the attack must make a success roll using adventurer level + agility bonus as the baseline score, and if they fail, they will inhale a portion of the ash. Every round thereafter, they must make a life force resistance roll against target score 10. As long as you continue to fail, you will suffer strike power 10 damage and 2 plus bonus damage 2 every round. This damage can only be reduced by adventurer level.

If you cast the spirit magic Missile Protection, you can protect yourself from being enwrapped by the ash. However, this magic will not work in time for characters who are already enwrapped by the ash. If you cast Turn Undead and the result is crumble away, the ash will cease activity.

#### [ Ghoul ]

- Monster Level=3
- Rarity=10
- Agility=14    Movement Speed=14
- Number=Several to dozens    Frequency=Moderate
- Intellect=Low    Reaction=Adversarial
- Attack Points=Fangs：10 (3)／Claw：11 (4)／Claw：11 (4)
- Strike Points=9+poison／8+poison／8+poison
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=14／11 (4)
- Mental Points／Resistance=10／10 (3)
- Special Abilities=Poison (Toxicity score 10, paralysis, lasts 1 day); Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Ruins, graveyards
- Languages=Those previous
- Perception=Pseudo

Ghouls are undead who scavenge and eat corpses. However, perhaps because killing and eating are the same thing, they often attack living things as well. Ghouls have paralyzing poison in their claws and fangs, and a character who suffers damage must succeed on a life force resistance roll against target score 10 or they will be paralyzed at the end of the next round. This paralysis lasts for one day.

#### [ Sin ]

- Monster Level=4
- Rarity=14
- Agility=14    Movement Speed=14
- Number=One to several    Frequency=Very Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Weapon：11 (4)    Strike Points=10
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=16／12 (5)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=Life point regenerate (3 points per round); Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Various
- Languages=Those previous
- Perception=Pseudo

Sin are a very special type of undead. A soul of someone who was greatly possessive in life will become undead as a sin. They remain in this world, trying to monopolize what they were attached to even after death. Their appearance remains the same as when they were alive, and other than their abnormally pale skin and cloudy eyes, they are no different from a normal human (however, their clothes may be tattered depending on the number of years since their death).

A sin usually refuses to leave the side of whatever it's attached to, and will attack anything that tries to take it away. Sin have no intelligence. They are driven only by an insatiable desire for possession, and are, so to speak, the dead who have fallen into madness and cannot be saved.

#### [ Wight ]

- Monster Level=4
- Rarity=12
- Agility=14    Movement Speed=14
- Number=One to several    Frequency=Moderate
- Intellect=Human    Reaction=Violent
- Attack Points=Claws：12 (5)    Strike Points=9+mental damage
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=14／12 (5)
- Mental Points／Resistance=14／12 (5)
- Special Abilities=Steal mental power (Strike power 10, bonus damage 4); Normal weapon immunity; Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Ruins, graveyards
- Languages=Those previous
- Perception=Pseudo

Wights are undead that possess people and feed on the energy of others. Normal weapons have no effect against this monster. To wound a wight, you need a silver or magical weapon. A wight's weapon is its sharp claws, and those who are dealt damage will have their life energy drained at the same time. If a wight's attack hits, your life force will suffer damage as well as your mental power. The damage dealt to mental power is merely the result of a strike power 10 strike roll plus bonus damage 4. For this, you can only reduce the damage with your character's adventurer level. Those whose mental power is reduced to 0 by this attack will die immediately and will then be revived as a new wight 24 hours later.

#### [ Haunt ]

A haunt is a being such a ghost or a vengeful spirit. These are broadly classified into three types: ghosts, specters, and phantoms, but they are collectively called haunts.

Haunts are souls that have remained in this world because they have unfinished business, or held a strong grudge against others in life. They then complain about their regrets and grudges to any third party they happen to encounter. If you can clear up those lingering regrets and grudges, they will cease to exist. A special case, however, is when one resents its own death itself and harbors hatred toward all living things. Such haunts are always hostile and attack all creatures they encounter, with intent to kill.

Haunts have a minimum monster level of 5, but if they had a higher adventurer level in life, or if they died harboring a particularly strong grudge, their level will be higher.

A special ability common to all haunts is possess. This is the act of taking over the body of a living being and using it for one's own purposes. If a haunt finds that a creature it comes into contact with does not sympathize with its feelings, it may attempt to possess them. The target of the possession must attempt a mental power resistance roll. If you fail, your body will be taken over. When a haunt takes over your body, it can use your character's abilities in addition to its own previous skills. Once you successfully resist, there is no danger of being possessed by the same haunt again. There's also 6th level holy magic called Exorcism. If you cast this magic, you will be freed from the haunt's possession. If a body is destroyed after being possessed, the haunt will become a phantom and be bound in place.

##### Ghost

- Monster Level=5
- Rarity=14
- Agility=14    Movement Speed=14
- Number=One, rarely multiple depending on the situation
- Frequency=Rare    Intellect=Human
- Reaction=Friendly, however, some are extremely adversarial
- Attack Points=Weapon：12 (5)    Strike Points=10
- Evasion Points=13 (6)    Defense Points=7
- Life Points／Resistance=14／13 (6)
- Mental Points／Resistance=20／14 (7)
- Special Abilities=Possess (Resist target score=12); Has previous skills; Bladed weapons cannot critical (Skeleton type); Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Various
- Languages=Those previous
- Perception=Pseudo

A ghost is a moving being whose corpse still holds a lingering grudge. Depending on how long ago they died, they can look like zombies (rotting corpses) or skeletons (moving skeletons). Their strength varies considerably depending on which abilities they had in life. The scores listed here are averages. All ability scores ​​will be the same as previous, except for mental power. Mental power is the only one that's previous + 6. They have all the skills they had previously. Those who had rune master skills can use magic of that level and magic power. However, they cannot use holy magic (but they can use dark magic). Also, to use ancient magic, they will still need a magical catalyst (such as a magic wand).

If a ghost's corpse is destroyed, it will always attempt to possess someone nearby. If this fails, it'll become a phantom (see below) and be bound in place. Even after becoming a phantom, it'll attempt to possess if given the chance.

When its lingering regrets and grudges are cleared, or when its mental points are reduced to 0 or less due to a Shade, etc. the ghost will vanish, leaving only a crumbled corpse behind.

When attacking a ghost in the form of a skeleton with a weapon, you cannot deal additional critical damage with a bladed weapon.

##### Specter

- Monster Level=5
- Rarity=14
- Agility=24    Movement Speed=24 (air)
- Number=One, rarely multiple depending on the situation
- Frequency=Rare    Intellect=Human
- Reaction=Friendly, however, some are extremely adversarial
- Attack Points=ー    Strike Points=ー
- Evasion Points=ー    Defense Points=ー
- Life Points／Resistance=ー／ー
- Mental Points／Resistance=20／14 (7)
- Special Abilities=Possess (Resist target score=12); Has previous skills; Physical attacks have no effect; Sleepless
- Habitat=Various
- Languages=Those previous
- Perception=Pseudo

A specter is a very troublesome entity, a grudge that has lost its physical body and remains in this world. The faint, transparent appearance it had in life takes on the form of a hazy shadow. Since it does not have a physical body, attacks such as weapons and damage magic are ineffective, and the only effective countermeasure is magic that has a mental effect. Those who had rune master skills previously can use magic. However, holy magic cannot be used. A magical catalyst is not required when using ancient magic. Also, after performing possession, they can freely use the skills they had previously.

When a specter's regrets or grudges are cleared, or when its mental points are reduced to 0 or less due to Shade, etc. it'll vanish.

##### Phantom

- Monster Level=5
- Rarity=14
- Agility=24    Movement Speed=0
- Number=One, rarely multiple depending on the situation
- Frequency=Rare    Intellect=Human
- Reaction=Friendly, however, some are extremely adversarial
- Attack Points=ー    Strike Points=ー
- Evasion Points=ー    Defense Points=ー
- Life Points／Resistance=ー／ー
- Mental Points／Resistance=ー／13 (6)
- Special Abilities=Possess (Resist target score=12); Most attacks immunity
- Habitat=Various
- Languages=Those previous
- Perception=Magic

A phantom is a being who by now is merely a grudge bound to a specific place, object, etc. They have almost no power to interfere with others, but it's impossible to counter them through normal means. Even Turn Undead has no effect on Phantoms. Only Exorcism and Save Soul can be expected to be effective.

A phantom's appearance is the same as a specter. It can also communicate its intentions while disappearing. At this time, it may cause rapping sounds or poltergeist phenomena.

A phantom has lost all of the skills it had previously. After possessing, it can only use the abilities of that body.

If you clear up its regrets and grudges, the phantom will vanish.

#### [ Jack-O-Lantern ]

- Monster Level=6
- Rarity=11
- Agility=18    Movement Speed=18 (air)
- Number=One to several    Frequency=Rare
- Intellect=High    Reaction=Adversarial
- Attack Points=Fangs：13 (6)    Strike Points=12
- Evasion Points=16 (9)    Defense Points=10
- Life Points／Resistance=14／14 (7)
- Mental Points／Resistance=21／15 (8)
- Special Abilities=6th level dark magic (Magic Intensity／Magic Power=16／9); Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Above swamps or ponds
- Languages=Regional
- Perception=Pseudo

A jack-o-lantern looks like a pumpkin, the vegetable, with a yellowish-orange face about 30 cm in diameter, that floats in the air. Its face has semicircular eyes and a mouth that arch downward, and a triangular nose that points upward, as if cut with a knife. There are no eyeballs, and an evil red light can be seen deep inside the eye sockets. They often float around above swamps and ponds, and if they spot prey, they'll attack straight away. Like ghouls, they live by scavenging dead flesh, but perhaps this does not satisfy their hunger, as they frequently attack the living.

This monster has dark magic abilities.

#### [ Dullahan ]

- Monster Level=7
- Rarity=14
- Agility=16    Movement Speed=16
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon：14 (7)    Strike Points=14
- Evasion Points=15 (8)    Defense Points=12
- Life Points／Resistance=20／16 (9)
- Mental Points／Resistance=20／16 (9)
- Special Abilities=Summon chariot; Summon headless horse; Normal weapon immunity; Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Unknown, appears in towns
- Languages=Regional
- Perception=Pseudo

A dullahan is a ghost that appears as a headless knight wearing armor. The armor shines as if it were freshly made. A dullahan carries a one-handed sword and no shield, but it's no wonder, as it carries its own head in its spare hand!

A Dullahan rides a chariot pulled by a headless horse (the horse is called a headless horse and the chariot is called a chariot of dullahan) and appears late at night at the door of the house it's aiming for. Then, it knocks on the door. When a resident opens the door and looks out, the dullahan points inside the house and prophesizes death, then leaves. Around one year later, the dullahan reappears at the house, chooses one person in the house, and kills them.

A dullahan can summon its chariot and headless horse at any time and in any place. However, one (?) dullahan has only one chariot and two headless horses, and if these are defeated, they cannot be summoned again.

You can avoid a death prophesied by a dullahan by killing it the first or second time it appears. It's no use for those who have received the prophecy of death to move away. The dullahan will always appear at the place you moved to (or to one of the places moved to, if the residents have split up and moved to different places), even if it's on the sea, or in a room that's been walled off on all sides.......

A dullahan can only be wounded by silver or magical weapons.

##### Chariot of Dullahan

- Monster Level=4
- Rarity=14
- Agility=16    Movement Speed=30／30 (air)
- Number=One    Frequency=Rare
- Intellect=None    Reaction=Adversarial
- Attack Points=Ram：14 (7)    Strike Points=15
- Evasion Points=13 (6)    Defense Points=8
- Life Points／Resistance=30／15 (8)
- Mental Points／Resistance=ー／12 (5)
- Special Abilities=Normal weapon immunity; Certain weapons resistant; Mental attack immunity; Certain magic immunity; Not affected by poison and illness
- Habitat=Unknown, appears with (or summoned by) dullahan
- Languages=None
- Perception=None

A chariot ridden by a dullahan, which has the ability to fly. The chariot can also attack while moving up to a maximum of 90 meters in one round. Also, it can hit-and-run different opposing characters again and again. A dullahan riding and controlling a chariot cannot attack on its own at the same time (because it's pulling the reins with one hand and holding its head in the other). Headless horses also cannot attack while pulling a chariot.

A chariot can only be dealt damage by silver or magical weapons. Furthermore, additional critical damage cannot be dealt by swords, spears, clubs, bows, crossbows, or barehanded (with magic cast). Criticals can occur as usual with axes, maces, flails, slings, rocks, and warhammers.

In the case of magic, cold-type and poison gas-type magic is completely ineffective, but other damage magic are effective. Turn Undead has no effect. Also, healing magic cannot deal damage.

To attack a dullahan aboard a chariot, you must suffer a -2 penalty to attack power. You can attack a headless horse that is pulling a chariot normally.

When its master dullahan is defeated, or when any one of the headless horses pulling it are defeated, the chariot loses the ability to act.

##### Headless Horse

- Monster Level=4
- Rarity=14
- Agility=12    Movement Speed=30／30 (air)
- Number=Two horses    Frequency=Rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Heel：10 (3)    Strike Points=12
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=20／13 (6)
- Mental Points／Resistance=ー／12 (5)
- Special Abilities=Normal weapon immunity; Mental attack immunity; Not affected by poison and illness; Damage from healing magic
- Habitat=Unknown, appears with (or summoned by) dullahan
- Languages=None
- Perception=Magic

Headless horses are the horses that pull the chariot with a dullahan on board, and can gallop through the air. They act faithfully to their master's commands and may also attack enemies. They cannot attack while pulling the chariot, but the dullahan can freely detach the chariot from the headless horses at will.

When a headless horse's master dullahan is defeated, it loses its ability to act.

#### [ Undead Knight ]

- Monster Level=8
- Rarity=14
- Agility=14    Movement Speed=14
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon：15 (8)    Strike Points=17+mental damage
- Evasion Points=16 (9)    Defense Points=13
- Life Points／Resistance=21／17 (10)
- Mental Points／Resistance=24／18 (11)
- Special Abilities=Steal mental power (Strike power 10, bonus damage 8); Gaze (Resist target score=15, mental damage, strike power 10, bonus damage 8); Normal weapon immunity; Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Ruins, deep in the woods
- Languages=Regional
- Perception=Pseudo

An undead knight is a ghost that appears in the form of a knight wearing armor, holding a large two-handed sword. Both the sword and armor have red rust and no sheen. You can touch the armor, but apart from the glowing red eyes behind the helmet, there's nothing to be found inside. After defeating an undead knight, all that remains is an empty, rusty suit of armor and a sword.

This monster wanders around alone, making its home in places humans don't approach. This monster roams alone in inaccessible places. Based on this, some sages claim that undead knights are the mere shadows of the former holy warriors of Pharis. It is said that they fell on their journey to defeat evil, but their will to fight remained and they turned into ghosts. Naturally, the priests of Pharis deny this, while agreeing with a different claim, which is that they're sentinels created by necromancy during the ancient kingdom period.

Undead knights cannot be wounded by ordinary weapons. You will need a silver or magical weapon to defeat them. Also, if an undead knight's attack hits, the character will suffer damage to their mental power in addition to normal damage. This damage is calculated as strike power 10 plus bonus damage 8, and armor defense power is useless. Only adventurer level and magical defense effects will work.

An undead knight can similarly drain the mental power of its enemies with its gaze. As a result, anyone struck by an undead knight's gaze (even from behind) will suffer damage to their mental power. Those whose mental power is reduced to 0 due to damage from an undead knight's weapons or gaze will die instantly and will be resurrected as a wight 24 hours later. For this reason, an undead knight may be accompanied by multiple wights. These wights are sometimes specifically called squire wights.

#### [ Wraith ]

- Monster Level=8
- Rarity=14
- Agility=24    Movement Speed=24 (air)
- Number=One    Frequency=Very Rare
- Intellect=High    Reaction=Neutral
- Attack Points=ー    Strike Points=ー
- Evasion Points=ー    Defense Points=ー
- Life Points／Resistance=ー／ー
- Mental Points／Resistance=16／16 (9)
- Special Abilities=8th level ancient magic (Magic Intensity／Magic Power=18／11); Retains previous skills; Physical attack immunity; Sleepless; Instantly killed by sunlight
- Habitat=Ruins
- Languages=Those previous (always includes low ancient)
- Perception=Pseudo

A wraith is a being whose ethereal body was separated from its physical body by the ancient magic spell Wraith Form and became undead because it did not return within the spell's duration. It resembles a specter, with a vaguely transparent image of when it was alive. The scores given here are for an average wraith, and can vary considerably depending on its previous knowledge, mental power, sorcerer skill level, etc.

Attacks using weapons or damaging spells have no effect at all on wraiths, which do not have a physical body, so the only effective countermeasure is magic that has a mental effect. Although a wraith has lost all of its physical abilities, its knowledge-related abilities and rune master skills are still effective, and it can use magic. However, holy magic cannot be used (dark magic is allowed). Unlike specters, wraiths do not have the ability to possess. If its mental points become 0 due to a Mental Attack, etc. the wraith will vanish. If it's directly exposed to sunlight, it will also disappear without even attempting to resist.

#### [ Mummy ]

##### Servant

- Monster Level=6
- Rarity=14
- Agility=10    Movement Speed=14
- Number=One to several    Frequency=Rare
- Intellect=Obeys commands    Reaction=Violent
- Attack Points=Arms：14 (7)    Strike Points=8+curse
- Evasion Points=13 (6)    Defense Points=8
- Life Points／Resistance=7／13 (6)
- Mental Points／Resistance=ー／14 (7)
- Special Abilities=Curse (Resist target score=13); Mental attack immunity; Not affected by poison and illness; Damage from healing magic; Weak to fire
- Habitat=Tombs
- Languages=None
- Perception=Pseudo

A mummy is a monster transformed by a magical ritual in ancient, and is buried together in a tomb as the keeper of its master's coffin. When a miscreant such as a graverobber appears, the mummy is given the mission to awaken and attack the intruder. If a mummy's attack hits, in addition to physical damage, a curse will befall you. The character must make a mental power resistance roll against target score 13. If they fail, they will no longer be able to recover any reductions in ability scores, including life force and mental power. Let's say an adventurer under this curse is bound with a rope and the game master says, Well, you have 0 agility and are disabled. At this time, even if the adventurer's rope is broken, his agility will not recover from 0 and he will still be unable to take any action! To break this curse, the holy magic Remove Curse is required.

Also, mental magic doesn't work on a mummy. Since a mummy is dry, it's weak to fire, so fire attacks receive a +10 bonus to strike power.

##### Master Mummy

- Monster Level=9
- Rarity=15
- Agility=14    Movement Speed=14
- Number=One    Frequency=Very rare
- Intellect=High    Reaction=Adversarial
- Attack Points=Arms：17 (10)    Strike Points=16+curse
- Evasion Points=17 (10)    Defense Points=11
- Life Points／Resistance=21／18 (11)
- Mental Points／Resistance=21／18 (11)
- Special Abilities=7th level ancient magic (Magic intensity／magic power=17／10); 7th level dark magic (Magic intensity／magic power=17／10); Curse (Resist target score=16); Mummy summon; Not affected by poison and illness; Sleepless; Damage from healing magic; Weak to fire
- Habitat=Tombs
- Languages=Low ancient
- Perception=Pseudo

A Master Mummy is an ancient member of a royal family or noble who followed a ritual in ancient and sleeps in a tomb as an undead. When a graverobber, etc. places their hands on its coffin, the master mummy rises and begins to act.

If a master mummy's attack hits, in addition to physical damage, a curse will befall you. The character must make a mental power resistance roll against target score 16. If they fail, they will not recover any reductions, including life force and mental power. To break this curse, the holy magic Remove Curse is required.

It is common for 10 or more mummies to be buried together in a master mummy's coffin chamber, furthermore, the master mummy has the ability to either make an individual mummy rise, or summon new mummies from nearby. This regeneration or summoning can only be done once per round. A master mummy can use this ability while taking other actions.

Since a master mummy is dry, it's weak to fire, so fire attack checks are made at plus 10 to strike power. Any mummies, either buried with or newly summoned, will continue to be active even after the master mummy has fallen, attacking those who have harmed their master to try and get revenge.

#### [ Vampire ]

There are three types of vampires: undead king, vampire, and lesser vampire. All types prolong their eternal life by sucking the lifeblood and mental power of others. A human whose blood is sucked by these vampires will also be turned into a lesser vampire. An undead king is a supreme spirit-user of the ancient kingdom, who has turned itself into an undead being, and holds great magical power. Vampires spontaneously emerge from among the servants of the dark gods. Those who have their blood sucked or their mental power taken by these vampires become lesser vampires. Also, even if their blood is sucked by a lesser vampire, a lesser vampire will still be created.

Vampires share several common characteristics. First, vampires have pale skin and a red glow in their eyes. These red eyes cause intense fear in those who see them. Anyone who makes eye contact with a vampire must first make a mental power resistance roll. The target score varies depending on the type of vampire, but in any case, if you fail to resist, you will be paralyzed with fear and unable to act. Even if the vampire removes its gaze, this paralysis continues until it disappears.

Vampires cannot be wounded by normal weapons. To defeat them, you will need a silver or magical weapon. Also, if a vampire's attack hits a character, in addition to normal damage, mental power will also be damaged. Armor defense power is useless against this damage. Only adventurer level and magical defense power are effective. Those whose mental power is reduced to 0 by this attack will die and will be resurrected 24 hours later as a lesser vampire.

Vampires maintain their mental points by sucking human blood. Vampires who temporarily lose their mental points due to magic, etc. cannot recover them unless they suck the blood of another human or steal the mental power of another human. A vampire can suck the lifeblood of one human who cannot resist in 10 minutes, allowing them to fully recover their mental points. Those who've had their blood sucked will lose their mental points and will be resurrected as a lesser vampire in 24 hours. Vampires can also steal mental power even with normal attacks, which are directly added to the vampire's mental points (but never exceed the upper limit).

If they cannot steal mental power for one full day, they will automatically lose 1 mental point.

A vampire's negative life force has strong regenerative power, and unless it becomes 0, it will automatically regenerate at a rate of 3 points per round.

Vampires hate sunlight. When exposed to sunlight, a vampire suffers 1 point of damage to both their life points and mental points each round. Life points do not regenerate under the sun.

##### Lesser Vampire

- Monster Level=3
- Rarity=13
- Agility=14    Movement Speed=14
- Number=Several to dozens    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Barehanded：10 (3)    Strike Points=5+mental damage
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=14／11 (4)
- Mental Points／Resistance=14／11 (4)
- Special Abilities=Steal mental power (Strike power 10, bonus damage 3); Gaze (Resist target score=10, paralysis by fear); Life point regenerate (3 points per round); Normal weapon immunity; Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Various
- Languages=Those previous
- Perception=Pseudo

A lesser vampire is a monster created by the transformation of a victim whose blood has been sucked by another vampire. They will always follow the commands of the vampire that transformed them (their parents, so to speak). They have emaciated, unhealthy pale skin, and their glowing red eyes cause intense fear in those who see them. A character who makes eye contact with a lesser vampire must first resist the gaze against target score 10. If you fail, you'll be paralyzed by fear and unable to act.

A lesser vampire cannot be wounded by normal weapons. You will need a silver or magic weapon to defeat them. In addition to normal damage, a character hit by a lesser vampire's attack will also suffer damage to their mental power.

##### Vampire

- Monster Level=10
- Rarity=13
- Agility=20    Movement Speed=20／20 (air)
- Number=One to several    Frequency=Very rare
- Intellect=High    Reaction=Adversarial
- Attack Points=Barehanded：17 (10)    Strike Points=14+mental damage
- Evasion Points=19 (12)    Defense Points=12
- Life Points／Resistance=26／20 (13)
- Mental Points／Resistance=26／20 (13)
- Special Abilities=8th level dark magic (Magic intensity／magic power=18／11); Steal mental power (Strike power 10, bonus damage 10); Gaze (Resist target score=17, paralysis by fear); Retains previous skills; Life point regenerate (3 points per round); Normal weapon immunity; Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Places with unholy soil
- Languages=Those previous
- Perception=Pseudo

Vampires are servants of the dark gods or those who seem to be particularly favored by the dark gods, and are resurrected as undead after death. Most abilities they had previously are retained. Additionally, they gain the power to use dark magic up to 8th level. They'll no longer be able to use holy magic, but if they had a holy magic skill of 9th level or greater, they'll be able to use dark magic at the same skill level. The scores given here are for an average vampire and will vary depending on the ability scores it had previously. If you take that into account, its dexterity, agility, intelligence, and strength will be previous +6, and its life force and mental power will be previous +12. Vampires have the ability to move while floating in the air.

Apart from the difference in scores and magical power already shown, a vampire's abilities, weaknesses and ecology are similar to those of a lesser vampire.

A vampire's negative power is strongly connected to the soil called unholy soil. If the vampire's life points become 0, or if its body crumbles away as a result of a "Turn Undead" spell being cast on it, the vampire's form will vanish into mist, but in one day it'll completely regenerate in its soil location. Vampires can also turn into mist at their own will before their life points reach 0, and regenerate in a place with soil. Even if their movement is blocked by magic such as Paralyze, etc. they can still turn into a mist.

If discovered by an adventurer, etc. while regenerating in a location with soil, a vampire will not be able to take its physical form. It'll remain a mist.

While a vampire is a mist, it cannot be wounded by sunlight or any other attack. The mist will eventually fade and the characters will no longer be able to see it.

Many vampires preserve this "soil" by preparing a coffin and lining it inside, while others simply keep it in a mound inside their room. A sage who has knowledge of vampires can look at the soil and completely find out its true identity through their knowledge ability. To do so, you must know about vampires and must also make a success roll against target score 16. You cannot attempt this success roll if you do not know about vampires.

If someone with the shaman skill looks at the soil, they can immediately tell that it's something out of the ordinary. If you're accompanied by a sage who knows about vampires, and further find out that the soil is not normal soil, you'll be able to deduce its true identity.

You can defeat a vampire by reducing its mental points to 0, or by removing the soil from its original location and reducing its life points to 0. However, cautious vampires usually keep soil in several locations.

##### Undead King

- Monster Level=15
- Rarity=13
- Agility=20    Movement Speed=20／20 (air)
- Number=One    Frequency=Very rare
- Intellect=Very high    Reaction=Adversarial
- Attack Points=Barehanded：22 (15)    Strike Points=19+mental damage
- Evasion Points=24 (17)    Defense Points=17
- Life Points／Resistance=26／25 (18)
- Mental Points／Resistance=32／26 (19)
- Special Abilities=10th level ancient magic (Magic intensity／magic power=22／15); 10th level dark magic (Magic intensity／magic power=22／15); Steal mental power (Strike power 10, bonus damage 15); Gaze (Resist target score=22, paralysis by fear); Life point regenerate (3 points per round); Normal weapon immunity; Not affected by poison and illness; Sleepless; Damage from healing magic
- Habitat=Places with unholy soil
- Languages=Low ancient
- Perception=Pseudo

The Undead King, is the name of the ultimate undead, the king of all without life, a powerful necromancer from the ancient kingdoms that gained eternal negative power through a lost spell. They are usually dressed in black robes and a hood. The scores given here are for an average undead king, and will vary depending on the abilities they had previously. If you take that into account, its dexterity and agility will be previous +6, its strength, intelligence, and life will be previous +12, and its mental power will be previous +18. That said, there aren't exactly enough undead kings in Forcelia to go taking averages...

Above all, the most frightening thing about the undead king is that it has great magical power. An undead king uses both ancient magic and dark magic up to at least 10th level.

Other characteristics are similar to those of a vampire. The same goes for the presence of soil.

### 13.2.10 Magical Creatures

#### [ Simulacra ]

- Monster Level=Based on original
- Rarity=14
- Agility=Based on original    Movement Speed=Based on original
- Number=One to several    Frequency=Rare
- Intellect=None    Reaction=Violent
- Attack Points／Strike Points／Evasion Points／Defense Points=Based on original
- Life Points／Resistance=Based on original／based on original
- Mental Points／Resistance=ー／Based on original
- Special Abilities=Duplication; Mental attack immunity; Not affected by poison and illness
- Habitate=Ruins
- Languages=None
- Perception=Pseudo

A simulacra is a kind of golem built during the ancient kingdom period. A simulacra duplicates the appearance and abilities of an enemy human creature and makes them its own.

They were often used to watch over people who did not use magic, such as slaves and savages, and to guard the places where they worked. A simulacra duplicates the belongings, weapons, armor, etc. of people it sees and attacks them. However, magical weapons and armor cannot be duplicated. Although they look the same, they don't even have magical power. If it duplicates someone who is holding a broadsword +1, it will attack with a broadsword with the same strike power, but will not receive any bonuses to attack power or bonus damage.

A simulacra's replication is only superficial, and is limited to weapon combat capability. It cannot duplicate someone's personality or even their memories. As far as is currently known, simulacra seem to be unable to speak or use any magic at all.

The only way to attack a simulacra is to attack directly with a weapon. Although it's a formidable enemy for a 10th level fighter, it's not a formidable opponent for a 1st level sorcerer (without the fighter, thief, or ranger skill).

#### [ Homunculus ]

Among the pseudo-life forms created by ancient magic, the homunculus is the closest to human. Although they're about one-tenth the size of a human, they have human-like intelligence and can speak.

Production of a homunculus is not always successful. In addition, creating a homunculus with new characteristics will inevitably be a process of trial and error. The same held true for the sorcerers of the ancient kingdoms period, who produced countless failures. The monsters called blobs are these failures, which were carelessly dumped into sewers and rivers, which turned feral and have survived to the present day.

##### Homunculus

- Monster Level=1
- Rarity=14
- Agility=14    Movement Speed=4／7 (air)
- Number=One    Frequency=Very rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Barehanded：8 (1)    Strike Points=1
- Evasion Points=10 (3)    Defense Points=3
- Life Points／Resistance=6／8 (1)
- Mental Points／Resistance=14／9 (2)
- Special Abilities=None in particular
- Habitat=Depends on the caster
- Languages=Low ancient
- Perception=Five senses

Homunculus are often created as distractions or scouts for rune masters. Most resemble humans, but some are ugly, resembling gargoyles, and some have wings and can fly.

Unlike golems, etc. homunculus have their own will, and in some cases they may rebel against their creators. Their life span is only a few years.

##### Blob

- Monster Level=8
- Rarity=15
- Agility=8    Movement Speed=8
- Number=One to several    Frequency=Rare
- Intellect=None    Reaction=Adversarial
- Attack Points=Ram：10 (3)    Strike Points=3
- Evasion Points=10 (3)    Defense Points=4
- Life Points／Resistance=16／10 (3)
- Mental Points／Resistance=ー／10 (3)
- Special Abilities=All weapons cannot critical; Iron corrosion; Mental attack immunity; Not affected by poison and illness
- Habitat=Decaying swamps, sewers
- Languages=None
- Perception=Magic

Sorcerers in the ancient kingdom often experimented with creating life, but would carelessly throw their failed creations into the sewers or rivers. The blob is said to be the result of such failed artificial life turning feral. It's a black, slimy, amorphous creature with no intellect, which attacks all living things.

A blob has a liquid inside it that corrodes iron. If you attack a blob with an iron weapon or if a blob's attack hits someone wearing iron armor, that equipment will corrode and become useless after 24 hours. However, magical weapons and armor, silver and mithril silver weapons and armor are not affected.

Also, attacks with any weapon cannot critical against the blob.

#### [ Puppet Golem ]

A puppet golem is a small, simple version of a golem that is created by giving temporary life to a tree branch, stone, etc. using an ancient magic spell. Depending on the material, there are four different types of puppet golems that can be created. They are oak, stone servant, bone servant, and skeleton warrior.

##### Oak

- Monster Level=2
- Rarity=13 (However, a sorcerer always knows)
- Agility=14    Movement Speed=14
- Number=One to several    Frequency=Rare
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Arms：10 (3)    Strike Points=6
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=12／10 (3)
- Mental Points／Resistance=ー／10 (3)
- Special Abilities=Mental attack immunity; Not affected by poison and illness
- Habitat=Various
- Languages=None
- Perception=Pseudo

An oak is a puppet golem the size of a human child, made from oak wood. They have no talents other than fighting.

##### Stone Servant

- Monster Level=3
- Rarity=15 (However, a sorcerer always knows)
- Agility=12    Movement Speed=12
- Number=One to several    Frequency=Rare
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Arms：11 (4)    Strike Points=13
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=16／11 (4)
- Mental Points／Resistance=ー／11 (4)
- Special Abilities=Mental attack immunity; Not affected by poison and illness
- Habitat=Various
- Languages=None
- Perception=Pseudo

A stone servant is a puppet golem about 1.5 meters tall, made from stone. They can perform simple tasks as well as fight.

##### Bone Servant

- Monster Level=3
- Rarity=15
- Agility=12    Movement Speed=18
- Number=One to several    Frequency=Rare
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Arms：11 (4)    Strike Points=8
- Attack Points=Weapon：11 (4)    Strike Points=9
- Evasion Points=11 (4)    Defense Points=5
- Life Points／Resistance=15／11 (4)
- Mental Points／Resistance=ー／11 (4)
- Special Abilities=Mental attack immunity; Bladed weapons cannot critical; Not affected by poison and illness
- Habitat=Various
- Languages=None
- Perception=Pseudo

A bone servant is a puppet golem made from the bones of living creatures. Usually they're humanoids, but other ones exist too. When armed, they're difficult to distinguish from a skeleton warrior. They are superior to stone servants, etc. in that they have eternal life and can carry out fairly complex commands.

Bladed weapons cannot critical against a bone servant.

##### Skeleton Warrior

- Monster Level=5
- Rarity=14 (However, a sorcerer always knows)
- Agility=18    Movement Speed=14
- Number=One to several    Frequency=Rare
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Weapon：12 (5)    Strike Points=11
- Evasion Points=14 (7)    Defense Points=10
- Life Points／Resistance=16／13 (6)
- Mental Points/Resistance=ー／13 (6)
- Special Abilities=Mental attack immunity; Bladed weapons cannot critical; Not affected by poison and illness
- Habitat=Uncertain
- Languages=None
- Perception=Pseudo

A skeleton warrior is a golem created from a magical dragon's tooth. Its appearance is that of a fully-armed skeleton, which uses its weapon and shield with mechanical precision. However, its intellect is low and it cannot accept complex or abstract commands. For this reason, skeleton warriors are often used for simple tasks, such as guarding treasure vaults, etc.

A skeleton warrior will attempt to carry out any commands they're given, unless the caster who created them gives them new commands in high ancient, or cancels any previously given commands. It's usually not possible to control, or cancel the commands of, a skeleton warrior created by someone else. Also, once created, a skeleton warrior will never return to its original tooth form.

Even if you attack a skeleton warrior with a bladed weapon, it will not cause a critical hit.

#### [ Imitator ]

An imitator is a clay-like artificial lifeform created by the sorcerers of the ancient kingdom, made in the shape of doors and treasure chests, and placed throughout castles and labyrinths to guard treasures and important people. Normally, they're in a state of suspended animation and do not move at all, and they look like stone or metal, but as soon as they are touched by a living creature, they activate immediately and attack. Since they can live for thousands of years in a state of suspended animation, many imitators are even now still awaiting intruders in old labyrinths.

An Imitator will not stop attacking until the intruders are repelled or wiped out, but since they're ordered to remain in a specific location, they will not pursue any enemies that run away.

Once combat is over, an imitator dissolves the bodies of the victims it killed in acid, completely absorbing them. The time required for absorption is several hours for a small imitator, but only a few dozen seconds for a large one. An imitator can also absorb iron, but cannot dissolve gold, silver, or jewelry, so it spits those out. Therefore, there will often be treasures that belonged to the victims scattered around the imitator. When it finishes absorbing, the imitator will return to its original state of suspended animation.

Imitators have no intelligence. The only words an imitator can understand are the keywords given to it by the sorcerer at the time it was created. If you say the keyword, the imitator will not attack. Even in the middle of combat, hearing the keyword will instantly return it to suspended animation.

Imitators come in a variety of shapes and sizes, but the three most common ones are chest imitators, door imitators, and floor imitators. There are also monsters called things, which are imitators that escaped after being created, and turned feral.

Imitators and things will disguise themselves as other objects, then perform a surprise attack. To avoid being surprised, a character must make a success roll against target score 16 using ranger skill level + intelligence bonus as the baseline score.

If you're caught by surprise, the imitator or thing will be given the first attack. At this time, a -4 penalty will be imposed on the character's evasion speed. Normal combat is possible from the 2nd round onwards.

##### Chest Imitator

- Monster Level=2
- Rarity=13
- Agility=10    Movement Speed=10
- Number=One    Frequency=Moderate
- Intellect=Almost none    Reaction=Violent
- Attack Points=Arms：10 (3)    Strike Points=4
- Evasion Points=10 (3)    Defense Points=6
- Life Points／Resistance=8／9 (2)
- Mental Points／Resistance=ー／10 (3)
- Special Abilities=Camouflage (Sense target score=16); Mental attack immunity; Not affected by poison and illness
- Habitat=Underground labyrinths, ruins
- Languages=None
- Perception=Magic

This is an imitator in the shape of a treasure chest. As soon as a thief touches it to examine it, it'll attack. Chest imitators can actually be used as treasure chests, so you may find treasure inside after defeating them.

##### Door Imitator

- Monster Level=3
- Rarity=13
- Agility=10    Movement Speed=10
- Number=One    Frequency=Rare
- Intellect=Almost none    Reaction=Violent
- Attack Points=Barehanded：10 (3)    Strike Points=5
- Evasion Points=10 (3)    Defense Points=7
- Life Points／Resistance=16／11 (4)
- Mental Points／Resistance=ー／11 (4)
- Special Abilities=Camouflage (Sense target score=16); Arm grab; Mental attack immunity; Not affected by poison and illness
- Habitat=Underground labyrinths, ruins
- Languages=None
- Perception=Magic

This is an imitator in the shape of a door. As soon as you touch the knob, it'll attack. Anyone hit by a door imitator's attack on the first round will have one arm grabbed and will suffer a -4 penalty to evasion on subsequent rounds. You can only use your other arm in combat, and your movement is restricted, so you cannot use ancient magic. The method of shaking your arm free is the same as strangling, but you will not suffer any damage from being grabbed, and you'll still be able to make sound.

##### Floor Imitator

- Monster Level=5
- Rarity=13
- Agility=10    Movement Speed=10
- Number=One    Frequency=Rare
- Intellect=Almost none    Reaction=Violent
- Attack Points=Arms：13 (6)    Strike Points=13
- Strike Points=11 (4)    Defense Points=9
- Life Points／Resistance=24／15 (8)
- Mental Points／Resistance=ー／13 (6)
- Special Abilities=Camouflage (Sense target score=16); Strangling; Mental attack immunity; Not affected by poison and illness
- Habitat=Underground labyrinths, ruins
- Languages=None
- Perception=Magic

This is the most dangerous type of imitator. The entire floor of one room is an imitator which attacks anyone who enters the room. Anyone standing on a floor imitator that's begun to move must suffer a -2 penalty to attack and evasion due to unstable footing. A floor imitator can attack anyone standing on top of it. Anyone hit by a floor imitator's attack will be enwrapped in its amorphous body and strangled.

##### Thing

- Monster Level=3
- Rarity=16
- Agility=12    Movement Speed=12
- Number=One    Frequency=Very rare
- Intellect=Human    Reaction=Neutral to adversarial
- Attack Points=Tentacles：10 (3)    Strike Points=7
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=16／11 (4)
- Mental Points／Resistance=12／11 (4)
- Special Abilities=Camouflage (Sense target score=16); Tentacle Attack 1D times; Not affected by poison and illness; Sleepless
- Habitat=Underground labyrinths, ruins
- Languages=Regional
- Perception=Magic

Like an imitator, a thing is an amorphous creature, and according to one theory it's said to be an imitator that's turned feral. The difference is that they have intellect and can transform into any creature so long as it's close to human size. Although it is nearly impossible to see through its clever transformation, in contrast to an imitator, it's not very good at transforming into inanimate objects.

Things often eat humans. They approach their prey in the form of a human or elf, catch their opponent off guard, then aim to attack when they're alone. They target humans because they're easier to deceive than animals. Animals have a keen sense of smell, so no matter how closely a thing resembles the real deal, they'll be able to tell by the difference in smell.

During combat, a thing can attack up to 6 times by transforming its body so as to produce numerous arms and tentacles. The game master must roll the dice to randomly determine how many attacks are made in a round.

#### [ Obsidian Dog ]

- Monster Level=3
- Rarity=15
- Agility=16    Movement Speed=24
- Number=One to several    Frequency=Rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Fangs：10 (3)    Strike Points=10
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=16／11 (4)
- Mental Points／Resistance=ー／11 (4)
- Special Abilities=Mental attack immunity; Not affected by poison and illness; Fire immunity
- Habitat=Underground labyrinths, ruins
- Languages=None
- Perception=Magic

This is a type of golem created through ancient magic. It looks like a dog made of obsidian. It's normally a harmless dog statue, but when its silver collar is removed, it becomes hostile towards all living things and attacks. The inhabitants of the ancient kingdoms used them as a spectacle to fight off savages. Occasionally an obsidian dog can be found still wearing its silver collar.

#### [ Gargoyle ]

- Monster Level=3
- Rarity=12
- Agility=12    Movement Speed=10／15 (air)
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Neutral
- Attack Points=Fangs：10 (3)／Claws：11 (4)
- Strike Points=10／9
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=16／11 (4)
- Mental Points／Resistance=10／10 (3)
- Special Abilities=Not affected by poison and illness; Sleepless
- Habitat=Ruins
- Languages=None
- Perception=Magic

A gargoyle is a species of golem, a statue brought to life through magic, but its flexible movements resemble those of a normal living creature. Its appearance resembles a stone statue, and if you close your eyes, you won't be able to tell it apart unless you look very closely. These monsters still exist in the ruins of the ancient kingdoms without ceasing activity, but the means to control them and the technology to create them have already been lost.

A gargoyle has wings on its back and can fly. It also has a tail. Its grotesque appearance is said to be because it was modeled after the lesser demon zalbard (described later). The size of a gargoyle is nearly 2 meters when standing upright. Unlike golems, etc. they act according to their own judgment without receiving commands. In other words, they may run away if they think they're at a disadvantage, or they may take advantageous tactics depending on the situation. Their personality is very insidious, and they're willing to resort to dirty measures.

#### [ Sí ]

- Monster Level=3
- Rarity=14
- Agility=17    Movement Speed=17
- Number=One to several    Frequency=Very rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon：11 (4)    Strike Points=4
- Evasion Points=12 (5)    Defense Points=5
- Life Points／Resistance=4／9 (2)
- Mental Points／Resistance=14／11 (4)
- Special Abilities=3rd level ancient magic (Magic intensity／magic power=12／5)
- Habitat=Ruins
- Languages=Low ancient
- Perception=Five senses

The sí is said to be an artificial lifeform created by the wizards of the ancient kingdoms. They mainly live in ancient ruins and have their own villages and small homes. They are highly intelligent and can handle magic. Their physique and appearance is similar to that of a grassrunner, but they have long, gangly limbs and unusually thin fingers.

They do not willingly go outside their home (ruins). A sí's weapon is a thin sword that resembles a needle. They also use ancient magic. This often includes lost spells among them.

#### [ Stalker ]

Stalkers are beings created through ancient magic rituals, using gas and many human souls. As their name suggests, they're meant to assassinate others. Stalkers are usually ghostly beings, who can move without being blocked by physical obstacles. Thus they can freely pass through small gaps in doors or holes in walls. However, since they cannot use magic, etc. if they attempt to carry out their original purpose, which is to kill, they must materialize before they attack. A materialized stalker can be wounded by damage magic, silver, and magical weapons, but cannot be wounded by normal weapons. When either its life or mental points reach 0, a stalker's spiritual bond will break and it'll disappear. Physical attacks are completely ineffective against a stalker in ghostly form.

In present day Forcelia, the technique used to create stalkers has been lost. Therefore, all stalkers adventurers will meet are survivors from the ancient kingdom.

Stalkers naturally follow the commands of their casters, but now that all the casters are dead, they remember the last command they were given and faithfully try to carry it out. Stalkers that were created but abandoned without being given any commands will act according to their violent tendencies, indiscriminately attacking anyone they come across.

Failures were also an inevitable part of stalker production. However, these failed creations became gaseous creatures called gizmos, which continue to live in present day Forcelia.

##### Gizmo

- Monster Level=3
- Rarity=15
- Agility=10    Movement Speed=13
- Number=One to several    Frequency=Rare
- Intellect=None    Reaction=Violent
- Attack Points=ー    Strike Points=ー
- Evasion Points=10 (3)    Defense Points=5
- Life Points／Resistance=14／11 (4)
- Mental Points／Resistance=ー／11 (4)
- Special Abilities=Noxious gas (Toxicity score 10, strike power 10, bonus damage 3); Mental attack immunity; Weapon immunity; Certain magic immunity; Weak to fire
- Habitat=Stagnant swamps
- Languages=None
- Perception=Magic

Gizmos are amorphous black gasses around 2 meters in diameter, which were failed attempts at stalkers. They live by inhaling the stench of decay emitted by dead animals. If there are no animal carcasses nearby, they will also try to kill living creatures and turn them into corpses.

Even if a gizmo's attack hits, it does not deal damage by itself. However, the body of a gizmo is poisonous gas, so those hit by it will inhale it and suffer damage resulting from a strike power 10 strike roll plus 3 points of bonus damage. However, if their resistance roll is successful, the strike power becomes 0. Armor cannot protect against gas, only adventurer level or magical protection can reduce the damage.

A gizmo cannot be attacked by weapons at all. Since they have no mind, Sleep Cloud and other types of magic that affect the mind are ineffective. Cold-type, wind cutter-type, stone-type, and poison gas-type damage magic is also ineffective. Only fire-type, electric-type, pure energy-type, and explosion-type magic attacks can deal damage. A gizmo's gas is highly flammable, so fire-type magic is particularly effective, and will add +10 to normal strike power during a check. Also, if you cast a Fire Weapon spell on your weapon and attack, it'll deal strike power 20 damage if it hits.

##### Gas Stalker

- Monster Level=4
- Rarity=14
- Agility=15    Movement Speed=15
- Number=One, rarely multiple    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Claws：12 (5)    Strike Points=9
- Evasion Points=12 (5)    Defense Points=6
- Life Points／Resistance=14／12 (5)
- Mental Points／Resistance=20／13 (6)
- Special Abilities=Normal weapon immunity; Not affected by poison and illness; Sleepless; Physical attack immunity while in ghostly form
- Habitat=Ruins
- Languages=None
- Perception=Pseudo, Magic while in ghostly form

A gas stalker is a Stalker created using a heavy, foul-smelling gas. Although it's usually invisible and doesn't make a sound, you can tell when it's approaching because the gas that makes up its body gives off a terrible odor. When it materializes, it appears as a naked devil with green skin and crazy bloodshot eyes.

##### Shadow Stalker

- Monster Level=5
- Rarity=14
- Agility=15    Movement Speed=15
- Number=One, rarely multiple    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Garrote：10 (3)    Strike Points=Special
- Evasion Points=13 (6)    Defense Points=7
- Life Points／Resistance=16／13 (6)
- Mental Points／Resistance=20／14 (7)
- Special Abilities=Choke (Strike power 10, bonus damage 5); Surprise attack (Sense target score=16); Normal attack immunity; Not affected by poison and illness; Sleepless; Physical attack immunity while in ghostly form
- Habitat=Ruins
- Languages=None
- Perception=Pseudo, Magic while in ghostly form

A shadow stalker is a stalker made using an extremely heavy black gas. Even when it's not materialized, the color of the black gas is clearly visible in a well-lit area, but when it's lost in darkness, it's barely recognizable. It also excels at moving around while pretending to be its opponent's shadow. A shadow stalker will materialize behind its opponent, holding a garrote in its hand. It'll then try to strangle the opponent to death with that garrote.

Those with the ranger skill can detect this attack using their sense danger ability if they succeed on a success roll against target score 16 using ranger skill level + intelligence bonus as the baseline score. If you can detect it, you can evade and attack as normal, but if you cannot, it will be a complete surprise attack, so you will not be able to attack, and will be attacked with no chance to respond. At this time, you'll suffer a -4 penalty to evasion.

Once a shadow stalker's attack hits, treat it as if the character is being strangled. The damage is strike power 10, plus 5 points of bonus damage. If an adventurer is wearing metal armor other than ring mail, they will not suffer any damage. Regardless of damage or armor, once character's life force rounds have passed, the character will suffocate and fall unconscious (life force 0). Every round from then on, you'll need to make a death check when applying damage (even if it's 0). For information on escaping, see grapple.

##### Air Stalker

- Monster Level=6
- Rarity=15
- Agility=15    Movement Speed=15
- Number=One, rarely multiple    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Weapon：13 (6)    Strike Points=12
- Evasion Points=14 (7)    Defense Points=8
- Life Points／Resistance=16／14 (7)
- Mental Points／Resistance=20／15 (8)
- Special Abilities=Normal attack immunity; Completely transparent; Not affected by poison and illness; Sleepless; Physical attack immunity while in ghostly form
- Habitat=Ruins
- Languages=None
- Perception=Pseudo, Magic while in ghostly form

An air stalker is a stalker created from transparent gas. Therefore, even when it materializes, it is completely invisible. For this reason, attacks on an air stalker and evasion against an air stalker's attacks are always -4.

Of course, it's not certain what form an air stalker will materialize in.......

#### [ Mutant Monster ]

- Monster Level=5
- Rarity=18
- Agility=10    Movement Speed=10
- Number=One    Frequency=Very rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Arms：13 (6)    Strike Points=11
- Evasion Points=11 (4)    Defense Points=8
- Life Points／Resistance=18／14 (7)
- Mental Points／Resistance=18／13 (6)
- Special Abilities=None in particular
- Habitat=Various
- Languages=Regional
- Perception=Five senses

This is a human who has mutated and gone berserk due to a special poison called Living Doll (see Poison List). They vary in appearance; some have four arms, some have a tail instead of legs, some have small wings, and some have scales all over their bodies.

Transformation from human to monster takes one round, during which they cannot attack, but they can still evade. Evasion points, defense points, and life points in the round during transformation use the monster's scores.

Even if struck by the poison, it does not completely turn them into a monster, and some memories of being human may remain. If you call out to them with all your heart, they may respond. If you cast the holy magic Cure Poison on them, you can return them to their human form.

In addition to Living Doll, it's said that there are several other poisons that can create mutant monsters. According to one theory, magical beasts such as scylla, etc. were born from such poison.

#### [ Golem ]

Golems are statues created by enchanters during the ancient kingdom period, and given pseudo-life. All they can do is blindly follow the commands of their sorcerer master. In the present day, the method of creating golems has been lost, and there are no sorcerers who can create golems.

Since golems have eternal life, some of them are still left in ruins, etc. Some of them were left as they were created, without any commands given. Such golems can be given commands using the ancient magic Command Golem.

A variety of materials were used to create golems. Typically, animal (or human) flesh, stone, wood, steel, and ceramics were commonly used. However, some were made of very unusual material, such as crystal, ruby, diamond, and mithril silver, as if to show off their skills.

Golems are generally humanoid, but there are many exceptions to this, and some come in special shapes that resemble animals, magical beasts, or mythical beasts such as dragons, etc.

Here, we will introduce data for three types of golems: the most frequently produced Flesh Golem and Iron Golem, and the extremely rare Mithril Golem which is considered the strongest. This data has been created with the assumption that their shape is humanoid.

##### Flesh Golem

- Monster Level=7
- Rarity=12
- Agility=12    Movement Speed=13
- Number=One    Frequency=Rare
- Intellect=Obeys Commands    Reaction=Command-based
- Attack Points=Arms：15 (8)    Strike Points=16
- Evasion Points=14 (7)    Defense Points=9
- Life Points／Resistance=30／18 (11)
- Mental Points／Resistance=ー／15 (8)
- Special Abilities=Mental attack immunity; Not affected by poison and illness
- Habitat=Ruins
- Languages=None
- Perception=Pseudo

A flesh golem is a golem made from dead flesh. Usually animal products were used, but perhaps because it was the ancient kingdom period, examples made from the bodies of slaves are also frequently seen. Golems are generally slow-moving creatures, but these have relatively flexible and agile bodies among them.

##### Iron Golem

- Monster Level=9
- Rarity=12
- Agility=6    Movement Speed=8
- Number=One    Frequency=Rare
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Arms：17 (10)    Strike Points=19
- Evasion Points=14 (7)    Defense Points=14
- Life Points／Resistance=50／23 (16)
- Mental Points／Resistance=ー／17 (10)
- Special Abilities=Weapons cannot critical; Certain magic resistant; Mental attack immunity; Not affected by poison and illness
- Habitat=Ruins
- Languages=None
- Perception=Pseudo

An iron golem is a golem made of iron, and is the slowest of all golems. However, in terms of hardness of body and size of life force, they're also terrifying beings that rival lesser dragons and titans.

Against an iron golem, weapons cannot deal additional critical damage. Also, damage spells such as cold-type, electric-type, stone-type, poison gas-type, and wind cutter-type are completely useless. Fire-type damage magic is effective, but a critical cannot occur. Earthquake-type, explosion-type, and pure energy-type damage magic is effective, and a critical can occur.

##### Mithril Golem

- Monster Level=13
- Rarity=16
- Agility=12    Movement Speed=15
- Number=One    Frequency=Very rare
- Intellect=Obeys commands    Reaction=Command-based
- Attack Points=Arms：21 (14)    Strike Points=25
- Evasion Points=19 (12)    Defense Points=19
- Life Points／Resistance=75／31 (24)
- Mental Points／Resistance=ー／21 (14)
- Special Abilities=Weapons cannot critical; Certain magic resistant; Mental attack immunity; Not affected by poison and illness
- Habitat=Ruins
- Languages=None
- Perception=Pseudo

Mithril Golems are extremely rare, and only one has been confirmed to exist to date. Since they're formed from mithril silver, which is hard but lightweight, they can make relatively agile movements, and they also have exceptionally hard bodies and large amounts of life force.

Against a mithril golem, weapons cannot deal additional critical damage. Also, damage spells such as cold-type, electric-type, stone-type, poison gas-type, and wind cutter-type are completely useless. Fire-type damage magic is effective, but a critical cannot occur. Earthquake-type, explosion-type, and pure energy-type damage magic is effective, and a critical can occur.

### 13.2.11 Daemons / Underworld Creatures

#### [ Aetherbeast ]

- Monster Level=4
- Rarity=15
- Agility=16    Movement Speed=21
- Number=One    Frequency=Very rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Fangs：11 (4)    Strike Points=10
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=14／12 (5)
- Mental Points／Resistance=16／12 (5)
- Special Abilities=Depends on appendages
- Habitat=Underground labyrinths, ruins
- Languages=None
- Perception=Five senses (illumination due to appendages)

These are beasts of the daemon world, said to be creatures created by daemons. They often work as servants of daemons. They're rarely encountered in the material world, and details of them are not well understood. The few eyewitness accounts are mixed, and its shape is not clear, but it's agreed that it looks like a combination of several animals from the material world.

Although this data is general, there are many different types of aetherbeasts. If the game master wishes, they may create special aetherbeasts.

#### [ Hellhound ]

- Monster Level=5
- Rarity=14
- Agility=15    Movement Speed=18
- Number=One    Frequency=Rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Fangs：12 (5)    Strike Points=12
- Evasion Points=12 (5)    Defense Points=8
- Life Points／Resistance=16／13 (6)
- Mental Points／Resistance=12／13 (6)
- Special Abilities=Fire breath in a 5 meter forward radius (Resist target score=12, strike power 10, bonus damage 5); Fire immunity
- Habitat=Deep caves, underground labyrinths
- Languages=None
- Perception=Five senses (Darkvision)

At first glance, the hellhound looks like a large black dog. However, in reality, it's a terrifying beast from the underworld, also known as the watchdog of Hell. Hellhounds have a 1 in 6 chance (if you roll 1 on 1D) of breathing fire from their mouths. Everyone within a 5 meter radius semicircle in front of the hellhound will suffer damage equal to a strike power 10 strike roll plus 5 points of bonus damage. Armor cannot protect against this fire; only adventurer level and magical defense can reduce the damage.

#### [ Cerberus ]

- Monster Level=9
- Rarity=13
- Agility=15    Movement Speed=18
- Number=One    Frequency=Very rare
- Intellect=Animal    Reaction=Adversarial
- Attack Points=Fangs (3 times)：15 (8)    Strike Points=17x3
- Evasion Points=15 (8)    Defense Points=12
- Life Points／Resistance=22／17 (10)
- Mental Points／Resistance=15／16 (9)
- Special Abilities=Fire breath in a 5 meter surrounding radius (Resist target score=15, strike power 20, bonus damage 8); Fire immunity
- Habitat=Deep within underground labyrinths
- Languages=None
- Perception=Five senses (Darkvision)

A cerberus is a large black dog with three heads, and is thought to be a variant of the hellhound. It's slightly larger than a hellhound, about as big as a medium-sized horse. When attacking, it uses all three of its heads to bite the same target at the same time.

Like a hellhound, a cerberus can also breathe fire. If a 1 is rolled on 1D, all three heads will breathe fire at the same time in three different directions. Everyone in a 5 meter radius surrounding the cerberus will suffer damage equal to a strike power 20 strike roll plus bonus damage 8. Armor cannot protect against this fire; only adventurer level and magical defense can reduce the damage.

Fire attacks have no effect on a cerberus.

#### [ Lesser Daemon ]

##### Grunel

- Monster Level=5
- Rarity=13
- Agility=14    Movement Speed=15
- Number=One to several    Frequency=Very rare
- Intellect=Human    Reaction=Adversarial, or command-based
- Attack Points=Weapon：12 (5)／Tail：12 (5)
- Strike Points=13／13
- Evasion Points=12 (5)    Defense Points=9
- Life Points／Resistance=22／14 (7)
- Mental Points／Resistance=20／14 (7)
- Special Abilities=5th level ancient magic (magic intensity／magic power=14／7); 3rd level dark magic (magic intensity／magic power=12／5); Strangling
- Habitat=Underground labyrinths, secluded ruins
- Languages=Low ancient
- Perception=Five senses (Darkvision)

A grunel is a humanoid lesser daemon with steel-blue skin. It's characterized by its long tail, which it can manipulate freely like a whip to attack or entangle enemies. If it uses its tail to entangle, treat this as a strangling attack. The target will be unable to move, and the grunel can attack with the weapon in its right hand. They have the ability to use ancient magic. They seem to have been especially proficient at enchanting, and often carry a magical sword. If a grunel has a magic sword, add a bonus of 1 point to both its attack points and strike points. They can also use dark magic.

##### Zalbard

- Monster Level=5
- Rarity=13
- Agility=14    Movement Speed=15／17 (air)
- Number=One to several    Frequency=Very rare
- Intellect=Human    Reaction=Adversarial, or command-based
- Attack Points=Claws：13 (6)    Strike Points=14
- Evasion Points=12 (5)    Defense Points=9
- Life Points／Resistance=25／15 (8)
- Mental Points／Resistance=18／14 (7)
- Special Abilities=3rd level dark magic (magic intensity／magic power=12／5); Breathe enough fire to engulf one person (Resist target score=12, strike power 10, bonus damage 5); Fire immunity
- Habitat=Underground labyrinths, secluded ruins
- Languages=Low ancient
- Perception=Five senses (Darkvision)

The zalbard is a lesser daemon that's said to be the model for the gargoyle. Its appearance is almost identical to that of a gargoyle, but its skin is fiery red. Its eyes are also bright red, and glow suspiciously. A zalbard's method of attack is the sharp claws on its hands, and it also has the power to breathe magical fire from its mouth. The fire breathed by a zalbard extends in a straight line, making one target within 5 meters its victim. Those attacked by the fire will suffer damage equal to a strike power 10 strike roll plus 5 points of bonus damage. If you succeed on a resistance roll, strike power becomes 0. In addition, fire and heat attacks cannot wound a zalbard. They have the ability to use dark magic.

##### Doubleburg

- Monster Level=5
- Rarity=14
- Agility=15    Movement Speed=12
- Number=One to several    Frequency=Very rare
- Intellect=Human    Reaction=Adversarial, or command-based
- Attack Points=Claws：13 (6)    Strike Points=12
- Evasion Points=12 (5)    Defense Points=9
- Life Points／Resistance=20／14 (7)
- Mental Points／Resistance=18／14 (7)
- Special Abilities=Shapeshift
- Habitat=Underground labyrinths, secluded ruins
- Languages=Low ancient, languages of the person it shapeshifts into
- Perception=Five senses (Darkvision)

A doubleburg is almost the same size as a human, and its entire body is pitch black. It has a bright red open mouth straight across its face, but no other features. This daemon has the ability to completely copy any opponent's appearance after just one look, including their clothes. If it spends one minute to observe them, it can imitate their tone of speech and gestures exactly. Therefore, it's not possible to discern whether it's the real thing by appearance alone. To shapeshift or shapeshift back requires one full round.

However, it cannot copy its opponent's abilities and memories. Even if it shapeshifts, a doubleburg's score data will not change at all. For example, even though it looks like it's wielding a weapon, it's actually a part of the doubleburg's own body that's been shapeshifted.

##### Ragnakang

- Monster Level=6
- Rarity=13
- Agility=10    Movement Speed=12／20 (air)
- Number=One    Frequency=Very rare
- Intellect=Human    Reaction=Adversarial, or command-based
- Attack Points=Fangs：13 (6)／Claws：14 (7)
- Strike Points=17+Poison／16
- Evasion Points=12 (5)    Defense Points=10
- Life Points／Resistance=30／17 (10)
- Mental Points／Resistance=20／15 (8)
- Special Abilities=3rd level dark magic (magic intensity／magic power=12／5); Poison (toxicity score 13, strike power 20, bonus damage 6)
- Habitat=Underground labyrinths, secluded ruins
- Languages=Low ancient
- Perception=Five senses (Darkvision)

A ragnakang is a lesser demon that looks like an upright dragon. It has wings reminiscent of a giant bat, can reach over 3 meters in height with its neck extended, and uses its long neck to attack by biting. It also uses its strong tail as a weapon. They perform these two attacks at the same time every round. Its sharp fangs contain a powerful poison, and those who fail to resist will immediately suffer damage equal to a strike power 20 strike roll plus 6 points of bonus damage.

##### Maligdorai

- Monster Level=7
- Rarity=15    Agility=14
- Movement Speed=15／20 (air)
- Number=One    Frequency=Very rare
- Intellect=High    Reaction=Adversarial, or command-based
- Attack Points=Needle x 2：14 (7)    Strike Points=16x2
- Evasion Points=14 (7)    Defense Points=9
- Life Points／Resistance=20／16 (9)
- Mental Points／Resistance=25／17 (10)
- Special Abilities=Illusion (Resist target score=17, mental damage=strike power 10, bonus damage 7)
- Habitat=Underground labyrinths, secluded ruins
- Languages=Low ancient
- Perception=Five senses (Darkvision)

The Maligdorai is a daemon whose upper body resembles an owl and lower body the hind legs of a goat, and its entire body is covered in feathers. As well as wings on its back, it has jointless tentacle-like viscera sprouting from the base of each wing. Its arms come to sharp gimlet-shaped points, and it performs physical attacks by stabbing with them.

A maligdorai's most frightening ability is illusion. The maligdorai can show illusions to surrounding creatures, dealing damage to their minds (these illusions have no effect on monsters that don't have mental points). When a maligdorai uses this illusion ability, those being targeted must make a mental power resistance roll against target score 17 at the beginning of the round. If the target succeeds, they will escape the effect and can act freely, but if the target fails to resist, they will see an illusion of what they fear as an enemy deep within their heart attacking them, and as a result will suffer strike power 10+ bonus damage 7 damage to their mental power. They will also be unable to take any actions.

Those who lose all their mental power due to an illusory attack will from then on be turned into a being that can be freely manipulated by the maligdorai. To recover from this, you must defeat their master, the maligdorai. Those being manipulated cannot recover their mental power through sleep or through magic such as Transfer Mental Power. Also, spells that affect the mind have no effect on those in this state.

A maligdorai can also show illusions to multiple creatures within its vision at the same time, but it must focus in order to perform the illusions. If its focus is interrupted or it's unable to focus due to making physical attacks, suffering damage, etc., then it cannot maintain its illusions. Illusions cannot be used in the round immediately after suffering damage.

Conversely, while the maligdorai is performing an illusion, the target must make a resistance roll against the illusion each round.

#### [ Greater Daemons ]

##### Doppelganger

- Monster Level=10
- Rarity=16
- Agility=14    Movement Speed=18
- Number=One    Frequency=Very rare
- Intellect=High    Reaction=Adversarial
- Attack Points=Claws: 18 (11)    Strike Points=20
- Evasion Points=16 (9)    Defense Points=14
- Life Points／Resistance=34／21 (14)
- Mental Points／Resistance=28／20 (13)
- Special Abilities=7th level ancient magic (magic intensity／magic power=16／9); Shapeshift
- Habitat=Underground labyrinths, secluded ruins
- Languages=Low ancient, languages of the person it shapeshifts into
- Perception=Five senses (Darkvision)

The doppleganger, which is in the same family as the doubleburg, albeit a greater species, has the appearance of a 3 meter tall giant with an entirely black body. Its has a bright red straight open mouth, but no other features besides that. A doppelganger can copy the appearance, abilities, memories, etc. of an opponent by observing them. At a glance, all they can capture is their appearance (including their belongings). If they observe them for one minute, they can imitate their tone of speech and gestures exactly. Then, if they observe them for over one hour, they will be able to completely copy their abilities and memories. To shapeshift or shapeshift back requires one full round.

A doppelganger who has copied the abilities and memories of an opponent can use all of their abilities. If they transform into a dragon, they can breathe fire, and if they transform into a 10th level fighter, they can fight with their attack power, strike power, and bonus damage. However, they cannot use holy magic or dragon roar magic (they can use other magic). In addition, a doppelganger can use its own ability, ancient magic.

If combat occurs without them shapeshifting, a doppelganger will fight primarily using ancient magic.

### 13.2.12 Humans

#### [ Normal Man ]

- Monster Level=0
- Rarity=ー (Everyone knows them)
- Agility=10    Movement Speed=10
- Number=One to hundreds    Frequency=Frequent
- Intellect=Human    Reaction=Friendly
- Attack Points=Farming Tools：7 (0)    Strike Points=3
- Evasion Points=8 (1)    Defense Points=2
- Life Points／Resistance=10／8 (1)
- Mental Points／Resistance=10／8 (1)
- Special Abilities=None in particular
- Habitat=Human villages
- Languages=Regional
- Perception=Five senses

Ordinary people such as villagers will not become enemies of adventurers. The data here is for when villagers, etc. with no fighting ability are drawn into combat.

#### [ Bandit ]

Bandits are those who build strongholds in the fields and hills, and make the surrounding area their territory, where they steal from passersby (mainly merchants).

##### Henchman

- Monster Level=1
- Rarity=5
- Agility=10    Movement Speed=10
- Number=Several to dozens    Frequency=Moderate
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon：8 (1)    Strike Points=5
- Evasion Points=8 (1)    Defense Points=4
- Life Points／Resistance=10／8 (1)
- Mental Points／Resistance=10／8 (1)
- Special Abilities=None in particular
- Habitat=Human villages, fields and hills near roads
- Languages=Regional
- Perception=Five senses

Bandit henchmen should generally be at about this level.

##### Leader

- Monster Level=2
- Rarity=5
- Agility=11    Movement Speed=11
- Number=One to several    Frequency=Moderate
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon：9 (2)    Strike Points=6
- Evasion Points=9 (2)    Defense Points=5
- Life Points／Resistance=11／9 (2)
- Mental Points／Resistance=11／9 (2)
- Special Abilities=None in particular
- Habitat=Human villages, fields and hills near roads
- Languages=Regional
- Perception=Five senses

Leader-class bandits that control several henchmen.

##### Chief

- Monster Level=3
- Rarity=5
- Agility=12    Movement Speed=12
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Adversarial
- Attack Points=Weapon：10 (3)    Strike Points=7
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=12／11 (4)
- Mental Points／Resistance=12/11 (4)
- Special Abilities=None in particular
- Habitat=Human villages, fields and hills near roads
- Languages=Regional
- Perception=Five senses

This data is for a chief class, who leads about 20 followers. If the bandits are large enough in scale, there will be more than one chief class with equal power. Please consider the standard ratio of henchmen : leaders : chiefs to be 16 : 4 : 1. If the scale reaches 80 people or more, there will be an even stronger boss. This boss's scores should equal the total scores of a chief +1. In this case, the ratio of henchmen : leaders : chiefs : bosses should be 64 : 16 : 4 : 1. Every time the scale of the bandits grows 4 times larger, there will be someone stronger to command them (add +1 to each score). For a group of bandits with 300 to 400 members, the leader's monster level should be 5, for more than 1000, it should be 6, for more than 5000, it should be 7......etc.

#### [ Soldier ]

The soldiers listed here are those who are responsible for maintaining public order in the city and protecting the royal castle. Therefore, you normally won't fight them.

##### Normal Soldier

- Monster Level=1
- Rarity=5
- Agility=12    Movement Speed=12
- Number=One to dozens    Frequency=Frequent
- Intellect=Human    Reaction=Friendly
- Attack Points=Weapon：8 (1)    Strike Points=5
- Evasion Points=9 (2)    Defense Points=5
- Life Points／Resistance=12／9 (2)
- Mental Points／Resistance=2／9 (2)
- Special Abilities=None in particular
- Habitat=Towns, villages
- Languages=Regional
- Perception=Five senses

The ordinary soldiers which are the large majority. This is also the standard of the resident class dispatched to rural villages.

##### Senior Soldier

- Monster Level=3
- Rarity=5
- Agility=13    Movement Speed=13
- Number=One to several    Frequency=Frequent
- Intellect=Human    Reaction=Friendly
- Attack Points=Weapon：10 (3)    Strike Points=8
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=13／11 (4)
- Mental Points／Resistance=13／11 (4)
- Special Abilities=None in particular
- Habitat=Towns, villages
- Languages=Regional
- Perception=Five senses

These are soldiers who guard major locations or command small groups. Most of these soldiers were promoted from normal soldiers and are also much older.

##### Knight

- Monster Level=5
- Rarity=5
- Agility=14    Movement Speed=14
- Number=One to several    Frequency=Moderate
- Intellect=Human    Reaction=Friendly
- Attack Points=Weapon：12 (5)    Strike Points=10
- Evasion Points=13 (6)    Defense Points=10
- Life Points／Resistance=14／13 (6)
- Mental Points／Resistance=14／13 (6)
- Special Abilities=None in particular
- Habitat=Towns
- Languages=Regional, common
- Perception=Five senses

These are soldiers in the position of leading dozens of people. They're made up of elites from the nobility, and soldiers who've been recognized for their skill. This level of skill is required to serve in the king's royal guard (though this depends on the country).

##### Knight Leader

- Monster Level=7
- Rarity=5
- Agility=15    Movement Speed=15
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Friendly
- Attack Points=Weapon：14 (7)    Strike Points=13
- Evasion Points=15 (8)    Defense Points=12
- Life Points／Resistance=15／15 (8)
- Mental Points／Resistance=15／15 (8)
- Special Abilities=None in particular
- Habitat=Towns
- Languages=Regional, common
- Perception=Five senses

These soldiers are mainly elites of noble background, and command units of 100 men. Some of them are even higher level. By making their monster level higher, you can increase each score by the same amount you increased the monster level.

#### [ Dark Priest Warrior ]

Priests who serve the wicked gods (mainly Phalaris) will often appear as enemies of the player characters. Since the teachings of the dark gods are what one would call evil, this is likely unavoidable. Many are also trained as warriors as part of the doctrine of Phalaris.

##### Beginner Priest

- Monster Level=1
- Rarity=10
- Agility=12    Movement Speed=12
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Depends on the situation
- Attack Points=Weapon：8 (1)    Strike Points=5
- Evasion Points=9 (2)    Defense Points=4
- Life Points／Resistance=12／9 (2)
- Mental Points／Resistance=12／9 (2)
- Special Abilities=1st level dark magic (magic intensity／magic power=10／3)
- Habitat=Human villages
- Languages=Regional
- Perception=Five senses

This is a so-called small fry class enemy. They rarely face adventurers alone, and are often led by a stronger priest.

##### Priest

- Monster Level=3
- Rarity=10
- Agility=14    Movement Speed=14
- Number=One to several    Frequency=Rare
- Intellect=Human    Reaction=Depends on the situation
- Attack Points=Weapon：10 (3)    Strike Points=8
- Evasion Points=11 (4)    Defense Points=7
- Life Points／Resistance=14／11 (4)
- Mental Points／Resistance=14／11 (4)
- Special Abilities=3rd level dark magic (magic intensity／magic power=12／5)
- Habitat=Human villages
- Languages=Regional
- Perception=Five senses

This is a priest class that has some degree of contact with the dark gods. Although seldom seen in the light of day, they are numerous in the underworld of Forcelia, often secretly planning and carrying out nefarious schemes.

##### High Priest

- Monster Level=5
- Rarity=10
- Agility=16    Movement Speed=16
- Number=One    Frequency=Rare
- Intellect=Human    Reaction=Depends on the situation
- Attack Points=Weapon：12 (5)    Strike Points=11
- Evasion Points=13 (6)    Defense Points=9
- Life Points／Resistance=16／13 (6)
- Mental Points／Resistance=16／13 (6)
- Special Abilities=5th level dark magic (magic intensity／magic power=12／5)
- Habitat=Human villages
- Languages=Regional
- Perception=Five senses

Those who reach the bigwig-class who plot great evil acts will tend to have a much deeper connection with the dark gods and can use powerful magic. There's even cases of a priest of this class ruling the entirety of a small village, unnoticed by the authorities.

### 13.2.13 Other

#### [ Lycanthrope ]

A Lycanthrope is a monster with the ability to change from human to beast form. When in human form, they may acquire and use various skills, including magic, just like an adventurer. When in beast form, they cannot act intelligently, but rather follow their instincts and go on killing sprees. Magic and skills cannot be used. The game master can decide on a lycanthrope's abilities while in human form (however, it should basically only have acquired skills up to its monster level), or use the fixed scores for a normal man as given here (please set the life points high).

Shapeshifting is affected by the waxing and waning of the moon. Compare the number of days since the new moon with 2D + 3 at nighttime or 2D + 9 in the daytime. When the number of days is 16 or more, compare it with 30 - the number of days (the waxing and waning of the moon in Forcelia is one cycle every 30 days). When the score is equal to or less than this, the lycanthrope will always enter beast form (the lycanthrope will always enter beast form on nights when the moon is full = 15 days).

Even when it's not, a lycanthrope can transform into a beast at their own will.

Lycanthropes have the ability to summon and control other beasts of their kind in their surroundings (wolves for werewolves, bears for werebears, etc.). Their habitat depends on the type of beast they shapeshift into. There may be some hiding their true identity and living among humans in towns and villages, but when their time comes, they're likely to take odd actions to hide their transformations.

Lycanthropy is a type of infectious illness, and those who are wounded by a lycanthrope in beast form are at risk of becoming a lycanthrope of the same species. See here for details on this illness.

##### Werewolf

- Monster Level=4
- Rarity=8
- Agility=16    Movement Speed=24
- Number=One to several    Frequency=Rare
- Intellect=Animal／Human    Reaction=Adversarial
- Attack Points=Fangs：11 (4)    Strike Points=12
- Evasion Points=12 (5)    Defense Points=8
- Life Points／Resistance=20／13 (6)
- Mental Points／Resistance=14／12 (5)
- Special Abilities=Normal weapon immunity after shifting into wolf; Infect (Intensity 7)
- Habitat=Human villages, forests
- Languages=Regional
- Perception=Five senses (Illumination)

A werewolf is a lycanthrope with the power to shapeshift into a wolf.

##### Werebear

- Monster Level=5
- Rarity=10
- Agility=14    Movement Speed=21
- Number=One to several    Frequency=Rare
- Intellect=Animal／Human    Reaction=Adversarial
- Attack Points=Fangs：12 (5)／Claw：13 (6)／Claw：13 (6)
- Strike Points=15／14／14
- Attack Points=Fangs：12 (5)／Strangle：14 (7)
- Strike Points=15／13
- Evasion Points=13 (6)    Defense Points=9
- Life Points／Resistance=26／15 (8)
- Mental Points／Resistance=14／13 (6)
- Special Abilities=Normal weapon immunity after shifting into bear; Infect (Intensity 7)
- Habitat=Human villages, forests
- Languages=Regional
- Perception=Five senses (Illumination)

A werebear is a lycanthrope with the power to shapeshift into a bear. Like a bear, it attacks with a bear hug (strangling).

##### Weretiger

- Monster Level=5
- Rarity=11
- Agility=21    Movement Speed=25
- Number=One to several    Frequency=Rare
- Intellect=Animal／Human    Reaction=Adversarial
- Attack Points=Fangs：12 (5)／Claw：13 (6)／Claw：13 (6)
- Strike Points=15／14／14
- Evasion Points=14 (7)    Defense Points=9
- Life Points／Resistance=24／15 (8)
- Mental Points／Resistance=14／13 (6)
- Special Abilities=Normal weapon immunity after shifting into tiger; Infect (Intensity 7)
- Habitat=Human villages, forests
- Languages=Regional
- Perception=Five senses (Illumination)

A weretiger is a lycanthrope with the power to shapeshift into a tiger.

#### [ Redcap ]

- Monster Level=3
- Rarity=12
- Agility=14    Movement Speed=14
- Number=One to several    Frequency=Rare
- Intellect=Low    Reaction=Adversarial
- Attack Points=Weapon：10 (3)    Strike Points=9
- Evasion Points=11 (4)    Defense Points=6
- Life Points／Resistance=15／11 (4)
- Mental Points／Resistance=15／11 (4)
- Special Abilities=Infection by gaze (Intensity 5)
- Habitat=Uncertain
- Languages=Regional
- Perception=Five senses

A redcap is a patient suffering from the disease of the same name, red cap, and whose depth has reached 2 or greater. See here for details on this disease.

## 13.3 Converting Character Data to Monster Data

Using the rules presented here, a game master can convert data created as a character into the format of a monster. There are two advantages to doing this.

### [ 1. The number of times the game master has to roll dice during combat will be drastically reduced ]

The game master will be freed from the labor of rolling dice, and will be able to manage enemy data in combat more easily. It'll also give you more time to provide guidance to players who are unfamiliar with the rules.

This is especially effective when there are many enemies.

### [ 2. Enemy strike rolls can no longer critical ]

If an enemy's strike roll is a critical, resulting in heavy damage or even death, the player may feel frustrated that they've been killed by a roll of the dice. This is because it's a process that cannot be dealt with by the player. If you change the enemy character's data to that of a monster, the damage will be a fixed score called strike points, so this kind of frustration should be less frequent.

So, let us show you how.

- Adventurer level adapts directly to monster level.
- Rarity seems unnecessary, so we'll omit it.
- Agility and movement speed use the character's agility ability score as it is.
- Attack points are the character's attack power + 7.
- For strike points, apply strike power to Table 13-1: Key Number = Expected Equivalents, then add bonus damage to the result. Critical target is normally 10, but if using the optional rule 16.2: Weapon and Armor Modifiers to have variation in a weapon's critical target, please look at the appropriate column.
- Evasion points are the character's evasion speed + 8.
- For defense points, apply defense power to the Key Number = Expected Equivalents table (No Critical), then add adventurer level to the result.
- Life points and mental points use the ability scores​​ life force and mental power as they are.
- Life point resistance and mental point resistance are each resistance +8.

The reason evasion points are calculated with +8 is because in combat between characters, if the attacker and the evader have the same final scores, the attack will fail, but between a character and a monster, the attack will hit. This is the same reason why resistance score is calculated with +8.

#### Table 13-1: Key Number = Expected Equivalents

| Critical Target 9 | Critical Target 10 | Critical Target 11 | Critical Target 12 | No Critical | Expected Value |
|---:|---:|---:|---:|---:|---:|
| 0–1   | 0–2   | 0–3   | 0–4   | 0–5   | 2  |
| 2–5   | 3–7   | 4–9   | 5–10  | 6–11  | 3  |
| 6–9   | 8–12  | 10–14 | 11–16 | 12–17 | 4  |
| 10–13 | 13–17 | 15–20 | 17–22 | 18–23 | 5  |
| 14–18 | 18–22 | 21–25 | 23–27 | 24–29 | 6  |
| 19–22 | 23–27 | 26–31 | 28–33 | 30–35 | 7  |
| 23–26 | 28–32 | 32–36 | 34–39 | 36–41 | 8  |
| 27–31 | 33–37 | 37–42 | 40–45 | 42–47 | 9  |
| 32–35 | 38–42 | 43–47 | 46–50 | 48–50 | 10 |

## 13.4 Representing Special Monsters with Character Data

Among monsters, there are some that have inherently strong individual differences. Take, for example, dark elves. These monsters, like adventurers, come in a variety of strengths, so it'd be more natural to describe them by their ability scores ​​and skill levels like adventurers.

Here, in order to represent monsters such as featherfolk, mermen, dark elves, noble lizardmen, and centaurs as characters, we'll show how to calculate the sub-ability scores ​​of each monster (Table 13-2: Determining Monster Sub-Ability Scores).

These rules were not designed with the idea of playing monsters as characters in mind. Please be careful.

#### Table 13-2: Determining Monster Sub-Ability Scores

| Sub-Ability Score | Featherfolk | Merman | Dark Elf | Noble Lizardman | Centaur |
|---|---|---|---|---|---|
| A | 2D    | 2D    | 1D+6 | 2D    | 2D   |
| B | 1D+6  | 1D+6  | 1D+6 | 1D+3  | 2D   |
| C | 2D    | 2D    | 1D+6 | 2D    | 2D   |
| D | 2D    | 2D    | 1D+6 | 2D    | 2D   |
| E | 1D+3  | 1/2D  | 1D   | 2D    | 1D+6 |
| F | 2D    | 2D    | 1/2D | 2D+6  | 1D+6 |
| G | 1D+2  | 2D    | 1D+4 | 2D    | 1D+6 |
| H | 2D+6  | 1D+6  | 1D+6 | 2D    | 1D   |

Note: A dark elf can add +4 to mental power resistance due to the blessings of the dark gods.

A noble lizardman's entire body is covered in scales which adds +5 to defense power.

## 13.5 Monster Level and Adventurer Level

A monster's monster level is a rough guide to its strength when it appears in a scenario. A monster level's score is basically set so that if it's equal to a character's adventurer level, the character will be stronger. If they're 1-2 levels higher, you'll be evenly matched, and if they're 3 levels higher, they'll be a formidable enemy.

When introducing them into a scenario, assume that enemies of the same or 1 level lower than a character's adventurer level will appear frequently, while an enemy of 2-3 levels greater will appear at the climax.

Of course, combat balance will vary depending on the special abilities of the monsters and the composition of the party. In particular, monsters that use magic are, without exception, more formidable enemies than their level suggests. Please consider this only as a guideline.

The monster level of a monster can also be used as a scale to express the size of an event (Table 13-3: Monster Level／Event Scale Comparisons).

In the case of NPCs as enemies, consider them to be two levels greater. A 3rd level dark priest is a level that would be too spicy for a novice adventurer.

#### Table 13-3: Monster Level / Event Scale Comparisons

| Level  | Event Scale |
|---|---|
| 1–2    | It's no big deal. Just a small problem in a small village |
| 2–4    | A crisis in a small village. Cue the novice adventurers. |
| 5–6    | Too spicy for a novice adventurer |
| 7–8    | A difficult enemy unless you're a moderate adventurer |
| 9–10   | A city-wide crisis |
| 11–13  | A nation-wide crisis |
| 14–15  | An Alecrast-wide crisis |

## 13.6 Handling Monster Special Abilities

Some monsters have numerous special abilities. Next, we will list these abilities and how to handle them in-game.

### 13.6.1 Special Attacks: Those That Make Mental Power Resistance Rolls

**《 Magic 》** — Monsters with this ability can use magic at the indicated level and magic intensity (magic power). Those with this ability often have an intellect equal to or greater than that of a human, and although they have their own preferences for which magic they use, they do not use it foolishly.

**《 Hypnotism 》** — This is the ability to hypnotize opponents. The targeted character must make a mental power resistance roll against the indicated target score. If you fail, you'll be manipulated at your opponent's will.

**《 Gaze／Ray 》** — This attacks opponents with a gaze or a ray. The targeted character must make a mental power resistance roll against the indicated target score. If you fail, you'll suffer the effects as indicated.

In some cases, the gaze or ray can be reflected off a mirror, etc. but if this is not specified, it cannot be reflected.

**《 Possess 》** — This is an ability used by the undead monster known as the haunt. The targeted character must make a mental power resistance roll against the indicated target score. If you fail, your body will be possessed. A haunt who has possessed a body can also use that character's abilities.

**《 Curse 》** — This is an attack method that brings disaster to those involved. There are several processes by which a curse can be brought about (such as normal physical attacks, by gaze, etc.), but in all cases you must ultimately make a mental power resistance roll against a set target score. If you fail, you will be affected by the curse. There are various types of curses. A typical mummy's curse prevents the recovery of all ability score reductions, including life force and mental power.

**《 Scream 》** — This lets out a ghastly scream, dealing damage to those who hear it. A character who hears this at point-blank range without first wearing earplugs must make a mental power resistance roll against the indicated target score, and will suffer the effects on a failure.

In the case of mandrake and alraune, you cannot attack or cast spells for one full round, and you will suffer a -4 penalty to evasion. At this time, if you roll double ones on the resistance roll, you will immediately go mad and become disabled. Furthermore, those who fail the resistance roll must make another one, this time a life force resistance roll, and if he or she fails, he or she will lose his or her hearing. At this time, if you roll double ones on the resistance roll, your life force will immediately become 0.

**《 Roar 》** — This is the dragon's special ability, to let out a roar that trembles the souls of those who hear it. It has no effect unless you hear it, but everyone who does hear it must make a mental power resistance roll. If you fail, you will suffer the effects specified on Table 5-5: Fears.

**《 Fire Breath 》** — Monsters with this ability can breathe fire. Characters exposed to the fire (the range of the fire varies by monster) will suffer damage. This damage cannot be prevented by armor, it can only be reduced by adventurer level and magical defense. You must also make a mental power resistance roll against the indicated target score, which if successful will result in a smaller amount of damage. (Strike power will be reduced by 10, and a critical will not occur)

**《 Stone／Wind Cutter 》** — The spirits, gnome and sylph, have this ability, and it's treated as damage magic. In other words, a strike roll damage check is made, and a successful mental power resistance roll will reduce strike power and prevent a critical from occurring.

**《 Disintegrate 》** — The spirits, will-o-wisps and shade, will disintegrate upon the slightest shock (for instance, by bumping into a character, etc.). At this time, the character will suffer damage to both their life force and mental power. This is treated as damage magic. In other words, a strike roll damage check is made, and a successful mental power resistance roll will reduce strike power and prevent a critical from occurring.

### 13.6.2 Special Attacks: Those That Make Life Force Resistance Rolls

**《 Poison 》** — Among monsters, there are some that carry a variety of poisons. When attacked by these monsters, you must make a life force resistance roll, using the indicated toxicity score as the target score. If you fail, you'll suffer an effect depending on the poison. Unless it's a poison that applies immediately (mainly damage), it can be treated with the holy magic Cure Poison or Refresh, or the spirit magic Restore Health.

For detailed rules regarding poison, please refer to 12.2.1: Poisons.

In the case of a poison that deals damage, if the resist is successful, then unless it's specified that no damage will be dealt, the effect will not be completely removed, it will merely reduce the strike power by 10 (and prevent criticals).

**《 Parasitism​ 》** — Among monsters, some can affect a character's central nervous system and take over their body. If you're attacked by a monster with this ability, you must make a life force resistance roll against the indicated target score. If you fail, your body will be taken over.

### 13.6.3 Special Attacks: Other

**《 Disease 》** — Some monsters bring about disease. The spirit power of a monster is balanced differently than that of a human, and can always cause illness. However, in most cases the infection power of this information imbalance is weak, so it doesn't pose much of a problem, but if a character is bitten by a bat or rat, it's highly contagious, so there's a high chance he or she will become ill.

When you're dealt damage by a monster with this ability, roll 2D and compare it with the progression intensity of each illness. If your roll is less than the progression intensity, you will be infected with the disease. Illnesses can be treated using the holy magic Cure Disease and Refresh, and the spirit magic Restore Health.

For detailed rules regarding illnesses, please refer to 12.2.2: Illnesses.

**《 Strangling 》** — This is an ability that many monsters have. If an attack with this ability is successful, then in subsequent rounds, the character will remain strangled, and the only thing he or she can do is try to escape.

To escape, make a success roll using adventurer level + strength bonus as the baseline score. The attack points of the attack is the target score (or the attack points of the hit, if using the optional rule to give monsters variance in attack points). If you succeed, you can break free, but if you fail, you'll automatically suffer damage at the end of the round. This is treated as normal damage, so it's possible to reduce it due to armor.

While being strangled, a character suffers a -4 penalty to evasion and is normally unable to make sound. Depending on the monster, the penalty may be smaller, or it might be possible to still make sound, but if this is the case it'll be specified in the description. Unless otherwise noted, the evasion penalty is -4 and magic is also considered not possible.

If a character is strangled and another is trying to rescue him or her by attacking, please refer to the optional rule for grappling for how to handle it.

**《 Capture 》** — This is similar to strangling, but it does not deal any damage. To escape, you must make the same check as for strangling. Normally you cannot move while captured, but in some special cases, this rule may be limited.

Regarding the process when another tries to rescue by attacking, it's the same as strangling.

**《 Entangling 》** — Sprays an adhesive, high-strength thread, etc. that binds a character. The character must make a success roll using adventurer level + strength bonus as the baseline score in order to escape. Each time you fail, you'll normally become more and more entangled, and the target score will increase each time. If the difference between the baseline score and the target score reaches 13 or greater, the character will be unable to escape on his or her own, and will eventually suffocate to death. Whether or not another can rescue them, by attacking or burning the thread, depends on the monster. In the case of the giant webspinner, which is a typical monster that performs this attack, it's almost impossible to cut the thread. Otherwise, if possible, defense points, destruction points, etc. are set for cutting the thread. When a thread is cut, damage will also be applied to the entangled character at the same time.

**《 Swallow Whole 》** — Swallow a character whole, digesting them. A swallowed character cannot escape until the monster is dead. Thus, during this time he or she will continue to suffer the set amount of damage (which can only be reduced by adventurer level) each round. A swallowed character can also attack from inside, if he or she has a dagger, shortsword, or similar small bladed weapon. In this case, make a hit check with a penalty of attack power -4, and if it hits, make a damage check as normal.

If you make an attack from outside to rescue a character inside, and kill the monster, (the same amount of) damage will be dealt to the character inside.

**《 Bloodsuck 》** — Automatically deals damage each round. This damage cannot be reduced by armor, only adventurer level and magical defense can help. At this time, the monster is eating the character. For this reason, when it's attacked by another, please refer to grapple.

**《 Acid 》** — Spits strong acid that deals damage. If it hits, you cannot make a resistance roll. Damage cannot be reduced by armor, only adventurer level and magical defense can help. Whether acid can deal damage to armor (for example, reduce defense by 1 point each time it hits, etc.) is the choice of each game master. Normally, the game will be easier to progress if it has no effect.

**《 Corrosion 》** — Automatically deals damage every round using acid or gas. This damage cannot be reduced by armor, only adventurer level and magical defense can help.

Magic that creates a curtain, such as Water Screen or Missile Protection, may be able to block or reduce the damage.

**《 Steal Mental Power 》** — At the same time a normal attack hits, mental power will also be damaged. This damage cannot be reduced by armor, only adventurer level and magical defense can help. This is an ability that undead normally have, and a character whose mental power is reduced to 0 by this attack will die instantly and will be resurrected as an undead (wight, vampire, etc.) 24 hours later.

**《 Iron Corrosion 》** — Acid or gas that corrodes iron. Life force will not be damaged, but metal weapons and armor will suffer damage, and become worn out and useless after a certain amount of time. Silver and magic weapons and armor are usually not affected.

### 13.6.4 Special Defense Abilities: Resistance to Weapons, Etc.

**《 Physical Attack Immunity 》** — Since it has no substance, it has no life points, so any attack methods that deal damage to life points (weapons, damage magic, etc.) are ineffective. It's also not affected by poison and illness.

You cannot touch this kind of monster directly, but it is possible to cast spells with a distance of touch.

**《 Weapon Immunity 》** — Attacks with weapons, no matter how powerful they are, or even if they're magical weapons, will have no effect at all. Even in combat between monsters, it's not possible for monsters that only have attack methods similar to weapons, such as fangs or claws, etc. to fight against them.

**《 Normal Weapon Immunity 》** — A silver or magical weapon is needed to defeat them. Normal weapons, no matter how powerful, cannot deal damage. In the case of combat between monsters, if a monster can also only be wounded by silver or magical weapons, or has a greater monster level than its opponent, it can deal damage to such a monster.

**《 Complete Immunity to Certain Weapons 》** — There are types of weapons that are completely ineffective due to their form, material, etc. Attacks with the indicated weapon, no matter how powerful or magical it is, will have no effect at all. Even in combat between monsters, if an opponent monster's attack method is equivalent to an ineffective weapon, it will not deal damage.

**《 Weapons Cannot Critical 》** — Weapons do not deal additional damage from criticals.

**《 Certain Weapons Cannot Critical 》** — There are weapons that cannot deliver effective strikes due to their form, etc. Attacks with the indicated weapon, no matter how powerful or magical it is, will never cause a critical.

**《 Darkness／Invisible 》** — They're very difficult to hit with a weapon, because they're under the cover of darkness, invisible, etc. When attacking such an enemy with a weapon you'll suffer a -4 penalty to attack power (points). If you have the ability to see in darkness or through invisibility, etc. you will not suffer this penalty.

**《 Keen Perception/Airborne 》** — They have keen perception and react very well to approaching weapons, etc., or can move quickly through the air. Therefore, they're difficult to hit with a weapon, so when you attack with a weapon, you'll suffer a -2 penalty to attack power (points).

**《 Water Adaptation 》** — Adapted to water. Characters will suffer a penalty according to 10.4: Water Combat, but monsters with this ability can act underwater without any penalty.

Some monsters with this ability may not be able to go on land at all, or may not be suited for land combat, so they'll suffer a -4 penalty to attack and evasion.

**《 Ice Adaptation 》** — Adapted to ice, and can act on ice fields without penalty. Characters suffer a -2 penalty to attack and evasion, even if they're equipped for ice.

**《 Snow Adaptation 》** — Adapted to snow, and can act in snow fields without penalty. Characters suffer a -2 penalty to attack and evasion, even if they're equipped for snow and cold.

### 13.6.5 Special Defense Abilities: Resistance to Magic and Similar Attacks

**《 Mental Attack Immunity 》** — Monsters, etc. that do not have intellect or mind have this ability, so magic with mental effects (Fear, etc.) is ineffective. If they do not have mental points (expressed as ー), magic that deals damage to mental points (Shade, etc.) is likewise ineffective.

**《 Sleepless 》** — They do not require rest or sleep in the usual sense. Therefore, they can never be put to sleep by magic, etc.

Monsters with this ability also automatically recover mental points. Recovery is 1/24th of mental points (rounded up) every hour.

However, vampires cannot automatically recover mental points.

**《 Certain Magic Resistant 》** — Resistant to some magic. This primarily means that damage magic cannot cause criticals. Please refer to each monster's description for further details.

**《 Fire Immunity 》** — Fire attacks are completely ineffective. Magic that deals damage with fire (Fire Bolt and Fireball) is completely useless, and the strike power bonus of Fire Weapon is also not added. If one of these monsters also has the ability normal weapon immunity, it cannot be wounded by a weapon that had Fire Weapon cast on it.

**《 Strong to Fire 》** — Resistant to fire attacks, so for magic that deals damage with fire (Fire Bolt and Fireball), checks are made at -10 to strike power (the strike power bonus of Fire Weapon is completely ineffective). Even if one of these monsters has the ability normal weapon immunity, it can still be wounded by a weapon that had Fire Weapon cast on it. However, strike power will be 0.

If you cast magic with a strike power of 10 on one of these monsters, such as Fire Bolt, and they resist it, you cannot make a strike roll and the damage dealt will only be magic power.

**《 Cold Immunity 》** — Cold-type attacks are completely ineffective. Magic that deals damage with cold (Ice Storm, etc.) is completely useless, Ice Coffin and Freeze are also ineffective.

**《 Strong to Cold 》** — Resistant to cold-type attacks, so for magic that deals damage with cold (Ice Storm, etc.), checks are made at -10 to strike power. Cold-based magic that does not deal damage (Ice Coffin and Freeze) will still take their usual effects.

In addition to these, if it says XX immunity, it's completely useless, and if it says strong to XX, damage magic checks are made at -10 to strike power.

### 13.6.6 Special Defense Abilities: Other Bonuses and Resistances

**《 Life Point Regenerate 》** — Has the powerful ability to regenerate life points. The indicated number of life points will automatically regenerate each round. Once life points reach 0, handling differs depending on each monster. Most die as is, but some are special, such as vampires.

**《 Regenerate 》** — The hydra has the ability to regenerate even if its heads are cut off. At the same time its life points are recovered, its number of attacks will also be restored.

**《 Not Affected by Poison and Illness 》** — Certain mythical beasts, magical beasts, undead powered by negative life, and pseudo-life forms created by magic, are free from poison and illness. These monsters are not affected by poison and illness. Ancient magic that alters the atmosphere (XX Cloud) is also ineffective.

**《 Camouflage 》** — Monsters with this ability disguise themselves in a particular way, wait for a victim to approach, then strike when he or she is not careful. To discover this, you must succeed on a resistance roll against the indicated target score using ranger skill level + intelligence bonus as the baseline score. If you fail, you'll suffer a surprise attack, with a -4 penalty to your evasion speed for one round, and you cannot counterattack or use magic. From the second round onwards, it'll be normal combat.

**《 Shapeshift 》** — It has the ability to shapeshift. This completely changes its appearance, so unless something stands out, it cannot be discovered with the sage's knowledge or the ranger's plant and animal check.

**《 Clairvoyance 》** — The mythical beast lynx has a sharp clairvoyance ability. For this reason, even if a character lurks in a place that's hidden from view, etc. he or she will be discovered instantly. Please note that this ability does not mean it'll be able to see behind it.

**《 Summon 》** — It has the ability to summon monsters of the same or different species. It can revive something that's already fallen, or summon from across space. This ability can be used even while performing other attacks, etc.

**《 Web 》** — Spiders, etc. can generate sticky webs. If a character inadvertently steps into it, he or she must make a resistance roll using adventurer level + agility bonus as the baseline score, and if he or she fails they'll be caught in the web. To escape from this state, you must make a resistance roll using adventurer level + strength bonus as the baseline score, similar to escaping from capture. Otherwise, you'll suffer a penalty based on the strength of the web.

### 13.6.7 Special Defense Abilities: Weaknesses

Different monsters have different weaknesses against certain kinds of attacks.

**《 Needs Bloodsucking to Maintain Life Points 》** — In order to maintain its life points, a lamia must suck human blood. Otherwise, it'll gradually weaken and die. It's treated as a weakness, but takes the form of an inconvenient habit.

**《 Needs Bloodsucking to Maintain Mental Points 》** — In order to maintain its mental points, a vampire must suck human blood. Otherwise, it'll gradually lose its mental points and eventually perish. It's treated as a weakness, but takes the form of an inconvenient habit.

**《 Damage From Healing Magic 》** — Undead that act with negative life force will suffer damage from healing magic that grants positive life force. They will suffer damage from Cure Wounds, and if Healing or Refresh are cast on them and they fail to resist, their life points will immediately become 0.

**《 Weak to Fire 》** — This is a weakness seen in plant-type monsters, dry monsters, and monsters that live in cold regions. They're weak to fire, so checks are made at +10 to strike power when using fire attacks. In the case of Fire Bolt, make a strike power 20 damage check (10 if the monster successfully resists), and in the case of Fire Weapon, add a +20 strike power bonus to the weapon.

In addition, for any other Weak to XX, checks against damage magic are made at +10 to strike power.
