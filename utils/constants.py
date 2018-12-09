from enum import Enum
import json


FRONTEND = False

class Settings(Enum):
    AI = 'is an ai'
    START_TYPE = 'type_of_start_state'
    START_PARAMS = 'params_for_start_state'
    SEARCH_TYPE = 'type_of_search'
    SEARCH_PARAMS = 'search_parmeters'
    AI_TYPE = 'eval_type'
    AI_PARAMS = 'ai parameters'


class StartType(Enum):
    RANDOM = 'random'
    BETTER = 'better'
    CHAMPION = 'champion'
    SIMPLE = 'simple'
    RANDOM_STRONG = 'random_strong'
    LS = 'ls'

class SearchType(Enum):
    NONE = 'no searcher'
    GREEDY = 'gready search'
    RANDOM = 'random'
    FULL = 'full_tree_search'
    STOCASTIC = 'stocatic_search'

class BasicSearchParams(Enum):
    SERACH_DEPTH = 'number of levels to expore'

class AIType(Enum):
    NONE = 'none'
    INVINCLBLE = 'invincible'
    REACHABLE = 'reachable'
    MODIFIED_REACHABLE = 'modified_reachable'
    PIECE_BASED_ADD = 'piece_based_add'
    PIECE_BASED_MUL = 'piece_based_mull'
    MC_PLAYOFF = 'monte_carlo_playoff_eval'
    MC_HUER = 'monte_carlo_huristic_eval'


class ReachableParameters(Enum):
    INITIAL_MOVE = 'initial' # 0 - 9
    ATTACKING_UNMOVED = 'attack unmoved' # 10 -19
    ATTACKING_WEAKER = 'attacking weaker' #20-29
    MOVE_TO_OTHER_SIDE = 'other side of the board' #30 -39
    MOVE_TO_RIGHT = 'move the price to the right' # 40 - 49
    MOVE_TO_OWN_SIDE = 'move to our side of the board'# 50 - 59
    MOVE_TO_LEFT = 'move to the left' # 60 - 69
    ATTACK_UNKNOWN_MOVED = 'attack an unkown peice that has moved' # 70-79
    MOVE_AROUND_LAKE = 'move around the lake' # 80 - 89
    MOVE_ALONG_WALL = 'move along the outer walls of the board'# 90 - 99
    RANDOM_MOVE = 'make a random move' # 100

paramStart = {
    ReachableParameters.INITIAL_MOVE.value : 0,
    ReachableParameters.ATTACKING_UNMOVED.value : 10,
    ReachableParameters.ATTACKING_WEAKER.value : 20,
    ReachableParameters.MOVE_TO_OTHER_SIDE.value : 30,
    ReachableParameters.MOVE_TO_RIGHT.value : 40,
    ReachableParameters.MOVE_TO_OWN_SIDE.value: 50,
    ReachableParameters.MOVE_TO_LEFT.value : 60,
    ReachableParameters.ATTACK_UNKNOWN_MOVED.value: 70,
    ReachableParameters.MOVE_AROUND_LAKE.value : 80,
    ReachableParameters.MOVE_ALONG_WALL.value : 90,
    ReachableParameters.RANDOM_MOVE.value : 100
}

modifiedParamStart = {
    ReachableParameters.INITIAL_MOVE.value : 0,
    ReachableParameters.ATTACKING_UNMOVED.value : 2,
    ReachableParameters.ATTACKING_WEAKER.value : 4,
    ReachableParameters.MOVE_TO_OTHER_SIDE.value : 6,
    ReachableParameters.MOVE_TO_RIGHT.value : 8,
    ReachableParameters.MOVE_TO_OWN_SIDE.value: 10,
    ReachableParameters.MOVE_TO_LEFT.value : 12,
    ReachableParameters.ATTACK_UNKNOWN_MOVED.value: 14,
    ReachableParameters.MOVE_AROUND_LAKE.value : 16,
    ReachableParameters.MOVE_ALONG_WALL.value : 18,
    ReachableParameters.RANDOM_MOVE.value : 20
}



