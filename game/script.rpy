# The game starts here.

# Game Play Defaults
default bond1 = False
default bond2 = False
default bond3 = False
default goHome = True
default bogbeastname = "Bog Beast"
image loading movie = Movie(play="images/anim_loading.webm", loop=True)
image starting movie = Movie(play="images/openAnim.webm", loop=False, keep_last_frame=True)
image menu loop = Movie(play="images/openAnim_Loop.webm", loop=True)
image spooktober = "spooktober_logo.png"

label splashscreen:
    scene black
    with Pause(1)

    show spooktober:
        zoom 0.7
        yalign 0.5
        xalign 0.5
    # show text "Developed for Spooktober Game Jam 2024":
    #     ypos 0.2
    with dissolve
    with Pause(2)

    # hide text with dissolve
    hide spooktober
    with dissolve
    with Pause(1)

    # $ renpy.movie_cutscene("images/openAnim.webm")
    show starting movie
    with Pause(5)

    return

label before_main_menu:
    show menu hold
    
    return

label start:
    camera:
        perspective True

    # For Debugging
    # jump scene1
    # jump scene2
    # jump scene3
    # jump scene4
    # jump scene5
    # jump scene6

    # Real start
    jump scene0

    # TODO: Do some kind of soft fade out to end?

    # This ends the game.
    return
