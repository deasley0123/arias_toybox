label scene5:
    # TODO: Add scene transition "A Meal, Some Drinks"
    scene bg bar:
        zoom 0.5
    n "The Beard & Brew is mostly empty when you and Aria make your way inside."
    nvl clear
    narrator "It sits on the forest-side edge of a small, but respectable village. Thatch, Wood, and plaster homes and businesses dot a mercantile square. Just beyond lies cleared land littered with ripe green and gold crops, swaying in the breeze."
    narrator "A simple, but wide and well-maintained dirt road snakes through the buildings. It comes from over distant hills and continues off into a different part of the forest. One you haven't spent the better part of your day traipsing through."
    narrator "You passed a broad sign calling the settlement Woldthwaite. It's a mouthful and you doubt you'll remember it."
    nvl clear

    j "It's a nice day around supper time.\nWhy it is so empty in here...?"
    n "You don't quite realize you've said your thought aloud until the bartender responds."
    m "Welcome back! 'Tis a beautiful day out!"
    m "Most of the folks in town are gathering in the square.\nTalkin' about what to do regardin' the business in the Weald."
    m "And there's hardly a visitor passin' through this year, exceptin' yourself I suppose!"
    m "Truth be told, I didn't expect to see you back so soon, if at all, given the trouble lately."
    n "You peer down at Aria who is staring open-mouthed at the Minotaur behind the bar and his sparkling shelves of bottles."
    j "I thought you said you'd never been in town before, Aria?"
    a "I haven't."
    a "This is my first time this far from home since I moved here with mom."
    j "Uhh... sorry, sir. This is our first time in. It's a lovely place you have here, though."
    m "Thank ye~"
    m "And my gravest apologies, 'tis rare to see a cat-folk in these parts."
    m "And you're the spittin' image of one who passed through less than a dozen moons ago."
    m "The Marquis had hired them to map the Kaistr Weald. Something about a land survey and resource bookkeeping."
    m "Not the domain of an old keg-head like me!"
    n "You don't quite know what to make of any of that, but before you can form a question Aria steps forward."
    a "Hail and well-met, oh tavern-keeper!"
    a "I am Aria of the deep Weald, and this is {shader=jitter:3.0,3.0}{i}Jophiel, the Duskbo-{/i}{/shader}"
    j "Hi, I'm Jo. This is Aria. We live off in the forest North of here."
    j "Just came into town for a drink and meal after a loooong day."
    a "Upon the conclusion of our {i}GRAND QUEST{/i}, our bellies did rumble and our throats did thirst."
    a "{shader=jitter:3.0,3.0}WE MUST CELEBRATE WITH A FEAST! AND TANKARDS OF YOUR FINEST MEAD!{/shader}"
    j "Please ignore that. She's very excited and also very much shouldn't be given alcohol."
    j "We would love a plate or bowl of whatever you have hot, and a couple glasses of..."
    a "Beer!"
    j "...Milk?"
    j "Not, uh, because I'm a cat. Er, cat-folk."
    j "I just saw some cows in those fields, and she's a growing girl."
    j "And I think she mostly just drinks water made from magic which can't be great for you."
    n "The Minotaur nods and gives you a wink with a wry chuckle."
    m "Not a problem, I keep some in the storehouse out back. Give me just a moment."
    n "He disappears from view and your stomach grumbles."
    n "You pat your hip where normally your wallet would be."
    j "Uhh... Aria?"
    j "Do you, perhaps, have any money?"
    a "Nope."
    a "But fear not, Jophiel!"
    a "I prepared for this."
    n "She pulls out a large lumpy black stone and sets it on the counter."
    n "Her eyes flash and the room briefly fills with light. You recoil, but when your eyes stop watering you see a beautiful gem sitting where the rock was."
    a "Ta-da! Transmutation!"
    n "Your brain races to consider how this child could disrupt whole economies."
    j "Uhh, wow. That looks great, Aria, but it might be a bit much."
    a "Oh, Jophiel, this is merely their cut of the spoils for sponsoring our expedition!"
    n "She pats her stomach."
    a "You don't think they deserve any less, do you?"
    j "Ah, no. I suppose when you put it that way..."
    n "A meal isn't exactly a sponsorship, and this hastily made gem isn't exactly a spoil of your quest, but you are too hungry to argue."
    n "The barkeep returns with two mugs and fills a couple bowls with a heavenly smelling soup from a warm pot behind the counter."
    m "Here you are, dig in!"
    n "SOME TIME PASSES"
    n "The soup was hearty and filling, and the milk was a bit lukewarm but satisfied a deep craving you were unsure you'd want to admit to."
    a "Wow, I'm stuffed."
    j "Yeah, that really hit the spot, huh?"
    a "Definitely! That was my first soup!"
    j "Really? Being a witch- uh, sorceress and all, I kind of expected you to have a big cauldron at home."
    j "Figured your mom was the soup type."
    a "No. Mom used to bring me berries and mushrooms from the forest, but I'm {i}\"old enough to make my own food\"{/i} now."
    a "She says she doesn't have to eat food and I need to grow past this sooner or later, so I've never had a meal like this before."
    a "It was soooooo goood!!"
    n "You don't know what to make of Aria's mother, given this world you find yourself in."
    n "It'd be definite neglect to not provide a child with food where you're from, but this is a world where a little girl can conjure some from thin air."
    n "Aria doesn't seem to have a great grasp of what's normal here, and neither do you, you're realizing."
    a "Tomorrow, we should come back here!"
    a "Or, maybe, we forage and make some soup!"
    a "Find a cauldron of our own!"
    j "Soup is actually one of the only things I know how to make."
    j "I'm no pro in the kitchen, but I took a food prep class in community college."
    j "We could try-"
    n "You trail off, feeling like you're forgetting something as you notice the lengthening shadows cast by the window."
    n "The sun is still up, but dusk isn't long, now."
    n "In all the excitement of the day, you'd almost forgotten your deal. The time to go back home is almost here."
    j "We should try heading back to your house. It'll be dusk here in an hour or so."
    a "Oh."
    a "Right."
    a "I'm sorry, I forgot about our promise."
    a "..."
    a "..."
    a "I guess I won't get to try your soup?"
    n "She looks at you, and she hesitates."
    a "Unless..."
    a "Unless, maybe, you stayed?"
    a "For just a few more days?"
    a "I could send you home at any dawn or dusk, it doesn't have to be tonight."
    menu:
        "You could stay.":
            jump choice_3_1
        "You need to go.":
            jump choice_3_2

