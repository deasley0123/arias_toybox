# Image / shown text transforms go in here

transform shaking_center:
    ypos 0.5
    block:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat
transform shaking:
    block:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat
transform shaking_extreme(factor):
    block:
        linear 0.1 xoffset -2*factor yoffset 2*factor
        linear 0.1 xoffset 3*factor yoffset -3*factor
        linear 0.1 xoffset 2*factor yoffset -2*factor
        linear 0.1 xoffset -3*factor yoffset 3*factor
        linear 0.1 xoffset 0 yoffset 0
        repeat
transform blur_box:
    block:
        blur 3

image aria_up_from_bottom_right:
    "aria excite hiding.png"   
    subpixel True xoffset -315.0 zoom 1.6
    yoffset 837.0 
    linear 0.75 yoffset -36.0 
    pause 0.85
    offset (-315.0, -36.0) 

image aria_jump_up_from_middle:
    "aria exhult jumping mopen.png"   
    subpixel True zoom .5
    yoffset 1500.0 
    linear 0.1 yoffset 200.0 
    pause 0.2
    offset (0.0, 200.0)

define dissolve_slow = Dissolve(3.0)

transform grey_out:
    subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.8)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None 

transform restore_color:
    subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None 

define fadehold = Fade(0.6, 0.75, 0.6)
define faaadehold = Fade(1, 0.75, 0.6)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
transform false_hide:
    subpixel True 
    alpha 1.0 
    linear 0.50 alpha 0.0 
transform un_hide:
    subpixel True 
    alpha 0.0 
    linear 0.50 alpha 1.0 

define encounter_dissolve = ImageDissolve("spotlight_alpha.png", 1.0, 8 , reverse=False)

label scene_transition(title=""):
    $ quick_menu = False
    scene loading movie with fadehold
    show text "{size=150}[title]{/size}" with dissolve_slow
    pause 1.0
    hide text
    with dissolve_slow
    $ quick_menu = True

    return

label minigame_transition:
    camera:
        subpixel True 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(1.2)*HueMatrix(0.0) 
        linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(1.2)*HueMatrix(0.0) 
        linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    pause 0.4
    camera:
        linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
 
    scene black with encounter_dissolve # TODO: Define a new image for this transition
    jump minigame

label end_text(title=""):
    show text "{size=150}[title]{/size}" with dissolve_slow
    pause 1.0
    hide text
    with dissolve_slow