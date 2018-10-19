from enum import Enum

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


piece_map = {piece_names[i]:i for i in range(len(piece_names))}

piece_diplay_map = {piece_names[i]:i for i in range(len(piece_names))}
piece_diplay_map[pieces.HIDDEN.value] = 999
piece_diplay_map[pieces.MOUNTAIN.value] = 111

