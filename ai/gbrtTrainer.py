from skopt import Optimizer
from game.engine import Engine
from game.config import *
import matplotlib.pyplot as plt
import numpy as np
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
        self.score_history = []

    def objective(self,params):
        self.ai_config[Settings.AI_PARAMS.value] = params
        wins = 0
        for i in range(self.n_games):
            self.engine.restart(self.max_moves,self.ai_config,self.opponent_config)
            winner = self.engine.run()
            if winner == 1:
                wins += 1.0
            elif winner == 0:
                wins += 0.5
        print wins / self.n_games
        self.score_history.append(wins / self.n_games)
        return 1 - (wins / self.n_games)

        #res = 0
        #for i in range(self.n_games):
        #    self.engine.restart(self.max_moves,self.ai_config,self.opponent_config)
        #    self.engine.run()
        #    val = self.engine.get_value(1,100,-1,500)
        #    res += val
        #print res
        #self.score_history.append(res)
        #return -res


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
            self.engine.run()
            val = self.engine.get_value(1,100,-1,500)
            res += val
        print res
        return -res

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
        wins = 0.0
        for i in range(self.n_games):
            self.engine.restart(self.max_moves,self.ai_config,self.opponent_config)
            winner = self.engine.run()
            if winner == 1:
                wins += 1.0
            elif winner == 0:
                wins += 0.5
            print winner
        return wins / (self.n_games * 10)


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

    #opponent_config = {
    #            Settings.AI.value : True,
    #            Settings.START_TYPE.value : StartType.CHAMPION.value,
    #            Settings.START_PARAMS.value : [],
    #            Settings.SEARCH_TYPE.value : SearchType.NONE.value,
    #            Settings.SEARCH_PARAMS.value : [],
    #            Settings.AI_TYPE.value :  AIType.REACHABLE.value,
    #            Settings.AI_PARAMS.value : []
    #        }
    opponent_config = {
                Settings.AI.value : True, #should this be Ai or person
                Settings.START_TYPE.value : StartType.RANDOM.value, #what kind of start state
                Settings.START_PARAMS.value : [], #any parameters for the stater
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
                Settings.SEARCH_PARAMS.value : [], #any parameters for the search
                Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
                Settings.AI_PARAMS.value : [] #any params for the ai
            }


    param_ranges = [(-1,1) for i in range(101)]
    init_params = [1 for i in range(101)]
    n_batches = 2
    n_iter = 100
    n_games = 5

    trainer = GBRTTrainer(1000, ai_config, opponent_config, param_ranges, n_iter, n_games, init_params, n_batches)
    trainer.train()
    print(trainer.evaluate())
    return trainer

def run_and_plot():
    trainer = run_test()
    scores = np.array(trainer.score_history)
    x = np.linspace(0,len(trainer.score_history)-1,len(trainer.score_history))
    plt.plot(x,scores)
    plt.show()

if __name__ == '__main__':
    run_and_plot()


