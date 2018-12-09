from ai.ls_startstate_trainer import LSStartStateTrainer
from utils.constants import *
from utils.search_utils import get_random_start
import numpy as np

def train():
    start = good_start_states[0]
    LSStartStateTrainer(start, 20, 131072, 2)

def randomTrain():
	i = np.random.randint(0, len(good_start_states)-1)
	start = good_start_states[i]
	start_temp = np.random.randint(2**10, 2**40)
	factor = np.random.randint(2, 10)
	LSStartStateTrainer(start, 20, start_temp, factor)

def start_w_random():
	LSStartStateTrainer(get_random_start(), 20, 1099511627776, 2)

if __name__ == "__main__":
	for i in range(0, 15):
		start_w_random()



#[2, 4, 12, 8, 3, 5, 11, 6, 12, 3, 3, 12, 4, 7, 2, 7, 12, 7, 3, 5, 4, 2, 12, 1, 9, 2, 5, 2, 12, 4, 6, 2, 2, 5, 2, 6, 3, 8, 10, 6]
#[4, 5, 2, 3, 2, 5, 11, 12, 7, 5, 4, 12, 3, 12, 8, 12, 5, 7, 6, 2, 2, 2, 9, 1, 7, 6, 3, 3, 8, 3, 2, 4, 12, 4, 2, 10, 2, 6, 12, 6]
#[2, 4, 12, 2, 3, 12, 11, 12, 3, 3, 4, 12, 3, 1, 8, 5, 7, 7, 5, 4, 5, 4, 12, 12, 9, 2, 3, 6, 2, 6, 6, 2, 2, 5, 7, 2, 6, 10, 8, 2]
#[2, 3, 12, 3, 5, 8, 11, 3, 3, 4, 5, 12, 4, 9, 7, 2, 12, 6, 12, 4, 2, 4, 12, 2, 12, 3, 7, 2, 8, 7, 6, 2, 1, 5, 2, 6, 2, 10, 5, 6]