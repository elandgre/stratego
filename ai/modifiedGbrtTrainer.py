
from utils.constants import *
import matplotlib.pyplot as plt
import numpy as np
from gbrtTrainer import GBRTTrainer

#############################################
# don't keep this code in for the long term #
#############################################
def run_training(ai_config, opponent_config, n_params):

    param_ranges = [(-1, 1) for i in range(n_params)]
    init_params = [1 for i in range(n_params)]
    n_batches = 2
    n_iter = 200
    n_games = 5

    trainer = GBRTTrainer(1000, ai_config, opponent_config, param_ranges, n_iter, n_games, init_params, n_batches)
    trainer.train()
    print(trainer.evaluate())
    return trainer

def run_and_plot(ai_config, opponent_config, filename, n_params):
    trainer = run_training(ai_config, opponent_config, n_params)
    good_param_file = open(filename, "a")
    for param in trainer.the_good_ones:
        print(param)
        good_param_file.write("{}\n".format(param))
    good_param_file.close()
    #scores = np.array(trainer.score_history)
    #x = np.linspace(0,len(trainer.score_history)-1,len(trainer.score_history))
    #plt.plot(x,scores)
    #plt.show()



