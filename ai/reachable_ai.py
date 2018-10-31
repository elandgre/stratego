from ai import AI
from game.config import *
from utils.constants import *


class ReachableAI(AI):
    def __init__(self,engine,start_time,time_per_move,starter,params):
        super(ReachableAI, self).__init__(engine,start_time,time_per_move, starter)
        self.parameters = params

    def get_starting_state(self):
        return self.starter.start()

    def _get_param_index(self, param, peice):
        return paramStart[param] + piece_map[peice] - 1

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
        max_val = self.parameters[ReachableParameters.RANDOM_MOVE]
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
        #TODO: move around lake
        #TODO: move along wall










