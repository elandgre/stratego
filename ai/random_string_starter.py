from starter import Starter
import numpy as np
from utils.constants import *

class RandomStrongStarter(Starter):
    def __init__(self,start_time):
        super(RandomStrongStarter, self).__init__(start_time)

    def start(self):
        i = np.random.randint(0, 4)
        start = good_start_states[i]
        return start

