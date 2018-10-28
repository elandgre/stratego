from searcher import Searcher
import random


class RandomSearcher(Searcher):
    def __init__(self, parameters):
        super(RandomSearcher, self).__init__(parameters)

    def search(self, state, valid_moves, time, evaluator):
        #note this expects valid moves in a list format.
        num_moves = len(valid_moves)
        if num_moves == 0:
          return None,None
        ran_move = int(random.random() * num_moves)
        return valid_moves[ran_move]