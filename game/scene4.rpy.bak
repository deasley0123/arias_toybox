label scene4:
    call scene_transition("The Weald part II")
    scene bg forest afternoon with fadehold
    # TODO: Bog beast cut-in front and center
    j "So, what are you going to name him?"
    n "You and Aria left the secluded bog, returning to something like a path through the forest. Or the weald, as the young girl calls it."
    n "The sun is high above you now, sending bright yellow-orange tinted light down through the trees."
    n "Aria holds up the \"Bog Beast,\" examining him with a tilt of her head."
    show aria think mclose:
        zoom 0.5
    show aria:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(3000.0, 400, 0.0) 
        linear 0.15 matrixtransform ScaleMatrix(1.1, 1.0, 1.0)*OffsetMatrix(1017.0, 400, 0.0)
        linear 0.10 matrixtransform ScaleMatrix(0.95, 1.0, 1.0)*OffsetMatrix(1017.0, 400, 0.0)
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1017.0, 400, 0.0)
    a "Hmm... Well, a formidable warrior such as this one deserves an equally fearsome name."
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1017.0, 400, 0.0)
    show aria at grey_out
    # TODO: toad croak
    n "The large angry-looking toad croaks at her, but makes no attempt to wriggle out of her grasp."
    show aria think shock mopen at restore_color
    a "I know!"
    show aria think mischief mcat at grey_out
    n "She stops walking, so suddenly that you nearly run into her."
    show aria smile proud mwideopen at restore_color
    show aria:
        zoom 0.7
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(855.0, 336, 0.0) 
    a "Jophiel! Since you helped so much in our quest, you deserve the honor of naming our new companion!"
    show aria smile proud mclose
    python:
        bogbeastname = renpy.input("Name the Bog Beast:", length=9)
        bogbeastname = bogbeastname.strip()
        if not bogbeastname:
            bogbeastname = "Bog Beast"
    show aria at grey_out
    j "How about \"[bogbeastname]\"?"
    show aria exhult jumping mopen at restore_color
    a "I love it!"
    show aria at grey_out
    n "She clears her throat, then brings the toad close, looking him in the eye, snout to snout."
    show aria stars intent mopenwide at restore_color
    a "Oh mighty Bog Beast, stalwart guardian of the Weald Queen's domain..."
    show aria stars intent mcat:
        subpixel True zoom 0.85 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(657.0, 183, 0.0) 
    a "Thy name is..."
    show aria stars intent intensifies:
        subpixel True zoom 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(450.0, 12, 0.0) 
    show aria at shaking
    a "{shader=jitter:3.0,3.0}[bogbeastname]!!!{/shader}"
    show aria:
        zoom 0.7
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(855.0, 336, 0.0) 
    show aria at grey_out
    b "*Ribbit*"
    show aria exhult jumping mopen at restore_color # TODO: Aria shaking then to the moon
    show aria at shaking
    a "He loves it too!"
    show aria tell secret mopen at restore_color
    a "Excellent choice, Jophiel."
    show aria tell secret mclose at grey_out
    j "Happy to help."
    show aria smile wave mclose # TODO: Add a new generic smiling Aria neutral pose, maybe arms behind leaning forward big smile
    n "You resume walking together. Aria holds [bogbeastname] in her hands for a while before the toad begins to struggle."
    show aria neutral wave mopen at restore_color
    a "What's wrong, [bogbeastname]? Do you need to use the little bog beast's room?"
    show aria neutral slightwave mclose at grey_out
    n "She grips him a little tighter. The toad produces a slightly angrier croak."

    if bond1 == False:
        n "You remember reading a book about parenting, back when you thought you might have kids one day."
        n "It said, {i}Children have to learn to be kind to others.{/i}"
    else:
        n "You remember her story about the tuna, the undead fish swimming around in a pit until it began to stink."
        n "\"{i}Mom didn't see much of a difference either way,\"{/i}\nAria had said."

    j "Hey, if he wants you to let him go, you have to let him go."
    show aria unfortunate slightwave mopen at restore_color
    a "B... But I don't want him to run away!"
    show aria unfortunate slightwave mclose at grey_out
    n "You nod seriously, and bite your lip to keep from smiling. You feel for this kid. It took you until your last breakup to finally learn this lesson yourself."
    n "You kneel down next to her so that you can look her face to face. You gently place your hands over hers."
    show aria reluctant hold arm mclose lookup
    j "You can't make anyone stay in your life unless they want to, Aria."
    j "If you give them the choice to stay, and they decide to leave, that's sad, but it's okay. It isn't your fault."
    # TODO: Shake the toad ci
    n "You pause. The toad wriggles, but she isn't holding him so tightly that she'll hurt him."
    show aria reluctant hold arm mclose lookdown
    n "She seems to be considering your words."
    j "Now if they want to leave, and you don't let them... well, you know how it feels when you're forced to do something you don't want to do, right?"
    show aria reluctant hold arm mopen lookup at restore_color
    a "Yeah..."
    show aria reluctant hold arm mclose lookup at grey_out
    n "She squeezes just a little tighter, for a moment."
    n "Then she sets the toad on the ground."
    b "*Ribbit*"
    # TODO: Bog beast goes away
    n "The toad looks around himself, then hops into a nearby fern."
    show aria disappointed hold arm mslight lookdown
    n "Aria sighs, and sniffles."
    show aria disappointed hold arm mslight lookup
    j "I bet he can still hear you. Do you want to tell him anything before he goes?"
    show aria disappointed hold arm mopen lookup at restore_color
    a "Bye, [bogbeastname]. I really wanted you to be my familiar."
    show aria disappointed hold arm mslight lookdown 
    a "..."
    show aria reluctant hold arm mopen lookup
    a "But if you want to keep guarding your lair, I guess that's okay too."
    show aria reluctant hold arm mclose lookup at grey_out
    j "He is the Weald Queen's stalwart guardian, after all."
    show aria reluctant hold arm mopen lookat at restore_color
    a "Yeah. He probably has lots of responsibilities."
    show aria reluctant hold arm mclose lookdown at grey_out
    j "Definitely."
    show aria close hug anxious at reset with dissolve
    show bg forest afternoon:
        subpixel True blur 8.0 
    with dissolve
    show aria at restore_color
    show aria:
        subpixel True zoom 0.95 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-45.0, -288, 0.0) 
    n "All at once, the young girl hugs you. The surprise of it nearly knocks you over." with vpunch
    show aria at grey_out
    menu:
        "Return her hug.":
            jump choice_2_1
        "Wait until she lets go.":
            jump choice_2_2

