init python:
    import copy
    empty_square = 0
    mined_square = 1
    flagged_square = 2

    mine_confirmation_structure = [
        [[-1, -1], [0, -1], [1, -1]],
        [[-1, 0], [1, 0]],
        [[-1, 1], [0, 1], [1, 1]]
    ]

    class Grid_Class(store.object):
        def __init__(self, _game_mode, _grid_dimensions, _number_of_mines):
            self.game_mode = _game_mode
            self.grid_dimensions = _grid_dimensions
            self.number_of_mines = _number_of_mines
            self.mine_placement_array = []
            self.adjacent_mines_array = []
            self.original_grid_structure = []

            self.grid_structure = []

            self.squares_still_hidden = _grid_dimensions[0] * _grid_dimensions[1]
            self.flags_active = 0
            self.mines_left = _number_of_mines
            self.starting_mine_total = _number_of_mines

            self.build_grid(self.grid_dimensions[0], self.grid_dimensions[1])

            self.completion_percent = 0
            #self.reveal_all_mines()

        def get_squares_still_hidden(self):
            return self.squares_still_hidden

        def decrement_squares_still_hidden(self):
            self.squares_still_hidden -= 1

        def get_flags_active(self):
            return self.flags_active

        def increment_flags_active(self, _xpos, _ypos):
            self.flags_active += 1

            for i in mine_confirmation_structure:
                for j in i:
                    if self.check_within_bounds((_xpos + j[0]), (_ypos + j[1])):
                        self.grid_structure[(_xpos + j[0])][(_ypos + j[1])].increment_surrounding_flags()
                    else:
                        pass


        def decrement_flags_active(self, _xpos, _ypos):
            self.flags_active -= 1

            for i in mine_confirmation_structure:
                for j in i:
                    if self.check_within_bounds((_xpos + j[0]), (_ypos + j[1])):
                        self.grid_structure[(_xpos + j[0])][(_ypos + j[1])].decrement_surrounding_flags()
                    else:
                        pass



        def get_mines_left(self):
            return self.starting_mine_total - self.flags_active

        def get_starting_mines_total(self):
            return self.starting_mine_total

        def confirm_mine_flagged_correctly(self, _square_pos):
            grid_side = self.grid_dimensions[0]
            for i in mine_confirmation_structure:
                for j in i:
                    x_pos_to_check = _square_pos[0] + j[0]
                    y_pos_to_check = _square_pos[1] + j[1]
                    if (x_pos_to_check > 0) and (x_pos_to_check < grid_side) and (y_pos_to_check > 0) and (y_pos_to_check < grid_side):
                        if self.grid_structure[y_pos_to_check][x_pos_to_check].get_square_state() == square_state_hidden:
                            return False
                        elif self.grid_structure[y_pos_to_check][x_pos_to_check].get_square_state() == square_state_flagged:
                            if self.grid_structure[y_pos_to_check][x_pos_to_check].get_contains_mine():
                                pass
                            else:
                                return False
                        elif self.grid_structure[y_pos_to_check][x_pos_to_check].get_square_state() == square_state_empty:
                            pass
                    else:
                        pass
            return True


        def get_grid_completion_percent(self, _inverted=False, _display=False):
            squares_to_discover = 0
            squares_revealed = 0
            squares_flagged_properly = 0
            squares_flagged = 0
            for i in self.grid_structure:
                for j in i:
                    if j.get_square_state() == square_state_empty:
                        squares_revealed += 1
                    elif j.get_square_state() == square_state_flagged:
                        if j.get_has_been_flagged_properly():
                            squares_flagged_properly += 1
                        else:
                            if j.get_contains_mine():
                                if self.confirm_mine_flagged_correctly(j.get_square_pos()):
                                    squares_flagged_properly += 1
                                else:
                                    squares_flagged += 1
                            else:
                                squares_flagged += 1
                    else:
                        squares_to_discover += 1

            if _display == False:
                squares_discovered = squares_revealed# + squares_flagged_properly
                number_of_squares = squares_to_discover + squares_discovered + squares_flagged
            else:
                squares_discovered = squares_revealed + squares_flagged# + squares_flagged_properly
                number_of_squares = squares_to_discover + squares_discovered


            percent_discovered = float(squares_discovered) * 100 / float(number_of_squares)

            if _display == False:
                if percent_discovered > self.completion_percent:
                    self.completion_percent = percent_discovered
                else:
                    percent_discovered = self.completion_percent

            if _inverted == False:
                return percent_discovered
            else:
                return 100.0 - percent_discovered

        def get_squares_discovered(self):
            squares_to_discover = 0
            squares_revealed = 0
            squares_flagged_correctly = 0
            for i in self.grid_structure:
                for j in i:
                    if j.get_square_state() == square_state_empty:
                        squares_revealed += 1
                    elif j.get_square_state() == square_state_flagged:
                        if j.get_contains_mine():
                            squares_flagged_correctly += 1
                        else:
                            squares_to_discover += 1
                    else:
                        squares_to_discover += 1

            return squares_revealed# + squares_flagged_correctly


        def increment_mines_left(self):
            self.mines_left += 1

        def decrement_mines_left(self):
            self.mines_left -= 1

        def check_victory_condition(self):
            if not game_manager.first_square:
                if (self.mines_left == 0) and (self.squares_still_hidden == self.starting_mine_total):
                    store.game_manager.set_game_state(game_won)
                    persistent.amount_of_wins += 1

        def get_original_grid_structure(self):
            return self.original_grid_structure

        def get_adjacent_mines_array(self):
            return self.adjacent_mines_array

        def get_mine_placement_array(self):
            return self.mine_placement_array

        def get_game_mode(self):
            return self.game_mode

        def get_grid_size(self):
            return self.grid_dimensions

        def get_grid_structure(self):
            return self.grid_structure

        def get_grid_structure_coords(self, _xpos, _ypos):
            return self.grid_structure[_xpos][_ypos]

        def reveal_square(self, _xpos, _ypos):
            if self.grid_structure[_xpos][_ypos].get_is_flagged():
                return
            elif self.grid_structure[_xpos][_ypos].get_contains_mine():
                if game_manager.first_square:
                    self.build_grid(self.grid_dimensions[0], self.grid_dimensions[1])
                    self.reveal_square(_xpos, _ypos)
                #    game_manager.first_selected_square.append([])
                #    game_manager.first_selected_square = self.grid_structure[_xpos][_ypos]
                #    if game_manager.get_game_mode() == mode_beginner:
                #        game_manager.build_grid(game_manager.get_game_mode, [9, 9], 16)
                #    elif game_manager.get_game_mode() == mode_intermediate:
                #         game_manager.build_grid(game_manager.get_game_mode, [16, 16], 40)
                #    elif game_manager.get_game_mode() == mode_advanced:
                #         game_manager.build_grid(game_manager.get_game_mode, [24, 24], 99)
                #    self._reveal_square(_xpos, _ypos)
                else:
                    self.reveal_all_mines()
                    game_manager.set_game_state(game_lost)
                    persistent.amount_of_losses += 1
            self.reveal_if_empty(_xpos, _ypos)
            self.check_victory_condition()
            #    return
            #else:
            #    self.grid_structure[_xpos][_ypos].set_is_revealed()

        def _reveal_square(self, _xpos, _ypos):
            if self.grid_structure[_xpos][_ypos].get_is_flagged():
                pass
            else:
                self.grid_structure[_xpos][_ypos].set_is_revealed()
                self.decrement_squares_still_hidden()

        def flag_square(self, _xpos, _ypos):
            if self.grid_structure[_xpos][_ypos].get_is_flagged() == False:
                self.grid_structure[_xpos][_ypos].set_is_flagged(True)
                self.grid_structure[_xpos][_ypos].set_state(square_state_flagged)
                self.increment_flags_active(_xpos, _ypos)
                if self.grid_structure[_xpos][_ypos].get_contains_mine() == True:
                    self.decrement_mines_left()



            elif self.grid_structure[_xpos][_ypos].get_is_flagged() == True:
                self.grid_structure[_xpos][_ypos].set_is_flagged(False)
                self.grid_structure[_xpos][_ypos].set_state(square_state_hidden)
                self.decrement_flags_active(_xpos, _ypos)
                if self.grid_structure[_xpos][_ypos].get_contains_mine() == True:
                    self.increment_mines_left()

            self.check_victory_condition()

        def get_flags_surrounding_square(self, _xpos, _ypos):
            return self.grid_structure[_xpos][_ypos].get_surrounding_flags()

        def reveal_all_surrounding_hidden_squares(self, _xpos, _ypos):
            for i in mine_confirmation_structure:
                for j in i:
                    if self.check_within_bounds(_xpos + j[0], _ypos + j[1]):
                        self.reveal_square((_xpos + j[0]), (_ypos + j[1]))
                    else:
                        pass

                self.grid_structure[_xpos][_ypos].set_clicked_to_clear_surrounding_squares()

        def check_within_bounds(self, _xpos, _ypos):
            within_bounds = True
            if (_xpos < 0) or (_ypos < 0):
                within_bounds = False
            elif (_xpos >= self.grid_dimensions[0]) or (_ypos >= self.grid_dimensions[1]):
                within_bounds = False
            return within_bounds

        def build_blank_grid(self, _size_y, _size_x):
            new_grid = []
            for i in range(_size_y):
                new_grid.append([])
                for j in range(_size_x):
                    new_grid[i].append(0)
            return new_grid

        def build_grid(self, _size_y, _size_x):
            mine_placement_array = self.roll_mines_locations(self.build_grid_chassis(_size_y, _size_x))
            self.mine_placement_array = self.copy_grid(mine_placement_array)
            adjacent_mines_array = self.build_adjacent_mines_array(mine_placement_array)
            self.adjacent_mines_array = self.copy_grid(adjacent_mines_array)
            for i in range(len(mine_placement_array)):
                for j in range(len(mine_placement_array[0])):
                    grid_square = Square_Class(mine_placement_array[i][j], [i, j], adjacent_mines_array[i][j])
                    self.grid_structure[i][j] = grid_square

        def build_grid_chassis(self, _size_y, _size_x):
            self.original_grid_structure = self.copy_grid(self.build_blank_grid(_size_y,_size_x))
            self.grid_structure = self.copy_grid(self.original_grid_structure)
            return self.copy_grid(self.original_grid_structure)

        def roll_mines_locations(self, _grid):
            return self.roll_mines(_grid)

        def roll_mines(self, _grid):
            new_grid = self.copy_grid(_grid)
            mines_to_roll = self.starting_mine_total
            while mines_to_roll != 0:
                indice_i = renpy.random.randint(0, len(_grid)-1)
                indige_j = renpy.random.randint(0, len(_grid[0])-1)
                if new_grid[indice_i][indige_j] == game_manager.first_selected_square:
                    continue
                if new_grid[indice_i][indige_j] != 1:
                    new_grid[indice_i][indige_j] = 1
                    mines_to_roll -= 1
            return new_grid

        def copy_grid(self, _grid):
            new_grid = copy.deepcopy(_grid)
            #for i in range(len(_grid)):
            #    new_grid.append([])
            #    for j in range(len(_grid[0])):
            #        new_grid[i].append(_grid[j][i])
            return new_grid


        def build_adjacent_mines_array(self, _mine_array):
            adjacent_mines_array = self.copy_grid(_mine_array)

            for i in range(len(_mine_array)):
                for j in range(len(_mine_array[0])):
                    if _mine_array[i][j] == mined_square:
                        right_valid = self._adjacent_mines_array_is_right_valid(j, len(_mine_array[0]) - 1)
                        left_valid = self._adjacent_mines_array_is_left_valid(j)
                        minus_valid = self._adjacent_mines_array_is_indice_minus_valid(i)
                        incremented_valid = self._adjacent_mines_array_is_indice_incremented_valid(i, len(_mine_array) - 1)

                        adjacent_mines_array[i][j] -= 9

                        if right_valid == True:
                            adjacent_mines_array[i][j + 1] += 1
                        if left_valid == True:
                            adjacent_mines_array[i][j - 1] += 1

                        if minus_valid == True:
                            adjacent_mines_array[i - 1][j] += 1
                            if left_valid == True:
                                adjacent_mines_array[i - 1][j - 1] += 1
                            if right_valid == True:
                                adjacent_mines_array[i - 1][j + 1] += 1

                        if incremented_valid == True:
                            adjacent_mines_array[i + 1][j] += 1
                            if left_valid == True:
                                adjacent_mines_array[i + 1][j - 1] += 1
                            if right_valid == True:
                                adjacent_mines_array[i + 1][j + 1] += 1

            return adjacent_mines_array

        def _adjacent_mines_array_is_right_valid(self, _indice, _top_value):
            if _indice != _top_value:
                return True
            else:
                return False

        def _adjacent_mines_array_is_left_valid(self, _indice):
            if _indice != 0:
                return True
            else:
                return False

        def _adjacent_mines_array_is_indice_minus_valid(self, _indice):
            if _indice != 0:
                return True
            else:
                return False

        def _adjacent_mines_array_is_indice_incremented_valid(self, _indice, _top_value):
            if _indice != _top_value:
                return True
            else:
                return False

        def reveal_if_empty(self, _xpos_j, _ypos_i):
            if (self.grid_structure[_xpos_j][_ypos_i].get_has_been_checked_for_empty() == False) and (self.grid_structure[_xpos_j][_ypos_i].get_is_flagged() == False):
                self.grid_structure[_xpos_j][_ypos_i].set_has_been_checked_for_empty()
                self._reveal_square(_xpos_j, _ypos_i)
                #self.grid_structure[_xpos_j][_ypos_i].set_is_revealed()
                #self.decrement_squares_still_hidden()
                if self.grid_structure[_xpos_j][_ypos_i].get_is_empty():
                    self.reveal_adjacent_empty_squares(_xpos_j, _ypos_i)

        def reveal_adjacent_empty_squares(self, _xpos_j, _ypos_i):
            #if _mine_array[_xpos_j][_ypos_i] == mined_square:
            right_valid = self._adjacent_mines_array_is_right_valid(_ypos_i, len(self.grid_structure[0]) - 1)
            left_valid = self._adjacent_mines_array_is_left_valid(_ypos_i)
            minus_valid = self._adjacent_mines_array_is_indice_minus_valid(_xpos_j)
            incremented_valid = self._adjacent_mines_array_is_indice_incremented_valid(_xpos_j, len(self.grid_structure) - 1)

            if right_valid == True:
                self.reveal_if_empty(_xpos_j, _ypos_i + 1)
            if left_valid == True:
                self.reveal_if_empty(_xpos_j, _ypos_i - 1)

            if minus_valid == True:
                self.reveal_if_empty(_xpos_j - 1, _ypos_i)
                if left_valid == True:
                    self.reveal_if_empty(_xpos_j - 1, _ypos_i - 1)
                if right_valid == True:
                    self.reveal_if_empty(_xpos_j - 1, _ypos_i + 1)

            if incremented_valid == True:
                self.reveal_if_empty(_xpos_j + 1, _ypos_i)
                if left_valid == True:
                    self.reveal_if_empty(_xpos_j + 1, _ypos_i - 1)
                if right_valid == True:
                    self.reveal_if_empty(_xpos_j + 1, _ypos_i + 1)

        def reveal_all_mines(self):
            for i in self.grid_structure:
                for j in i:
                    if j.get_contains_mine():
                        j.set_is_revealed()

        def flag_all_squares(self, _value):
            for i in self.grid_structure:
                for j in i:
                    if (j.get_is_flagged() != _value) and (j.get_is_revealed() == False):
                        j.set_is_flagged(_value)
