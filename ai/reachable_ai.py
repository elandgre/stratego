from ai import AI


class ReachableParameters(Enum):
    INITIAL_MOVE = 'initial' # 0 - 9
    ATTACKING_UNMOVED = 'attack unmoved' # 10 -19
    ATTACKING_WEAKER = 'attacking weaker' #20-29
    WALK_TO_SIDE = 'walk to side of a peice? or other side of the board' #30 -39
    MOVE_TO_RIGHT = 'move the price to the right' # 40 - 49
    MOVE_TO_OWN_SIDE = 'move to our side of the board'# 50 - 59
    MOVE_TO_LEFT = 'move to the left' # 60 - 69
    ATTACK_UNKNOWN_MOVED = 'attack an unkown peice that has moved' # 70-79
    MOVE_AROUND_LAKE = 'move around the lake' # 80 - 89
    MOVE_ALONG_WALL = 'move along the outer walls of the board'# 90 - 99
    RANDOM_MOVE = 'make a random move' # 100 - 109

paramStart = {
    ReachableParameters.INITIAL_MOVE.value : 0,
    ReachableParameters.ATTACKING_UNMOVED.value : 10,
    ReachableParameters.ATTACKING_WEAKER.value : 20,
    ReachableParameters.WALK_TO_SIDE.value : 30,
    ReachableParameters.MOVE_TO_RIGHT.value : 40,
    ReachableParameters.MOVE_TO_OWN_SIDE.value: 50,
    ReachableParameters.MOVE_TO_LEFT.value : 60,
    ReachableParameters.ATTACK_UNKNOWN_MOVED.value: 70,
    ReachableParameters.MOVE_AROUND_LAKE.value : 80,
    ReachableParameters.MOVE_ALONG_WALL : 90,
    ReachableParameters.RANDOM_MOVE : 100
}

def get_param_index(param, peice):
    return paramStart[param] + piece_map[peice] - 1

class ReachableAI(AI):
    def __init__(self,engine,start_time,time_per_move,starter,params):
        super(BasicAI, self).__init__(engine,start_time,time_per_move, starter)
        self.parameters = params

    def get_starting_state(self):
        return self.starter.start()

    def get_move(self):
        state = self.engine.get_state()
        valid_moves = self.engine.get_valid_moves()
        time = self.time_per_move

        other_pieces = self.engine.get_oponents_peices()
        other_moved_peices = self.engine.get_oponents_moved_peices()
        #appaently this does set minus in python
        other_unmoved_peices = other_pieces - other_moved_peices


        max_val = 0
        max_move = (None, None)
        for move in valid_moves:
            start, end = move
            piece = self.engine.get_peice_at(start)
            val = append(eval_move(move, piece, other_pieces, other_moved_peices, other_unmoved_peices))
            if(val > max_val):
                max_val = val
                max_move = move
        return max_move

    def eval_move(self, (start, end), piece, other_pieces, other_moved_peices,other_unmoved_peices):
        valuation = 0
        #intial
        if self.engine.is_first_move():
            valuation += parameters[get_param_index(ReachableParameters.INITIAL_MOVE.value, piece)]
        #attack unmoved
        if end in other_unmoved_peices:
            valuation += parameters[get_param_index(ReachableParameters.ATTACKING_UNMOVED.value, piece)]
        #attack waeker
        if end in other_pieces:
            other_peice = elf.engine.get_peice_at(end)
            if piece_map[other_piece] < piece_map[piece]:
                valuation += parameters[get_param_index(ReachableParameters.ATTACKING_WEAKER.value, piece)]
        #TODO: walk to otherside
        #TODO: move to right
        #TODO: move to own side
        #TODO: move to left
        #TODO: attack unknown moved
        #TODO: move around lake
        #TODO: move along wall
        #TODO: random









