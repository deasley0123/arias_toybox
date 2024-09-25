label fissure:
    call scene_transition("Homecoming")
    camera:
        zpos -20
    scene bg aria cottage dusk
    with fadehold
    n "The air is oppressively still in this clearing. The dense forest around it blocks much of the day's fading light."
    n "What light there is may just as well be coming from the moon, out full and early in the dimming sky."
    n "Your eyes still catch nearly every detail. A fallen branch here, a rustling bush there."
    n "The eyes of those with you are not so adept. Even by the torchlight that some carry, the uneven ground here is a tripping hazard."
    n "As a result, you've pulled ahead of the group and nearly reached the house yourself when you notice it."
    n "The stumbling feet and occasional curses from the group behind you have vanished completely."
    n "Your ears swivel, and then your head, but it's too late."
    show bg at shaking
    n "The ground, uneven yet stable behind you moments ago has fissured. Jagged and bottomless grooves have swallowed the posse."
    n "Some you see hanging on to crumbling ledges and roots. They look to be calling out to you, to each other for help, but no sound reaches your ears."
    n "With the barest shudder for such violence, their last remaining handholds and footholds crumble away, as does the ground beneath you."
    n "You freeze up as your body pitches downwards."
    show black with PushMove(0.6, "pushup") # TODO: Replace black with ending CG
    n "You've dreamt of falling before, but your unconscious mind could not emulate the numb terror filling you now."
    if goHome == True:
        n "The moon recedes before your grasping hand."
        n "You wordlessly realize you won't be making it home after all."
    else:
        n "The moon recedes before your grasping hand as you mutter out a silent apology to Aria."
        n "You won't be around to soothe her loneliness after all."
    
    return
    # TODO: Fissure End card