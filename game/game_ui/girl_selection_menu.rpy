init python:
    def check_id(_girl_id):
        the_id = _girl_id
        if _girl_id < 0:
            the_id = store.number_of_girls - 1
        elif _girl_id == store.number_of_girls:
            the_id = 0
        return the_id

    def pick_girl(_girl_id):
        persistent.current_girl_id = check_id(_girl_id)

    def get_girl_card_base(_girl_id):
        return get_selection_screen_sprite(check_id(_girl_id), selection_screen_base)

    def get_girl_card_hover(_girl_id):
        return get_selection_screen_sprite(check_id(_girl_id), selection_screen_hover)

    def get_girl_card_selected(_girl_id):
        return get_selection_screen_sprite(check_id(_girl_id), selection_screen_selected)

    def left_arrow_func():
        new_id = store.current_girl_id - 1
        store.current_girl_id = check_id(new_id)

    def right_arrow_func():
        new_id = store.current_girl_id + 1
        store.current_girl_id = check_id(new_id)

screen girl_selection_menu:
    tag menu

    add "gui/black_background.png"

    if check_id(store.current_girl_id - 1) == persistent.current_girl_id:
        add get_girl_card_selected(persistent.current_girl_id)
    else:
        imagebutton:
            idle get_girl_card_base(store.current_girl_id - 1)
            hover get_girl_card_hover(store.current_girl_id - 1)
            action Function(pick_girl, store.current_girl_id - 1)
            activate_sound "audio/Menu_Sounds_V2_Modern_LOADSAVE.mp3"

    if store.current_girl_id == persistent.current_girl_id:
        add get_girl_card_selected(persistent.current_girl_id) xpos 640
    else:
        imagebutton:
            xpos 640
            idle get_girl_card_base(store.current_girl_id)
            hover get_girl_card_hover(store.current_girl_id)
            action Function(pick_girl, store.current_girl_id)
            activate_sound "audio/Menu_Sounds_V2_Modern_LOADSAVE.mp3"

    if check_id(store.current_girl_id + 1) == persistent.current_girl_id:
        add get_girl_card_selected(persistent.current_girl_id) xpos 1280
    else:
        imagebutton:
            xpos 1280
            idle get_girl_card_base(store.current_girl_id + 1)
            hover get_girl_card_hover(store.current_girl_id + 1)
            action Function(pick_girl, store.current_girl_id + 1)
            activate_sound "audio/Menu_Sounds_V2_Modern_LOADSAVE.mp3"


    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "gui/arrow_left.png"
        hover "gui/arrow_left_hover.png"
        action Function(left_arrow_func)
        style "arrow_buttons"

    imagebutton:
        xalign 1.0
        yalign 0.5
        idle "gui/arrow_right.png"
        hover "gui/arrow_right_hover.png"
        action Function(right_arrow_func)
        style "arrow_buttons"

    imagebutton:
        xpos 25
        ypos 955
        idle "settings_back_button"
        action ShowMenu("character_screen_menu")
        style "back_button"



    # Imagebutton of the girl currently selected