label choice_3_1:
    $ goHome = False
    n "What is your life back home, really?"
    n "You live on your own in the small flat your grandmother left you in her will."
    n "Your cheap car is paid off. Your job is just gig work. There's hardly anything in the fridge to spoil."
    n "You have nothing pressing, not even a house plant to water."
    n "Without realizing it, you'd already molded your life into a shape you could leave at any time."
    n "A break from your rut, maybe even a long one, could be for the best."
    n "Today hasn't been a relaxing one."
    n "You woke up in a strange place with a strange body and a strange child. Most of the day has been exhausting hiking through dense woods."
    n "But it all feels a little less strange now, and you feel... satisfied? Maybe happier, too, than you have in ages."
    j "You know, I'm not sure I'm in such a rush anymore."
    j "I could stay for a while."
    a "{shader=jitter:3.0,3.0}REALLY?!{/shader}"
    j "Yeah, really."
    j "We should probably make our way back before dark, though."
    jump resume_3

label choice_3_2:
    $ goHome = False
    n "You had expected this, to a degree. The thought had even crossed your mind about staying."
    n "But this world, this body, it is all so unfamiliar to you. It isn't home."
    n "While you may be in a bit of a rut back on Earth, visiting here and spending time with Aria has reminded you that truly anything is possible."
    n "Running away here will not change your life for the better, you have to go back and make those changes for yourself."
    n "And maybe you'll fail again, or it won't work out like you hoped. But it will be your life to live, not one that anyone else would make for you."
    n "Resolved, you see the longing in her eyes, and you know what you say next will break her heart a little."
    n "You also know that life comes with heartbreak as part of the package. You do your best to soften the blow."
    j "Aria, I've really enjoyed today. Together we subdued the mighty Bog Beast!"
    j "I was in a rough spot when you pulled me here, but just like [bogbeastname], I have a place I have to return to."
    j "Will you take me home?"
    a "Yeah. I can do that."
    jump resume_3

label resume_3:
    n "Before you can stand up to pay or leave, the buckle on Aria's hat begins to glow."
    a "Oh, oh, OH! Oh, no."
    a "Mom's home."
    n "The buckle glows brighter, and with a flash Aria is gone."
    j "Uh, Aria? {shader=jitter:3.0,3.0}Aria!{/shader}"
    m "What in the gods was that? Teleportation?"
    j "Uhhh, I'm really not sure. Maybe?"
    j "She is a sorceress. Said her mom was too. Mom lives out in the forest doing some kind of research in the area?"
    m "Out in the Weald? Didn't figure anyone lived out there. There's nothing but trees between here and Rimmond."
    m "The woods have always been dangerous, but the last few years have been fraught with disappearances and strange sightings."
    j "Yeah, some Green-Eyed Demon, right?"
    j "We met a short guy and a... tree-person? They mentioned something like that."
    m "Aye. They sent me a message by bluebird earlier."
    m "Said they had found a clear set of signs, a trail deeper into the Weald."
    m "Never did hear more."
    m "That's the business the town is discussing in the square."
    m "Talk is, a posse of seasoned hunters and retired knights from the farmholds around here were going to head out before dark."
    m "I intend to close up here and go with them. If that girl and her mother are out there, they may know a thing or two... or be in danger themselves."
    if goHome == True:
        n "Your only ticket home is with Aria or her mom. Whatever the danger, you've got to make it back there tonight."
    else:
        n "Aria disappearing wasn't a wrinkle you expected when you said you'd stay."
        n "But if Aria's mom is back and you're going to stick around..."
        n "Well, it would be good to cover everything with her anyways."

    m "Sounds like you have an idea of where they're living. Care to join our posse tonight?"
    menu:
        "There is safety in numbers.":
            jump choice_4_1

        "You'd rather go alone.":
            jump choice_4_2

label choice_4_1:
    $ mob = True
    j "Yeah, I'd feel better with some company. And I think I could find my way back to her place."
    n "It's true. Perhaps because she summoned you here, you feel a gentle pull to the forest. Towards Aria."
    jump resume_4

label choice_4_2:
    $ mob = False
    j "Sorry, I've had a long day and a lot to think about. I'll get there faster on my own."
    n "The Minotaur eyes you with concern but lets you leave without accosting you further."
    n "Perhaps because she summoned you here, you feel a gentle pull in your chest towards the forest. Towards Aria."
    jump resume_4

label resume_4:
    n "More than just the physical, there is an intangible void left by Aria's absence."
    n "When she's around, you're pulled along break-neck by her current. Her adventure games, her strange logic."
    n "She has more zest for life in her little finger than you've felt in years."
    n "With her gone, everything slows, and the unanswered questions of the day resurface in your mind."
    n "Unease sets in as the sun drops lower on the horizon."