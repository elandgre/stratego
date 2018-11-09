from utils.search_utils import get_random_start

import random



class LS_start_state_trainer:
    def __init__(self, start = None):
        if start == None:
            start = get_random_start()

        self.n_games = 30
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

    def evaluate(self, last_start, next_start):
        wins = 0
        self.player_config[Settings.START_PARAMS.value] = next_start
        self.opponent_config[Settings.START_PARAMS.value] = last_start


        for i in range(self.n_games):
            self.engine.restart(self.player_config,self.opponent_config)
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

        next_start = last_start.copy()
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
                for j2 in range(j1 -1, j1 + 2):
                    if(i1 == i2 and j1 == j2): continue
                    s2 = 10 * i2 + j2
                    if(count == n):
                        if (not s2 < 0) and (not s2 >= len(last_start)):
                            valid = True

                    count+=1

        next_start = last_start.copy()
        temp = next_start[s1]
        next_start[s1] = next_start[s2]
        next_start[s2] = temp
        return next_start

    def simulated_annealing(self, factor):
        cur = start
        while True :





