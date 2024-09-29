default snail_select = False
default turtle_select = False
default damselfly_select = False
default newt_select = False
default toad_select = False

image mg background = "mg-assets/mg-background.png"
image cattail = "mg-assets/cattail-idle.png"
image lilypad_bundle = "mg-assets/lilypad-bundle.png"
image snail_silhouette = "mg-assets/snail-silhouette.png"
image turtle_silhouette = "mg-assets/turtle-silhouette.png"
image damselfly_silhouette = "mg-assets/damselfly-silhouette.png"
image newt_silhouette = "mg-assets/newt-silhouette.png"
image toad_silhouette = "mg-assets/toad-silhouette.png"

image snail:
    pause 1.0
    "mg-assets/snail-sprite.png"

image turtle:
    pause 1.0
    "mg-assets/turtle-sprite.png"

image damselfly:
    pause 1.0
    "mg-assets/damselfly-sprite.png"

image newt:
    pause 1.0
    "mg-assets/newt-sprite.png"

image toad:
    "mg-assets/toad-sprite.png"

image text0 = "mg-assets/textbox0.png"
image text1 = "mg-assets/textbox1.png"
image text2 = "mg-assets/textbox2.png"
image text3 = "mg-assets/textbox3.png"
image text4 = "mg-assets/textbox4.png"
image text5 = "mg-assets/textbox5.png"
image text6 = "mg-assets/textbox6.png"
image text7 = "mg-assets/textbox7.png"

image toad_ani_idle:
    "mg-assets/animations/toad-blink-1.png"
    pause 0.1
    "mg-assets/animations/toad-blink-2.png"
    pause 0.1
    "mg-assets/animations/toad-blink-3.png"
    pause 0.1
    "mg-assets/animations/toad-blink-4.png"
    pause 0.1
    "mg-assets/animations/toad-blink-1.png"
    pause 1.0
    "mg-assets/animations/toad-croak-1.png"
    pause 0.2
    "mg-assets/animations/toad-croak-2.png"
    pause 0.2
    "mg-assets/animations/toad-croak-3.png"
    pause 0.2
    "mg-assets/animations/toad-croak-4.png"
    pause 0.2
    "mg-assets/animations/toad-croak-5.png"
    pause 0.2
    "mg-assets/animations/toad-croak-6.png"
    pause 0.2
    "mg-assets/animations/toad-blink-1.png"
    pause 3.0
    repeat

image toad_ani_hover:
    "mg-assets/animations/toad-blink-hl-1.png"
    pause 0.1
    "mg-assets/animations/toad-blink-hl-2.png"
    pause 0.1
    "mg-assets/animations/toad-blink-hl-3.png"
    pause 0.1
    "mg-assets/animations/toad-blink-hl-4.png"
    pause 0.1
    "mg-assets/animations/toad-blink-hl-1.png"
    pause 1.0
    "mg-assets/animations/toad-croak-hl-1.png"
    pause 0.2
    "mg-assets/animations/toad-croak-hl-2.png"
    pause 0.2
    "mg-assets/animations/toad-croak-hl-3.png"
    pause 0.2
    "mg-assets/animations/toad-croak-hl-4.png"
    pause 0.2
    "mg-assets/animations/toad-croak-hl-5.png"
    pause 0.2
    "mg-assets/animations/toad-croak-hl-6.png"
    pause 0.2
    "mg-assets/animations/toad-blink-hl-1.png"
    pause 3.0
    repeat

image cattail_ani_idle:
    "mg-assets/animations/cattail-sway-2.png"
    pause 1.0
    "mg-assets/animations/cattail-sway-3.png"
    pause 1.0
    "mg-assets/animations/cattail-sway-2.png"
    pause 1.0
    "mg-assets/animations/cattail-sway-1.png"
    pause 1.0
    repeat

image cattail_ani_hover:
    "mg-assets/animations/cattail-sway-hl-2.png"
    pause 1.0
    "mg-assets/animations/cattail-sway-hl-3.png"
    pause 1.0
    "mg-assets/animations/cattail-sway-hl-2.png"
    pause 1.0
    "mg-assets/animations/cattail-sway-hl-1.png"
    pause 1.0
    repeat

transform cattail_center:
    xpos 0.37 ypos 0.245
    zoom 1.25

transform reveal_position:
    xalign 0.5 yalign 0.7

transform slide_down:
    xalign 0.5 yalign 0.001
    ease 1.0 yalign 0.7
    pause 1.0
    linear 1.0 alpha 0.0

