init python:
    import sys
    character_sylvia = 0
    character_shera = 1
    character_marcella = 2
    character_yuuki = 3
    character_flavia = 4
    character_rose = 5
    character_destiny = 6
    character_mina = 7

    girls_sprites_main_menu_pos = 0
    girls_sprites_selection_screen_pos = 1
    girls_sprites_difficulty_choice_menu_pos = 2
    girls_sprites_strip_pos = 3
    girls_sprites_gravure_pos = 4

    main_menu_base = 0
    main_menu_hover = 1

    difficulty_choice_base = 0

    selection_screen_base = 0
    selection_screen_hover = 1
    selection_screen_selected = 2

    class Gravure_Not_Found(Exception):
        pass

    def get_main_menu_sprite(_girl_id, pose = main_menu_base):
        if pose == main_menu_base:
            return "images/characters/" + get_girl_name(_girl_id) + "/main_menu_base.webp"
        else:
            return "images/characters/" + get_girl_name(_girl_id) + "/main_menu_hover.webp"

    def get_selection_screen_sprite(_girl_id, pose = selection_screen_base):
        if pose == selection_screen_base:
            return "images/characters/" + get_girl_name(_girl_id) + "/card_base.webp"
        elif pose == selection_screen_hover:
            return "images/characters/" + get_girl_name(_girl_id) + "/card_hover.webp"
        else:
            return "images/characters/" + get_girl_name(_girl_id) + "/card_selected.webp"

    def get_difficulty_choice_sprite(_girl_id, pose = difficulty_choice_base):
        if pose == difficulty_choice_base:
            return "images/characters/" + get_girl_name(_girl_id) + "/difficulty_choice_base.webp"
        else:
            return "images/characters/" + get_girl_name(_girl_id) + "/difficulty_choice_hover.webp"

    #def GirlIDRequestedTooHigh(Exception):
    #    pass


    def get_strip_sprite(_girl_id, _strip_id):
        if _strip_id < 1:
            #raise Exception("Strip ID (" + str(_strip_id) + ") requested under 1.")
            return "images/characters/" + get_girl_name(_girl_id) + "/strip/strip_" + str(1) + ".webp"
        elif  _strip_id > get_girl_strip_amount(_girl_id):
            return "images/characters/" + get_girl_name(_girl_id) + "/strip/strip_" + str(get_girl_strip_amount(_girl_id)) + ".webp"
        else:
            return "images/characters/" + get_girl_name(_girl_id) + "/strip/strip_" + str(_strip_id) + ".webp"

    def get_mine_sweeper_girl_sprite():
        percent_clothed = game_manager.get_percent_completion()
        #num_of_squares = game_manager.get_grid_size()[0] * game_manager.get_grid_size()[0]
        #squares_discovered = game_manager.get_squares_discovered()
        girl_sprite = ""

        #strip_step = 100.0 / get_girl_strip_amount(persistent.current_girl_id)
        #while strip_step != int(strip_step):
            #num_of_squares * 10
            #squares_discovered * 10
        #    strip_step * 10
        #    percent_clothed * 10
        percent_step = 100.0 / get_girl_strip_amount(persistent.current_girl_id)

        current_strip_step = 0
        while percent_clothed > percent_step:
            current_strip_step += 1
            percent_clothed -= percent_step

        girl_sprite = get_strip_sprite(persistent.current_girl_id, current_strip_step+1)
        if get_girl_strip_stage_unlocked(persistent.current_girl_id) < current_strip_step + 1:
            set_girl_strip_unlocked(persistent.current_girl_id, current_strip_step + 1)

        #if percent_clothed > 80:
        #    girl_sprite = get_strip_sprite(0)
        #elif percent_clothed > 60:
        #    girl_sprite = get_strip_sprite(1)
        #elif percent_clothed > 40:
        #    girl_sprite = get_strip_sprite(2)
        #elif percent_clothed > 20:
        #    girl_sprite = get_strip_sprite(3)
        #elif percent_clothed > 0:
        #    girl_sprite = get_strip_sprite(4)
        #else:
        #    girl_sprite = get_strip_sprite(5)

        return girl_sprite

    def get_gravure_image(_girl_id, _gravure_id, _thumbnail = False):
        if _gravure_id <= get_girl_gravure_amount(_girl_id):

            if _thumbnail == True:
                #return im.Scale("images/characters/" + get_girl_name(_girl_id) + "/gravure/gravure_" + str(_gravure_id) + ".png", 400, 225)
                return Transform("images/characters/" + get_girl_name(_girl_id) + "/gravure/gravure_" + str(_gravure_id) + ".webp", xsize=400, ysize=225, fit='contain')
            else:
                if _girl_id != 6 or _gravure_id != 25 or store.persistent.animations_on == False:
                    return "images/characters/" + get_girl_name(_girl_id) + "/gravure/gravure_" + str(_gravure_id) + ".webp"
                else:
                    return "gravure_25_anim"
        else:
            image_to_return = False

    def get_strip_image(_girl_id, _strip_id, _thumbnail = False):
        if _strip_id <= get_girl_strip_amount(_girl_id):

            if _thumbnail == True:
                #return im.Scale("images/characters/" + get_girl_name(_girl_id) + "/gravure/gravure_" + str(_gravure_id) + ".png", 400, 225)
                #try:
                return Transform("images/characters/" + get_girl_name(_girl_id) + "/strip/strip_" + str(_strip_id) + ".webp", xsize=400, ysize=225, fit='contain')
                #except IOError:
                #    return Transform("animated_game_bg", xsize=400, ysize=225, fit='contain')

            else:
                return "images/characters/" + get_girl_name(_girl_id) + "/strip/strip_" + str(_strip_id) + ".webp"

        else:
            image_to_return = False


    def get_gallery_image_mosaic(_girl_id, _lower_border, _higher_border, gravure_or_strip = 0):
        gallery_mosaic = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        image_id = _lower_border
        x_pos = 0
        y_pos = 0

        for i in range(3):
            for j in range(3):
                if gravure_or_strip == 0:
                    gallery_mosaic[i][j] = [
                        get_gravure_image(_girl_id, image_id, True),
                        image_id,
                        j,
                        i
                    ]
                else:
                    gallery_mosaic[i][j] = [
                        get_strip_image(_girl_id, image_id, True),
                        image_id,
                        j,
                        i
                    ]
                image_id += 1

        return gallery_mosaic


    #class Sprites_Manager(store.object):
    #    def __init__(self):
    #        ""

    #    def display_
