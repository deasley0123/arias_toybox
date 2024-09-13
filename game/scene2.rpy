label scene2:
    # TODO: Add scene transition "The Weald part I"
    scene bg aria cottage day with fadehold
    n "The house you were summoned into is a small cottage in a clearing, surrounded on all sides by forest."
    n "You leave it behind, still and silent, after watching Aria magic the bundled sheets back up through her window."
    scene bg forest morning with fade
    n "You walk through the brush at first but quickly hit a narrow path."
    n "Aria runs ahead and back, to and fro, eyeing every tree, bush, and rock with profound interest."
    n "Your mind wanders."
    nvl clear
    narrator "The more you walk, the more you're certain you don't {i}feel{/i} like a doll. Granted, you've never been a doll before, but you're pretty sure even the most carefully made dolls don't have vocal cords, or ears that twitch toward new sounds, or tails that swish to keep balance, or stomachs that flip every time the girl in the witch hat rounds a bend out of your sight."
    narrator "Even your paws... they {i}are{/i} paws, complete with retractable claws just like a cat would have. But your... fingers? They curl and flex with more dexterity than you'd expect. You have no problem picking up and holding a stick when you try."
    narrator "Your eyesight is better, too. You could never afford one of those 4K TVs, but you imagine they'd be like this. Colors seem brighter, details clearer. You can see and hear every leaf rustling in the breeze. It's a little overwhelming, actually."
    nvl clear
    narrator "Especially as you notice, these trees... they don't look like any trees you've ever seen. You're not a nature buff or anything, you doubt you could tell an oak from an aspen, but you've never seen leaves shaped like these, or bark that forms in quite this way. The forest is still a palette of greens and browns, sunlight filtering through the canopy and rippling across the forest floor, but even then... Is the sunlight a little more orange than you remember?"
    narrator "It's the moss on a stone you pass that finally does it. The moss is light purple, studded with tiny blooms of the deepest blue you've ever seen in a plant. It's the sort of thing you'd expect to see at the bottom of the ocean, or maybe on an alien planet in a video game, but not here. You reach out to touch it, and it feels just like moss. You scratch some of it off the stone with your dexterous new claws. It falls to the ground in a small clump."
    nvl clear
    narrator "\n\n\n\n\nYou didn't realize it until now, but some part of you was treating all of this as an extremely vivid dream.\n\nEven as you settled into this new body.\n\nEven as a child explained the rules of soul-summoning.\n\nEven as you watched that same child do actual magic in front of you, effortlessly levitating those sheets."
    nvl clear
    j "Holy shit."
    j "This is real. This is actually happening."

    show aria_jump_up_from_middle
    with vpunch
    a "Yeah! Isn't it great?"

    hide aria_jump_up_from_middle
    show aria exhult jumping mopen:
        zoom 0.5
        offset (420, 200.0)
    show aria at grey_out
    n "You'd whispered it to yourself, unaware that Aria had ambled her way back to you."
    n "At her voice, you jump slightly. Your tail puffs out as every hair stands on end."

    show aria smile wave mopen at restore_color
    a "This is the Great Weald where the Queen oversees her realm."
    show aria serious slightwave mopen
    a "Its beauty only tarnished by the darkness that lurks in its deepest depths."
    show aria at grey_out
    j "... The Bog Beast?"
    show aria stars intent intensifies at restore_color
    a "THE BOG BEAST!"
    show aria smirk chunibyo r_eclose
    
    show aria smirk chunibyo r_eclose:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -270.0, -2052.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with dissolve
    hide aria with Dissolve(1.0)
    n "Aria sprints forward again, disappearing from view."
    n "You glance around again. The trees rustle with another breeze. Slowly, your tail smooths out again."
    j "Do you actually know where we're going?"
    a "Yep!"
    j "Do you walk out here with your mom sometimes?"
    a "No, this is my first time."
    j "Okay. So, then... are you {i}sure{/i} you know where we're going? This is, um... the Great Weald, after all. Seems pretty big. Easy to get lost."
    a "It's gigantic! But don't worry, Jophiel. I have this!"
    n "She holds up something flat, smooth and slightly teardrop-shaped. As she turns it, it catches a beam of sunlight for a brief moment and reflects it into your eyes."
    j "A mirror?"
    a "A {i}magic{/i} mirror. It shows anything I ask it to. That's how I've kept track of the bog beast, deep in his murky lair."
    a "That's how I know about your world too. Your people have strange magic."
    a "I like watching the big colorful monsters chase each other around. Why do you let them eat you?"
    j "I don't... what? What monsters?"
    a "You know, the big shiny ones! They have black feet that roll, and sometimes they beep like weird birds!"
    a "And people jump right into their mouths, but I've seen the monsters spit them out too. They're all over the place there."
    a "They even sleep outside your houses at night. Are they your pets?"
    j "Are... are you talking about cars?"
    a "Are you a beast-master? Do you and these 'cars' share a special bond?"
    menu:
        "Cars are just machines.":
            jump choice_1_1
        "Play along.":
            jump choice_1_2
    jump resume_1

