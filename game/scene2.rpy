label scene2:
    call scene_transition("The Weald part I") from _call_scene_transition_2
    scene bg aria cottage day with fadehold
    n "The house you were summoned into is a small cottage in a clearing, surrounded on all sides by forest."
    n "You leave it behind, still and silent, after watching Aria magic the bundled sheets back up through her window."
    scene bg forest morning with fade
    n "You walk through the brush at first but quickly hit a narrow path."
    # TODO: Stetch Goal - Add a transform that throws up three different close renders of Aria with great interest at different angles across the screen
    n "Aria runs ahead and back, to and fro, eyeing every tree, bush, and rock with profound interest."
    n "Your mind wanders."
    nvl clear
    narrator "The more you walk, the more you're certain you don't {i}feel{/i} like a doll. Granted, you've never been a doll before, but you're pretty sure even the most carefully made dolls don't have vocal cords, or ears that twitch toward new sounds, or tails that swish to keep balance, or stomachs that flip every time the girl in the witch hat rounds a bend out of your sight." with dissolve
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
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 1.0
        linear 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -270.0, -2052.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 0.0
    n "Aria sprints forward again, disappearing from view."
    hide aria with dissolve
    n "You glance around again. The trees rustle with another breeze. Slowly, your tail smooths out."
    n "Hardly expecting a response, you cup your paws together around your mouth and call out."
    j "Do you actually know where we're going?"
    show aria grin teach mopen r_eclose lookat at reset
    show aria:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-2007.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.15 matrixtransform ScaleMatrix(1.1, 1.0, 1.0)*OffsetMatrix(-1017.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(0.95, 1.0, 1.0)*OffsetMatrix(-1017.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1017.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    a "Yep!"
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1017.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show aria at grey_out
    j "Shi- uh, geez! Hi, Aria."
    j "How do you know the way? Do you walk out here with your mom sometimes?"
    show aria reluctant hold arm mopen lookup at restore_color
    a "No, this is my first time."
    show aria at grey_out
    j "Okay. So, then... are you {i}sure{/i} you know where we're going? This is, um... the Great Weald, after all. Seems pretty big. Easy to get lost."
    
    show aria smile shrug mopen at restore_color
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-100.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
    a "It's gigantic!" 
    show aria smile showcase mopen:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-100.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.50 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(638.0, 0.0, -801.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with dissolve
    a "But don't worry, Jophiel. I have this!"
    show aria smile showcase mclose at grey_out
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(638.0, 0.0, -801.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
    show ci mirror at reset
    n "She holds up something smooth, ornate, and reflective. As she turns it, it catches a beam of sunlight."
    j "A mirror?"
    show aria grin teach mopen eclose at restore_color
    a "A {i}magic{/i} mirror. It shows anything I ask it to. That's how I've kept track of the bog beast, deep in his murky lair."
    show aria confuse shrug mclose
    a "That's how I know about your world, too. Your people have strange magic."
    show aria confuse shrug mopen
    a "I like watching the big colorful monsters chase each other around. Why do you let them eat you?"
    show aria confuse shrug mclose at grey_out
    j "I don't... what? What monsters?"
    show aria stars intent mopenwide at restore_color
    a "You know, the big shiny ones! They have black feet that roll, and sometimes they beep like weird birds!"
    show aria smile proud mwideopen
    a "And people jump right into their mouths, but I've seen the monsters spit them out too. They're all over the place there."
    show aria tell secret mopen
    a "They even sleep outside your houses at night. Are they your pets?"
    show aria tell secret mclose at grey_out
    j "Are... are you talking about cars?"
    show aria stars intent intensifies at restore_color
    a "Are you a beast-master? Do you and these 'cars' share a special bond?"
    menu:
        "Cars are just machines.":
            jump choice_1_1
        "Play along.":
            jump choice_1_2
    jump resume_1

label choice_1_1:
    $ bond1 = False
    show aria at grey_out
    j "Uh... no."
    j "Cars aren't beasts, they're not alive.\nThey're just machines."
    show aria confuse shrug mopen at restore_color
    a "What's a \'machine\'?"
    show aria confuse shrug mclose at grey_out
    j "It's a tool. A big, complicated tool."
    j "I do drive one for work, but I kind of hate it."
    show aria reluctant hold arm mopen lookdown at restore_color
    a "Oh. They seem neat, but maybe that's just through the mirror."
    show aria reluctant hold arm mclose lookup at grey_out
    j "I mean, there are some nice cars. I originally started my job to save for a good one."
    j "But now I think I'd be happiest to never get in a car again."
    show aria reluctant hold arm mopen lookat at restore_color
    a "...Does it stink in their mouth?"
    show aria at grey_out
    j "They're still not alive.\n...but yes."
    jump resume_1

label choice_1_2:
    $ bond1 = True
    show aria at grey_out
    j "Not every car-mancer does, but I'd like to think me and my car have a special bond, yeah."
    show aria at restore_color
    hide ci mirror with dissolve
    show aria:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(638.0, 0.0, -801.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.20 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    a "Really? What's their name?"
    show aria at grey_out
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    j "Well, the breed is what's known locally as a \'Prius\', which is kind of a thoroughbred for my job."
    j "So, I named him Seabiscuit after this famous racehorse."
    j "Which is funny because he is {i}not{/i} fast." 
    j "But he is efficient! Which counts for something."
    show aria smile shrug mopen at restore_color
    a "Wow. I've never met a horse, but I asked Mom for a tuna one time."
    show aria at grey_out
    j "A tuna? Like, the fish?"
    show aria exhult jumping mopen at restore_color
    a "Yep! I dug a pit back behind the house and filled it with water."
    show aria reluctant hold arm mopen lookdown
    a "I thought she'd bring it home alive, but it was already dead. She didn't see much of a difference either way."
    show aria grin teach mopen eclose
    a "I really wanted to see it swim around in the pool I dug, though, so I re-animated it!"
    show aria confuse shrug mopen
    a "I got up early every day to re-apply the spell, but Mom only let me keep it until it started to stink."
    show aria confuse shrug mclose at grey_out
    j "Sounds like one heck of a birthday present."
    show aria confuse shrug mopen at restore_color
    a "Birthday?"
    show aria confuse shrug mclose at grey_out
    s "Oh. Maybe they don't have those here."
    s "In my world, every year, your friends and family celebrate the day you were born."
    s "They give you gifts, you might eat a cake together, that kind of thing."
    show aria reluctant hold arm mclose lookdown at restore_color
    a "Gifts, huh?"
    show aria reluctant hold arm mopen lookup
    a "Hmm... I'd love to have my own familiar someday."
    show aria reluctant hold arm mopen lookat
    a "A living one, I mean. I'd feed it and take it for walks."
    show aria salute mopen
    a "Like the tuna!"
    show aria excite hiding:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1.0, 945.0, 300.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.8 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1.0, 243.0, 300.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    a "If it was pretty small, it could even live in my room with me."
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1.0, 243.0, 300.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show aria at grey_out
    j "Does it get pretty lonely with your mom being gone like she is?"
    show aria at restore_color
    show aria disappointed hold arm mslight lookdown:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

    a "Yeah sometimes she's gone for a really long time."
    show aria disappointed hold arm mopen lookup
    a "I'd get pretty bored and hungry, but eventually I discovered how to create food with magic, and Mom gave me my mirror to see the world."
    show aria disappointed hold arm mslight lookat
    a "But she always says it's too dangerous for me to go out on my own."
    show aria smile wave msmall
    a "So, I'm really glad you're here with me now!"
    show aria smile wave mopen
    a "It's nice to have someone to talk to."
    # TODO: show aria slightsmile slightwave mclose
    show aria neutral slightwave mclose at grey_out
    n "She's putting on a brave face, but you can connect with the deep loneliness it's covering."
    n "You've often felt it yourself. When was the last time you spoke to someone, really?"
    jump resume_1

label resume_1:
    hide ci mirror
    hide aria with dissolve
    # TODO: chrunching brush SFX
    n "Your chat is cut short by crunching brush. Your ears swivel automatically to the sound."
    n "You hear two sets of feet approaching, one larger, one small."
    n "You have only a moment to stop and marvel at just how much your new ears can tell you before you get their voices too."
    qg "No, I'm telling you it's not possible! The gouges are too deep for a bear!"
    qt "And I'm saying you don't even hang out with bears! I've met some pretty big bears."
    qt "I had a nursery mate, a fir, who was the local rub tree for some real grizzly types."
    qt "They'd take whole chunks out of him sometimes, but, like, he never gave his safe word or anything, so I think it was all above board."
    qg "Above {i}BOARD{/i}? ...Was that a pun, Toorg? You know how I feel about puns."
    t "Aw, come on Gerald, I know you've got a sense of humor in there somewhere."
    g "No room. Too much anger, too little body."
    show gerald mclosed hdown:
        subpixel True 
        xpos 0.2
        ypos 0.3
        zoom .36
        matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(1007.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.4 matrixtransform ScaleMatrix(-1.1, 1.0, 1.0)*OffsetMatrix(450.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(-0.95, 1.0, 1.0)*OffsetMatrix(450.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(450.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    n "A gnomish sort pushes past a tree and into view."
    show gerald:
        matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix( 450.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show toorg cheeky lookat at reset
    show toorg behind gerald
    show toorg:
        zoom 0.6
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-800.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.4 matrixtransform ScaleMatrix(1.1, 1.0, 1.0)*OffsetMatrix(-90.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(0.95, 1.0, 1.0)*OffsetMatrix(-90.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-90.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    n "...then the tree pushes past the gnome. The tree-person??"
    show toorg:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-90.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show toorg at grey_out
    show gerald at grey_out
    n "Their conversation trails off as they meet your gaze."
    show aria excite hiding:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(300.0, 945.0, 300.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.8 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(300.0, 243.0, 300.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with dissolve
    a "Oh!! Greetings fellow travelers! 'Tis fate that must have brought us together."
    show aria smile wave mopen:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1398.0, 54.0, -1800.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with dissolve
    a "I am Aria of the Weald Queen's court!"
    show aria smile showcase mopen # TODO: Stretch goal, add an eclose version of this
    a "And this is {i}Jophiel the Duskborn, catfolk master thi-{/i}"
    show aria at grey_out
    j "It's just Jo. I'm chaperoning."
    show aria smile proud mopen at restore_color
    a "We are bound by venerable purpose."
    show aria stars intent mopenwide
    a "We have set upon a {shader=jitter:3.0,3.0}MIGHTY QUEST!{/shader}"
    show aria stars intent mcat at grey_out
    j "Yeah, so-"
    show aria at restore_color
    show aria stars intent intensifies:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(867.0, 54.0, -630.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    a "{shader=jitter:3.0,3.0}WE SEEK TO CAPTURE THE TERRIBLE BOG BEAST! FATED COMPATRIOTS, WILL YOU JOIN US IN THIS QUEST, OR ARE YE COWARDS?!{/shader}"
    show aria at grey_out
    show gerald squint mopen hdown:
        subpixel True matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(243.0, 108.0, 369.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show gerald at restore_color
    with dissolve
    g "Hey, whoa, chill kid. We've got some purpose of our own."
    show gerald squint mclosed hdown at grey_out
    show toorg cheeky armup lookup at restore_color
    t "I'd even say it's at least a little venerable, too."
    # TODO: Add a rim to Toorg to make him stand out a little
    show toorg cheeky armup lookat at grey_out
    show gerald mopen hdown at restore_color
    g "Yeah, Toorg and I, we're mercen- {i}Adventurers{/i} passing through the Kaistr Weald. We slept at the Beard & Brew in town last night."
    show gerald mopen hpoint
    g "Barkeep there said this neck of the woods is pretty dangerous."
    show gerald squint mopen hdown
    g "Some kind of \"green-eyed demon\" been spotted, folks disappeared."
    show gerald mclosed hdown at grey_out
    show toorg cheeky lookat at restore_color
    t "The town is offering a bounty for the creature, so we're hunting it."

    show toorg at grey_out
    show aria think mclose at restore_color
    a "A green-eyed demon??"
    show aria point self mopen
    a "Heh, I have green eyes."
    show aria think shock mopen
    a "Wait... I HAVE GREEN EYES!"
    show aria rawr mopen
    a "I'm fearsome!"
    show aria smile proud eclose mwideopen
    a "You must be looking for me!"
    show aria rawr mcat
    a "Beware! I will not go quietly."
    show aria at grey_out
    n "You glance down at the girl, then at the adventurers."
    j "Aria, didn't you say this is your first time out here?"
    show aria confuse shrug mopen at restore_color
    a "Well, yeah."
    show aria at grey_out
    j "That would make it pretty difficult to make anyone disappear from the woods, don't you think?"
    show aria disappointed hold arm mopen lookdown at restore_color
    a "Yeah..."
    show aria disappointed hold arm mslight lookdown at grey_out
    n "She says it sadly, like you've knocked the wind from her sails."
    show toorg cheeky armup lookat at restore_color
    t "Your partner's got a point. A few of them, actually."
    show toorg at grey_out
    n "He nods toward your paws. You hadn't realized it, but your claws had extended as they approached."
    show gerald mopen hpoint at restore_color
    g "And while they might be packing some potent scratchers, I don't think you're capable of that kind of damage, kiddo."
    show gerald mclosed hpoint at grey_out
    show ci tree gouged at center
    show ci:
        subpixel True zoom 0.57 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -72.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    n "The gnome gestures to a thick trunk nearby. It's bark has been raked through, leaving deep gouges in the hard wood underneath."
    show gerald mclosed hpoint at grey_out
    show aria pout mclose lookat at restore_color # TODO: aria pout, have her look opposite way
    a "(pouting) I could do it with magic."
    show aria pout mclose eclose at grey_out
    n "It would take you most of a day with an axe to {i}start{/i} to do that kind of damage to a tree of that size."
    n "You weren't sure how much to believe about the young girl's childish tale,"
    n "but you're starting to worry this Bog Beast business may be more than you bargained for."
    hide ci with dissolve
    j "Hey, maybe your Bog Beast and this Green-Eyed Demon are the same?"
    j "We could use some more hands against such a dangerous foe."
    show aria think mclose at restore_color
    a "Hmm... more company on our quest {i}WOULD{/i} be grand, but I can't hold my fellow adventurers back from their own."
    show aria confuse shrug mopen
    a "The Bog Beast doesn't have green eyes, and it has no teeth or claws among its horrors that could do this."
    show aria confuse shrug mclose at grey_out
    j "Ah. Great. Of course it doesn't."
    show gerald mopen hdown at restore_color
    g "Well, the Barkeep didn't mention a bounty for a Bog Beast, anywho."
    show gerald mclosed hdown at grey_out
    show toorg cheeky armup lookat at restore_color
    t "Best of luck on your Quest, child! We must BRANCH out from here on our own."
    show toorg cheeky lookat at grey_out
    show gerald squint mopen hdown at restore_color
    g "Alright, if you've got time to pun you've got time to march."
    # show gerald:
    #     matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix( 450.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show gerald squint mopen hpoint:
        matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(400.0, 0.0, 0.0)
        linear 0.4 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-400.0, 0.0, 0.0)
    with dissolve
    g "Let's widen our search for more signs of this demon."
    show gerald squint mopen hpoint:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-400.0, 0.0, 0.0)
    show toorg at restore_color
    show toorg cheeky lookat:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(90.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 1.0
        linear 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-730.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 0.0
    show gerald:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-400.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 1.0
        linear 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-930.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 0.0
    n "The two of them crunch off through the brush, deeper into the woods."
    hide toorg
    hide gerald
    show aria exhult jumping mopen at restore_color
    a "That was a fun break! But I hope you're ready, Jo!"
    show aria stars intent mcat
    a "Soon we shall greet our {shader=jitter:3.0,3.0}destined foe!{/shader}"
    show aria smirk chunibyo r_eclose:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(867.00, 54.0, -630.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 1.0
        linear 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -270.0, -2052.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 0.0
    pause(1.0)
    hide aria
    n "You swallow hard and step nervously after her."

    jump scene3