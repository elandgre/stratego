from starter import Starter
from utils.constants import *
from utils.search_utils import get_random_start
import random

class RandomStarter(Starter):
    def __init__(self,start_time):
        super(RandomStarter, self).__init__(start_time)

    def start(self):
        return get_random_start()

