import sys

class Player:
    def __init__(self,engine,ai=None):
        self.ai = ai
        self.engine = engine
        self.start_move = (-1, -1)
        self.end_move = (-1, -1)

    def set_move(self, move):
        self.start_move = (move[0][0], move[0][1])
        self.end_move = (move[1][0], move[1][1])

    def get_move_pos(self):
        (x1, y1) = self.start_move
        (x2, y2) = self.end_move

    def get_starting_state(self):
        if not self.ai:
            return [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
        else:
            return self.ai.get_starting_state()

    def get_move(self):
        if not self.ai:
            invalid_input = True
            while invalid_input:
                try:
                    #sys.stdout.write("input your move: ")
                    if FRONTEND :
                        (x1,y1),(x2,y2) = self.get_move_pos()
                    else:
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