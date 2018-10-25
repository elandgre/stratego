from enum import Enum


TIME_PER_MOVE = 10

class Settings(Enum):
  AI = 'is an ai'
  START_TYPE = 'type_of_start_state'
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
  Settings.AI.value : False,
  Settings.START_TYPE.value : StartType.RANDOM.value,
  Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
  Settings.SEARCH_DEPTH.value : 1,
  Settings.SEARCH_WIDTH.value : 1,
  Settings.EVALUATION_TYPE.value : None,
  Settings.EVALUATION_PARAMS.value : {
    EvaluationType.FLAG_ATTACK.value : {
      FlagAttackParams.RADIUS.value : 1
    },
    EvaluationType.FLAG_DEFENCE.value : {
      FlagDefenceParams.RADIUS.value : 1
    },
    EvaluationType.STRATEGIC_DEFENCE.value : {
      StrategicDefenceParams.RADIUS.value : 1
    }
  }
}

player2_config = {
  Settings.AI.value : False,
  Settings.START_TYPE.value : StartType.RANDOM.value,
  Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
  Settings.SEARCH_DEPTH.value : 1,
  Settings.SEARCH_WIDTH.value : 1,
  Settings.EVALUATION_TYPE.value : None,
  Settings.EVALUATION_PARAMS.value : {
    EvaluationType.FLAG_ATTACK.value : {
      FlagAttackParams.RADIUS.value : 1
    },
    EvaluationType.FLAG_DEFENCE.value : {
      FlagDefenceParams.RADIUS.value : 1
    },
    EvaluationType.STRATEGIC_DEFENCE.value : {
      StrategicDefenceParams.RADIUS.value : 1
    }
  }
}
