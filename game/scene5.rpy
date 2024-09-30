label scene5:
    call scene_transition("A Meal, Some Drinks") from _call_scene_transition_5
    scene bg bar:
        zoom 0.5
    with fadehold
    n "The Beard & Brew is mostly empty when you and Aria make your way inside."
    nvl clear
    narrator "It sits on the forest-side edge of a small, but respectable village. Thatch, wood, and plaster homes and businesses dot a mercantile square. Just beyond lies cleared land littered with ripe green and gold crops, swaying in the breeze." with dissolve
    narrator "A simple, but wide and well-maintained dirt road snakes through the buildings. It comes from over distant hills and continues off into a different part of the forest. One you haven't spent the better part of your day traipsing through."
    narrator "You passed a broad sign calling the settlement Woldthwaite. It's a mouthful and you doubt you'll remember it."
    nvl clear

    j "It's a nice day around supper time.\nWhy it is so empty in here...?"
    n "You don't quite realize you've said your thought aloud until the bartender responds."
    show bartender grin eclose mopen holdout at reset
    show bartender:
        zoom 0.8
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-300.0, 0.0, 0.0)
    with dissolve # TODO: GEt fancy
    m "WELCOME IN! 'Tis a beautiful day out!" with vpunch
    show bartender grin eopen mopen
    m "Most of the folks in town are gathering in the square.\nTalkin' about what to do regardin' the business in the Weald."
    show bartender grin eopen mopen holdout
    m "And there's hardly a visitor passin' through this year, exceptin' yourself I suppose!"
    show bartender concern eopen mclose
    m "Truth be told, I didn't expect to see YOU back so soon, if at all."
    show bartender at grey_out
    show aria stars intent mopenwide at reset
    show aria:
        zoom 0.5
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1026.0, 378.0, 0.0)
    n "You peer down at Aria who is staring open-mouthed at the Minotaur behind the bar and his sparkling shelves of bottles."
    show aria at grey_out
    j "I thought you said you'd never been in town before, Aria?"
    show aria confuse shrug mclose at restore_color
    a "I haven't."
    show aria confuse shrug mopen
    a "This is my first time this far from home since I moved here with mom."
    show aria stars intent mcat at grey_out
    j "Uhh... sorry, sir. This is our first time in. It's a lovely place you have here, though."
    show bartender grin eclose mopen holdout at restore_color
    m "Thank ye~"
    show bartender regret eopen mopen
    m "And my gravest apologies, 'tis rare to see a cat-folk in these parts."
    show bartender resolute eopen mopen
    m "And you're the spittin' image of one who passed through less than a dozen moons ago."
    show bartender grin eopen mopen
    m "The Marquis had hired them to map the Kaistr Weald. Something about a land survey and resource bookkeeping."
    show bartender grin eclose mopen holdout
    m "Not the domain of an old keg-head like me!"
    show bartender at grey_out
    n "You don't quite know what to make of any of that, but before you can form a question Aria steps forward."
    show aria smile wave mopen at restore_color
    a "Hail and well-met, oh tavern-keeper!"
    show aria smile proud eclose mwideopen
    a "I am Aria of the deep Weald, and this is {shader=jitter:3.0,3.0}{i}Jophiel, the Duskbo-{/i}{/shader}"
    show aria at grey_out
    j "Hi, I'm Jo. This is Aria. We live off in the forest North of here."
    j "Just came into town for a drink and meal after a loooong day."
    show aria rawr mopen at restore_color
    a "Upon the conclusion of our {i}GRAND QUEST{/i}, our bellies did rumble and our throats did thirst."
    show aria stars intent intensifies
    a "{shader=jitter:3.0,3.0}WE MUST CELEBRATE WITH A FEAST! AND TANKARDS OF YOUR FINEST MEAD!{/shader}"
    show aria at grey_out
    j "Please ignore that. She's very excited and also very much shouldn't be given alcohol."
    j "We would love a plate or bowl of whatever you have hot, and a couple glasses of..."
    show aria exhult jumping mopen at restore_color
    a "Beer!" with vpunch
    show aria at grey_out
    j "...Milk?"
    j "Not, uh, because I'm a cat. Er, cat-folk."
    j "I just saw some cows in those fields, and she's a growing girl."
    j "And I think she mostly just drinks water made from magic which can't be great for you."
    show bartender at restore_color # TODO: bartender wink
    show bartender:
        linear .2 yoffset 10
        linear .2 yoffset -10
        linear .2 yoffset 10
        linear .2 yoffset -10
        linear .1 yoffset 0
    n "The Minotaur nods and gives you a wink with a wry chuckle."
    show bartender grin eopen mopen:
        yoffset 0
    m "Not a problem, I keep some in the storehouse out back. Give me just a moment."
    show bartender at false_hide # TODO: Get fancy
    n "He disappears from view and your stomach grumbles."
    show bartender:
        alpha 0.0
    n "You pat your hip where normally your wallet would be."
    j "Uhh... Aria?"
    j "Do you, perhaps, have any money?"
    show aria smile shrug mclose at restore_color
    camera:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.48 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-315.0, -18.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.58)
    a "Nope."
    show aria grin teach mopen eclose
    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-315.0, -18.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    a "But fear not, Jophiel!"
    show aria grin teach mopen r_eclose lookat
    a "I prepared for this."
    show aria smile showcase mclose
    show ci rock at center
    show ci rock:
        subpixel True zoom 0.4 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -108.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    n "She pulls out a large lumpy black stone and sets it on the counter."
    show ci gem
    n "Her eyes flash and the room briefly fills with light. You recoil, but when your eyes stop watering you see a beautiful gem sitting where the rock was." with flash
    show aria smile showcase mopen
    a "Ta-da! Transmutation!"
    show aria at grey_out
    n "Your brain races to consider how this child could disrupt whole economies."
    j "Uhh, wow. That looks great, Aria, but it might be a bit much."
    show aria grin teach mopen r_eclose at restore_color
    a "Oh, Jophiel, this is merely their cut of the spoils for sponsoring our expedition!"
    show aria satisfied pat stomach eopen mclose at grey_out
    n "She pats her stomach."
    show aria neutral wave mopen at restore_color
    a "You don't think they deserve any less, do you?"
    show aria smile wave mclose at grey_out
    j "Ah, no. I suppose when you put it that way..."
    n "A meal isn't exactly a sponsorship, and this hastily made gem isn't exactly a spoil of your quest, but you are too hungry to argue."
    hide ci with dissolve
    camera:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-315.0, -18.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.48 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.58)
    show bartender at un_hide
    n "The barkeep returns with two mugs and fills a couple bowls with a heavenly smelling soup from a warm pot behind the counter."
    show bartender:
        alpha 1.0
    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show aria stars intent intensifies at restore_color
    m "Here ye are, DIG IN!" with vpunch
    show bartender at false_hide
    camera:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-315.0, -18.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)  
    show aria satisfied pat stomach eclose mclose at grey_out
    with fadehold
    n "The soup was hearty and filling, and the milk was a bit lukewarm but satisfied a deep craving you were unsure you'd want to admit to."
    show aria satisfied pat stomach eclose mopen at restore_color
    a "Wow, I'm stuffed."
    show aria satisfied pat stomach eopen mclose at grey_out
    j "Yeah, that really hit the spot, huh?"
    show aria exhult jumping mopen at restore_color
    a "Definitely! That was my first soup!"
    show aria at grey_out
    j "Really? Being a witch- uh, sorceress and all, I kind of expected you to have a big cauldron at home."
    j "Figured your mom was the soup type."
    show aria pout mclose lookaway at restore_color
    a "No. Mom used to bring me berries and mushrooms from the forest, but I'm {i}\"old enough to make my own food\"{/i} now."
    show aria point self mopen
    a "She says she doesn't have to eat food and I need to grow past this sooner or later, so I've never had a meal like this before."
    show aria satisfied pat stomach eclose mopen
    a "It was soooooo goood!!"
    show aria satisfied pat stomach eclose mclose at grey_out
    n "You don't know what to make of Aria's mother, given this world you find yourself in."
    n "It'd be definite neglect to not provide a child with food where you're from, but this is a world where a little girl can conjure some from thin air."
    n "Aria doesn't seem to have a great grasp of what's normal here, and neither do you, you're realizing."
    show aria stars intent mopenwide at restore_color
    a "Tomorrow, we should come back here!"
    show aria rawr mslight lookat
    a "Or, maybe, we forage and make some soup!"
    show aria exhult jumping mopen
    a "Find a cauldron of our own!"
    show aria at grey_out
    j "Soup is actually one of the only things I know how to make."
    j "I'm no pro in the kitchen, but I took a food prep class in community college."
    j "We could try-"
    n "You trail off, feeling like you're forgetting something as you notice the lengthening shadows cast by the window."
    n "The sun is still up, but dusk isn't long, now."
    n "In all the excitement of the day, you'd almost forgotten your deal. The time to go back home is almost here."
    j "We should try heading back to your house. It'll be dusk here in an hour or so."
    show aria neutral wave mclose at restore_color
    a "Oh."
    show aria unfortunate slightwave mopen
    a "Right."
    show aria disappointed hold arm mslight lookdown
    a "I'm sorry, I forgot about our promise."
    show aria disappointed hold arm mopen lookdown
    a "..."
    show aria disappointed hold arm mslight lookdown
    a "..."
    show aria disappointed hold arm mopen lookup
    a "I guess I won't get to try your soup?"
    show aria at grey_out
    n "She looks at you, and she hesitates."
    show aria reluctant hold arm mopen lookdown at restore_color
    a "Unless..."
    show aria reluctant hold arm mopen lookup
    a "Unless, maybe, you stayed?"
    show aria reluctant hold arm mopen lookdown
    a "For just a few more days?"
    show aria reluctant hold arm mopen lookat
    a "I could send you home at any dawn or dusk, it doesn't have to be tonight."
    show aria excite hiding
    menu:
        "You could stay.":
            jump choice_3_1
        "You need to go.":
            jump choice_3_2

