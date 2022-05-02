init python:
    destiny_gravure_25_path = "images/characters/destiny/gravure/animated/gravure_25"

image gravure_25_anim = Movie(play="images/characters/destiny/gravure/animated/gravure_25/0.webm")


image destiny_animated_background = Movie(play="images/characters/destiny/destiny_background.webm")
image flavia_animated_background = Movie(play="images/characters/flavia/flavia_background.webm")
image marcella_animated_background = Movie(play="images/characters/marcella/marcella_background.webm")
image marcella_animated_background_2 = Movie(play="images/characters/marcella/marcella_background_2.webm")
image mina_animated_background = Movie(play="images/characters/mina/mina_background.webm")
image rose_animated_background = Movie(play="images/characters/rose/rose_background.webm")
image shera_animated_background = Movie(play="images/characters/shera/shera_background.webm")
image sylvia_animated_background = Movie(play="images/characters/sylvia/sylvia_background.webm")
image yuuki_animated_background = Movie(play="images/characters/yuuki/yuuki_background.webm")

init python:
    main_menu_background_list = [
        "sylvia_animated_background",
        "shera_animated_background",
        ["marcella_animated_background", "marcella_animated_background_2"],
        "flavia_animated_background",
        "yuuki_animated_background",
        "rose_animated_background",
        "destiny_animated_background",
        "mina_animated_background"
    ]
