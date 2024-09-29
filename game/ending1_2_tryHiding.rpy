label try_hiding_ending:
    show aria serious slightwave mopen at restore_color
    a "For now, mom is waaaaay too mad to tell her about you."
    show aria stop mopen
    a "She said she'd be right back. You gotta hide before she returns!"
    show aria nervous hold hat mclose lookaway at grey_out
    n "Aria fidgets, nervous, then she glances at her open toybox."
    show aria think shock mopen at restore_color
    a "That will work! Since it was a toy before, your body should be able to..."
    hide aria with dissolve
    n "She waves her hand and you feel your body quiver. Your limbs go numb as they shrink tight to you." with hpunch
    n "In an instant, you fall to the floor, doll-sized once more." with vpunch
    show bg box view:
        zoom 1.05
    show ci box view
    with dissolve
    n "Aria picks you up and deposits you inside her toy box. You see through your eyes, but your mouth does not move."
    show aria stop mopen lighting behind ci
    show aria stop mopen lighting:
        subpixel True zoom 0.8 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 765.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with dissolve
    a "I'm so, so, soooooo sorry, but this will just be for a bit! Just until Mom cools off!"
    show aria stop mclose lookup lighting
    n "As if on cue, you hear a door downstairs."
    show aria stop mshh lighting
    a "Shhhhh!"
    scene black 
    with PushMove(0.6, "pushdown")
    n "Aria closes the lid on the box. The world goes dark."
    n "At first you hear nothing."
    n "Then, unintelligible snippets of an increasingly fiery argument."
    a "{shader=jitter:3.0,3.0}No! NO!{/shader} You can't do this, Mom!!"
    a "She's my friend! {shader=jitter:3.0,3.0}She's my friend!!{/shader}"
    mom "When will you learn, Aria? You're not allowed to play with your food."
    show cg caught hiding:
        zoom 0.6
    with dissolve
    n "The box cracks open. Aria sobs. You see a hand reaching in towards you."
    n "Then, in and instant, you see and feel nothing at all."
    pause 2
    call ending_title("Try Hiding", "Ending 2 of 7") from _call_ending_title_1
    return