label start:
    $store.current_play_mode = store.character_selection_menu_mode

    if store.current_play_mode == play_mode_story:
        call story_mode from _call_story_mode
    elif store.current_play_mode == play_mode_quickie:
        call game_mode from _call_game_mode
    return

label story_mode:
    "Story Mode."
    return

label game_mode:
    call game_setup from _call_game_setup
    call main_game_loop from _call_main_game_loop
    return

label game_setup:
    #call screen difficulty_choice_screen with dissolve
    $game_manager.set_game_running(True)
    return

label main_game_loop:
    while game_manager.get_game_running():
        #$dialog_manager.update_dialog_status()
        call screen minesweeper_screen(game_manager.get_game_mode()) with dissolve
    return
