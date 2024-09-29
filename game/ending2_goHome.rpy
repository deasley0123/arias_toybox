label go_home_endings:
    show aria point self mopen at restore_color
    a "Me? I'm fine. But we have to hurry, the suns going down!"
    show aria point self mclose at grey_out
    n "She's right. The sun is dropping low. Darkness will be here soon."
    show aria grin teach mopen r_eclose lookat at restore_color
    a "I have everything set up, already."
    hide aria
    show bg go home ritual dark
    with dissolve
    n "She settles you down in the now-familiar circle. You take what will probably be your last look around this attic." with vpunch
    n "You're oddly nostalgic for the space."
    show aria smile wave msmall:
        subpixel True zoom 0.8 
        matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(1674.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 297.0, 0.0) 
        linear 0.42 matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(792.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, -36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 297.0, 0.0) 
    with Pause(0.52)
    show aria smile wave msmall:
        matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(792.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, -36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 297.0, 0.0) 
    a "Hey."
    show aria smile wave mopen:
        subpixel True matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(280.0, -100.0, 220.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 297.0, 0.0) 
    with dissolve
    a "Are you ready to go?"
    show aria smile wave mclose at grey_out
    if bond1+bond2 == 2:
        n "Some part of you wants to pepper Aria with questions, follow up on the concerns the mob from town raised on the way here."
        show aria unfortunate wave mclose
        n "But you see how Aria is just barely holding together, resolved to honor her promise."
        n "You won't sully her effort, and you trust her. Whatever the truth may be."
        show aria smile wave mclose
        j "Yeah, I'm ready."
    else:
        n "You think of the posse in the forest, the fears they shared, the trembling hands gripping their pitchforks."
        show aria unfortunate wave mclose
        j "I didn't see your mom when I came in. Is she gone so soon after getting back?"
        show aria disappointed hold arm mopen lookdown at restore_color
        a "No, she was... mad. I don't think she's gonna leave me alone again for a bit."
        show aria disappointed hold arm mslight lookdown at grey_out
        n "You would expect her to be more excited about her mom being around more, but mostly Aria looks troubled."
        show aria disappointed hold arm mopen lookat at restore_color
        a "She only left just now to \"take care of some pests in the woods.\""
        show aria disappointed hold arm mslight lookat at grey_out
        n "Your mind spins rational explanations.\nPerhaps she's already aware of the danger and off to go and aid the town?" 
        n "Or... perhaps...\nThere is a next question to ask, but you can't quite bring it to your lips before you notice the sky growing truly dark."
        n "You may not have every answer, in fact you're not sure you want them, but you do know for certain that you can't spend any more time searching."
        n "You need to go home."
        j "That might be for the best. It's probably better for you if you don't have to explain me being here."
        j "I think I'm ready, Aria. Send me home."
    show bg go home ritual
    with dissolve
    n "You were asleep for this the first time, so you're not quite sure what to expect. You feel something like a static charge in your fur as the ritual begins."
    if bond1+bond2 < 2:
        show aria reluctant hold arm mclose lookup
    j "Thank you, Aria."
    j "Not just for sending me back, but... for bringing me here, too. I'm glad it was me you summoned."
    if bond1+bond2 == 2:
        show aria unfortunate wave mclose
        n "Her smiling facade cracks a little."
    show aria sad hold arm mopen eclose at restore_color
    a "I'll miss you."
    show aria sad hold arm mopen lookdown
    a "I'm grateful it was you, too."
    show aria reluctant hold arm mopen lookdown
    a "I hope things get better for you in Cleveland."
    show aria reluctant hold arm mclose lookup at grey_out
    j "Me too. I think they will."
    j "I may not meet the requirements for your spell anymore, but you're welcome to peer in on me in your mirror anytime."
    j "And \"Jophiel\" will still be here for you even when I'm gone."
    if bond1+bond2 == 2:
        show aria reluctant hold arm mopen lookat at restore_color
        a "I think I like Serena even better than Jophiel."
        show bg go home ritual brighter
        with dissolve
        n "You feel the magic swell beneath you. Your body grows light as your soul and conscious mind begin to separate."
        # TODO: Add in our the ending CG
        n "The last you see of this world is the tear stained smile of the young sorceress."
        scene black with faaadehold
        nvl clear
        narrator "When you woke up in your world again, it would have been easy enough to dismiss everything you experienced as nothing but a vivid dream."
        narrator "Even if you did lose far more time than usual \"sleeping.\" Even if your own body felt strangely foreign for a little while."
        narrator "Even if, around Halloween, the sight of a child in a witch hat made you choke up."
        narrator "You didn't dismiss it, though. It was real enough for you. And you were going make good on what you told Aria. You would find ways to enjoy life again."
        narrator "After all, if she was going to look in on you from time to time, you wanted to make your life an adventure."
        nvl clear
        # TODO: Go Home End card
        call ending_title("Go Home", "Ending 4 of 7") from _call_ending_title_3
        return
    else:
        show aria sad hold arm mopen lookdown at restore_color
        a "Yeah."
        show bg go home ritual brighter with dissolve
        n "You feel the magic swell beneath you. Your body grows light as your soul and conscious mind begin to separate."
        n "While you were focused on Aria, even your sensitive ears missed the footsteps on the stairs."
        show cg go home complicated:
            zoom 0.6
            matrixtransform ScaleMatrix(-1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)
        with dissolve
        n "The last you see of this world is the tear stained face of the young sorceress, gazing up, anxious, at her returned mother."
        pause 2.0
        scene black with faaadehold
        nvl clear
        narrator "You don't know what happened to her next."
        narrator "You returned to your world. If anyone noticed you were gone, they didn't show it."
        narrator "It would have been easy to dismiss everything that happened as a vivid dream. And you tried to. Even when you lost nearly a whole day \"sleeping.\" Even when your own body felt strangely foreign to you afterward."
        narrator "Even when, around Halloween, just the sight of a kid in a witch hat made your heart twist in your chest."
        nvl clear
        narrator "You told yourself it was a dream. It had to be. Aria didn't exist except as some strange corner of your subconscious."
        narrator "One that was urging you to live life a little more like it matters, maybe."
        narrator "...Or maybe just to call your mom."
        narrator "What was the other option, after all? If it was all real, if she did exist in some other world..."
        narrator "Then that hand on her shoulder was also real. And so was the look of dread in her eyes when she looked up."
        narrator "And also, just as real, was the fact that you left, and there's nothing you can do now."
        nvl clear
        narrator "\n\n\n\n\n\n\n\nSo you went back to your life. And you tried not to think about the strange dream, or the ways things might have changed if you had let them."
        nvl clear
        # TODO: Go Home... End card
        call ending_title("Go Home...", "Ending 5 of 7") from _call_ending_title_4
        return
    return