label choice_3_1:
    $ goHome = False
    show aria at grey_out
    nvl clear
    narrator "What is your life back home, really?" with dissolve
    narrator "You live on your own in the small flat your grandmother left you in her will."
    narrator "Your cheap car is paid off. Your job is just gig work. There's hardly anything in the fridge to spoil."
    narrator "You have nothing pressing, not even a house plant to water."
    nvl clear
    narrator "Without realizing it, you'd already molded your life into a shape you could leave at any time."
    narrator "A break from your rut, maybe even a long one, could be for the best."
    narrator "Today hasn't been a relaxing one. You woke up in a strange place with a strange body and a strange child. Most of the day has been exhausting hiking through dense woods."
    narrator "But it all feels a little less strange now, and you feel... satisfied? Maybe happier, too, than you have in ages."
    nvl clear
    j "You know, I'm not sure I'm in such a rush anymore." with dissolve
    j "I could stay for a while."
    show aria stars intent intensifies at restore_color
    a "{shader=jitter:3.0,3.0}REALLY?!{/shader}"
    show aria at grey_out
    j "Yeah, really."
    j "We should probably make our way back before dark, though."
    jump resume_3

label choice_3_2:
    $ goHome = True
    show aria at grey_out
    nvl clear
    narrator "You had expected this, to a degree. The thought had even crossed your mind about staying." with dissolve
    narrator "But this world, this body, it is all so unfamiliar to you.\nIt isn't home."
    narrator "While you may be in a bit of a rut back on Earth, visiting here and spending time with Aria has reminded you that truly anything is possible."
    narrator "Running away to this magical land will not change your life for the better, you have to go back and make those changes for yourself."
    nvl clear
    narrator "And maybe you'll fail again, or it won't work out like you hoped. But it will be your life to live, not one that anyone else would make for you."
    narrator "Resolved, you see the longing in her eyes, and you know what you say next will break her heart a little."
    narrator "You also know that life comes with heartbreak as part of the package. You do your best to soften the blow."
    nvl clear
    j "Aria, I've really enjoyed today. Together we subdued the mighty Bog Beast!" with dissolve
    j "I was in a rough spot when you pulled me here, but just like [bogbeastname], I have a place I have to return to."
    j "Will you take me home?"
    show aria disappointed hold arm mslight lookat at restore_color
    a "Yeah. I can do that."
    jump resume_3

