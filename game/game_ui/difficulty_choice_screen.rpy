screen difficulty_choice_screen:
    if store.persistent.animations_on:
        add "animated_game_bg"
    else:
        add "main_game_background"
    #add get_difficulty_choice_sprite(persistent.current_girl_id)

    imagebutton:
        focus_mask True
        xcenter 0.7
        ycenter 0.3
        idle "difficulty_choice_beginner_button"
        hover "difficulty_choice_beginner_button_hover"
        action Call("beginner_mode_game")
        style "button_with_sound"
        #action Function(difficulty_screen_set_game_mode, mode_beginner)
    imagebutton:
        focus_mask True
        xcenter 0.7
        ycenter 0.5
        idle "difficulty_choice_intermediate_button"
        hover "difficulty_choice_intermediate_button_hover"
        action Call("medium_mode_game")
        style "button_with_sound"
        #action Function(difficulty_screen_set_game_mode, mode_intermediate)
    imagebutton:
        focus_mask True
        xcenter 0.7
        ycenter 0.7
        idle "difficulty_choice_advanced_button"
        hover "difficulty_choice_advanced_button_hover"
        action Call("advanced_mode_game")
        style "button_with_sound"
        #action Function(difficulty_screen_set_game_mode, mode_advanced)

    use girl_pick_interface
