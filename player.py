import sys
class Player:
    def __init__(self,engine,ai=None):
        self.ai = ai
        self.engine = engine

    def get_starting_state(self):
        if not self.ai:
            return [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]

    def get_move(self):
        if not self.ai:
            invalid_input = True
            while invalid_input:
                try:
                    sys.stdout.write("input your move: ")
                    (x1,y1),(x2,y2) = input()
                    invalid_input = False
                except Exception as e:
                    print "input must be of the form: (x1,y1),(x2,y2)"
                    print "where (x1,y1) is the starting position"
                    print "and (x2,y2) is the ending position"
            return (x1,y1),(x2,y2)
    def is_human(self):
        return not self.ai