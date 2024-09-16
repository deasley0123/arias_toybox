label scene3:
    # TODO: Add scene transition "The Bog Beast"
    scene bg bog day with fadehold
    # TODO: Finish description at start
    n "(description to be completed) Reeds, bullrush, sunlit murky pond. Lilly pads, crickets and frogsong. Canopy of trees closing over the ponds like a cathedral. Note: Been a lot of breeze, but the air is still now.. waiting"
    scene bg bog plus cut in
    show ci cattails behind bg
    n "something, something there are patches of reeds lining the sitting placid waters."
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
    # TODO: show aria lay crossed enarrow mwide
    a "I can smell him on the wind."
    # TODO: show aria lay crossed enarrow mopen
    a "I can hear his slumbering breaths."
    # TODO: show aria lay crossed surprise mopen / mclose
    n "She gasps, a small delicate thing."
    show aria lay smallwave lookat mopen
    a "Be still, he hasn't noticed us yet."
    show aria lay smallwave lookat mclose
    n "You peer over her shoulder, trying to see what she sees. You whisper back."
    j "What am I looking for?"
    n "Your mind spins with images of prehistoric behemoths, of shambling masses of vine and thorn, of every cryptid ever caught on blurry film."
    n "Glimpses of half-submerged reeds morph into sharpened dorsal spines. Moss riddled logs conceal bristling fur, crouching beasts coiled to pounce."
    # TODO: Light come down center animation, aria dissolves in.
    a "{i}His stench is his first line of defense.{/i}"
    a "{i}The scent has felled many a party before they ever reached him.{/i}"
    a "{i}Stomaching that, his next danger is his thundering, guttural call.{/i}"
    a "{i}It echoes in your mind, driving you to {shader=jitter:1.0,1.0}madness.{/shader}{/i}"
    a "{i}All of that is but harbinger of what he is capable of.{/i}"
    a "{i}His true talent lies in his camouflage. His bark-like skin itself is perfectly suited to ambush.{/i}"
    a "{i}He watches the world with patient, cunning eyes.{/i}"
    a "{i}No one who dares observe him lives to tell the tale.{/i}"
    a "{i}And yet, {shader=jitter:2.0,2.0}I see him now!{/shader}{/i}"
    n "Your fur stands on end, and you feel a hiss building in the back of your throat."
    n "Your eyes dilate to the extreme, taking in every swishing reed, every rocking lily pad."
    j "Where is he? In the water? In the trees?"
    a "{i}He reclines, perched upon his verdant throne.{/i}"
    a "{i}His mighty thighs and the crown of his brow are adorned with horns.{/i}"
    a "{i}Every muscle ripples, tensed for war!{/i}"
    n "A large toad on a lily pad catches a passing bug, tongue flashing briefly."
    n "Aria dives into the reeds."
    a "{shader=jitter:3.0,3.0}HE'S SEEN US! Now, Jophiel!!{/shader}"
    j "Now what!? All I see is some toad!" with vpunch

    jump scene4