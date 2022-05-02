init python:
    current_screen_game_screen = 0

screen dialog_screen(_current_screen, _dialog):
    if _current_screen == current_screen_game_screen:
        use game_dialog_screen(_dialog)

screen game_dialog_screen(_dialog):
    #add "game_textbox" xpos ypos
    frame:
        background "game_textbox"
        padding (25, 100)
        xysize(500, 300)
        text _dialog
        xpos 150
        ypos 650
