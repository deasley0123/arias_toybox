# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aria", who_style="aria_say_label", what_style="aria_say_dialogue")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # image aria wave = im.Scale('aria wave.png', 1080/2, 1920/2)
    show aria wave:
        zoom 0.5
        xalign 0.5
        yalign 1.0

    # These display lines of dialogue.

    a "Hi there!!! My name is Aria!"

    a "We dont have a script yet..." 
    a "-so I hope you'll stay with me while you wait!"

    # This ends the game.

    return
