from game.config import *
from starter import Starter

class ChampionStarter(Starter):
    def __init__(self,start_time):
        self.start_time = start_time

    def start(self):
        return [2,3,12,2,3,12,11,12,3,3,4,12,4,7,8,5,12,5,6,4,5,4,12,1,9,2,7,7,8,2,6,2,2,5,2,6,3,10,2,6]
        