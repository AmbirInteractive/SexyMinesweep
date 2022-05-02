default code_entered = ""

init python:
    def flush_code():
        store.code_entered = ""

    def toggle_promo_links():
        if persistent.promo_activated == True:
            persistent.promo_activated = False
        else:
            persistent.promo_activated = True

    def wipe_save():
        persistent.cheat_code_used = False
        persistent.promo_activated = True

        persistent.current_girl_id = 0
        persistent.amount_of_wins = 0
        persistent.amount_of_losses = 0

        for i in persistent.girls_data_repo:
            i[girls_data_repo_strip_unlocked_pos] = 0
            i[girls_data_repo_gravure_unlocked_pos] = 0
            i[girls_data_repo_wins_pos] = 0
            i[girls_data_repo_losses_pos] = 0

screen code_ui:
    tag menu

    add gui.game_menu_background
    add "gui/pick_girl_background.png" xsize 510 xcenter 0.5 ycenter 0.5

    if persistent.cheat_code_used == False:
        text "Dev Commands: Locked."
    elif persistent.cheat_code_used == True:
        text "Dev Commands: Unlocked.\nLook for 'Unlock Gallery' in the gallery menu and 'win' in the game menu.\nBoth are at the top left of the screen."

        textbutton "Toggle main menu promo links":
            xalign 1.0
            action Function(toggle_promo_links)
            activate_sound "audio/GetAPowerUp.wav"

        textbutton "Wipe save":
            xalign 1.0
            yalign 1.0
            action Function(wipe_save)

    if persistent.promo_activated == True:
        text "Main menu promo links: Active." ypos 150
    else:
        text "Main menu promo links: Inactive." ypos 150

    input default "":
        xcenter 0.5
        ycenter 0.5
        pixel_width(500)
        value VariableInputValue("code_entered")

    textbutton "Ok":
        xcenter 0.6
        ycenter 0.55
        action [Function(input_code, code_entered), Function(flush_code)]

    imagebutton:
        xpos 25
        ypos 955
        idle "settings_back_button"
        action ShowMenu("preferences")
        style "back_button"
