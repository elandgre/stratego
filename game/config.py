from enum import Enum


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











