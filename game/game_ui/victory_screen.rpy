init python:
    def award_points():
        if store.game_manager.get_game_mode() == mode_beginner:
            return 1
        elif store.game_manager.get_game_mode() == mode_intermediate:
            return 3
        elif store.game_manager.get_game_mode() == mode_advanced:
            return 9

    def claim_victory():
        if get_girl_gravure_stage_unlocked(persistent.current_girl_id) < get_girl_gravure_amount(persistent.current_girl_id):
            store.gravure_to_display_upon_win = get_girl_gravure_stage_unlocked(persistent.current_girl_id) + 1
        else:
            store.gravure_to_display_upon_win = get_girl_gravure_stage_unlocked(persistent.current_girl_id)
        #persistent.sylvia_gravure_stage_unlocked += 1
        set_girl_gravure_unlocked(persistent.current_girl_id, award_points())
        store.victory_claimed = True

    def left_arrow_victory_func():
        if store.gravure_to_display_upon_win > 1:
            store.gravure_to_display_upon_win -= 1
        else:
            pass

    def right_arrow_victory_func():
        if store.gravure_to_display_upon_win < get_girl_gravure_stage_unlocked(persistent.current_girl_id):
            store.gravure_to_display_upon_win += 1
        else:
            pass

    def get_victory_persistent_value(_get_gravure_value = True):
        return persistent_getter_functions[persistent.current_girl_id](_get_gravure_value)


default victory_claimed = False

screen victory_screen:
    if get_gravure_image(persistent.current_girl_id, store.gravure_to_display_upon_win):
        add get_gravure_image(persistent.current_girl_id, store.gravure_to_display_upon_win)
    else:
        add "main_game_background"
        text "Gravure to display: [store.gravure_to_display_upon_win] \nCouldn't be found."
    imagebutton:
        xalign 0.0
        yalign 1.0
        idle "game_screen_main_menu_button"
        action Function(go_to_main_menu)
        style "back_button"

    # Arrow left
    if store.gravure_to_display_upon_win > 1:
        imagebutton:
            xalign 0.0
            ypos 50
            idle "gui/arrow_left.png"
            hover "gui/arrow_left_hover.png"
            action Function(left_arrow_victory_func)
            style "arrow_buttons"
    # Arrow right
    if (store.gravure_to_display_upon_win <= get_girl_gravure_amount(persistent.current_girl_id)) and (store.gravure_to_display_upon_win < get_girl_gravure_stage_unlocked(persistent.current_girl_id)):
        imagebutton:
            xalign 1.0
            ypos 50
            idle "gui/arrow_right.png"
            hover "gui/arrow_right_hover.png"
            action Function(right_arrow_victory_func)
            style "arrow_buttons"
