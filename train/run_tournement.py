from ai.tournement import Tournement
from utils.constants import *

tourney = Tournement({
    AI_FIELD : {
      AIType.REACHABLE.value: ['train/good_reachable.txt'],
      AIType.MODIFIED_REACHABLE.value : ['train/good_modified_reachable.txt'],
      AIType.PIECE_BASED_ADD.value : ['train/good_piece_based_add.txt'],
      AIType.PIECE_BASED_MUL.value : ['train/good_piece_based_mul.txt']
    },
    START_FIELD : []
  }, 1000)


best_ai, _ = tourney.playoff(4)


print best_ai

