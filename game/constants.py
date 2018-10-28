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

starting_pieces_per_player = 40

piece_map = {piece_names[i]:i for i in range(len(piece_names))}

piece_diplay_map = {piece_names[i]:i for i in range(len(piece_names))}
piece_diplay_map[pieces.HIDDEN.value] = 999
piece_diplay_map[pieces.MOUNTAIN.value] = 111