label choice_1_1:
    j "Uh... no."
    j "Cars aren't beasts, they're not alive.\nThey're just machines."
    a "What's a \'machine\'?"
    j "It's a tool. A big, complicated tool."
    j "I do drive one for work, but I kind of hate it."
    a "Oh. They seem neat, but maybe that's just through the mirror."
    j "I mean, there are some nice cars. I originally started my job to save for a good one."
    j "But now I think I'd be happiest to never get in a car again."
    a "...Does it stink in their mouth?"
    j "They're still not alive.{p}...but yes."
    jump resume_1

label choice_1_2:
    j "Not every car-mancer does, but I'd like to think me and my car have a special bond, yeah."
    a "Really? What's their name?"
    j "Well, the breed is what's known locally as a \'Prius\', which is kind of a thoroughbred for my job."
    j "So, I named him Seabiscuit after this famous racehorse."
    j "Which is funny because he is {i}not{/i} fast." 
    j "But he is efficient! Which counts for something."
    a "Wow. I've never met a horse, but I asked Mom for a tuna one time."
    j "A tuna? Like, the fish?"
    a "Yep! I dug a pit back behind the house and filled it with water."
    a "I thought she'd bring it home alive, but it was already dead. She didn't see much of a difference either way."
    a "I really wanted to see it swim around in the pool I dug, though, so I re-animated it!"
    a "I got up early every day to re-apply the spell, but Mom only let me keep it until it started to stink."
    j "Sounds like one heck of a birthday present."
    a "Birthday?"
    s "Oh. Maybe they don't have those here."
    s "In my world, every year, your friends and family celebrate the day you were born."
    s "They give you gifts, you might eat a cake together, that kind of thing."
    a "Gifts, huh?"
    a "Hmml... I'd love to have my own familiar someday."
    a "A living one, I mean. I'd feed it and take it for walks."
    a "Like the tuna!"
    a "If it was pretty small, it could even live in my room with me."
    j "Does it get pretty lonely with your mom being gone like she is?"
    a "Yeah sometimes she's gone for a really long time."
    a "I used to get pretty bored and hungry, but then I learned how to create food with magic, and eventually Mom gave me my mirror to see the world."
    a "She always says it's too dangerous for me to go out on my own."
    a "So, I'm really glad you're here with me now!"
    a "It's nice to have someone to talk to."
    n "She's putting on a brave face, but you can connect with the deep loneliness it's covering."
    n "You've often felt it yourself. When was the last time you spoke to someone, really?"
    jump resume_1

