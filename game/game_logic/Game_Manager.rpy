init python:
    game_lost = 0
    game_in_progress = 1
    game_won = 2
    class Game_Manager(store.object):
        def __init__(self):
            self.game_running = True
            self.game_state = game_in_progress
            self.grid_structure = []
            self.first_square = True
            self.first_selected_square = []

        def get_original_grid_structure(self):
            return self.grid_structure.get_original_grid_structure()

        def get_adjacent_mines_array(self):
            return self.grid_structure.get_adjacent_mines_array()

        def get_mine_placement_array(self):
            return self.grid_structure.get_mine_placement_array()

        def get_game_state(self):
            return self.game_state

        def get_game_mode(self):
            return self.grid_structure.get_game_mode()

        def get_game_running(self):
            return self.game_running

        def get_grid_structure(self):
            return self.grid_structure.get_grid_structure()

        def get_grid_structure_coords(self, _xpos, _ypos):
            return self.grid_structure.get_grid_structure_coords(_xpos, _ypos)

        def reveal_square(self, _xpos, _ypos):
            if self.first_square:
                self.grid_structure.reveal_square(_xpos, _ypos)
                # self.first_selected_square = self.get_grid_structure_coords(_xpos, _ypos)
                # if self.get_game_mode() == mode_beginner:
                #     self.build_grid(self.get_game_mode, [9, 9], 16)
                # elif self.get_game_mode() == mode_intermediate:
                #      self.build_grid(self.get_game_mode, [16, 16], 40)
                # elif self.get_game_mode() == mode_advanced:
                #      self.build_grid(self.get_game_mode, [24, 24], 99)
                self.grid_structure.reveal_square(_xpos, _ypos)
                self.first_square = False
            else:
                self.grid_structure.reveal_square(_xpos, _ypos)


        def set_game_running(self, _new_state):
            self.game_running = _new_state

        def set_game_state(self, _new_state):
            self.game_state = _new_state

        def setup_game(self, _game_mode):
            self.game_running = True
            self.game_state = game_in_progress
            self.first_square = True
            if _game_mode == mode_beginner:
                # self.build_grid(_game_mode, [9, 9], 0)
                self.build_grid(_game_mode, [9, 9], 10)

            elif _game_mode == mode_intermediate:
                # self.build_grid(_game_mode, [16, 16], 0)
                self.build_grid(_game_mode, [16, 16], 40)

            elif _game_mode == mode_advanced:
                # self.build_grid(_game_mode, [24, 24], 0)
                self.build_grid(_game_mode, [24, 24], 99)


        def get_grid_size(self):
            return self.grid_structure.get_grid_size()

        def get_squares_discovered(self):
            return self.grid_structure.get_squares_discovered()

        def build_grid(self, _game_mode, _grid_dimensions, _number_of_mines):
            self.grid_structure = Grid_Class(_game_mode, _grid_dimensions, _number_of_mines)

        def build_blank_grid(self, _game_mode, _size_x, _size_y):
            self.grid_structure = Grid_Class(_game_mode, [_size_x, _size_y], 0)

        def check_victory_condition(self):
            self.grid_structure.check_victory_condition()

        def flag_square(self, _xpos, _ypos):
            self.grid_structure.flag_square(_xpos, _ypos)

        def get_percent_completion(self, _inverted=False, _display=False):
            return self.grid_structure.get_grid_completion_percent(_inverted, _display)

        def flag_all_squares(self, _value):
            self.grid_structure.flag_all_squares(_value)

        def get_flags_surrounding_square(self, _xpos, _ypos):
            return self.grid_structure.get_flags_surrounding_square(_xpos, _ypos)

        def reveal_all_surrounding_hidden_squares(self, _xpos, _ypos):
            self.grid_structure.reveal_all_surrounding_hidden_squares(_xpos, _ypos)

        #def restart_game(self):
