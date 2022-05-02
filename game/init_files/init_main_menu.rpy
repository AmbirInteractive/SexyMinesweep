init python:
    def main_menu_left_arrow_func():
        new_id = persistent.current_girl_id - 1
        persistent.current_girl_id = check_id(new_id)

    def main_menu_right_arrow_func():
        new_id = persistent.current_girl_id + 1
        persistent.current_girl_id = check_id(new_id)

image main_menu_title = "images/objects/main_menu/main_menu_title.png"

image main_menu_story_start_button = "gui/laff_uis/MAIN_SCREEN/story.png"
image main_menu_quickie_start_button = "gui/laff_uis/MAIN_SCREEN/quickie.png"

image main_menu_about_button = "gui/laff_uis/MAIN_SCREEN/about.png"
image main_menu_preferences_button = "gui/laff_uis/MAIN_SCREEN/Settings.png"
image main_menu_help_button = "gui/laff_uis/MAIN_SCREEN/help.png"
image main_menu_quit_button = "gui/laff_uis/MAIN_SCREEN/quit.png"
image main_menu_gallery_button = "gui/laff_uis/MAIN_SCREEN/gallery.png"

image main_menu_story_start_button_hover = "gui/laff_uis/MAIN_SCREEN/story_hover.png"
image main_menu_quickie_start_button_hover = "gui/laff_uis/MAIN_SCREEN/quickie_hover.png"

image main_menu_about_button_hover = "gui/laff_uis/MAIN_SCREEN/about_hover.png"
image main_menu_preferences_button_hover = "gui/laff_uis/MAIN_SCREEN/Settings_hover.png"
image main_menu_help_button_hover = "gui/laff_uis/MAIN_SCREEN/help_hover.png"
image main_menu_quit_button_hover = "gui/laff_uis/MAIN_SCREEN/quit_hover.png"
image main_menu_gallery_button_hover = "gui/laff_uis/MAIN_SCREEN/gallery_hover.png"
