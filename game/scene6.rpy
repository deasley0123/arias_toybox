label scene6:
    call scene_transition("The Weald part III")
    # TODO: Switch for painterly video
    scene bg aria cottage dusk
    with fadehold
    n "The posse from the town is larger than you expected, but less professional than the barkeep made it sound."
    n "There are roughly two dozen able-bodied adults, mostly humans, which is somewhat surprising given Aria is the only human you'd interacted with today."
    n "But there is only one spear and two real swords to go around, with a collection of sharp farm tools and heavy mallets otherwise."
    n "Some also carry bows, but they look distinctly hand-made and somewhat crudely at that."
    n "This isn't a town of warriors. Apart from the barkeep, nobody else from the town even seems brave enough to talk to you, outsider and cat-person that you are."
    n "The barkeep does more than make up for what the posse lacks, though. Both in might for your expedition and in conversation. He makes idle chatter with you about the recent harvest (quite good) and the regional taxes (too high)."
    n "When that topic is exhausted, he asks you about yourself, and your relationship to Aria. You lie hastily that you were hired to watch over her while her mom is away, although it was through an intermediary and you haven't actually met her mom, yet."
    n "To support your story, you describe what you can of your day. Adventuring in the woods, meeting Toorg and Gerald, catching a toad, and coming to town. You fill him in as well on the damage you saw in the woods, and Gerald's bag you saw there."
    n "He was quiet while you recounted your day, only nodding along and listening patiently to you prattle, but he speaks up now. He's abrupt with you for the first time today."
    b "Why didn't you mention that earlier, at my tavern?"
    j "Sorry, I guess I should have. I just didn't want to scare the kid."
    n "At the mention of Aria and the tavern, you remember the gem she made."
    j "Oh, that's right! I also needed to give this to you. I forgot about it when she disappeared."
    j "We didn't have any money to pay you for the meal and milk, so she made you this gem."
    n "He accepts it from you with a deeply troubled look."
    j "Yeah, I'm not sure if that's enough or really counts as currency? I can ask her mom to reimburse you, maybe?"
    b "This is... she made this? Out of what?"
    j "Uh, like a rock. A normal rock as far as I could tell."
    n "He scrutinizes you like he's sizing you up. Your honesty, your capabilities, your intentions."
    j "I'm sorry I don't have better answers for you. I know basically nothing about magic."
    b "Well, I'm no mage myself, but I was a guard in the palace in Rimmond for many years before retiring here."
    b "No COURT mage could perform transmutation on this level so casually, never mind an apprentice of her age. That teleportation earlier too."
    b "This girl is... something else."
    b "I also kept something from you. There was more to the message I received from Gerald."
    b "He said the markings seemed strategic rather than instinctual. A warning for people, not beasts. There were faint traces of magic, too."
    b "I've been retired to Woldthwaite damn near 10 years. No head, no tail, no hide nor hair of anyone living out here in the Weald like this."
    n "As he waits for your response, you realize this is where this conversation was always leading."
    n "Under the cover of polite concern, he had extracted exactly what he needed to determine you were not a threat, and that Aria and her mother might be."
    b "The child had green eyes, and I'd bet anything the mother does too."
    n "You start to immediately stammer out a defense for Aria but you stop yourself."
    n "You can't outright deny she's powerful, and you haven't even seen her mom. They may be right to be suspicious."
    n "But you note the way the others in the posse have been watching you and listening to this conversation unfold. You see how they grip their weapons."
    n "This posse is starting to feel more like a mob, and you're not sure which end of the pitchfork you'll end up on."
    menu:
        "Protect Aria.":
            jump choice_5_1
        "Lead them to her.":
            jump choice_5_2
    n ""
