# The game starts here.
default bond1 = False
default bond2 = False
default bond3 = False
default goHome = True
default angryMob = False

label start:
    camera:
        perspective True

    # For Debugging
    jump scene1
    jump scene2
    jump scene3
    jump scene4

    # Real start
    jump scene0

    # TODO: Do some kind of soft fade out to end?

    # This ends the game.
    return
