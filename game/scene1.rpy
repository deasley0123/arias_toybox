label scene1:
    # Bring in summoning CG, animate from dark and blurry to clear.
    show cg summoning:
        subpixel True 
        blur 20.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.14)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 
        linear 1.00 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.14)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(1.10)
    show cg summoning:
        blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.14)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    n "" with vpunch
    
    q "Hello? Helloooo? Is anyone in there?"
    q "Blink twice if you can hear me!"
    q "They're not blinking." 
    q "{shader=jitter:3.0, 3.0}THEY'RE NOT BLINKIN-{/shader}\nWait, you don't have eyelids."
    q "Uhhh... How about nodding?"
    q "Maybe with a little help..."
    scene cg summoning hand:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.14)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with dissolve
    n "A small hand reaches out to touch your head."
    n "It's warm."


    scene bg attic day with Fade(0.5, 0.5, 0.5)
    n "You sit up."
    n "Above you is an unfamiliar ceiling. Pitched wooden beams over a small attic."
    # TODO: SFX - Birdsong
    n "Early light streams golden through the window. The morning birdsong is foreign but beautiful."
    n "The walls are strewn with drawings, the uneven floor littered with books and candles."
    n "There is a small, unmade bed in the corner, a disheveled arrangement of sheets and leather tomes."

    show aria_up_from_bottom_right at shaking
    n "The owner of which peers over her hat at you, uncomfortably close now."

    hide aria_up_from_bottom_right with dissolve
    show aria excite hiding:
        subpixel True matrixanchor (0.5, 0.5) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(162.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(810, 117.0, -1881.0)*OffsetMatrix(0.0, 0.0, 288.0) 
    with dissolve
    n "You shift away, and she skitters back."
    
    show aria exhult jumping mopen
    with dissolve
    show aria exhult jumping mopen:
        subpixel True matrixanchor (0.5, 0.5) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(162.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(810, 117.0, -1881.0)*OffsetMatrix(0.0, 0.0, 288.0) 
        linear 0.4 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-126.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(828.0, 162.0, -522.0)*OffsetMatrix(0.0, 0.0, 288.0)
    with Pause(1.0)
    show aria exhult jumping mopen:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-126.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(828.0, 162.0, -522.0)*OffsetMatrix(0.0, 0.0, 288.0)
    q "Hey! You moved! That's great!! It worked!! I'm AMAZING!!!"

    show aria at grey_out
    s "Where am I? Who are you? What's going on? Why-"

    # TODO: Either a cut-in focusing on the blood circle, or a just a pan down and to the left
    n "You are becoming aware of your body in spurts. Currently seated, your hands support you."
    n "The ground feels tacky to touch, prompting you to really see it... and your hands."
    s "Why is the ground covered in blood? {shader=jitter:2.0, 2.0}WHY ARE MY HANDS PAWS?!?{/shader}"

    show aria at restore_color
    show aria smile wave mopen:
        xalign 0.3
    a "I'm Aria! You're my favorite doll!"

    hide aria
    show aria stars intent mopenwide:
        xpos 0.0
        ypos 0.0
    a "{i}\"Jophiel the Duskborn, catfolk master thief\nRight hand of the Weald Queen! Unmatched in the fields of battle AND wits-{/i}\""
    
    show aria at grey_out
    s "My name is Serena.\nI'm an Uber driver from Cleveland."
    s "What on Earth are you talking about?"

    show aria smile wave msmall at restore_color
    a "Ah! That's just the thing! You're not on {i}Earth{/i} anymore at all!"

    show aria smile wave mopen
    a "I've summoned you here, {i}Jophiel{/i}, to help me perform a mighty deed."

    show aria serious slightwave mopen
    a "We're going on a {b}{i}Quest.{/i}{/b}"

    show aria stars intent intensifies
    a_excite "AREN'T YOU EXCITED?!" with vpunch

    show aria at grey_out
    n "The young girl beams. The blood-drawn ritual circle under you is starting to dry on the raw wood planks."
    n "You make one last futile attempt at normalcy."

    show aria stars intent mcat:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, -500.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    s "Is this... is this some kind of TikTok trend? Is someone filming me right now?"

    show aria confuse shrug mclose at restore_color
    a "What's a TikTok?"

    show aria confuse shrug mopen
    a "Is it like a clock?? I don't have a clock, silly!"

    show aria serious slightwave mopen
    a "I'm not allowed around time anymore."

    show aria at grey_out
    s "..."

    show aria serious slightwave mclose at restore_color
    a "..."

    show aria at grey_out
    s "..."
    n "You change the subject."
    
    show aria smile wave mclose
    s "That hat... are you some kind of witch? Assuming any of this is real at all and it's not just a really weird dream."
    n "You had a slice of mushroom and black olive pizza last night, but they were just {i}button mushrooms{/i}, right? Not the other kind...?"
    
    show aria grin teach mopen eclose at restore_color
    a "Ahem. I am a SORCERESS, not a witch!"

    show aria grin teach mopen r_eclose lookat
    a "The hat is for style."
    show aria smirk chunibyo r_eclose
    show aria at grey_out
    n "She poses, obviously trying to appear cool.\nYou brush some dust off your knee and stand."
    n "You're a little taller than you were before, probably, although there isn't anything familiar to measure against in here."
    s "Great, so you're a sorceress, and I'm a... toy? A five-foot talking cat?"
    n "You feel the pointed ears in your hair and the weight of a long, thin tail stretching out behind you."
    show aria smirk chunibyo r_squint at restore_color
    a "Well, Jophiel-"
    show aria at grey_out
    show aria smirk chunibyo r_eclose
    s "It's Serena."
    show aria grin teach mopen r_eclose lookat at restore_color
    a "Hmmmm... That doesn't sound like much of a {i}quest{/i} name. \'Serenas\" don't really go to do great deeds."
    show aria at grey_out
    n "You almost interject about the accomplishments of the famous people on Earth who share your name."
    n "But it's not like you've ever really done anything, personally, so you bite your tongue."
    show aria confuse shrug mclose at restore_color
    a "Besides! Didn't you want to be someone else?"
    show aria at grey_out
    n "Her question is genuine in a way children's questions often are, but your pulse quickens all the same."
    s "What do you mean?"
    s "...How did you know that?"
    show aria smile wave mclose at restore_color
    a "Oh, it's a condition for my spell. I can only summon willing souls. It only works if you don't want to be who or where you are."
    show aria confuse shrug mopen
    a "I wouldn't want to pull you here if you were happy back home."
    show aria reluctant hold arm mclose lookdown
    a "Soul magic like that makes me feel icky."
    show aria at grey_out
    n "This line of conversation is making you think about yourself more critically than is comfortable."
    n "You change the subject again."
    s "What about my body here, then? Shouldn't I be soft, small, and full of cotton stuffing or something?"
    show aria smile shrug mclose at restore_color
    a "Nope! I tried this spell before with lower quality stuff, but... it didn't work out."
    show aria disappointed hold arm mopen lookup
    a "I HAD a rocking horse."
    show aria salute mopen
    a "Maple Stirrup, you will be remembered."
    show aria smile shrug mclose
    a "I didn't really expect it to work with YOU either, but it's probably because Mom made Jophiel for me."
    show aria smile shrug mopen
    a "She's a much more powerful Sorceress than me, so you must be made of quality stuff!"
    show aria exhult jumping mopen
    a "As soon as your soul took root, you became big like that!"
    show aria at grey_out
    s "Wow. Okay. So many questions about that. A lot to unpack there."
    n "You sense an opportunity. If her mother is a powerful sorceress as well, maybe she could fix whatever is going on here and send you home?"       
    s "So, uh, your mom is around then? I think we might be in need of some parental supervision."
    show aria disappointed hold arm mslight lookdown at restore_color
    a "No, Mom is away conducting her research. She's been away for a while. It's just me here while she's gone."
    show aria at grey_out
    n "Aria's smile falls away for the first time since you woke. Her clear discomfort around this question gives you pause, but you push ahead regardless."
    s "Oh, well, if she's been away for a while then that must be our quest? Let's go and find your mom!"
    show aria serious slightwave mclose at restore_color
    a "No, I'm forbidden from interfering with Mom's work."
    show aria at grey_out
    s "Oh. Then-"
    show aria grin teach mopen eclose at restore_color
    a "Our quest is something of far greater, far NOBLER importance!"
    show aria at grey_out
    s "Well, maybe-"
    show aria stars intent mopenwide at restore_color
    a "Within this forest lies a creature foul and perverse.\nTo battle it is to court danger.\nTo challenge it is foolhardiness personified."        
    show aria stars intent mcat
    a "BUT IT MUST BE DONE! THE BOG BEAST MUST BE CAPTURED!"
    show aria stars intent intensifies
    a_excite "AND IF IT IS NOT BY OUR HAND, THEN BY WHOSE!?"
    show aria at grey_out
    s "Anyone's! Yours! But not mine! I don't even have hands!?"
    show aria confuse shrug mopen at restore_color
    a "But I'm not allowed in the forest without supervision."
    show aria reluctant hold arm mclose lookdown
    a "And Mom is never around to supervise me."
    show aria reluctant hold arm mopen lookat
    a "But you're an adult. You could supervise me..."
    show aria at grey_out
    n "This conversation is going nowhere. Or, at least, nowhere you want to go."
    s "Aria, please. I understand you're bored, and maybe a little lonely, but I can't stay here, okay?"
    s "I need to go home."
    show aria disappointed hold arm mslight lookdown at restore_color
    a "..."
    show aria disappointed hold arm mopen lookat
    a "I understand."
    show aria at grey_out
    s "Okay, good-"
    show aria reluctant hold arm mopen lookdown at restore_color
    a "If that's what you really want, I will send you home."
    show aria reluctant hold arm mopen lookat
    a "I promise."
    show aria reluctant hold arm mclose lookdown
    a "..."
    show aria reluctant hold arm mopen lookup
    a "But I can only open a gate between worlds when the borders are thinnest."
    show aria at grey_out
    n "You feel a sinking weight in your stomach."
    s "When's that?"
    show aria reluctant hold arm mopen lookat at restore_color
    a "Dawn and Dusk."
    show aria sad hold mopen eclose
    a "I can't send you home until tonight."
    show aria at grey_out
    n "The weight in your stomach grows."
    show aria reluctant hold arm mopen lookup at restore_color
    a "So, since I can't send you back yet anyways...\nAnd I still need adult supervision..."
    show aria excite hiding at grey_out
    n "You swallow hard and sigh. Her big eyes look up at you full of hope.\nWhen was the last time you looked at anything like that?"
    # TODO: Add aria stars excite hiding
    s "Well, I've never been on any quests before. Certainly haven't encountered any bog beasts, so I don't know how much help I'll be."
    n "Even as you're speaking, you recognize that there isn't really a choice here."
    n "You can whine and drag your feet, but the little girl in front of you is powerful enough to summon you from another world, apparently."
    n "If she wants to go on a quest, you're going on a quest. You can't even get her to call you by your actual name."
    s "But first, before any questing, my name-"
    show aria smile wave mopen at restore_color
    a "Jophiel."
    show aria smile wave mclose at grey_out
    s "Serena."
    show aria serious slightwave mopen at restore_color
    a "Jophiel."
    show aria serious slightwave mclose at grey_out
    s "..."
    s "Jo."
    show aria serious slightwave mclose at restore_color # TODO: Evaluate timing, add waits for autoplay
    a "..."
    show aria stars intent mcat at grey_out
    j "So, where is this bog beast anyhow?"
    show aria smirk chunibyo r_eclose at restore_color # TODO: Update chuni pose to use sideways vulcan over closed eye, revisit eye slight open
    a "The bog beast slumbers in the murk at the heart of this very forest."
    show aria at grey_out
    j "So... Maybe 20 minutes?"
    show aria confuse shrug mopen at restore_color
    a "More like an hour. I've got little legs."
    show aria at grey_out # TODO: Add much wider smile
    n "You consider the young girl in front of you. Her smile reaches her ears."
    n "Even if you had a choice in any of this, you'd have a tough time saying no to those bright green eyes."
    show aria exhult jumping mopen
    j "Better get moving then."
    n "With glee, she rushes to the window, throws it open, and lets down her sheets. You realize now that they've already been tied nicely for such a purpose."
    show aria at restore_color
    a "Down we go!"
    show aria at grey_out
    j "We're not gonna use the door?"
    show aria confuse shrug mclose at restore_color
    a "Mom will know if we go that way! Besides, going out the window is how you always start an adventure!"
    hide aria with dissolve # TODO: Get a bit fancier with this move out
    n "She throws you one last smile before sliding over the sill and down out of sight."
    n "You sigh once more as you toss your own leg over and look down. The house is only one floor, plus this attic, so it isn't far to go."
    show ci aria forest edge with dissolve
    n "Aria is near the forest edge a dozen meters away. She waves you on enthusiastically."
    s "Just what have I gotten myself into?"
    jump scene2