class PieceBasedParameters(Enum):
    PIECE_VALUE = 'initial' # 0 - 9
    MOVE_FORWARD = 'other side of the board' #10
    MOVE_TO_RIGHT = 'move the price to the right' #11
    MOVE_BACKWARD = 'move to our side of the board'#12
    MOVE_TO_LEFT = 'move to the left' #13
    ATTACKING = 'attacking' #14
    RANDOM_MOVE = 'make a random move' #15
    OP = 'op'
    PARAMS = 'params'

class PieceBasedOp(Enum):
    ADD = 'add'
    MUL = 'mul'

pieceBasedParamStart = {
    PieceBasedParameters.PIECE_VALUE.value : 0,
    PieceBasedParameters.MOVE_FORWARD.value : 10,
    PieceBasedParameters.MOVE_TO_RIGHT.value : 11,
    PieceBasedParameters.MOVE_BACKWARD.value : 12,
    PieceBasedParameters.MOVE_TO_LEFT.value : 13,
    PieceBasedParameters.ATTACKING.value: 14,
    PieceBasedParameters.RANDOM_MOVE.value : 15,
}

FILENAME_FIELD = 'FILENAME'
AI_FIELD = 'ai'
START_FIELD = 'start'

MS_BETWEEN_MOVES = 1000



class pieces(Enum):
    EMPTY = 'empty'
    SPY = 'spy'
    SCOUT = 'scout'
    MINER = 'miner'
    SERGEANT = 'sergeant'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    MAJOR = 'major'
    COLONEL = 'colonel'
    GENERAL = 'general'
    MARSHAL = 'marshal'
    FLAG = 'flag'
    BOMB = 'bomb'
    MOUNTAIN = 'mountain'
    HIDDEN = 'hidden'


piece_names = [
    pieces.EMPTY.value,
    pieces.SPY.value,
    pieces.SCOUT.value,
    pieces.MINER.value,
    pieces.SERGEANT.value,
    pieces.LIEUTENANT.value,
    pieces.CAPTAIN.value,
    pieces.MAJOR.value,
    pieces.COLONEL.value,
    pieces.GENERAL.value,
    pieces.MARSHAL.value,
    pieces.FLAG.value,
    pieces.BOMB.value,
    pieces.MOUNTAIN.value
]


starting_piece_counts = {
    pieces.SPY.value: 1,
    pieces.SCOUT.value: 8,
    pieces.MINER.value: 5,
    pieces.SERGEANT.value: 4,
    pieces.LIEUTENANT.value: 4,
    pieces.CAPTAIN.value: 4,
    pieces.MAJOR.value: 3,
    pieces.COLONEL.value: 2,
    pieces.GENERAL.value: 1,
    pieces.MARSHAL.value: 1,
    pieces.FLAG.value: 1,
    pieces.BOMB.value: 6
}


mobile_pieces = set([
    pieces.SPY.value,
    pieces.SCOUT.value,
    pieces.MINER.value,
    pieces.SERGEANT.value,
    pieces.LIEUTENANT.value,
    pieces.CAPTAIN.value,
    pieces.MAJOR.value,
    pieces.COLONEL.value,
    pieces.GENERAL.value,
    pieces.MARSHAL.value])

starting_pieces_per_player = 40

piece_map = {piece_names[i]:i for i in range(len(piece_names))}


piece_diplay_map = {piece_names[i]:i for i in range(len(piece_names))}
piece_diplay_map[pieces.HIDDEN.value] = 999
piece_diplay_map[pieces.MOUNTAIN.value] = 111

aggressive_strong_start = [7, 3, 3, 3, 4, 12, 11, 12, 12, 3, 7, 2, 7, 1, 6, 5, 12, 4, 5, 2, 4, 2, 8, 8, 9, 2, 4, 12, 12, 5, 10, 6, 5, 3, 2, 6, 2, 2, 2, 6]

decent_start = [3, 12, 4, 12, 4, 2, 3, 3, 12, 11, 4, 8, 1, 3, 12, 2, 6, 5, 5, 12, 5, 2, 7, 5, 12, 2, 7, 7, 8, 3, 6, 2, 4, 9, 6, 2, 2, 10, 2, 6]

good_start = [3, 2, 3, 3, 4, 12, 11, 12, 3, 2, 6, 4, 7, 1, 7, 5, 12, 4, 12, 4, 10, 2, 7, 8, 2, 6, 12, 5, 12, 5, 2, 8, 5, 2, 6, 2, 9, 3, 2, 6]

