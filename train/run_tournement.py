from ai.tournement import Tournement
from utils.constants import *

tourney = Tournement({
    AI_FIELD : {
      AIType.REACHABLE.value: ['good_reachable.txt'],
      AIType.MODIFIED_REACHABLE.value : ['good_modified_reachable.txt'],
      AIType.PIECE_BASED.value : []
    },
    START_FIELD : []
  }, 1000)


best_ai, _ = tourney.playoff()


print best_ai

