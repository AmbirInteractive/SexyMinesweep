init python:
    def difficulty_screen_set_game_mode(_game_mode):
        game_manager.setup_game(_game_mode)

label beginner_mode_game:
    $game_manager.setup_game(mode_beginner)
    return

label medium_mode_game:
    $game_manager.setup_game(mode_intermediate)
    return

label advanced_mode_game:
    $game_manager.setup_game(mode_advanced)
    return