label resume_1:
    n "Your chat is cut short by crunching brush. Your ears swivel automatically to the sound."
    n "You hear two sets of feet approaching, one larger, one small."
    n "You have only a moment to stop and marvel at just how much your new ears can tell you before you get their voices too."
    qg "No, I'm telling you it's not possible! The gouges are too deep for a bear!"
    qt "And I'm saying you don't even hang out with bears! I've met some pretty big bears."
    qt "I had a nursery mate, a fir, who was the local rub tree for some real grizzly types."
    qt "They'd take whole chunks out of him sometimes, but, like, he never gave his safe word or anything, so I think it was all above board."
    qg "...was that a pun, Toorg? You know how I feel about puns."
    t "Aw, come on Gerald, I know you've got a sense of humor in there somewhere."
    g "No room. Too much anger, too little body."
    n "A gnomish sort pushes past a tree and into view."
    n "...then the tree pushes past the gnome. The tree-person??"
    n "Their conversation trails off as they meet your gaze."
    n "The two emerge from the brush, an imposing tree-man and a gnomish sort. Their conversation trails off as they meet your gaze."
    a "Oh!! Greetings fellow travelers! 'Tis fate that must have brought us together."
    a "I am Aria of the Weald Queen's court! And this is {i}Jophiel the Duskborn, catfolk master thi-{/i}"
    j "It's just Jo. I'm chaperoning."
    a "We are bound by venerable purpose."
    a "We have set upon a {shader=jitter:3.0,3.0}MIGHTY QUEST!{/shader}"
    j "Yeah, so-"
    a "{shader=jitter:3.0,3.0}WE SEEK TO CAPTURE THE TERRIBLE BOG BEAST! FATED COMPATRIOTS, WILL YOU JOIN US IN THIS QUEST, OR ARE YE COWARDS?!{/shader}"
    g "Hey, whoa, chill kid. We've got some purpose of our own."
    t "I'd even say it's at least a little venerable, too."
    g "Yeah, Toorg and I, we're mercen- {i}Adventurers{/i} passing through the Kaistr Weald. We slept at the Beard & Brew in town last night."
    g "Barkeep there said this neck of the woods is pretty dangerous. Some kind of \"green-eyed demon\" been spotted, folks disappeared."
    t "The town is offering a bounty for the creature, so we're hunting it."
    a "A green-eyed demon?"
    a "Wait...{p}I have green eyes!"
    a "I'm fearsome!"
    a "You must be looking for me!{p}Beware! I will not go quietly."
    n "You glance down at the girl, then at the adventurers."
    j "Aria, didn't you say this is your first time out here?"
    a "Well, yeah."
    j "That would make it pretty difficult to make anyone disappear from the woods, don't you think?"
    a "Yeah..."
    n "She says it sadly, like you've knocked the wind from her sails."
    t "Your partner's got a point. A few of them, actually."
    n "He nods toward your paws. You hadn't realized it, but your claws had extended as they approached."
    g "And while they might be packing some potent scratchers, I don't think you're capable of that kind of damage, kiddo."
    n "The gnome gestures to a thick trunk nearby. It's bark has been raked through, leaving deep gouges in the hard wood underneath."
    a "(pouting) I could do it with magic."
    n "It would take you most of a day with an axe to {i}start{/i} to do that kind of damage to a tree of that size."
    n "You weren't sure how much to believe about the young girl's childish tale,"
    n "but you're starting to worry this Bog Beast business may be more than you bargained for."
    j "Hey, maybe your Bog Beast and this Green-Eyed Demon are the same?"
    j "We could use some more hands against such a dangerous foe."
    a "Hmm... more company on our Quest would be grand, but I can't hold my fellow adventurers back from their own."
    a "The Bog Beast doesn't have green eyes, and it has no teeth or claws among its horrors that could do this."
    j "Ah. Great. Of course it doesn't."
    g "Well, the Barkeep didn't mention a bounty for a Bog Beast, anywho."
    t "Best of luck on your Quest, child! We must branch out from here on our own."
    g "Alright, if you've got time to pun you've got time to march."
    g "Let's widen our search for more signs of this demon."
    n "The two of them crunch off through the brush, deeper into the woods."
    a "That was a fun break! But I hope you're ready, Jo!"
    a "Soon we shall greet our {shader=jitter:3.0,3.0}destined foe!{/shader}"
    n "You swallow hard and step nervously after her."