label choice_2_1:
    $ bond2 = True
    show aria at restore_color
    n "You're soft at first, worried a stray claw might dig into her if you aren't careful."
    show aria close hug recovering
    n "But, after a moment, you hold her as tightly as she holds you."
    n "She's so small."
    show aria close hug comforted
    n "Her heart beats so fast. Her arms feel so fragile around your neck."
    n "Eventually she releases you, and you let her go."
    jump resume_2
label choice_2_2:
    $ bond2 = False
    show aria at restore_color
    n "The hug shouldn't surprise you so much. You're her favorite doll, after all. Who else would she go to for comfort?"
    show aria close hug sad
    n "Even so, you can't bring yourself to hug her back. You just let her hold you until she's ready to let go."
    n "Gradually, she does."
    jump resume_2

label resume_2:
    show bg forest afternoon:
        subpixel True blur 0.0
    with dissolve
    hide aria with dissolve
    show aria sad hold arm mopen eclose:
        zoom 0.7
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(300, 300, 0.0) 
    show aria at grey_out
    j "You did good. That's a tough thing to do, but it's important."
    n "She sniffles."
    show aria sad hold arm mopen lookdown at restore_color
    a "I'm going to be alone again."
    show aria at grey_out
    j "Only for a little while. Just until your mom comes back. Right?"
    show aria disappointed hold arm mslight lookdown
    n "She's quiet for a long time."
    n "She's quiet for long enough that you start to wonder if that was the wrong thing to say, somehow."
    n "That's all this was, wasn't it?"
    n "Keeping a bored, magical little girl entertained? Keeping her company while Mom is away?"
    n "You didn't sign up for any of this. You only barely signed up to take her on this quest. And only because you had no other choice."
    n "She brought you into this world, and she's your only way back."
    n "You stand up, and dust a fallen leaf off your shoulder."
    show aria reluctant hold arm mclose lookdown
    j "Well..."
    j "You're not alone right now. I'm here with you. And it isn't sundown yet."
    show aria reluctant hold arm mclose lookup
    j "So, where to next?"
    n "She watches you for a moment. The color gradually returning to her cheeks, her breath evening."
    show aria reluctant hold arm mopen lookup at restore_color
    a "There's a town not too far from here."
    show aria neutral wave mopen
    a "Upon accomplishing our quest, we should eat together together to celebrate."
    show aria neutral wave mclose at grey_out
    j "Food is good. How far?"
    j "Twenty minutes?"
    show aria point self mopen at restore_color
    a "Hmmm... I've still got..."
    show aria point self mclose at grey_out
    j "Right. Got it. Little legs."
    show aria excite hiding at restore_color
    a "Yeah."
    show aria smile showcase mopen:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(300, 336, 0.0) alpha 1.0
        linear 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -270.0, -2052.0) alpha 0.0
    a "This way!"
    n "She rushes off. You follow."
    scene bg forest afternoon with fadehold
    # TODO: Fade to black like you're moving on, then don't
    n "You walk all of three minutes before stopping again."
    show ci arboreal massacre:
        ypos -0.3
        xpos -0.0
    nvl clear
    narrator "You notice the stillness first, your whiskers twitching in the suddenly silent forest. You reach out to stop Aria, but she sees it now too." with dissolve
    narrator "Like a gash ripped through skin, the trees and underbrush in front of you are slashed and torn apart. Tree trunks lay with clumps of dirt caught in their 
    newly unearthed roots, the leaves on the branches still green where they haven't been shaken off completely."
    narrator "One of the upturned trees has claw marks like the ones Toorg and Gerald pointed out. Others are hardly recognizable as trees at all."
    nvl clear
    n "Aria's voice is even softer than it was by the pond." with dissolve
    show aria disappointed hold arm mopen lookat:
        subpixel True zrotate -36.0 
        zoom 0.7
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1857, 300, 0.0) 
        linear 1.00 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1236, 300, 0.0) 
    pause 1.1
    a "What do you think did that?"
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1236, 300, 0.0) 
    show aria at grey_out
    j "No idea. Let's try not to find out."
    show aria pout mclose lookat at restore_color
    a "But-"
    show aria:
        linear 1.00 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1857, 300, 0.0) 
    n "You put a hand to her back and turn her away from the arboreal massacre."
    show aria:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1857, 300, 0.0) 
    j "One adventure per meal. Feast first, then we'll see about this. Only fair, right?"
    show aria poutless mclose lookat reclose:
        linear 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1436, 300, 0.0) 
    a "Okay..."
    hide aria with dissolve
    n "She sighs, but her stomach rumbles pitifully."
    n "You glance back as you walk away."
    show ci2 gerald bag:
        xpos 0.0
        ypos -0.3
    show ci2 with dissolve
    n "You hope you distracted her before she noticed the bag hanging in the branches of the clawed tree."
    n "The bag that you're certain Gerald was wearing earlier."
    jump scene5