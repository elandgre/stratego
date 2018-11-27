from utils.search_utils import get_random_start
from utils.constants import *
from game.engine import Engine
import random

import numpy as np
import copy

class LSStartStateTrainer:
    def __init__(self, start = None, n_games = 10, start_temp = 1024, factor = 2):
        self.start = start
        if start == None:
            self.start = get_random_start()


        self.delta = 0.00001
        self.n_games = n_games
        #make both of them random, but the simpel start state
        self.player_config = {
                Settings.AI.value : True, #should this be Ai or person
                Settings.START_TYPE.value : StartType.SIMPLE.value, #what kind of start state
                Settings.START_PARAMS.value : [], #any parameters for the stater
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
                Settings.SEARCH_PARAMS.value : [], #any parameters for the search
                Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
                Settings.AI_PARAMS.value : [] #any params for the ai
            }
        self.opponent_config = {
                Settings.AI.value : True, #should this be Ai or person
                Settings.START_TYPE.value : StartType.SIMPLE.value, #what kind of start state
                Settings.START_PARAMS.value : [], #any parameters for the stater
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
                Settings.SEARCH_PARAMS.value : [], #any parameters for the search
                Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
                Settings.AI_PARAMS.value : [] #any params for the ai
            }

        self.engine = Engine(1000)

        self.best = self.simulated_annealing(start_temp, factor)

        print(self.best)

    def evaluate(self, last_start, next_start):
        wins = 0
        self.player_config[Settings.START_PARAMS.value] = next_start
        self.opponent_config[Settings.START_PARAMS.value] = last_start


        for i in range(self.n_games):
            self.engine.restart(1000, self.player_config,self.opponent_config)
            res = self.engine.run()
            if res == 0:
                wins += 0.5
            else:
                wins += (res == 1)

        print(float(self.n_games - wins) / self.n_games)
        return float(self.n_games - wins) / self.n_games

    def get_random_next(self, last_start):
        i = int(random.random() * len(last_start))
        j = i
        while j == i :
            j = random.random() * len(last_start)

        next_start = copy.copy(last_start)
        temp = next_start[i]
        next_start[i] = next_start[j]
        next_start[j] = temp
        return next_start

    def get_similar_random_next(self, last_start):
        #want to swap two neighboring pieces
        s1 = int(random.random() * len(last_start))
        i1,j1 = s1 / 10, s1 %10
        s2 = s1

        valid = False
        while (not valid):
            n = int(random.random() * 8)
            count = 0
            for i2 in range(i1 -1, i1 +2):
                if valid : break
                for j2 in range(j1 -1, j1 + 2):
                    if valid : break
                    if(i1 == i2 and j1 == j2): continue
                    s2 = 10 * i2 + j2
                    if(count == n):
                        if (not s2 < 0) and (not s2 >= len(last_start)):
                            #print(s2)
                            valid = True

                    count+=1

        next_start = copy.copy(last_start)

        #print("s1 : {}".format(s1))
        #print("s2 : {}".format(s2))

        temp = next_start[s1]
        next_start[s1] = next_start[s2]
        next_start[s2] = temp
        return next_start

    def simulated_annealing(self, start_temp, factor):
        cur = self.start
        temp = start_temp
        while True :
            if temp <= self.delta : return cur
            next_start = self.get_similar_random_next(cur)
            e = self.evaluate(cur, next_start)
            if (e > 0.5) :
                cur = next_start
            else :
                should_use_anyways = random.random()
                p = np.exp( (e - 0.5) / temp)
                if(should_use_anyways < p):
                    cur = next_start
            temp = temp / factor






