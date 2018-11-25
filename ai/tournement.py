#config format:
# {
#   'ai': {
#       'reachable': {
#           'filenames': []
#       },
#       'modified_reachable': {
#           'filenames': []
#        },
#       'peice_based': {
#           'filenames': []
#        }
#   },
#   'start':[]
# }

#files should contain lines of parameter values

from utils.constants import *
import random
import json

#seed random with a roughly random number
random.seed(149893425)

class Tournement:
    def __init__(self, config, max_moves):
        self.ai_configs = []
        for filename in config[AI][AIType.REACHABLE.value]:
            self.ai_configs += read_file_into_configs(filename, reachable_config)
        for filename in config[AI][AIType.MODIFIED_REACHABLE.value]:
            self.ai_configs += read_file_into_configs(filename, mod_reachable_config)
        for params in config[AI][AIType.PIECE_BASED.value]:
            #TODO
            pass


        self.start_configs = []

        for filename in config[START]:
            self.start_configs += read_file_into_configs(filename, flexible_start_config)


        self.engine = Engine(max_moves,None, None)

        self.max_moves = max_moves


    def playoff(param_lst, num):
        this_round = param_lst
        next_round = []

        while len(this_round) > num:
            for i in range(int(len(this_round)/2)):
                config1 = param_lst[i]
                config2 = param_lst[i+1]

                # do a playoff and the winner goes to the next round
                self.engine.restart(self.max_moves,config1,config2)
                winner = self.engine.run()
                if winner == 1:
                    next_round.append(config1)
                elif winner == 2:
                    next_round.append(config2)
                else:
                    #in the event of a tie, play again with twice the number of
                    #moves to try to determine the winner
                    self.engine.restart(2 * self.max_moves,config1,config2)
                    winner = self.engine.run()
                    if winner == 1:
                        next_round.append(config1)
                    elif winner == 2:
                        next_round.append(config2)
                    else:
                        #double tie indicates the configs are about the same
                        #so its safe to just randomly pick one to move on to
                        #the next round
                        if random.random() < 0.5:
                            next_round.append(config1)
                        else:
                            next_round.append(config2)
            if(len(this_round) % 2 != 0):
                next_round.append(this_round[-1])

            this_round = next_round
            next_round = []

        return this_round


    def playoff():
        best_ai = playoff(self.ai_configs)
        best_start = playoff(self.start_configs)
        return best_ai, best_start





