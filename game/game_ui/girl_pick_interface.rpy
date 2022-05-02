screen girl_pick_interface:
    imagebutton:
        xpos 357
        focus_mask True
        idle get_main_menu_sprite(persistent.current_girl_id)
        hover get_main_menu_sprite(persistent.current_girl_id, main_menu_hover)
        action ShowMenu("girl_selection_menu")

    imagebutton:
        xalign 0.15
        yalign 0.5
        idle "gui/arrow_left.png"
        hover "gui/arrow_left_hover.png"
        action Function(main_menu_left_arrow_func)
        style "arrow_buttons"

    imagebutton:
        xalign 0.45
        yalign 0.5
        idle "gui/arrow_right.png"
        hover "gui/arrow_right_hover.png"
        action Function(main_menu_right_arrow_func)
        style "arrow_buttons"

    add "gui/pick_girl_background.png" xcenter 0.3 ycenter 0.95
    text "PICK YOUR GIRL" xcenter 0.3 ycenter 0.95 style "pick_your_girl_style"
