from enum import Enum

FILENAME = 'FILENAME'
AI = 'ai'
START = 'start'

MS_BETWEEN_MOVES = 3000

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
    param_strings = text.split('\n')
    for params in param_strings:
        lst = json.loads(params)
        conf = config_maker(lst)
        conf[FILENAME] = filename
        configs.append()
    file.close()

    return configs






