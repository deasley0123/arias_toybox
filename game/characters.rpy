# Declare characters used by the game.
define narrator = nvl_narrator
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
    color "#C8A2C8CC"
    outlines [(absolute(3), "#000C", absolute(0), absolute(0))]
    ypos 0.4
    size 38
style aria_say_dialogue is say_dialogue:
    font "gui/SuperLarky-nALLR.ttf"
    size 26
    color "#FFF"
    outlines [(absolute(3), "#000", absolute(0), absolute(0))]
    ypos 0.3
    line_spacing 3


define s = Character("Serena", who_style="serena_say_label", what_style="serena_say_dialogue")
define j = Character("Jo", who_style="jo_say_label", what_style="serena_say_dialogue")
style jo_say_label is aria_say_label:
    color "#FF964CCC"
style serena_say_label is say_label:
    font "gui/LibreFranklin-VariableFont_wght.ttf"
    bold True
    color "#FF964CCC"
    outlines [(absolute(3), "#000C", absolute(0), absolute(0))]
    ypos 0.5
    size 44
    kerning 2
style serena_say_dialogue is say_dialogue:
    font "gui/LibreFranklin-VariableFont_wght.ttf"
    size 33
    bold True
    color "#FFF"
    outlines [(absolute(3), "#000", absolute(0), absolute(0))]
    kerning 2
    ypos 0.28
    line_spacing 2

define t = Character("Toorg", who_style="toorg_say_label", what_style="toorg_say_dialogue")
define qt = Character("???",  who_style="toorg_say_label", what_style="toorg_say_dialogue")
style toorg_say_label is say_label:
    font "gui/Kalam-Bold.ttf"
    bold True
    color "#d3ea6273"
    outlines [(absolute(3), "#000C", absolute(0), absolute(0))]
    ypos 0.45
    size 44
    kerning 4
style toorg_say_dialogue is say_dialogue:
    font "gui/Kalam-Regular.ttf"
    size 36
    bold True
    color "#FFF"
    outlines [(absolute(3), "#000", absolute(0), absolute(0))]
    kerning 2
    ypos 0.25
    line_spacing -15

define g = Character("Gerald", who_style="gerald_say_label", what_style="gerald_say_dialogue")
define qg = Character("???", who_style="gerald_say_label", what_style="gerald_say_dialogue")
style gerald_say_label is say_label:
    font "gui/YatraOne-Regular.ttf"
    bold True
    color "#ff655a73"
    outlines [(absolute(3), "#000C", absolute(0), absolute(0))]
    ypos 0.5
    size 43
    kerning 4
style gerald_say_dialogue is say_dialogue:
    font "gui/YatraOne-Regular.ttf"
    size 32
    bold True
    color "#FFF"
    outlines [(absolute(3), "#000", absolute(0), absolute(0))]
    kerning 2
    ypos 0.27
    line_spacing 0

define b = Character("[bogbeastname]", who_style="bb_say_label", what_style="bb_say_dialogue")
style bb_say_label is input:
    color '#3d7a00'
    size 44
    ypos 0.0
style bb_say_dialogue is say_dialogue:
    color "#FFF"
    ypos 0.3

define m = Character("Barkeep", who_style="minotaur_say_label", what_style="minotaur_say_dialogue")
style minotaur_say_label is say_label: 
    font "gui/ShortStack-Regular.ttf"
    bold True
    color "#5286e096"
    outlines [(absolute(3), "#000C", absolute(0), absolute(0))]
    ypos 0.5
    size 46
    kerning 4
style minotaur_say_dialogue is say_dialogue:
    font "gui/ShortStack-Regular.ttf"
    size 34
    bold True
    color "#FFF"
    outlines [(absolute(3), "#000", absolute(0), absolute(0))]
    kerning 1
    ypos 0.28
    line_spacing 1

define mom = Character("Mom", who_style="mom_say_label", what_style="mom_say_dailogue")
style mom_say_label is say_label: 
    font "gui/AmaticSC-Regular.ttf"
    bold True
    color "#00c52496"
    outlines [(absolute(3), "#000C", absolute(0), absolute(0))]
    ypos 0.3
    size 50
    kerning 4
style mom_say_dailogue is say_dialogue:
    font "gui/AmaticSC-Regular.ttf"
    size 50
    bold True
    color "#FFF"
    outlines [(absolute(3), "#000", absolute(0), absolute(0))]
    kerning 3
    ypos 0.28
    line_spacing 1
