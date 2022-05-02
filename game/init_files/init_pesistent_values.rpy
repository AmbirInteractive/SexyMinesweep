init -1:
    default persistent.current_password = None

    default persistent.cheat_code_used = False
    default persistent.promo_activated = True
    default persistent.animations_on = True
    default persistent.mobile_build_on = False

    default persistent.current_girl_id = 0
    default persistent.amount_of_wins = 0
    default persistent.amount_of_losses = 0

    default persistent.girls_data_repo = [
        ["sylvia", 8, 27, 0, 0, 0, 0],
        ["shera", 8, 27, 0, 0, 0, 0],
        ["marcella", 8, 27, 0, 0, 0, 0],
        ["yuuki", 8, 27, 0, 0, 0, 0],
        ["flavia", 8, 27, 0, 0, 0, 0],
        ["rose", 8, 27, 0, 0, 0, 0],
        ["destiny", 8, 27, 0, 0, 0, 0],
        ["mina", 8, 27, 0, 0, 0, 0]
    ]

    init python:
        cheat_password = "WeirdParrot"
        girls_repo = [
            ["sylvia", 8, 27],
            ["shera", 8, 27],
            ["marcella", 8, 27],
            ["yuuki", 8, 27],
            ["flavia", 8, 27],
            ["rose", 8, 27],
            ["destiny", 8, 27],
            ["mina", 8, 27],
            ["talia", 8, 9],
            ["sylph", 8, 9]
        ]

        girls_data_repo_name_pos = 0
        girls_data_repo_strip_pos = 1
        girls_data_repo_gravure_pos = 2
        girls_data_repo_strip_unlocked_pos = 3
        girls_data_repo_gravure_unlocked_pos = 4
        girls_data_repo_wins_pos = 5
        girls_data_repo_losses_pos = 6

        def get_girl_name(_girl_id):
            return persistent.girls_data_repo[_girl_id][girls_data_repo_name_pos]

        def get_girl_strip_amount(_girl_id):
            return persistent.girls_data_repo[_girl_id][girls_data_repo_strip_pos]

        def get_girl_gravure_amount(_girl_id):
            return persistent.girls_data_repo[_girl_id][girls_data_repo_gravure_pos]

        def get_girl_strip_stage_unlocked(_girl_id):
            return persistent.girls_data_repo[_girl_id][girls_data_repo_strip_unlocked_pos]

        def get_girl_gravure_stage_unlocked(_girl_id):
            return persistent.girls_data_repo[_girl_id][girls_data_repo_gravure_unlocked_pos]

        def get_girl_wins(_girl_id):
            return persistent.girls_data_repo[_girl_id][girls_data_repo_wins_pos]

        def get_girl_losses(_girl_id):
            return persistent.girls_data_repo[_girl_id][girls_data_repo_losses_pos]

        def set_girl_strip_unlocked(_girl_id, _new_value):
            if _new_value <= get_girl_strip_amount(_girl_id) and _new_value > 0:
                persistent.girls_data_repo[_girl_id][girls_data_repo_strip_unlocked_pos] = _new_value
            else:
                persistent.girls_data_repo[_girl_id][girls_data_repo_strip_unlocked_pos] = get_girl_strip_amount(_girl_id)

        def set_girl_gravure_unlocked(_girl_id, _increase):
            if get_girl_gravure_stage_unlocked(_girl_id) + _increase <= get_girl_gravure_amount(_girl_id):
                persistent.girls_data_repo[_girl_id][girls_data_repo_gravure_unlocked_pos] = get_girl_gravure_stage_unlocked(_girl_id) + _increase
            else:
                persistent.girls_data_repo[_girl_id][girls_data_repo_gravure_unlocked_pos] = get_girl_gravure_amount(_girl_id)

        def update_girls_data_repo():
            if persistent.current_password != cheat_password:
                persistent.cheat_code_used = False
                persistent.promo_activated = True
                persistent.current_password = cheat_password

            temp_repo = girls_repo

            for i in range(len(temp_repo)):
                if i < len(persistent.girls_data_repo):
                    persistent.girls_data_repo[i][girls_data_repo_name_pos] = temp_repo[i][girls_data_repo_name_pos]
                    persistent.girls_data_repo[i][girls_data_repo_strip_pos] = temp_repo[i][girls_data_repo_strip_pos]
                    persistent.girls_data_repo[i][girls_data_repo_gravure_pos] = temp_repo[i][girls_data_repo_gravure_pos]
                else:
                    persistent.girls_data_repo.append([temp_repo[i][girls_data_repo_name_pos], temp_repo[i][girls_data_repo_strip_pos], temp_repo[i][girls_data_repo_gravure_pos], 0, 0, 0, 0])


        update_girls_data_repo()
