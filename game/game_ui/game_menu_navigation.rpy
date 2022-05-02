label return_to_main_menu:
    menu:
        "Are you sure you want to return to main menu?"
        "Yes":
            $renpy.full_restart()
        "No":
            return
    return

screen game_menu_navigation():

    textbutton "Codes" xalign 1.0 action ShowMenu("code_ui")

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        #textbutton _("Preferences") action ShowMenu("preferences")
        imagebutton:
            idle "main_menu_preferences_button"
            hover "main_menu_preferences_button_hover"
            action ShowMenu("preferences")
            style "button_with_sound"





        if _in_replay:

            textbutton _("History") action ShowMenu("history")
            style "button_with_sound"

            textbutton _("End Replay") action EndReplay(confirm=True)
        if not main_menu:
            #textbutton _("Main Menu") action MainMenu()
            imagebutton:
                idle "settings_main_menu_button"
                hover "settings_main_menu_button_hover"
                action MainMenu()
                style "button_with_sound"

        imagebutton:
            idle "main_menu_about_button"
            hover "main_menu_about_button_hover"
            action ShowMenu("about")
            style "button_with_sound"
        #textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")
            imagebutton:
                idle "main_menu_help_button"
                hover "main_menu_help_button_hover"
                action ShowMenu("help")
                style "button_with_sound"

        imagebutton:
            idle "main_menu_gallery_button"
            hover "main_menu_gallery_button_hover"
            #hover "settings_gallery_button_hover"
            action ShowMenu("gallery_screen")
            style "button_with_sound"

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            #textbutton _("Quit") action Quit(confirm=not main_menu)
            imagebutton:
                idle "main_menu_quit_button"
                hover "main_menu_quit_button_hover"
                action [Play("sound", "audio/UI_button08.wav"), Quit(confirm=not main_menu)]
                hover_sound "audio/Menu_Sounds_V2_Metallic_HOLD.mp3"



#settings_highscore_button
#settings_load_button


#settings_start_button
