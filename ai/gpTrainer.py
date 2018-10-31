from skopt import Optimizer
class GBRTTrainer(): #trains using Bayesian global optimization with GPs against random play
	def __init__(self,training_ai,param_ranges,n_iter,n_games):
        self.training_ai = training_ai
		self.starting_params = starting_params
        self.param_ranges = param_ranges
        self.n_iter = n_iter
        self.n_games = n_games


    def objective(params):
        wins = 0
        #for i in range(self.n_games)
        #    wins += (self.engine.run() == 1)
        #return wins / self.n_games

	def train():
		opt = Optimizer(self.param_ranges,"GBRT")
		r = opt.run(self.objective,n_iter=self.n_iter)
		self.params = r.x
		print("trained paramaters are: ")
		print(r.x)

    def evaluate(params):
	   return self.objective(params)

