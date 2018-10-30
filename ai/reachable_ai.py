from ai import AI

class ReachableAI(AI):
    def __init__(self,engine,start_time,time_per_move,starter,params):
        super(BasicAI, self).__init__(engine,start_time,time_per_move, starter)
        self.parameters = params

    def get_starting_state(self):
        return self.starter.start()

    def get_move(self):
        state = self.engine.get_state()
        valid_moves = self.engine.get_valid_moves()
        time = self.time_per_move


        max_valuation = 0
        max_move = (None, None)
        for move in valid_moves:
            valuation.append(eval_move(moves))
