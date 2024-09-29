label stay_endings:
    hide ci with dissolve
    n "You almost jump out of your skin when you feel something touch your arm."
    show aria stop mopen:
        zoom 0.7
        xpos 0.2
        ypos 0.32
    a "SERENA!! Mom's gonna be really mad if she finds us down here!" with vpunch
    show aria at grey_out
    n "Aria hisses a whisper at you- {i}Serena{/i}.\nWhatever game you were playing before, even Aria has dropped it in this place."
    show aria nervous hold hat mopen lookaway at restore_color
    a "I'm {i}suuuper{/i} not allowed in mom's workshop.\nI've never been down here before. She'll know we came in."
    show aria nervous hold hat mclose lookaway at grey_out
    show aria:
        subpixel True matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)
    n "Aria is preoccupied, glancing back at the stairs. Too worried about you and now her mom, she hasn't taken a good look around yet."
    show aria nervous hold hat mclose lookat
    show aria:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)
    s "Aria, this is very bad. Where is your mom?"
    s "Where is your mom right now?"
    show aria disappointed hold arm mopen lookdown at restore_color
    a "She was already really, really, {i}really{/i} mad when I wasn't home earlier."
    show aria disappointed hold arm mslight lookdown
    a "I didn't think she'd be leaving me alone again any time soon."
    show aria disappointed hold arm mopen lookup
    a "But then she said something about \"pests in the forest\" and told me to stay here and wait until she came back."
    show aria disappointed hold arm mslight lookat at grey_out
    n "You know that your time is limited. This room, the stories you heard, the town's fears."
    n "You feel certain that if you're still here when Aria's mother returns, you will not survive."
    n "...Even if the mob arrives instead, you're pretty sure the result will be the same."
    s "Aria, I don't want to scare you, and I don't say this as a game or to hurt you."
    s "Your mom made that damage in the forest. The one who's been taking people? It's her."
    n "You take a deep, shuddering breath. And then you drop the pit from your stomach into hers."
    s "And I'm pretty sure that if I'm still here when she gets back... she'll kill me."
    show aria stop mopen
    n "Aria stares at you and stammers weakly in protest."
    show aria at restore_color
    a "No- no, you've... You've been so nice to me, and you even said you'd stay! She wouldn't!"
    show aria neutral slightwave mclose
    a "She wouldn't..."
    show aria disappointed hold arm mslight lookdown at grey_out
    s "Aria, do you remember the adventurers we met in the woods?"
    show aria disappointed hold arm mslight lookat:
        linear .2 yoffset 10
        linear .2 yoffset -10
        linear .2 yoffset 10
        linear .2 yoffset -10
        linear .1 yoffset 0
    show ci shelf behind aria with dissolve
    n "She nods. You direct her eyes up to the shelf in front of you."
    show aria:
        yoffset 0
    s "She... she's done something to them. Something very, very bad."
    s "I think I, this body, your... toy. I think I was someone else before. Someone who met the same fate as them and I don't know how many others."
    s "And when she comes back..."
    n "You swallow hard."
    s "That'll be me. Again."
    show aria disappointed hold arm mslight lookup # TODO: Do a nervous variant with smaller irises, incline the head
    n "She stares at the doll-sized people for what feels like an eternity. Her own panicked tears begin to well in her green eyes."
    hide ci shelf with dissolve
    s "I know, I know it is a lot to process. But, Aria, I have to go-"
    show aria disappointed hold arm mslight lookat
    n "She looks at you now. Her lip trembles."
    n "You take a deep breath, trying desperately to steady yourself."
    s "And I think you should come with me."
    n "You want to live, but you aren't prepared to sacrifice her to whatever life she might face here."
    n "This is also a lot of information all at once, most of it life-changing. You can see her mind spinning."
    # TODO: hide ci
    camera:
        subpixel True 
        ease 1.3 zpos -300.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-99.0, -63.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    n "You crouch down to her level, and you take her hands in yours."
    show aria disappointed hold arm mslight lookdown
    camera:
        subpixel True zpos -300.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-99.0, -63.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    j "{i}You{/i} are my Weald Queen, Aria. And I, Jophiel, am your right hand."
    j "Enemies approach us now from several fronts. As your trusted guardian, your safety is paramount to me."
    j "But I am still new to this realm, and I require your might and cunning."
    show aria disappointed hold arm mslight lookat
    j "..."
    s "Please, Aria.{p}I can't get us to safety alone."
    show aria sad hold arm mopen lookdown
    n "She considers you silently at first."
    n "The secrets you've revealed seem to have shaken her, but not to her foundations."
    n "You suspect some part of her knew already. Her imagined worlds and daring escapades a welcome distraction from her harsh reality."
    show aria sad hold arm mopen eclose at restore_color
    a "We..."
    show aria reluctant hold arm mopen lookat
    a "We probably can't just run away through the Weald."
    show aria at grey_out
    j "Right, you've got little legs."
    show aria reluctant hold arm mopen lookdown at restore_color
    a "And Mom knows the forest reaaally well."
    show aria nervous hold hat mclose lookaway at grey_out
    n "Thinking about your options, she tugs on her hat nervously."
    show aria think shock mopen at restore_color
    a "Right! My hat! The buckle!"
    show aria smile shrug mopen
    a "I'm not as skilled as Mom, but I could probably reverse the enchantment on it."
    show aria smile shrug mclose at grey_out
    j "What would that do?"
    show aria smile proud mwideopen at restore_color
    a "Rather than bring me to her, it could send us away!"
    show aria unfortunate slightwave mopen
    a "Only..."
    show aria unfortunate slightwave mclose at grey_out
    j "Only?"
    show aria serious slightwave mopen at restore_color
    a "I can't control where it goes. It might be really far from here."
    show aria serious slightwave mclose at grey_out
    n "You're silent, thinking about her suggestion when you hear the door upstairs creak open."
    show aria serious slightwave mclose lookaway
    n "The way Aria freezes, you don't have to ask who it is." with hpunch
    n "You take hold of her hands again."
    if bond1+bond2 == 2:
        show aria disappointed hold arm mslight lookdown
        j "It's okay, Aria. I'm here with you, and wherever we end up, I won't leave you alone."
        show aria disappointed hold arm mslight lookat at restore_color
        show aria:
            linear .2 yoffset 10
            linear .2 yoffset -10
            linear .2 yoffset 10
            linear .2 yoffset -10
            linear .1 yoffset 0
        n "She nods and grips your hands tighter."
        show aria close hug comforted hat glow:
            subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-135.0, -252.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        with dissolve
        n "Then she closes her eyes and pulls you close. Her buckle begins to glow with a deep purple hue."
        scene black with flash
        camera:
            subpixel True zpos 0.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        nvl clear
        narrator "In an instant, the two of you are somewhere else. It isn't easy to start over when you don't know where you are or where you're going. But the two of you are together." with fade
        narrator "Whether it be school, work, your relationships or your goals, you half-assed everything in your life before. But you throw yourself into this with determination you didn't know you had in you."
        narrator "You try to find opportunities to make Aria smile every day. It isn't easy taking care of someone else, but you can't imagine anything more worth doing."
        narrator "It's you and her in a new world. She summoned you because she needed you, and until she no longer needs you, you'll be by her side."
        nvl clear
        call ending_title("Stay", "Ending 6 of 7") from _call_ending_title_5
        return
    else:
        s "We need to go."
        show aria nervous hold hat mopen lookaway
        n "Aria hesitates one last time. You see the gears turning in her mind, but you fail to recognize it in time."
        show aria close hug anxious:
            subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-135.0, -252.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        with dissolve
        n "Then she throws her arms around you... and her hat on your head."
        show aria close hug sad
        a "Goodbye, Serena."
        scene black with flash
        camera:
            subpixel True zpos 0.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        n "She let's go, and in an instant, you are somewhere else."
        nvl clear
        narrator "It isn't easy to start over when you don't know where you are, but you throw yourself into it. You have a destination, and you won't get there without all your effort."
        narrator "You know you came from the Kaistr Weald. There is a nearby capital city, Rimmond. You even remember the town's name, Woldthwaite."
        narrator "You ask a lot of questions, more than most people can even answer, but slowly you understand the basics of this foreign world."
        nvl clear
        show 
        narrator "Once you have your bearings and save enough to buy a map, you return there. To the Weald. To Aria's cottage."
        narrator "The cottage is empty. The basement cleared out, and the attic, too. You don't know where Aria and her mother went, but the trail here goes cold."
        narrator "Without Aria, you are as unmoored in this world as you were in Cleveland. But you aren't stuck anymore, and you've proven resilient carving out a living here."
        narrator "You wanted to stay here as a second chance at living. You'll have to figure out what that means for yourself."
        nvl clear
        call ending_title("Stay...", "Ending 7 of 7") from _call_ending_title_6
        return
