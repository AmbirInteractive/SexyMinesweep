init -3 python:
    import renpy.store as store
    import renpy.exports as renpy
    from operator import attrgetter
    #game_menu_screen = None

    config.keymap['game_menu'].remove('mouseup_3')

    # Archive declaration
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("soundtrack", "all")
    build.archive("videos", "all")
    build.archive("misc", "all")

    # Archive scripts
    build.classify("game/**.rpyc", "scripts")

    # Archive images
    build.classify("game/**.png", "images")
    build.classify("game/**.jpg", "images")

    # Archive audio tracks
    build.classify("game/**.mp3", "soundtrack")
    build.classify("game/**.wav", "soundtrack")
    build.classify("game/**.ogg", "soundtrack")

    # Archive video assets
    build.classify("game/**.webm", "videos")
    build.classify("game/**.mp4", "videos")

    # Archive misc stuff
    build.classify("game/**.TTF", "misc")
    build.classify("game/**.htm", "misc")
    build.classify("game/**.html", "misc")
    #build.classify("game/**.txt", "misc")

    # Exclude .rpy
    build.classify("game/game_logic/**.rpy", None)
    build.classify("game/game_scenes/**.rpy", None)
    build.classify("game/game_ui/**.rpy", None)
    build.classify("game/init_files/**.rpy", None)
    build.classify("game/gui.rpy", None)
    build.classify("game/options.rpy", None)
    build.classify("game/screens.rpy", None)
    build.classify("game/script.rpy", None)

    # Include
    #build.classify("game/adding_girl.rpy", "all")

    # Other exclusions
    build.classify("**.zip", None)
    build.classify("**.docx", None)
    build.classify("**.pdn", None)
    build.classify("**.jpeg", None)
    build.classify("**.7z", None)
    build.classify("game/old/**", None)

    renpy.sound.set_volume(0.5)

    def input_code(the_code):

        if the_code == persistent.current_password:
            persistent.cheat_code_used = True
            renpy.play("audio/GetAPowerUp.wav", "sound")
        else:
            renpy.play("audio/PointSelected.wav", "sound")

    def switch_main_menu():
        store.main_menu_current_background += 1
        if store.main_menu_current_background >= len(main_menu_background_list):
            store.main_menu_current_background = 0
        if store.main_menu_current_background == character_marcella:
            toggle_marcella_background()

    def toggle_marcella_background():
        if store.current_marcella_background == 0:
            store.current_marcella_background = 1
        else:
            store.current_marcella_background = 0

    play_mode_story = 0
    play_mode_quickie = 1

    character_selection_mode_story = 0
    character_selection_mode_quickie = 1

    def set_play_mode(_play_mode):
        store.current_play_mode = _play_mode

    def set_character_selection_menu_mode(_mode):
        store.character_selection_menu_mode = _mode

    def fix_menu_background():
        if store.main_menu_current_background >= len(main_menu_background_list):
            store.main_menu_current_background = 0


default _game_menu_screen = "preferences"
define config.rollback_enabled = False

default game_manager = Game_Manager()
#default sprites_manager = Sprites_Manager(sylvia_sprite_states_repo)
#default dialog_manager = Dialog_Manager(sylvia_dialog_collection)

style game_menu_titles:
    font "fonts/ethnocentric_rg.ttf"
    size 100

style gallery_titles:
    font "fonts/ethnocentric_rg.ttf"
    size 50

style pick_your_girl_style:
    font "fonts/ethnocentric_rg.ttf"
    size 30

style button_with_sound:
    activate_sound "audio/UI_button08.wav"
    hover_sound "audio/Menu_Sounds_V2_Metallic_HOLD.mp3"

style arrow_buttons:
    activate_sound "audio/Menu_Sounds_V2_Metallic_FORWARD.mp3"
    hover_sound "audio/Menu_Sounds_V2_Metallic_HOLD.mp3"

style back_button:
    activate_sound "audio/Menu_Sounds_V2_Metallic_BACKWARD.mp3"
    hover_sound "audio/Menu_Sounds_V2_Metallic_HOLD.mp3"

style regular_tiles_clicked:
    activate_sound "audio/UI_button05.wav"

style mines_clicked:
    activate_sound "audio/UI_button06.wav"

transform resize_to_tumbnail:
    xsize 400
    ysize 225

default number_of_girls = 10
default current_girl_id = persistent.current_girl_id
default gallery_girl_id = persistent.current_girl_id
default gravure_to_display_upon_win = 1
default click_mode = 0

default main_menu_current_background = persistent.current_girl_id
default current_marcella_background = 0

default current_play_mode = play_mode_story
default character_selection_menu_mode = character_selection_mode_story
