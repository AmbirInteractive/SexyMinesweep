init python:
    mode_beginner = 0
    mode_intermediate = 1
    mode_advanced = 2
    mode_custom_grid_size = 3

    #900 + ((960 - x)/2) / ((60 + y)/2)
    beginner_top_right_pos = [1236, 396]
    medium_top_right_pos = [1124, 284]
    advanced_top_right_pos = [996, 156]

    display_mode_show = 0
    display_mode_game = 1

screen minesweeper_screen(_game_mode, _display_mode=display_mode_game):
    if store.persistent.animations_on:
        add "animated_game_bg"
    else:
        add "main_game_background"
    add "minesweep_zone" xpos 900 ypos 60
    use minesweeper_ui
    add get_mine_sweeper_girl_sprite()
    if _game_mode == mode_beginner:
        use beginner_minesweeper_screen(_display_mode)
    elif _game_mode == mode_intermediate:
        use intermediate_minesweep_screen(_display_mode)
    elif _game_mode == mode_advanced:
        use advanced_minesweep_screen(_display_mode)

    if persistent.cheat_code_used == True:
        textbutton "Win" action Function(wincheat)
        textbutton "Flag all squares" action Function(cheat_flag_all_squares) ypos 40
        textbutton "Unflag all squares" action Function(cheat_unflag_all_squares) ypos 80

    # if dialog_manager.get_display_dialog():
    #     use dialog_screen(current_screen_game_screen, dialog_manager.get_display_dialog())

    if game_manager.get_game_state() == game_lost:
        text "You lost..." xalign 0.5 yalign 0.5
    #    use dialog_screen(current_screen_game_screen, lose_dialog)
    elif game_manager.get_game_state() == game_won:
        if store.victory_claimed == False:
            add "gui/a_thing.png" xalign 0.5 yalign 0.5
            text "You won" xpos 900 ypos 480
            imagebutton:
                xpos 900
                ypos 540
                idle "gui/next_button.png"
                hover "gui/next_button_hover.png"
                action Function(claim_victory)
        else:
            use victory_screen
        #text "You won!" xalign 0.5 yalign 0.5
    #    use dialog_screen(current_screen_game_screen, win_dialog)
    # use validation_screen

screen minesweeper_ui:
    #add "minesweep_overlay"

    if game_manager.get_game_state() == game_won:
        add "game_screen_main_menu_button_grey" xalign 0.65 yalign 0.95
        add "game_screen_restart_button_grey" xalign 0.8 yalign 0.95
    else:
        use mobile_game_ui

        imagebutton:
            xalign 0.65
            yalign 0.95
            idle "game_screen_main_menu_button"
            hover "game_screen_main_menu_button_hover"
            action ShowMenu("preferences")
            #action Function(go_to_main_menu)
            style "button_with_sound"
        imagebutton:
            xalign 0.8
            yalign 0.95
            idle "game_screen_restart_button"
            hover "game_screen_restart_button_hover"
            action [Call("restart_game"), With(dissolve)]
            style "button_with_sound"


    text "Mines left:"+str(game_manager.grid_structure.get_mines_left()) xalign 0.75 ypos 50 font "fonts/ethnocentric_rg.ttf" size 25

    text "Percent completion:"+ str(int(game_manager.get_percent_completion(False, True))) xalign 0.8 font "fonts/ethnocentric_rg.ttf" size 32

screen beginner_minesweeper_screen(_display_mode):
    add "beginner_grid" xpos beginner_top_right_pos[0] ypos beginner_top_right_pos[1]
    use mine_array(beginner_top_right_pos[0] + 1, beginner_top_right_pos[1] + 1, _display_mode)

screen intermediate_minesweep_screen(_display_mode): #512 x 512
    #add "intermediate_grid" xpos medium_top_right_pos[0] ypos medium_top_right_pos[1]
    use mine_array(medium_top_right_pos[0] + 1, medium_top_right_pos[1] + 1, _display_mode)

screen advanced_minesweep_screen(_display_mode): #768 x 768
    #add "advanced_grid" xpos advanced_top_right_pos[0] ypos advanced_top_right_pos[1]
    use mine_array(advanced_top_right_pos[0] + 1, advanced_top_right_pos[1] + 1, _display_mode)

screen mine_array(_xpos, _ypos, _display_mode):
    if (game_manager.get_game_state() == game_in_progress) and (_display_mode == display_mode_game) and (persistent.mobile_build_on == False):
        use mine_array_game_in_progress(_xpos, _ypos)
    elif (game_manager.get_game_state() == game_in_progress) and (_display_mode == display_mode_game):
        use mobile_game_squares_array(_xpos, _ypos)
    else:# (game_manager.get_game_state() == game_lost) or (game_manager.get_game_state() == game_won):
        use mine_array_game_ended(_xpos, _ypos)