label resume_3:
    show aria at grey_out
    n "Before you can stand up to pay or leave, the buckle on Aria's hat begins to glow."
    show aria surprised buckle glow mslight lookaway at restore_color
    a "Oh, oh, OH! Oh, no."
    show aria surprised buckle glow mslight lookat
    a "Mom's home."
    hide aria with flash
    n "The buckle glows brighter, and with a flash Aria is gone."
    j "Uh, Aria???"
    j "{shader=jitter:3.0,3.0}Aria!?!{/shader}"
    camera:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-315.0, -18.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.48 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.58)
    show bartender resolute eopen mopen at un_hide
    m "What in the gods was that? Teleportation?"
    show bartender:
        alpha 1.0
    show bartender at grey_out
    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    j "Uhhh, I'm really not sure. Maybe?"
    j "She is a sorceress. Said her mom was too. Mom lives out in the forest doing some kind of research in the area?"
    show bartender regret eopen mopen at restore_color
    m "Out in the Weald? Didn't figure anyone lived out there. There's nothing but trees between here and Rimmond."
    show bartender concern eopen mclose
    m "The woods have always been dangerous, but the last few years have been fraught with disappearances and strange sightings."
    show bartender at grey_out
    j "Yeah, some Green-Eyed Demon, right?"
    j "We met a short guy and a... tree-person? They mentioned something like that."
    show bartender regret eopen mopen at restore_color
    m "Aye. They sent me a message by bluebird earlier."
    m "Said they had found a clear set of signs, a trail deeper into the Weald."
    m "Never did hear more."
    show bartender resolute eopen mopen
    m "That's the business the town is discussing in the square."
    m "Talk is, a posse of seasoned hunters and retired knights from the farmholds around here were going to head out before dark."
    m "I intend to close up here and go with them. If that girl and her mother are out there, they may know a thing or two... or be in danger themselves."
    show bartender at grey_out
    if goHome == True:
        n "Your only ticket home is with Aria or her mom. Whatever the danger, you've got to make it back there tonight."
    else:
        n "Aria disappearing wasn't a wrinkle you expected when you said you'd stay."
        n "But if Aria's mom is back and you're going to stick around..."
        n "Well, it would be good to cover everything with her anyways."
    show bartender grin eopen mopen holdout at restore_color
    m "Sounds like you have an idea of where they're living. Care to join our posse tonight?"
    show ci2 gerald bag:
        zoom 0.7
        xpos 0.4
        ypos -0.1
    with dissolve
    show bartender at grey_out
    n "In your mind's eye, you see the ruined bit of forest again. Gerald's bag hanging there."
    j "Yeah, I'd feel better with some company. And I think I could find my way back to her place."
    hide ci2
    hide bartender
    with Dissolve(1.0)
    n "It's true. Perhaps because she summoned you here, you feel a gentle pull to the forest. Towards Aria."
    n "More than just the physical, there is an intangible void left by Aria's absence."
    n "When she's around, you're pulled along break-neck by her current. Her adventure games, her strange logic."
    n "She has more zest for life in her little finger than you've felt in years."
    n "With her gone, everything slows, and the unanswered questions of the day resurface in your mind."
    n "Unease sets in as the sun drops lower on the horizon."

    jump scene6