from ai.tournement import Tournement
from utils.constants import *
import json

tourney = Tournement({
    AI_FIELD : {
      AIType.REACHABLE.value: [],#['train/good_reachable.txt'],
      AIType.MODIFIED_REACHABLE.value : [], #['train/good_modified_reachable.txt'],
      AIType.PIECE_BASED_ADD.value : [],#['train/good_piece_based_add.txt'],
      AIType.PIECE_BASED_MUL.value : ['train/good_piece_based_mul.txt']
    },
    START_FIELD : []#['train/simulated_annealing_results.txt']
  }, 1000)

for i in range(0, 1):

	best_ai, best_start = tourney.playoff(5)


	print best_ai
	#print best_start

	if best_start != []:
		f = open("train/tournament_best_starts.txt", "a")
		f.write("{}\n".format(json.dumps(best_start)))
		f.close()

	#if best_ai != []:
	#	g = open("train/tournament_best_ai.txt","a")
  #	g.write("{}\n".format(json.dumps(best_ai)))
	#	g.close()