from starter import Starter
from utils.constants import *
import random

class RandomStarter(Starter):
  def __init__(self,start_time):
    super(RandomStarter, self).__init__(start_time)

  def start(self):
    placements = []

    for piece in starting_piece_counts:
      for piece_count in range(starting_piece_counts[piece]):
        placements.append(piece_map[piece])

    random.shuffle(placements)
    print(placements)
    return placements

