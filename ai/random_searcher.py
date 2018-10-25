from searcher import Searcher

class RandomSearcher(Searcher):
    def __init__(self, parameters):
        pass

    def search(self, state, valid_moves, time, evaluator):
      #return best move given the search with evaluator
        raise NotImplementedError