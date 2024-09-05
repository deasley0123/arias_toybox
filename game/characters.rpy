# Declare characters used by the game.
define q = Character("???", who_style="aria_say_label", what_style="aria_say_dialogue")
define n = Character("")

define a = Character("Aria", who_style="aria_say_label", what_style="aria_say_dialogue")
define a_excite = Character(
    "Aria", 
    who_style="aria_say_label",
    what_style="aria_say_dialogue", 
    what_textshader="jitter:3.0, 3.0"
)
style aria_say_label is say_label:
    font "gui/SuperLarky-nALLR.ttf"
    color "#FFF8"
    outlines [(absolute(2), "#0009", absolute(0), absolute(0))]
    ypos 0.4
    size 38
style aria_say_dialogue is say_dialogue:
    font "gui/SuperLarky-nALLR.ttf"
    size 26
    color "#FFF"
    outlines [(absolute(2), "#000", absolute(0), absolute(0))]
    ypos 0.3
    line_spacing 3


define s = Character("Serena", who_style="serena_say_label", what_style="serena_say_dialogue")
define j = Character("Jo", who_style="aria_say_label", what_style="serena_say_dialogue")
style serena_say_label is say_label:
    font "gui/LibreFranklin-VariableFont_wght.ttf"
    color "#FFF8"
    outlines [(absolute(2), "#0009", absolute(0), absolute(0))]
    ypos 0.4
    size 38
    kerning 1
style serena_say_dialogue is say_dialogue:
    font "gui/LibreFranklin-VariableFont_wght.ttf"
    size 33
    color "#FFF"
    outlines [(absolute(2), "#000", absolute(0), absolute(0))]
    kerning 1
    ypos 0.28
    line_spacing 2
    

define narrator = nvl_narrator