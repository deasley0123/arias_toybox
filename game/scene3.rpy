label scene3:    
    call scene_transition("The Bog Beast") from _call_scene_transition_3
    scene bg bog day with fadehold
    # TODO: Finish description at start
    n "The trees thin out and give way to reeds and bullrush. The ground under your feet grows muddy as you approach a murky pond, bright sunlight glinting off the water."
    scene bg bog plus cut in
    show ci cattails behind bg
    with dissolve
    n "Cricket chirps and frog song mingle on the gentle breeze. Patches of reeds sway gently, lining placid waters."
    show aria lay crossed lookaway mclose:
        zoom 0.5
        subpixel True 
        matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(899.0, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.17 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(789.4659090909091, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 41.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.15 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(692.8181818181819, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 31.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.16 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(621.9431818181819, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 41.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.16 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(542.2088068181819, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 31.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(454.62180397727275, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 41.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.14 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(332.0, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show aria behind bg
    n "Aria is clambering across the ground on all fours, her face obscured by cattails."
    show aria:
        matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(332.0, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show aria lay smallwave lookat mopen # TODO: Stretch goal, do an open-close hand gesture
    n "She gestures for you to crouch down next to her. You step gingerly to keep your feet from sinking in the muck."
    show aria lay crossed lookaway mclose
    n "She whispers in your general direction as she peers through the reeds, but she doesn't turn her face."
    show aria lay crossed lookaway mopen
    a "We're upon him now."
    show aria lay crossed enarrow mwide
    a "I can smell him on the wind."
    show aria lay crossed enarrow mopen
    a "I can hear his slumbering breaths."
    show aria lay crossed surprise mopen
    n "She gasps, a small delicate thing."
    show aria lay shush lookat
    a "Be still, he hasn't noticed us yet."
    scene bg bog close day with irisout # TODO: Stretch goal, add some vignetting or maybe some foreground reeds at the sides of our view
    n "You peer over her shoulder, trying to see what she sees."
    n "You whisper back."   
    j "What am I looking for?"
    n "Your mind spins with images of prehistoric behemoths, of shambling masses of vine and thorn, of every cryptid ever caught on blurry film."
    n "Glimpses of half-submerged reeds morph into sharpened dorsal spines. Moss riddled logs conceal bristling fur, crouching beasts coiled to pounce."
    show spotlight:
        subpixel True alpha 0.65 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.3)*SaturationMatrix(1.0)*BrightnessMatrix(0.1)*HueMatrix(0.0) 
    show aria grimace cover nose:
        zoom 0.4
    show aria at center
    with dissolve
    a "{i}His stench is his first line of defense.{/i}"
    show aria play dead mopen eopen
    a "{i}The scent has felled many a party before they ever reached him.{/i}"
    show aria tell secret mopen
    a "{i}Stomaching that, his next danger is his thundering, guttural call.{/i}"
    show aria rawr mopen
    a "{i}It echoes in your mind, driving you to {shader=jitter:1.0,1.0}madness.{/shader}{/i}"
    show aria serious slightwave mclose
    a "{i}All of that is but harbinger of what he is capable of.{/i}"
    show aria excite hiding
    a "{i}His true talent lies in his camouflage. His bark-like skin is perfectly suited to ambush.{/i}"
    show aria rawr mslight lookaway
    a "{i}He watches the world with patient, cunning eyes.{/i}"
    show aria rawr mslight lookat
    a "{i}No one who dares observe him lives to tell the tale.{/i}"
    show aria stars intent intensifies # TODO: Make Aria move in closer at the end, maybe incrementally with the last few?
    a "{i}And yet, {shader=jitter:2.0,2.0}I see him now!{/shader}{/i}"
    hide aria
    hide spotlight
    with dissolve # TODO: I think we should go for that vignette here too
    n "Your fur stands on end, and you feel a hiss building in the back of your throat."
    n "Your eyes dilate to the extreme, taking in every swishing reed, every rocking lily pad."
    j "Where is he? In the water? In the trees?"
    scene bg bog close plus cut in
    show ci cattails behind bg
    show aria lay crossed enarrow mopen:
        zoom 0.5
        matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(332.0, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show aria behind bg
    with dissolve
    a "{i}He reclines, perched upon his verdant throne.{/i}"
    show aria lay crossed enarrow mwide
    a "{i}His mighty thighs and the crown of his brow are adorned with horns.{/i}"
    show aria lay crossed surprise mopen
    a "{i}Every muscle ripples, tensed for war!{/i}"
    show aria at grey_out
    n "A large toad on a lily pad catches a passing bug, tongue flashing briefly."
    show aria at restore_color
    show aria:
        subpixel True 
        matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(332.0, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 36.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.50 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(998.0, -54.0, 0.0)*RotateMatrix(0.0, 0.0, 306.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    n "Aria dives into the reeds."
    show aria excite hiding:
        subpixel True 
        matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(287.0, 783.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.50 matrixtransform ScaleMatrix(-1.0, 1.0, 0.0)*OffsetMatrix(287.0, 468.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    a "{shader=jitter:3.0,3.0}HE'S SEEN US! Now, Jophiel!!{/shader}"
    hide aria
    show bg bog close day
    with dissolve
    j "\'Now\' WHAT!? All I see is some toad!" with vpunch
    # TODO: Add minigame transition
    nvl clear

    jump minigame_transition

label scene3_last_line:
    j "...Are you serious?"
    jump scene4