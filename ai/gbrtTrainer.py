from skopt import Optimizer
from game.engine import Engine
from game.config import *

class GBRTTrainer(): #trains using Bayesian global optimization with GBRT against random play
    def __init__(self,ai_config,opponent_config,param_ranges,n_iter,n_games):
        self.ai_config = ai_config
        self.opponent_config = opponent_config
        self.param_ranges = param_ranges
        self.n_iter = n_iter
        self.n_games = n_games
        self.engine = Engine(self.ai_config, self.opponent_config)

    def objective(self,params):
        self.ai_config[Settings.AI_PARAMS.value] = params
        wins = 0
        for i in range(self.n_games):
            self.engine.restart(self.ai_config,self.opponent_config)
            res = self.engine.run()
            if res == 0:
                wins += 0.5
            else:
                wins += (res == 1)
        print(float(wins) / self.n_games)
        return float(wins) / self.n_games

    def train(self):
        opt = Optimizer(self.param_ranges,"GBRT")
        r = opt.run(self.objective,n_iter=self.n_iter)
        self.params = r.x
        #print("trained paramaters are: ")
        #print(r.x)

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
                Settings.START_TYPE.value : StartType.RANDOM.value,
                Settings.START_PARAMS.value : [],
                Settings.SEARCH_TYPE.value : SearchType.NONE.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value :  AIType.REACHABLE.value,
                Settings.AI_PARAMS.value : []
            }

    opponent_config = {
                Settings.AI.value : True,
                Settings.START_TYPE.value : StartType.RANDOM.value,
                Settings.START_PARAMS.value : [],
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value : AIType.NONE.value,
                Settings.AI_PARAMS.value : []
            }
    param_ranges = [(-1,1) for i in range(101)]
    n_iter = 500
    n_games = 5

    trainer = GBRTTrainer(ai_config, opponent_config, param_ranges, n_iter, n_games)
    trainer.train()
    print(trainer.evaluate())

if __name__ == '__main__':
    run_test()

