from ai import AI

class BasicAI(AI):
    def __init__(self,engine,start_time,time_per_move,starter,evaluator,searcher):
        super(BasicAI, self).__init__(engine,start_time,time_per_move, starter)
        self.evaluator = evaluator
        self.searcher = searcher

    def get_starting_state(self):
        return self.starter.start()

    def get_move(self):
        state = self.engine.get_state()
        valid_moves = self.engine.get_valid_moves()
        time = self.time_per_move
        evaluator = self.evaluator
        return self.searcher.search(state, valid_moves, time, evaluator)