label choice_5_1:
    n "Aria may be deeply magical, but she's just a lonely child."
    n "She only brought you here because you didn't want to be yourself. She took your lesson to heart and let [bogbeastname] go."
    if goHome == True:
        n "Even though it will mean her search for companionship continues, she's promised to honor your deal and send you home."
    else:
        n "Although it has only been a day, she's become dear to you. You decided to stay here to care for her and find purpose for yourself."
    n "She doesn't deserve a mob at her door."
    j "Hey. Aria is just an innocent little kid. I spent the whole day with her."
    j "Her magic may be the real deal, but she would never hurt anyone."
    j "I think her mom might be kind of shit at being a mom, but I'm not going to bring a bunch of armed and angry assholes to her door on a hunch!"
    b "I'm sorry, Jophiel, but that {i}hunch{/i} is what we have, and we're going to pursue it to the end."
    n "The air is still as the minotaur and the rest of the mob all watch you. A few of the members at the back start to shuffle around. Soon you'll be surrounded."
    n "You don't give them the chance. You turn and run without another thought."
    n "Despite their numbers advantage, you quickly lose them. It's simple, really."
    n "Your eyes are made for the fading light. Your feet are lighter than theirs, and your footfalls are near silent even in all the brush."
    n "Their rough voices calling for you to stop and wait have long faded away behind you when the trees grow too dense to traverse."
    n "You stop, but the tugging in your chest still directs you forwards."
    n "You scratch your head. You may not know this whole forest, but you {i}really{/i} don't remember this tight copse of trees here, so close to Aria's house."
    n "You are searching for a way around when you hear a familiar croak."
    b "*ribbit*"
    n "[bogbeastname] sits nonplussed at the base of one of the larger trees."
    n "You take a step towards him, and when you do he jumps up and {i}through{/i} the solid tree as if it isn't there."
    j "Uh... [bogbeastname]?"
    n "You reach out to the tree, and at first touch it feels real enough, but as you press on it the sensation of the bark surface starts to give way."
    n "Hesitantly, you push your way through the tree, or the illusion of one. Your fur stands on end as you do, and you feel a strange pressure in your head."
    n "It's similar to the pressure you'd feel right before your ears popped on a plane, only it's all through your skull, deep behind your eyes. It builds and builds."
    n "Until it too pops, and you're on the other side. You see Aria's cottage, a thin trail of smoke rising from the chimney, the illusion warding you away now behind you."
    j "Well, that explains why nobody has found the place."
    j "I guess I'll go in through the door this time."
    jump scene7

label choice_5_2:
    n "Unbidden, the image of Aria holding the toad too tightly comes to your mind."
    if bond1 == True:
        n "And you recall her story about reviving the dead tuna to play with."
    n "There is also, of course, the whole matter of kidnapping your soul and stuffing you in this body."
    n "Aria has a great deal of power and very little in her life to make sure she uses it safely or responsibly."
    n "Her mother isn't even around most of the time, it seems, and what you've heard of her secondhand is not exactly comforting."
    n "There's the apparent neglect of her daughter, her suspcicious \'research.\'"
    if bond1 == True:
        n "Aria even said that her mom doesn't see a lot of difference between the living and the dead."
    n "There are a lot of red flags, and if she really is an incredible sorceress too... Well, the folks in town have a strong case to ask some more questions from the source."
    j "You're... you're right to be suspicious, I think."
    j "I have a lot of unanswered questions, too. I'll take us to her house."
    j "Hopefully we can get some answers."
    j "But I need you to promise me to do for them what you've done with me here. Ask questions first."
    b "Of course! This is a hunt for a demon, and we'll not take any hasty action until we know more."
    if goHome == False:
        if bond1 + bond2 == 2:
            n "You choose to trust his words for now, but if anything starts going badly, you'll do everything you can to get Aria away to safety."
            n "You decided to stay here for her, and you won't allow her to be hurt, not while she's in your care."
        else:
            n "You choose to trust his words for now, but you start to wonder if your decision to say was such a good one after all."
    else:
        n "You choose to trust his words for now. Maybe while they're busy talking with mom, you could have Aria send you home?"
    n "Following the tugging in your chest and your memories from the day, you lead the town towards the clearing where Aria's house is."
    n "But in your path stands a dense copse of unfamiliar trees. Too dense to really fit through, and stretching on for some distance to either side."
    j "Huh. That's weird. It should be right through here, but... I don't think these trees were here this morning."
    b "Could be druid-craft at work. I think we've brought along an axe or two."
    n "A few men step forward to take swings. When the first's axe connects with a tree, all of the trees shudder and burst into mist, popping almost like balloons."
    n "Beyond, you see the familiar clearing, smoke rising from the home's chimney."
    b "Strong warding. We'd best be careful as we continue on."
    n "You follow after, a strong sinking pit in your stomach."
    jump fissure