# Settings button assets
image settings_main_menu_button = "gui/laff_uis/MAIN_SCREEN/main_menu.png"
image settings_main_menu_button_hover = "gui/laff_uis/MAIN_SCREEN/main_menu_hover.png"

image settings_back_button = "gui/laff_uis/BACK_BUTTON.png"
image settings_back_button_hover = "gui/laff_uis/BACK_BUTTON_hover.png"

image settings_gallery_button = "gui/game_menu_a_gallery_button.png"
image settings_gallery_button_hover = "gui/game_menu_a_gallery_button_hover.png"

image checkbox = "gui/checkbox.png"
image checkbox_checked = "gui/checkbox_1.png"
image checkbox_hover = "gui/checkbox_hover.png"
image checkbox_checked_hover = "gui/checkbox_1_hover.png"

init python:
    def get_animations_checkbox_idle():
        if store.persistent.animations_on:
            return "checkbox_checked"
        else:
            return "checkbox"

    def get_animations_checkbox_hover():
        if store.persistent.animations_on:
            return "checkbox_checked_hover"
        else:
            return "checkbox_hover"

    def toggle_animations():
        store.persistent.animations_on = not store.persistent.animations_on

    def get_mobile_checkbox_idle():
        if store.persistent.mobile_build_on:
            return "checkbox_checked"
        else:
            return "checkbox"

    def get_mobile_checkbox_hover():
        if store.persistent.mobile_build_on:
            return "checkbox_checked_hover"
        else:
            return "checkbox_hover"

    def toggle_mobile():
        store.persistent.mobile_build_on = not store.persistent.mobile_build_on
