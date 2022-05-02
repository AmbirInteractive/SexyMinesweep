init python:
    square_state_hidden = 0
    square_state_flagged = 1
    square_state_mine = 2
    square_state_empty = 3


    class Square_Class(store.object):
        def __init__(self, _contains_mine, _square_pos, _nearby_mines):
            self.state = square_state_hidden
            self.is_revealed = False
            self.contains_mine = _contains_mine
            self.is_flagged = False
            self.square_pos = _square_pos
            self.nearby_mines = _nearby_mines
            self.has_been_checked_for_empty = False
            self.has_been_flagged_properly = False
            self.has_been_checked_for_proper_flag = False
            self.surrounding_flags = 0
            self.clicked_to_clear_surrounding_squares = False

        def get_has_been_flagged_properly(self):
            return self.has_been_flagged_properly
        def set_has_been_flagged_properly(self, _set):
            self.has_been_flagged_properly = _set
        def get_has_been_checked_for_proper_flag(self):
            return self.has_been_checked_for_proper_flag

        def get_has_been_checked_for_empty(self):
            return self.has_been_checked_for_empty

        def set_has_been_checked_for_empty(self):
            self.has_been_checked_for_empty = True

        def get_is_empty(self):
            if (self.get_contains_mine() == False) and (self.get_nearby_mines() == 0) and (self.get_is_flagged() == False):
                return True
            else:
                return False

        def get_nearby_mines(self):
            return self.nearby_mines

        def get_square_state(self):
            return self.state

        def get_square_pos(self):
            return self.square_pos

        def get_is_revealed(self):
            return self.is_revealed

        def get_contains_mine(self):
            return self.contains_mine

        def get_is_flagged(self):
            return self.is_flagged

        def set_is_revealed(self, _new_status=True):
            if self.is_flagged == False:
                self.is_revealed = _new_status
                if self.is_revealed == True:
                    if self.get_contains_mine() == True:
                        self.state = square_state_mine
                    else:
                        self.state = square_state_empty
                return True
            else:
                return False

        def set_is_flagged(self, _new_state):
            self.is_flagged = _new_state

        def set_state(self, _new_state):
            self.state = _new_state

        def get_surrounding_flags(self):
            return self.surrounding_flags

        def increment_surrounding_flags(self):
            self.surrounding_flags += 1

        def decrement_surrounding_flags(self):
            self.surrounding_flags -= 1

        def set_clicked_to_clear_surrounding_squares(self):
            self.clicked_to_clear_surrounding_squares = True

        def get_clicked_to_clear_surrounding_squares(self):
            return self.clicked_to_clear_surrounding_squares
