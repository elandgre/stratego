import sys
from utils.constants import *

class Player:
    def __init__(self, backend, engine,ai=None):
        self.ai = ai
        self.engine = engine
        self.start_move = (-1, -1)
        self.end_move = (-1, -1)
        self.backend = backend

    def set_move(self, move):
        self.start_move = (move[0][0], move[0][1])
        self.end_move = (move[1][0], move[1][1])

    def get_move_pos(self):
        return self.start_move, self.end_move


    def get_starting_state(self):
        if not self.ai:
            return good_start_states[0]
        else:
            return self.ai.get_starting_state()

    def get_move(self):
        if not self.ai:
            #sys.stdout.write("input your move: ")

            if not self.backend :
                (x1,y1),(x2,y2) = self.get_move_pos()
            else:
                invalid_input = True
                while invalid_input:
                    try :
                        sys.stdout.write("input your move: ")
                        (x1,y1),(x2,y2) = input()
                        invalid_input = False
                    except Exception as e:
                        print "input must be of the form: (i1,j1),(i2,j2)"
                        print "where (i1,j1) is the starting position"
                        print "and (i2,j2) is the ending position"
            return (x1,y1),(x2,y2)
        else:
            return self.ai.get_move()

    def is_human(self):
        return not self.ai