label caught_snooping_ending:
    n "Your body freezes as you feel a hand on your shoulder." with hpunch
    camera:
        subpixel True 
        zpos 0.0 
        ease 3.50 zpos -300.0 
    show bg basement:
        subpixel True 
        blur 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        ease 3.5 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.1)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  blur 1.0
    pause 3.5
    n "You feel a change in the air, a pressure unlike anything you've experienced before."
    camera:
        zpos -300.0 
    show bg basement:
        blur 1.0 
    n "Some prime instinct, a fear buried deep, roots your body in place. You don't even dare to turn your face."
    mom "You're not supposed to be here." # TODO: Watson's Kinetic text dripping
    show bg basement:
        additive 0.0 blur 1.05 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.14)*SaturationMatrix(3.17)*BrightnessMatrix(0.0)*HueMatrix(234.0) 
    n "Her grip tightens on your shoulder, and you feel stabbing pain throughout your body as your soul is forcibly separated from your conscious mind." with flash
    n "You couldn't fight it even if you knew how. You can't even let out a cry of terror or pain before it is over."
    scene black with faaadehold
    n "Everything goes dark."
    # TODO: Include ending CG
    return