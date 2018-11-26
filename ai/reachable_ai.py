from ai import AI
from utils.constants import *
import numpy as np
import random

class ReachableAI(AI):
    def __init__(self,engine,start_time,time_per_move,starter,params=None):
        super(ReachableAI, self).__init__(engine,start_time,time_per_move, starter)
        if params==None or len(params) < 101:
            self.parameters = np.ones(101)
        else:
            self.parameters = params

    def get_starting_state(self):
        return self.starter.start()

    def _get_param_index(self, param, piece=None):
        if(piece == None and ReachableParameters(param) == ReachableParameters.RANDOM_MOVE):
            return paramStart[param]
        elif(piece == None):
            return -1
        return paramStart[param] + piece_map[piece] - 1

    def get_random_move(self,valid_moves):
        num_moves = len(valid_moves)
        if num_moves == 0:
          return None,None
        ran_move = int(random.random() * num_moves)
        return valid_moves[ran_move]

    def get_move(self):
        state = self.engine.get_state()
        valid_moves = self.engine.get_valid_moves()
        time = self.time_per_move

        other_pieces = self.engine.get_oponents_peices()
        other_moved_peices = self.engine.get_oponents_moved_peices()
        revealed_peices = self.engine.get_oponents_revealed_peices()
        #appaently this does set minus in python
        other_unmoved_peices = other_pieces - other_moved_peices
        other_unknown_pieces = other_pieces - revealed_peices

        #initialize to a random move for simplicity
        max_val = self.parameters[self._get_param_index(ReachableParameters.RANDOM_MOVE.value)]
        max_move = self.get_random_move(valid_moves)
        for move in valid_moves:
            start, end = move
            piece = self.engine.get_peice_at(start)
            val = self.eval_move(move, piece, other_pieces, other_moved_peices, other_unmoved_peices, other_unknown_pieces)
            if(val > max_val):
                max_val = val
                max_move = move
        return max_move

    def eval_move(self, (start, end), piece, other_pieces, other_moved_pieces,other_unmoved_pieces, other_unkown_pieces):
        valuation = 0

        #intial
        if self.engine.is_first_move():
            valuation += self.parameters[self._get_param_index(ReachableParameters.INITIAL_MOVE.value, piece)]
        #attack unmoved
        if end in other_unmoved_pieces:
            valuation += self.parameters[self._get_param_index(ReachableParameters.ATTACKING_UNMOVED.value, piece)]
        #attack waeker
        if end in other_pieces:
            other_piece = self.engine.get_peice_at(end)
            if piece_map[other_piece] < piece_map[piece]:
                valuation += self.parameters[self._get_param_index(ReachableParameters.ATTACKING_WEAKER.value, piece)]
        (i1, j1) = start
        (i2, j2) = end
        # walk to otherside
        if i2 > i1 :
            valuation += self.parameters[self._get_param_index(ReachableParameters.MOVE_TO_OTHER_SIDE.value, piece)]
        # move to right
        if j2 > j1 :
            valuation += self.parameters[self._get_param_index(ReachableParameters.MOVE_TO_RIGHT.value, piece)]
        # move to own side
        if i2 < i1 :
            valuation += self.parameters[self._get_param_index(ReachableParameters.MOVE_TO_OWN_SIDE.value, piece)]
        # move to left
        if j2 < j1 :
            valuation += self.parameters[self._get_param_index(ReachableParameters.MOVE_TO_LEFT.value, piece)]
        #attack unknown moved
        if end in other_moved_pieces and end in other_unkown_pieces:
            valuation += self.parameters[self._get_param_index(ReachableParameters.ATTACK_UNKNOWN_MOVED.value, piece)]
        #move around lake
        lake_squares = {(4,1),(4,4),(4,5),(4,6),(5,1),(5,4),(5,5),(5,6)}
        # end and not start are next to lakes
        if end in lake_squares and not start in lake_squares:
            valuation += self.parameters[self._get_param_index(ReachableParameters.MOVE_AROUND_LAKE.value, piece)]
        # start and not end are next to lakes
        elif start in lake_squares and not end in lake_squares:
            valuation -= self.parameters[self._get_param_index(ReachableParameters.MOVE_AROUND_LAKE.value, piece)]
        #move along wall
        # | does set union
        outer_squares = {(0,j) for j in range(10)} | {(9,j) for j in range(10)}
        # end and not start in outer squares
        if end in outer_squares and not start in outer_squares:
            valuation += self.parameters[self._get_param_index(ReachableParameters.MOVE_ALONG_WALL.value, piece)]
        # start and not end in outer squares
        elif start in outer_squares and not end in outer_squares:
            valuation += self.parameters[self._get_param_index(ReachableParameters.MOVE_ALONG_WALL.value, piece)]
        return valuation








