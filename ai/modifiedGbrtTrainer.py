
from utils.constants import *
import matplotlib.pyplot as plt
import numpy as np
from gbrtTrainer import GBRTTrainer

#############################################
# don't keep this code in for the long term #
#############################################
def run_training(ai_config, opponent_config):



    param_ranges = [(-1,1) for i in range(21)]
    init_params = [1 for i in range(21)]
    n_batches = 2
    n_iter = 100
    n_games = 5

    trainer = GBRTTrainer(1000, ai_config, opponent_config, param_ranges, n_iter, n_games, init_params, n_batches)
    trainer.train()
    print(trainer.evaluate())
    return trainer

def run_and_plot():
    trainer = run_test()
    good_param_file = open("good_modified_reachable.txt", "a")
    for param in trainer.the_good_ones:
        print(param)
        good_param_file.write("{}\n".format(param))
    good_param_file.close()
    #scores = np.array(trainer.score_history)
    #x = np.linspace(0,len(trainer.score_history)-1,len(trainer.score_history))
    #plt.plot(x,scores)
    #plt.show()


if __name__ == '__main__':
    run_and_plot()


