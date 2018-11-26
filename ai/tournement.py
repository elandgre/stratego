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
from game.engine import Engine
#seed random with a roughly random number
random.seed(149893425)

class Tournement:
    def __init__(self, config, max_moves):
        self.ai_configs = []
        for filename in config[AI_FIELD][AIType.REACHABLE.value]:
            self.ai_configs += read_file_into_configs(filename, reachable_config)
        for filename in config[AI_FIELD][AIType.MODIFIED_REACHABLE.value]:
            self.ai_configs += read_file_into_configs(filename, mod_reachable_config)
        for params in config[AI_FIELD][AIType.PIECE_BASED_ADD.value]:
            self.ai_configs += read_file_into_configs(filename, piecebased_config_add)
        for params in config[AI_FIELD][AIType.PIECE_BASED_MUL.value]:
            self.ai_configs += read_file_into_configs(filename, piecebased_config_mul)


        self.start_configs = []

        for filename in config[START_FIELD]:
            self.start_configs += read_file_into_configs(filename, flexible_start_config)


        self.engine = Engine(max_moves,None, None)

        self.max_moves = max_moves


    def play_against(self, config1, config2, n_games=5):
        player1_wins = 0
        player2_wins = 0
        for i in range(n_games):
            self.engine.restart(self.max_moves,config1,config2)
            winner = self.engine.run()
            if winner == 1 :
                player1_wins +=1
            elif winner == 2:
                player2_wins += 1

        if player1_wins > player2_wins :
            return 1
        elif player1_wins < player2_wins:
            return 2
        else :
            return 0


    def playoff_helper(self, param_lst, num):
        this_round = param_lst
        next_round = []

        i = 1
        while len(this_round) > num:
            print("round {}, {} configurations left".format(i, len(this_round)))
            i+=1
            random.shuffle(this_round)
            for i in range(int(len(this_round)/2)):
                config1 = param_lst[i]
                config2 = param_lst[i+1]

                # do a playoff and the winner goes to the next round
                winner = self.play_against(config1, config2)
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


    def playoff(self, num=1):
        print('finding the best ai configurations')
        best_ai = self.playoff_helper(self.ai_configs, num)
        print('finding the best start state')
        best_start = self.playoff_helper(self.start_configs, num)
        return best_ai, best_start

#observations from training
#full reachable takes a long time to find states that result in winning all 10 of the games
#modified reachable finds such states faster but those states often loose to the
#full reachable ones, it seems because the parameter state space is so much larger
#for the full reachable its harder for the optimizer to optimize, but these lead to
#better solutions

#when we attempted training the ais against another reachable AI with all the
#parameters set to 1 the optimizer had a hard time finding solutions that would win
#significantly, this seemed to cause the optimizer to essentially find AIs that
#just avoided loosing, which meant that the ais learned to run out the clock
#so that the game would be called a tie after the max number of iterations
#even using different evaluation functions to encourage winning more
#few AIs we found that could win more than 0.6 or 0.7 percent of the time


#in order to preserve the properies of the reachable ai but decrease the
#parameter space I created an AI called piece based which has a parameter
#value for each piece and a parameter value of different types of moves
#with the result that the sum of the parameters for the type of moves was either
#added to or multiplied by the piece parameter value.

#multiplying found strong solutions faster than reachable, and additive slower
#than reachable, but in the tournement style evaluations of all the types of
#paramters both additive and multiplicative piece based beat out the reachable
#solutions

#the best AI found currently:
#{'ai parameters': [1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1, -1, 1, 0, -1, 0, 0, 1, 1, -1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, 0, -1, 0, 0, -1, 1, 1, -1, -1, 0, -1, -1, 0, 1, 0, 0, 0, -1, 1, -1, -1, 1, -1, -1, 0, -1, 0, 0, -1, -1, 0, 0, 0, 0, 1, 0, 1, 0, -1, -1, -1, -1, 0, -1, -1, 1, -1, 1, -1, 0, 1, -1, -1, 0, 0, -1, -1, 0, 0, 0, 1, -1, 0, 1, 0], 'eval_type': 'reachable', 'search_parmeters': [], 'FILENAME': 'good_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}

#better:
#[{'ai parameters': [0, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 0, 1, 0, 1, -1], 'eval_type': 'piece_based_mull', 'search_parmeters': [], 'FILENAME': 'train/good_modified_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'},
#{'ai parameters': [0, -1, 1, 1, 0, 0, -1, 1, 0, 0, 1, -1, 0, 1, 0, 0, 0, 0, -1, 0, 0], 'eval_type': 'piece_based_add', 'search_parmeters': [], 'FILENAME': 'train/good_modified_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'},
#{'ai parameters': [-1, 1, 1, 1, 1, 0, -1, 1, -1, 0, 1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0], 'eval_type': 'piece_based_mull', 'search_parmeters': [], 'FILENAME': 'train/good_modified_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}]



