from ai import AI
from utils.constants import *
import numpy as np
import random


class PieceBasedAI(AI):
    def __init__(self,engine,start_time,time_per_move,starter,params=None, op=None):
        super(PieceBasedAI, self).__init__(engine,start_time,time_per_move, starter)
        self.op = op
        if self.op == None:
            self.op = PieceBasedOp.ADD.value

        if params==None or len(params) < 21:
            self.parameters = np.ones(21)
        else:
            self.parameters = params

    def get_starting_state(self):
        return self.starter.start()

    def _get_param_index(self, param, piece=None):
        if(PieceBasedParameters.PIECE_VALUE.value == param):
            return piece
        else :
            return modifiedParamStart[param]

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

        #forward
        if i2 > i1 :
            valuation += self.parameters[self._get_param_index(PieceBasedParameters.MOVE_FORWARD.value)]
        #right
        if j2 > j1 :
            valuation += self.parameters[self._get_param_index(PieceBasedParameters.MOVE_TO_RIGHT.value)]

        #backward
        if i2 < i1 :
            valuation += self.parameters[self._get_param_index(PieceBasedParameters.MOVE_BACKWARD.value)]
        #left
        if j2 < j1 :
            valuation += self.parameters[self._get_param_index(PieceBasedParameters.MOVE_TO_LEFT.value)]
        #attack
        if end in other_pieces:
            valuation += self.parameters[self._get_param_index(PieceBasedParameters.ATTACKING.value)]
        (i1, j1) = start
        (i2, j2) = end

        #piece
        piece_val = self.parameters[self._get_param_index(PieceBasedParameters.PIECE_VALUE.value, piece)]

        valuation = self.combine(piece_val, valuation)

        return valuation



    def combine(self, piece_val, val):
        if self.op == PieceBasedOp.ADD.value:
            return piece_val + val
        elif self.op == PieceBasedOp.MUL.value:
            return piece_val * val
        else:
            return val
