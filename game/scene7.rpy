image cottage main: 
    "bg aria cottage main.jpg"
label scene7:
    call scene_transition("Homecoming") from _call_scene_transition_7
    scene bg aria cottage door
    with fadehold
    n "The front door to the small cottage has no lock. You suppose there's no need, or rather, the illusion you passed through {i}was{/i} the lock."
    show cottage main behind bg
    pause 0.1
    show bg aria cottage door:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 1.0 
        linear 0.80 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 135.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) alpha 0.0 
    n "You quietly clear your throat as you swing the door open, intending to call out."
    show bg aria cottage main
    n "But the air within the cottage is silent, still, and any sound you were going to make dies in your throat."
    n "It feels wrong to break this silence. Dangerous, somehow."
    nvl clear
    narrator "There is a small hearth, fire burning gently, herbs drying on the mantle. The fading sunlight illuminates little. Most of the room remains in shadow." with dissolve
    narrator "In front of you is a staircase leading to Aria's room in the attic."
    narrator "To your left is a narrow door just barely cracked open, a soft glow bleeding along the door's edge."
    nvl clear
    menu:
        "Go upstairs":
            jump choice_6_1
        "Go through the narrow door":
            jump choice_6_2

label choice_6_1:
    n "You're fairly certain that you'll find Aria in the attic." with dissolve
    if goHome == True:
        n "Not only is it her room, but it's where the summoning circle is, and she did promise to send you home."
    scene bg cottage stairs up:
        zoom 0.7
        xalign 0.5
        yalign 0.5
    with dissolve
    n "Your ears swivel and your whiskers twitch, on keen alert as you ascend the stairs."
    n "The floorboards above you creak lightly, and you freeze."
    show bg:
        subpixel True 
        blur 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        ease 3.5 zpos 300.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.1)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  blur 1.0
    n "You can almost peer over the lip of the floorboards, so you take one more step up."
    scene bg aria attic dusk with PushMove(0.6, "pushdown")
    n "The moment you do, two little hands wrench you up the rest of the stairs with surprising strength." with vpunch
    show aria stars intent mopenwide at center
    show aria:
        zoom 0.6
        ypos 1500
        xpos 0.6
    a "Jophiel!"
    show aria at grey_out
    n "She hugs you quickly, then lets go of everything but your hand."
    show aria smile wave mopen at restore_color
    a "I'm so glad you made it back safe!"
    show aria neutral slightwave mclose
    a "When Mom summons me like that, there's nothing I can do. I'm sorry."
    show aria at grey_out
    j "Hey, it's okay. Are you alright?"
    show aria:
        linear .2 yoffset 10
        linear .2 yoffset -10
        linear .2 yoffset 10
        linear .2 yoffset -10
        linear .1 yoffset 0
    n "She nods quickly. Too quickly, as if she's trying to dismiss the question."
    if goHome == True:
        jump go_home_endings
    else:
        jump try_hiding_ending

label choice_6_2:
    n "Your heart only recently settled from fleeing the mob in the woods. It begins to race again as you approach the door."
    if goHome == True:
        n "Aria promised to take you home, and you know your ticket back is the ritual circle upstairs, but..."
    n "You need more answers than you have, and you know Aria can only tell you so much."
    scene bg cottage stairs down:
        zoom 0.7
    with fade
    n "You gently pull open the door. A series of cold, stone stairs lead you down into the earth."
    n "Every tuft of fur on your body stands, a warning. You push your fear aside and continue."
    n "An acrid, foreign stench immediately assaults your nostrils. Followed by a smell you only know from visiting your grandmother in her final days."
    show black with fade
    n "It's the smell of death."
    scene bg basement with fade
    n "You find an arcane studio of sorts.\nThere's a cauldron, a table of magical implements, books, scrolls, tinctures, and tools."
    n "...but also bits of body and flesh, jars of pieces and parts, and dolls. Shrunken forms."
    n "You step into the room, clutching at your mouth and nose. Your eyes are glued to the back. A shelf."
    show ci shelf with Dissolve(0.8)
    n "Two figures you unfortunately recognize the likeness of. A tree-person and a gnomish sort."
    n "The bile you've been holding back stings your throat as tears of fear and frustration gather in the creases of your eyes."
    if goHome == True:
        jump caught_snooping_ending
    else:
        jump stay_endings