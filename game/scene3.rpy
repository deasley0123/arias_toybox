label scene3:
    # TODO: Add scene transition "The Bog Beast"
    scene bg bog day with fadehold
    # TODO: Finish description at start
    n "(description to be completed) Reeds, bullrush, sunlit murky pond. Lilly pads, crickets and frogsong. Canopy of trees closing over the ponds like a cathedral. Note: Been a lot of breeze, but the air is still now.. waiting"
    # TODO: show aria gremlin mode
    n "Aria is clambering across the ground on all fours, her face obscured by cattails."
    hide aria with dissolve
    # TODO: show ci cattails
    # TODO: various arias on the cut in. 
    # aria close smile lookat
    # aria close smile lookaway
    n "She gestures for you to crouch down next to her. You step gingerly to keep your feet from sinking in the muck."
    n "She whispers in your general direction as she peers through the reeds, but she doesn't turn her face."
    a "We're upon him now."
    a "I can smell him on the wind."
    a "I can hear his slumbering breaths."
    n "She gasps, a small delicate thing."
    a "Be still, he hasn't noticed us yet."
    n "You peer over her shoulder, trying to see what she sees. You whisper back."
    j "What am I looking for?"
    n "Your mind spins with images of prehistoric behemoths, of shambling masses of vine and thorn, of every cryptid ever caught on blurry film."
    n "Glimpses of half-submerged reeds morph into sharpened dorsal spines. Moss riddled logs conceal bristling fur, crouching beasts coiled to pounce."
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