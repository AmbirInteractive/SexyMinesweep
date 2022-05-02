init python:
    def grid_square_click_action(_xpos, _ypos):
        game_manager.reveal_square(_xpos, _ypos)
    def grid_square_alternate_click_action(_xpos, _ypos):
        game_manager.flag_square(_xpos, _ypos)


    def grid_flag_click_action():
        pass
    def grid_flag_alternate_click_action(_xpos, _ypos):
        game_manager.flag_square(_xpos, _ypos)

    def go_to_main_menu():
        game_manager.set_game_running(False)
        # ui.close()
        renpy.full_restart()

    def wincheat():
        store.game_manager.set_game_state(game_won)

    def cheat_flag_all_squares():
        store.game_manager.flag_all_squares(True)
    def cheat_unflag_all_squares():
        store.game_manager.flag_all_squares(False)

    def play_click_sound(_contains_mine):
        if _contains_mine and game_manager.first_square == False:
            renpy.play("audio/Explosion_001.wav", "sound")
        else:
            renpy.play("audio/UI_button05.wav", "sound")

    def reveal_all_surrounding_hidden_squares(_xpos, _ypos):
        store.game_manager.reveal_all_surrounding_hidden_squares(_xpos, _ypos)

label restart_game:
    call screen difficulty_choice_screen
    return

label call_confirmation_screen:
    call screen confirmation_screen
    return

label return_to_game:
    call screen minesweeper_screen(game_manager.get_game_mode(), display_mode_game)
    return
