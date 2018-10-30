from enum import Enum


TIME_PER_MOVE = 10

class Settings(Enum):
    AI = 'is an ai'
    START_TYPE = 'type_of_start_state'
    SEARCH_PARAMS = 'search_parmeters'
    SEARCH_TYPE = 'type_of_search'
    SEARCH_DEPTH = 'depth_of_search'
    SEARCH_WIDTH = 'percentage_of_stocastic_paths_expored'
    EVALUATION_TYPE = 'eval_type'
    EVALUATION_PARAMS = 'eval_paramters'


class StartType(Enum):
    RANDOM = 'random'
    BETTER = 'better'

class SearchType(Enum):
    RANDOM = 'random'
    FULL = 'full_tree_search'
    STOCASTIC = 'stocatic_search'

class EvaluationType(Enum):
    NONE = 'none'
    FLAG_ATTACK = 'flag_attack'
    FLAG_DEFENCE = 'flag_defence'
    STRATEGIC_DEFENCE = 'strat_defence'
    MIXED = 'combination'

class FlagAttackParams(Enum):
    RADIUS = 'radius'

class FlagDefenceParams(Enum):
    RADIUS = 'radius'

class StrategicDefenceParams(Enum):
    RADIUS = 'radius'

player1_config = {
    Settings.AI.value : True,
    Settings.START_TYPE.value : StartType.RANDOM.value,
    Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
    Settings.SEARCH_PARAMS.value : {
            Settings.SEARCH_DEPTH.value : 1,
            Settings.SEARCH_WIDTH.value : 1
    },
    Settings.EVALUATION_TYPE.value : EvaluationType.NONE.value,
    Settings.EVALUATION_PARAMS.value : {
        FlagAttackParams.RADIUS.value : 1
    }
}

player2_config = {
    Settings.AI.value : True,
    Settings.START_TYPE.value : StartType.RANDOM.value,
    Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
    Settings.SEARCH_PARAMS.value : {
            Settings.SEARCH_DEPTH.value : 1,
            Settings.SEARCH_WIDTH.value : 1
    },
    Settings.EVALUATION_TYPE.value :  EvaluationType.NONE.value,
    Settings.EVALUATION_PARAMS.value : {
        FlagAttackParams.RADIUS.value : 1
    }
}





class ReachableParameters(Enum):
    INITIAL_MOVE = 'initial' # 0 - 9
    ATTACKING_UNMOVED = 'attack unmoved' # 10 -19
    ATTACKING_WEAKER = 'attacking weaker' #20-29
    WALK_TO_SIDE = 'walk to side of a peice' #30 -39
    MOVE_TO_RIGHT = 'move the price to the right' # 40 - 49
    MOVE_TO_OWN_SIDE = 'move to our side of the board'# 50 - 59
    MOVE_TO_LEFT = 'move to the left' # 60 - 69
    ATTACK_UNKNOWN_MOVED = 'attack an unkown peice that has moved' # 70-79
    MOVE_AROUND_LAKE = 'move around the lake' # 80 - 89
    MOVE_ALONG_WALL = 'move along the outer walls of the board'# 90 - 99
    RANDOM_MOVE = 'make a random move' # 100 - 109


