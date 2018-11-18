
class MonteCarloSearcher(Searcher):
	def __init__(self, parameters):
        self.num_playouts = parameters['num_playouts']
        self.max_depth = paramters['max_depth']


def search(self, state, valid_moves, time, evaluator):
        #note this expects valid moves in a list format.
        self.searcher_helper()
        player1_turn = self.engine.is_player1_turn()

        num_moves = len(valid_moves)


        if num_moves == 0:
          return None,None

def search_helper(self, board, engine, num_playouts, max_depth, current_player, is_player1):
