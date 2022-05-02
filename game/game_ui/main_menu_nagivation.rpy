init python:
    main_menu_box_xpos = 0.66
    main_menu_box_ypos = 380
    main_menu_spacing = 10

screen main_menu_navigation:
    vbox:
        style_prefix "navigation"

        xcenter main_menu_box_xpos
        ypos main_menu_box_ypos

        spacing main_menu_spacing

#        imagebutton:
#            idle "main_menu_story_start_button"
#            hover "main_menu_story_start_button_hover"
#            action [Function(set_play_mode, play_mode_story), Start()]
#            style "button_with_sound"

        imagebutton:
            idle "main_menu_quickie_start_button"
            hover "main_menu_quickie_start_button_hover"
            action [Function(set_character_selection_menu_mode, character_selection_mode_quickie), ShowMenu("character_screen_menu")]
            style "button_with_sound"

        imagebutton:
            idle "main_menu_preferences_button"
            hover "main_menu_preferences_button_hover"
            action ShowMenu("preferences")
            style "button_with_sound"

        imagebutton:
            idle "main_menu_about_button"
            hover "main_menu_about_button_hover"
            action ShowMenu("about")
            style "button_with_sound"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            imagebutton:
                idle "main_menu_help_button"
                hover "main_menu_help_button_hover"
                action ShowMenu("help")
                style "button_with_sound"

        imagebutton:
            idle "main_menu_gallery_button"
            hover "main_menu_gallery_button_hover"
            action ShowMenu("gallery_screen")
            style "button_with_sound"

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton:
                idle "main_menu_quit_button"
                hover "main_menu_quit_button_hover"
                action Quit(confirm=not main_menu)
                style "button_with_sound"
