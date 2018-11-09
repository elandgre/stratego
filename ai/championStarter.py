from game.config import *
from starter import Starter
from utils.constants import *

class ChampionStarter(Starter):
    def __init__(self,start_time):
        self.start_time = start_time

    def start(self):
        return good_start_states[0]
        