label scene0:
    call scene_transition("The Summoning") from _call_scene_transition_1
    play music_2 rain loop fadein 0.5
    scene black with fadehold
    narrator "It was a rainy Tuesday night."
    play music "<silence 1.5>"
    queue music tv noloop
    queue music tv_ctd loop
    narrator """
    You came home from work to your small studio apartment, changed into sweatpants, 
    grabbed a drink from the fridge and sat on the floor in front of your TV because
    it was more comfortable than your shitty IKEA couch.
    """
    narrator """
    You flipped through channels and eventually settled on a network game show you remembered 
    watching with your grandmother when you were little.
    """

    narrator "It's more commercials than content now, so you quickly got bored and started scrolling on your phone."

    nvl clear

    narrator "A friend of yours from high school posted some engagement photos. Another made a pregnancy announcement."

    narrator """
    You thought about congratulating them, but you haven't spoken to either of them in years.
    Best case scenario, they would invite you to some celebratory event you couldn't afford to attend. 
    """

    narrator """
    Besides, you've already called in enough days at work that requesting any more would probably get you fired.
    So instead you drank and kept scrolling, eyes half glazed over. 
    """

    stop music fadeout 10
    stop music_2 fadeout 10
    play music_3 summoning_buildup fadein 4.0 noloop
    narrator """
    Eventually you can't keep your eyes open at all anymore. You lean your head back against your couch
    and fall asleep, wishing you could be anyone and anywhere else.
    """

    nvl clear

    stop music
    play music_2 summoning_big_buildup noloop
    stop music_3 fadeout 4.0
    show text "When you open your eyes again, you are no longer in your apartment." at shaking_center
    n "{alpha=0.0}When you open your eyes again, you are no longer in your apartment" # This exists to set the autoplay speed right
    hide text
    jump scene1