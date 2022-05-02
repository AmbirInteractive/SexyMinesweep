default strip_gravure_gallery = 0
default first_number_of_page = 1
default last_number_of_page = 9
default current_gravure_to_display = 1
default current_strip_to_display = 1
default display_reward_flag = False

init python:
    tumbnail_overlays = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    def toggle_gravure_gallery():
        store.strip_gravure_gallery = 0
        store.first_number_of_page = 1
        store.last_number_of_page = 9

    def toggle_strip_gallery():
        store.strip_gravure_gallery = 1
        store.first_number_of_page = 1
        store.last_number_of_page = 9

    def left_arrow_gallery_func():
        new_id = store.gallery_girl_id - 1
        store.gallery_girl_id = check_id(new_id)
        store.first_number_of_page = 1
        store.last_number_of_page = 9

    def right_arrow_gallery_func():
        new_id = store.gallery_girl_id + 1
        store.gallery_girl_id = check_id(new_id)
        store.first_number_of_page = 1
        store.last_number_of_page = 9

    def left_arrow_gravure_func():
        if store.current_gravure_to_display > 1:
            store.current_gravure_to_display -= 1
        else:
            pass

    def right_arrow_gravure_func():
        if store.current_gravure_to_display < get_girl_gravure_amount(store.gallery_girl_id):
            store.current_gravure_to_display += 1
        else:
            pass

    def left_arrow_strip_func():
        if store.current_strip_to_display > 1:
            store.current_strip_to_display -= 1
        else:
            pass

    def right_arrow_strip_func():
        if store.current_strip_to_display < get_girl_strip_amount(store.gallery_girl_id):
            store.current_strip_to_display += 1
        else:
            pass

    def toggle_display_gravure(_gravure_id):
        store.current_gravure_to_display = _gravure_id
        store.display_reward_flag = True

    def toggle_display_strip(_strip_id):
        store.current_strip_to_display = _strip_id
        store.display_reward_flag = True

    def get_current_gravure_to_display():
        return get_gravure_image(store.gallery_girl_id, store.current_gravure_to_display)
    def get_current_strip_to_display():
        return get_strip_image(store.gallery_girl_id, store.current_strip_to_display)

    def return_to_gallery():
        store.display_reward_flag = False

    def next_action():
        store.first_number_of_page += 9
        store.last_number_of_page += 9
    def prev_action():
        store.first_number_of_page -= 9
        store.last_number_of_page -= 9

    def gallery_unlock_cheat():
        girl_id = 0
        for i in persistent.girls_data_repo:
            set_girl_strip_unlocked(girl_id, get_girl_strip_amount(girls_data_repo_strip_pos))
            set_girl_gravure_unlocked(girl_id, get_girl_gravure_amount(girls_data_repo_gravure_pos))
            girl_id += 1

    def toggle_overlay_for_tumbnail(x_pos, y_pos):
        if tumbnail_overlays[x_pos][y_pos] == 0:
            tumbnail_overlays[x_pos][y_pos] = 1
        else:
            tumbnail_overlays[x_pos][y_pos] = 0

screen gallery_screen:
    tag menu
    # Background
    add "gui/backgrounds/main_menu_backgrounds/main_menu_background.webp"
    if persistent.cheat_code_used == True:
        textbutton "Unlock gallery" action Function(gallery_unlock_cheat)
    # Top part background?
    # Name of the current girl
    if store.display_reward_flag == True:
        if strip_gravure_gallery == 0:
            add get_current_gravure_to_display()

            # Arrow left
            if store.current_gravure_to_display > 1:
                imagebutton:
                    xalign 0.0
                    ypos 50
                    idle "gui/arrow_left.png"
                    hover "gui/arrow_left_hover.png"
                    action Function(left_arrow_gravure_func)
                    style "arrow_buttons"
            # Arrow right
            if (store.current_gravure_to_display < get_girl_gravure_amount(store.gallery_girl_id)) and (store.current_gravure_to_display < get_girl_gravure_stage_unlocked(store.gallery_girl_id)):
                imagebutton:
                    xalign 1.0
                    ypos 50
                    idle "gui/arrow_right.png"
                    hover "gui/arrow_right_hover.png"
                    action Function(right_arrow_gravure_func)
                    style "arrow_buttons"


        elif strip_gravure_gallery == 1:
            add get_current_strip_to_display() xalign 0.5

            # Arrow left
            if store.current_strip_to_display > 1:
                imagebutton:
                    xalign 0.0
                    ypos 50
                    idle "gui/arrow_left.png"
                    hover "gui/arrow_left_hover.png"
                    action Function(left_arrow_strip_func)
                    style "arrow_buttons"
            # Arrow right
            if (store.current_strip_to_display < get_girl_strip_amount(store.gallery_girl_id)) and (store.current_strip_to_display < get_girl_strip_stage_unlocked(store.gallery_girl_id)):
                imagebutton:
                    xalign 1.0
                    ypos 50
                    idle "gui/arrow_right.png"
                    hover "gui/arrow_right_hover.png"
                    action Function(right_arrow_strip_func)
                    style "arrow_buttons"

        imagebutton:
            xpos 25
            ypos 955
            idle "settings_back_button"
            hover "settings_back_button_hover"
            action Function(return_to_gallery)
            style "back_button"

    else:
        text get_girl_name(store.gallery_girl_id) xalign 0.5 ypos 30 style "gallery_titles"

        use gallery_icons

    # Arrow left
        imagebutton:
            xalign 0.0
            ypos 50
            idle "gui/arrow_left.png"
            hover "gui/arrow_left_hover.png"
            action Function(left_arrow_gallery_func)
            style "arrow_buttons"
    # Arrow right
        imagebutton:
            xalign 1.0
            ypos 50
            idle "gui/arrow_right.png"
            hover "gui/arrow_right_hover.png"
            action Function(right_arrow_gallery_func)
            style "arrow_buttons"

        imagebutton:
            xpos 25
            ypos 955
            idle "settings_back_button"
            hover "settings_back_button_hover"
            action Return()
            style "back_button"

        if store.strip_gravure_gallery == 1:
            imagebutton:
                xpos 1700
                ypos 600
                idle "gui/laff_uis/gravure.png"
                hover "gui/laff_uis/gravure_hover.png"
                action Function(toggle_gravure_gallery)
                style "button_with_sound"
        else:
            add "gui/laff_uis/gravure_grey.png" xpos 1700 ypos 600
        if store.strip_gravure_gallery == 0:
            imagebutton:
                xpos 1700
                ypos 700
                idle "gui/laff_uis/strip.png"
                hover "gui/laff_uis/strip_hover.png"
                action Function(toggle_strip_gallery)
                style "button_with_sound"
        else:
            add "gui/laff_uis/strip_grey.png" xpos 1700 ypos 700

        if strip_gravure_gallery == 0:
            if store.last_number_of_page < get_girl_gravure_amount(store.gallery_girl_id):
                imagebutton:
                    xpos 1770
                    ypos 885
                    idle "gui/next_button.png"
                    hover "gui/next_button_hover.png"
                    action  Function(next_action)
                    style "arrow_buttons"
        else:
            if store.last_number_of_page < get_girl_strip_amount(store.gallery_girl_id):
                imagebutton:
                    xpos 1770
                    ypos 885
                    idle "gui/next_button.png"
                    hover "gui/next_button_hover.png"
                    action  Function(next_action)
                    style "arrow_buttons"

        if store.first_number_of_page != 1:
            imagebutton:
                xpos 1770
                ypos 955
                idle "gui/prev_button.png"
                hover "gui/prev_button_hover.png"
                action Function(prev_action)
                style "arrow_buttons"

