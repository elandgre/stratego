from skopt import Optimizer
from game.engine import Engine
from game.config import *

class GBRTTrainer(): #trains using Bayesian global optimization with GBRT against random play
    def __init__(self,max_moves,ai_config,opponent_config,param_ranges,n_iter,n_games,init_params,n_batches = 1):
        self.ai_config = ai_config
        self.opponent_config = opponent_config
        self.param_ranges = param_ranges
        self.n_iter = n_iter
        self.n_games = n_games
        self.max_moves = max_moves
        self.engine = Engine(self.max_moves,self.ai_config, self.opponent_config)
        self.params = init_params
        self.n_batches = n_batches

    def objective(self,params):
        self.ai_config[Settings.AI_PARAMS.value] = params
        wins = 0
        for i in range(self.n_games):
            self.engine.restart(self.max_moves,self.ai_config,self.opponent_config)
            res = self.engine.run()
            if res == 0:
                wins += 0.5
            else:
                wins += (res == 1)
        print(float(self.n_games - wins) / self.n_games)
        return float(self.n_games - wins) / self.n_games


    def train(self):
        opt = Optimizer(self.param_ranges,"GP")
        r = opt.run(self.objective,n_iter=self.n_iter)
        self.params = r.x
        #print("trained paramaters are: ")
        #print(r.x)

    def objective_batchwise(self,params):
        full_params = self.params[:self.training_param_range[0]] + params + self.params[self.training_param_range[1]:]
        self.ai_config[Settings.AI_PARAMS.value] = full_params
        wins = 0
        for i in range(self.n_games):
            self.engine.restart(self.max_moves,self.ai_config,self.opponent_config)
            res = self.engine.run()
            if res == 0:
                wins += 0.5
            else:
                wins += (res == 1)
        print(float(self.n_games - wins) / self.n_games)
        return float(self.n_games - wins) / self.n_games

    def train_batchwise(self):
        opt = Optimizer(self.param_ranges,"GP")
        for batch in range(self.n_batches):
            print("starting a batch")
            for start in range(10):
                print("starting a round of optimization")
                self.training_param_range = [start*10, start*10 + 10]
                opt = Optimizer(self.param_ranges[start*10:start*10 + 10],"GP")
                r = opt.run(self.objective,n_iter=self.n_iter)
                self.params[start*10:start*10 + 10] = r.x

    def evaluate(self):
        res = 0
        for i in range(10):
            res += self.objective(self.params)
        return res/10


#############################################
# don't keep this code in for the long term #
#############################################
def run_test():
    ai_config = {
                Settings.AI.value : True,
                Settings.START_TYPE.value : StartType.CHAMPION.value,
                Settings.START_PARAMS.value : [],
                Settings.SEARCH_TYPE.value : SearchType.NONE.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value :  AIType.REACHABLE.value,
                Settings.AI_PARAMS.value : []
            }

    opponent_config = {
                Settings.AI.value : True,
                Settings.START_TYPE.value : StartType.CHAMPION.value,
                Settings.START_PARAMS.value : [],
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value : AIType.NONE.value,
                Settings.AI_PARAMS.value : []
            }

    param_ranges = [(-1,1) for i in range(101)]
    init_params = [1 for i in range(101)]
    n_batches = 5
    n_iter = 10
    n_games = 5

    trainer = GBRTTrainer(1000, ai_config, opponent_config, param_ranges, n_iter, n_games, init_params,n_batches)
    trainer.train_batchwise()
    print(trainer.evaluate())

if __name__ == '__main__':
    run_test()

