# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aria", who_style="aria_say_label", what_style="aria_say_dialogue")


# The game starts here.

label start:

    scene bg attic day

    show aria smile wave:
        zoom 0.5
        xalign 0.5
        yalign 1.0

    # These display lines of dialogue.

    a "Hi there!!! My name is Aria!"

    a "We dont have a script yet..." 
    a "-so I hope you'll stay with me while you wait!"

    # This ends the game.

    return