screen gallery_icons:
    if store.strip_gravure_gallery == 0:
        for i in get_gallery_image_mosaic(store.gallery_girl_id, store.first_number_of_page, store.last_number_of_page):
            for j in i:
                if j[0]:
                    if get_girl_gravure_stage_unlocked(store.gallery_girl_id) >= j[1]:
                        imagebutton:
                            xpos 200 + (j[2]*400) + (j[2]*120)
                            ypos 140 + (j[3]*225) + (j[3]*60)
                            idle j[0]
                            action [Function(toggle_display_gravure, j[1]), Function(toggle_overlay_for_tumbnail, j[3], j[2])]# Display the image this is linked with.
                            hovered Function(toggle_overlay_for_tumbnail, j[3], j[2])
                            unhovered Function(toggle_overlay_for_tumbnail, j[3], j[2])
                    else:
                        add "gui/lock_base.png" xpos 200 + (j[2]*400) + (j[2]*120)  ypos 140 + (j[3]*225) + (j[3]*60)
                else:
                    pass

        for i in range(3):
            for j in range(3):
                if tumbnail_overlays[i][j] == 1:
                    add "gui/gallery_hover.png" xpos (200 + (j*400) + (j*120)) ypos (140 + (i*225) + (i*60))
    elif store.strip_gravure_gallery == 1:
        for i in get_gallery_image_mosaic(store.gallery_girl_id, store.first_number_of_page, store.last_number_of_page, 1):
            for j in i:
                if j[0]:
                    if get_girl_strip_stage_unlocked(store.gallery_girl_id) >= j[1]:
                        imagebutton:
                            xpos 200 + (j[2]*400) + (j[2]*120)
                            ypos 140 + (j[3]*225) + (j[3]*60)
                            idle "gui/blank_gallery_image.png"
                            action [Function(toggle_display_strip, j[1]), Function(toggle_overlay_for_tumbnail, j[3], j[2])]# Display the image this is linked with.
                            hovered Function(toggle_overlay_for_tumbnail, j[3], j[2])
                            unhovered Function(toggle_overlay_for_tumbnail, j[3], j[2])

                        add j[0] xpos 200 + (j[2]*400) + (j[2]*120) + 106 ypos 140 + (j[3]*225) + (j[3]*60)
                    else:
                        add "gui/lock_base.png" xpos 200 + (j[2]*400) + (j[2]*120)  ypos 140 + (j[3]*225) + (j[3]*60)
                else:
                    pass

        for i in range(3):
            for j in range(3):
                if tumbnail_overlays[i][j] == 1:
                    add "gui/gallery_hover.png" xpos (200 + (j*400) + (j*120)) ypos (140 + (i*225) + (i*60))

screen gravure_screen:
    if store.strip_gravure_gallery == 0:
        add get_gravure_image(store.gallery_girl_id, store.current_gravure_to_display)
    elif store.strip_gravure_gallery == 1:
        add get_strip_image(store.gallery_girl_id, store.current_strip_to_display) xalign 0.5
    imagebutton:
        xpos 25
        ypos 955
        idle "settings_back_button"
        hover "settings_back_button_hover"
        action Function(return_to_gallery)