defensive_start = [4, 2, 3, 12, 4, 3, 3, 12, 11, 12, 12, 6, 1, 7, 5, 2, 6, 5, 12, 4, 3, 2, 8, 7, 12, 5, 10, 7, 5, 8, 9, 6, 2, 4, 2, 2, 2, 3, 6, 2]

weak_start = [3, 12, 4, 2, 3, 12, 3, 3, 12, 11, 5, 4, 12, 2, 7, 3, 5, 6, 5, 12, 7, 2, 12, 1, 8, 4, 2, 7, 8, 4, 2, 6, 5, 9, 2, 6, 2, 10, 6, 2]

champion_start = [2,3,12,2,3,12,11,12,3,3,4,12,4,7,8,5,12,5,6,4,5,4,12,1,9,2,7,7,8,2,6,2,2,5,2,6,3,10,2,6]

in_order_start = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]

good_start_states = [
    champion_start,
    aggressive_strong_start,
    decent_start,
    good_start,
    defensive_start]

general_start_states = [
        in_order_start,
        weak_start]

def random_config():
    return {
        Settings.AI.value : True, #should this be Ai or person
        Settings.START_TYPE.value : StartType.CHAMPION.value, #what kind of start state
        Settings.START_PARAMS.value : [], #any parameters for the stater
        Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
        Settings.SEARCH_PARAMS.value : [], #any parameters for the search
        Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
        Settings.AI_PARAMS.value : [] #any params for the ai
    }

def reachable_config(params):
    return {
        Settings.AI.value : True,
        Settings.START_TYPE.value : StartType.CHAMPION.value,
        Settings.START_PARAMS.value : [],
        Settings.SEARCH_TYPE.value : SearchType.NONE.value,
        Settings.SEARCH_PARAMS.value : [],
        Settings.AI_TYPE.value :  AIType.REACHABLE.value,
        Settings.AI_PARAMS.value : params
    }

def mod_reachable_config(params):
    return {
        Settings.AI.value : True,
        Settings.START_TYPE.value : StartType.CHAMPION.value,
        Settings.START_PARAMS.value : [],
        Settings.SEARCH_TYPE.value : SearchType.NONE.value,
        Settings.SEARCH_PARAMS.value : [],
        Settings.AI_TYPE.value :  AIType.MODIFIED_REACHABLE.value,
        Settings.AI_PARAMS.value : params
    }

def piecebased_config_add(params):
    return {
        Settings.AI.value : True,
        Settings.START_TYPE.value : StartType.CHAMPION.value,
        Settings.START_PARAMS.value : [],
        Settings.SEARCH_TYPE.value : SearchType.NONE.value,
        Settings.SEARCH_PARAMS.value : [],
        Settings.AI_TYPE.value :  AIType.PIECE_BASED_ADD.value,
        Settings.AI_PARAMS.value : params
    }

def piecebased_config_mul(params):
    return {
        Settings.AI.value : True,
        Settings.START_TYPE.value : StartType.CHAMPION.value,
        Settings.START_PARAMS.value : [],
        Settings.SEARCH_TYPE.value : SearchType.NONE.value,
        Settings.SEARCH_PARAMS.value : [],
        Settings.AI_TYPE.value :  AIType.PIECE_BASED_MUL.value,
        Settings.AI_PARAMS.value : params
    }

def flexible_start_config(params):
    return {
        Settings.AI.value : True, #should this be Ai or person
        Settings.START_TYPE.value : StartType.SIMPLE.value, #what kind of start state
        Settings.START_PARAMS.value : params, #any parameters for the stater
        Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
        Settings.SEARCH_PARAMS.value : [], #any parameters for the search
        Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
        Settings.AI_PARAMS.value : [] #any params for the ai
    }


def read_file_into_configs(filename, config_maker):
    configs = []

    file = open(filename, 'r')
    text = file.read()

    param_strings = text.splitlines()
    for params in param_strings:
        lst = json.loads(params)
        conf = config_maker(lst)
        conf[FILENAME_FIELD] = filename
        configs.append(conf)
    file.close()

    return configs






