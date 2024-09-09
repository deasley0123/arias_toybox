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
transform blur_box:
    block:
        blur 3

image aria_up_from_bottom_right:
    "aria excite hiding.png"    
    xalign 0.0
    yalign 0.0
    subpixel True xoffset -315.0 zoom 2.2 
    yoffset 837.0 
    linear 0.75 yoffset -36.0 
    pause 0.85
    offset (-315.0, -36.0) 

transform grey_out:
    subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.8)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None 

transform restore_color:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None 

