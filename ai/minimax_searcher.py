class MinimaxSearcher(searcher):
	def __init__(self, parameters):
		super(RandomSearcher, self).__init__(parameters)
		
	def search(self, state, valid_moves, time, evaluator):
		