init python:
    click_mode_reveal = 0
    click_mode_flag = 1

screen mobile_game_ui:
    if store.persistent.mobile_build_on:
        vbox:
            xpos 900
            ypos 60
            if store.click_mode == click_mode_reveal:
                add "cursor_square_toggled"
                imagebutton:
                    focus_mask True
                    idle "flag_button"
                    hover "flag_hover"
                    action Function(toggle_click_mode)
            elif store.click_mode == click_mode_flag:
                imagebutton:
                    focus_mask True
                    idle "cursor_square"
                    hover "cursor_square_hover"
                    action Function(toggle_click_mode)
                add "flag_toggled"

screen mobile_game_squares_array(_xpos, _ypos):
    for i in game_manager.get_grid_structure():
        for j in i:
            if j.get_is_revealed() == False and j.get_is_flagged() == False:
                if store.click_mode == click_mode_reveal:
                    imagebutton:
                        xpos _xpos + 32*j.get_square_pos()[1]
                        ypos _ypos + 32*j.get_square_pos()[0]
                        idle "hidden_square"
                        hover "hidden_square_hover"
                        action [Function(play_click_sound, j.get_contains_mine()), Function(grid_square_click_action, j.get_square_pos()[0], j.get_square_pos()[1])]

                elif store.click_mode == click_mode_flag:
                    imagebutton:
                        xpos _xpos + 32*j.get_square_pos()[1]
                        ypos _ypos + 32*j.get_square_pos()[0]
                        idle "hidden_square"
                        hover "hidden_square_hover"
                        action [Function(grid_square_alternate_click_action, j.get_square_pos()[0], j.get_square_pos()[1])]

            else:
                if j.get_is_flagged() == True:
                    if store.click_mode == click_mode_reveal:
                        imagebutton:
                            xpos _xpos + 32*j.get_square_pos()[1]
                            ypos _ypos + 32*j.get_square_pos()[0]
                            idle "flag"
                            hover "flag"
                            action Function(grid_flag_click_action)

                    elif store.click_mode == click_mode_flag:
                        imagebutton:
                            xpos _xpos + 32*j.get_square_pos()[1]
                            ypos _ypos + 32*j.get_square_pos()[0]
                            idle "flag"
                            hover "flag"
                            action Function(grid_flag_alternate_click_action, j.get_square_pos()[0], j.get_square_pos()[1])

                elif j.get_contains_mine() == True:
                    add "mine" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]
                else:
                    if j.get_nearby_mines() != 0:
                        if j.get_surrounding_flags() >= j.get_nearby_mines():
                            imagebutton:
                                xpos _xpos + 32*j.get_square_pos()[1]
                                ypos _ypos + 32*j.get_square_pos()[0]
                                idle "square"
                                #hover "square_hover"
                                action Function(reveal_all_surrounding_hidden_squares, _xpos, _ypos)
                                style "regular_tiles_clicked"
                        else:
                            add "square" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]

                        text str(j.get_nearby_mines()) xpos _xpos + 32*j.get_square_pos()[1] + 4  ypos _ypos + 32*j.get_square_pos()[0] - 3
                    else:
                        add "square" xpos _xpos + 32*j.get_square_pos()[1] ypos _ypos + 32*j.get_square_pos()[0]