screen mine_array_game_in_progress(_xpos, _ypos):
    for i in game_manager.get_grid_structure():
        for j in i:
            if j.get_is_revealed() == False and j.get_is_flagged() == False:
                imagebutton:
                    xpos _xpos + 32*j.get_square_pos()[1]
                    ypos _ypos + 32*j.get_square_pos()[0]
                    idle "hidden_square"
                    hover "hidden_square_hover"
                    action [Function(play_click_sound, j.get_contains_mine()), Function(grid_square_click_action, j.get_square_pos()[0], j.get_square_pos()[1])]
                    alternate [Function(grid_square_alternate_click_action, j.get_square_pos()[0], j.get_square_pos()[1])]

            else:
                if j.get_is_flagged() == True:
                    imagebutton:
                        xpos _xpos + 32*j.get_square_pos()[1]
                        ypos _ypos + 32*j.get_square_pos()[0]
                        idle "flag"
                        hover "flag"
                        action Function(grid_flag_click_action)
                        alternate Function(grid_flag_alternate_click_action, j.get_square_pos()[0], j.get_square_pos()[1])
                elif j.get_contains_mine() == True:
                    add "mine" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]
                else:
                    if j.get_nearby_mines() != 0:
                        if (j.get_surrounding_flags() >= j.get_nearby_mines()) and (j.get_clicked_to_clear_surrounding_squares() == False):
                            imagebutton:
                                xpos _xpos + 32*j.get_square_pos()[1]
                                ypos _ypos + 32*j.get_square_pos()[0]
                                idle "square"
                                #hover "square_hover"
                                action Function(reveal_all_surrounding_hidden_squares, j.get_square_pos()[0], j.get_square_pos()[1])
                                style "regular_tiles_clicked"
                        else:
                            add "square" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]

                        text str(j.get_nearby_mines()) xpos _xpos + 32*j.get_square_pos()[1] + 4  ypos _ypos + 32*j.get_square_pos()[0] - 3
                    else:
                        add "square" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]

screen mine_array_game_ended(_xpos, _ypos):
    for i in game_manager.get_grid_structure():
        for j in i:
            if j.get_is_revealed() == False and j.get_is_flagged() == False:
                add "hidden_square" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]
                #imagebutton:
                #    xpos _xpos + 32*j.get_square_pos()[1]
                #    ypos _ypos + 32*j.get_square_pos()[0]
                #    idle "hidden_square"
                #    hover "hidden_square_hover"
                #    action Function(grid_square_click_action, j.get_square_pos()[0], j.get_square_pos()[1])
                #    alternate Function(grid_square_alternate_click_action, j.get_square_pos()[0], j.get_square_pos()[1])
            else:
                if j.get_is_flagged() == True:
                    add "flag" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]
                    #imagebutton:
                    #    xpos _xpos + 32*j.get_square_pos()[1]
                    #    ypos _ypos + 32*j.get_square_pos()[0]
                    #    idle "flag"
                    #    hover "flag"
                    #    action Function(grid_flag_click_action)
                    #    alternate Function(grid_flag_alternate_click_action, j.get_square_pos()[0], j.get_square_pos()[1])
                elif j.get_contains_mine() == True:
                    add "mine" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]
                else:
                    add "square" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]
                    if j.get_nearby_mines() != 0:
                        text str(j.get_nearby_mines()) xpos _xpos + 32*j.get_square_pos()[1] + 4  ypos _ypos + 32*j.get_square_pos()[0] - 3

#screen mine_array_game_won(_xpos, _ypos):


screen validation_screen:
    for i in range(len(game_manager.get_adjacent_mines_array())):
        for j in range(len(game_manager.get_adjacent_mines_array()[i])):
            text str(game_manager.get_adjacent_mines_array()[i][j]) xpos 30 * j ypos 30 * i

    for i in range(len(game_manager.get_mine_placement_array())):
        for j in range(len(game_manager.get_mine_placement_array()[i])):
            text str(game_manager.get_mine_placement_array()[i][j]) xpos 30 * j ypos 500 + (30 * i)

    # for i in range(len(placeholder_beginner_grid)):
    #     for j in range(len(placeholder_beginner_grid[i])):
    #         text str(placeholder_beginner_grid[i][j]) xpos 500 + (30 * j) ypos 30 * i

screen confirmation_screen:
    use minesweeper_screen(game_manager.get_game_mode(), display_mode_show)

    add "confirmation_screen_box"

    imagebutton:
        xpos 389
        ypos 520
        idle "confirmation_screen_yes"
        focus_mask True
        action Function(go_to_main_menu)
    imagebutton:
        xpos 949
        ypos 526
        idle "confirmation_screen_no"
        focus_mask True
        action Call("return_to_game")


#screen return_to_main_menu_validation:
    # Display the minesweeper screen as the background of the screen.
#    use minesweeper_screen(game_manager.get_game_mode(), display_mode_show)
    # Display the choice window

    # Display the choice buttons


#screen restart_game_validation:
    # Display the minesweeper screen as the background of the screen.
#    use minesweeper_screen(game_manager.get_game_mode(), display_mode_show)
    # Display the choice window

    # Display the choice buttons
