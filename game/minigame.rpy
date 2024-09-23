label minigame:
    $bogBeastBool = False
    $snailSelect = False

    #screen used for main minigame in order to access image buttons
    screen mg:
        image "mg-assets/mg-background.png"
        image "mg-assets/border-right.png"
        image "mg-assets/border-left.png"
        image "mg-assets/flowered-lilypad.png" align(0.5, 0.6) zoom 0.75
        image "mg-assets/textbox3.png" align(0.5, 1.0)

        imagebutton auto "mg-assets/cattail-%s.png" align(0.85, 0.5) action SetVariable("snailSelect", True)
        imagebutton auto "mg-assets/cattail-%s.png" align(0.65, 0.01) action NullAction()
        imagebutton auto "mg-assets/cattail-%s.png" align(0.35, 0.01) action NullAction()
        imagebutton auto "mg-assets/cattail-%s.png" align(0.15, 0.5) action NullAction()

        if snailSelect:
            image "mg-assets/cattail-snail.png" align(0.85, 0.5)

    # test screen for "whos that bog beast" reveal
    screen snail:
        image "mg-assets/mg-background.png"
        image "mg-assets/border-right.png"
        image "mg-assets/border-left.png"
        image "mg-assets/cattail-idle.png"
        image "mg-assets/textbox-5.png"

    call screen mg

    # calls to another screen don't work, hiding previous screen doesn't work
    if snailSelect:
        call screen snail
        hide screen mg
        show screen snail
        scene bg attic day