transform slide_up:
    xalign 0.5 yalign 0.7
    ease 1.0 yalign 0.001
    pause 1.0

transform toad_reveal:
    xalign 0.47 yalign 0.35
    pause 3.0
    linear 1.0 alpha 0.0

transform toad_position:
    xalign 0.47 yalign 0.35

define fade = Fade(0.5, 0.0, 0.5)

label minigame:
    python:
        if snail_select and turtle_select and damselfly_select and newt_select:
            toad_select = True
    call screen mg

    #screen used for main minigame in order to access image buttons
    screen mg:
        add "mg-assets/mg-background.png"
        add "mg-assets/flowered-lilypad.png" align(0.5, 0.6) zoom 0.75
        add "mg-assets/textbox1.png" align(0.5, 1.0)

        #snail button
        if snail_select:
            add "mg-assets/cattail-snail.png" align(0.85, 0.5)
        else: 
            imagebutton:
                idle "cattail_ani_idle"
                hover "cattail_ani_hover"
                align(0.85, 0.5) 
                action [Jump("snail_reveal"), Hide("mg")]

        #turtle button
        if turtle_select:
            add "mg-assets/cattail-turtle.png" align(0.65, 0.01)
        else: 
            imagebutton:
                idle "cattail_ani_idle"
                hover "cattail_ani_hover" 
                align(0.65, 0.01) 
                action [Jump("turtle_reveal"), Hide("mg")]

        #damselfly button
        if damselfly_select:
            add "mg-assets/cattail-damselfly.png" align(0.35, 0.01)
        else: 
            imagebutton:
                idle "cattail_ani_idle"
                hover "cattail_ani_hover" 
                align(0.35, 0.01) 
                action [Jump("damselfly_reveal"), Hide("mg")]

        #newt button
        if newt_select:
            add "mg-assets/cattail-newt.png" align(0.15, 0.5)
        else: 
            imagebutton:
                idle "cattail_ani_idle"
                hover "cattail_ani_hover"
                align(0.15, 0.5)
                action [Jump("newt_reveal"), Hide("mg")]

        if toad_select:
            imagebutton:
                idle "toad_ani_idle"
                hover "toad_ani_hover"
                align(0.47, 0.35)
                action [Jump("toad_reveal"), Hide("mg")]
        else:
            add "toad_ani_idle" align(0.47, 0.35)

label snail_reveal:
    show mg background 
    show snail_silhouette zorder 0 at slide_up
    show cattail zorder 1 at cattail_center
    show text0
    pause 1.0
    show snail_silhouette zorder 3 at slide_down
    show snail zorder 2 at reveal_position
    pause 3.0
    show text5
    hide text0
    $snail_select = True
    pause 3.0
    hide snail
    hide snail_silhouette
    hide cattail
    hide text5
    jump minigame

label turtle_reveal:
    show mg background
    show turtle_silhouette zorder 0 at slide_up
    show cattail zorder 1 at cattail_center
    show text0
    pause 1.0
    show turtle_silhouette zorder 3 at slide_down
    show turtle zorder 2 at reveal_position
    pause 3.0
    show text7
    hide text0
    $turtle_select = True
    pause 3.0
    hide turtle
    hide turtle_silhouette
    hide cattail
    hide text7
    jump minigame

label damselfly_reveal:
    show mg background
    show damselfly_silhouette zorder 0 at slide_up
    show cattail zorder 1 at cattail_center
    show text0
    pause 1.0
    show damselfly_silhouette zorder 3 at slide_down
    show damselfly zorder 2 at reveal_position
    pause 3.0
    show text4
    hide text0
    $damselfly_select = True
    pause 3.0
    hide damselfly
    hide damselfly_silhouette
    hide cattail
    hide text4
    jump minigame

label newt_reveal:
    show mg background
    show newt_silhouette zorder 0 at slide_up
    show cattail zorder 1 at cattail_center
    show text0
    pause 1.0
    show newt_silhouette zorder 3 at slide_down
    show newt zorder 2 at reveal_position
    pause 3.0
    show text6
    hide text0
    $newt_select = True
    pause 3.0
    hide newt
    hide newt_silhouette
    hide cattail
    hide text6
    jump minigame

label toad_reveal:
    show mg background
    show text3
    show lilypad_bundle:
        xalign 0.5 yalign 0.4
        zoom 0.8
    show toad_silhouette zorder 2 at toad_reveal
    show toad zorder 1 at toad_position
    pause 7.0
    jump scene3_last_line