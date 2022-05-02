screen character_screen_menu:
    tag menu

    if store.character_selection_menu_mode == character_selection_mode_story:
        use story_mode_character_choice
    elif store.character_selection_menu_mode == character_selection_mode_quickie:
        use difficulty_choice_screen

    imagebutton:
        xpos 25
        ypos 955
        idle "settings_back_button"
        hover "settings_back_button_hover"
        action [Function(go_to_main_menu), Return()]
        style "back_button"
