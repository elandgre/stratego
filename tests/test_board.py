from game.board import *
from utils.constants import *

def test_init():
    #simple test to make sure that the constructor runs
    board = Board()

def test_player1():
    #tests that player 1 can be added to the board
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    try_one = board.add_player(a_start_state,1)
    assert try_one

def test_player1_dup():
    #tests that player 1 can not be added to the board twice
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    try_one = board.add_player(a_start_state,1)
    try_two = board.add_player(a_start_state,1)
    assert try_one
    assert not try_two

def test_player2():
    #tests that player 1 can be added
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    try_one = board.add_player(a_start_state,1)
    try_two = board.add_player(a_start_state,2)
    assert try_one
    assert try_two

def test_player2_two_before_one():
    #tests that player 1 can not be added before player two
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    try_one = board.add_player(a_start_state,2)
    try_two = board.add_player(a_start_state,1)
    assert try_one
    assert not try_two

def test_player2_dup():
    #tests that player 2 can not be added to the board twice
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    try_one = board.add_player(a_start_state,1)
    try_two = board.add_player(a_start_state,2)
    try_three = board.add_player(a_start_state,2)
    assert try_one
    assert try_two
    assert not try_three

def test_invalid_pieces():
    #tests that the peices have to be valid peices
    board = Board()
    too_many = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12,12]
    not_enough = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12]
    bad_peice = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,-1,13]
    try_one = board.add_player(too_many,1)
    try_two = board.add_player(not_enough,1)
    try_three = board.add_player(bad_peice,1)
    assert not try_one
    assert not try_two
    assert not try_three

def test_player_rel():
    #tests that players peices are in the right place relative to their side
    #and the other player peices
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    for i in range(4):
        for j in range(10):
            pos = (i) * 10 + j
            assert view_one[9-i][9-j] == a_start_state[pos]
            assert view_two[9-i][9-j] == a_start_state[pos]
            assert view_one[9-i][9-j] == view_two[9-i][9-j]

def test_not_win():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    assert not board.get_winner()

def test_simple_move():
    #tests simple valid move
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (5, 9)

    old_view_one = board.get_player_view(1)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    view_one = board.get_player_view(1)
    assert old_view_one[old[0]][old[1]] == view_one[new[0]][new[1]]
    assert view_one[old[0]][old[1]] == piece_diplay_map[pieces.EMPTY.value]

    board.move(new, old, 1)

    final_view_one = board.get_player_view(1)
    assert np.array_equal(old_view_one, final_view_one)

def bad_move(board, old, new, player):
    old_view_one = board.get_player_view(player)

    assert not board.is_valid_move(old, new, player)
    assert not board.move(old, new, player)

    view_one = board.get_player_view(player)

    assert np.array_equal(old_view_one, view_one)


def test_moving_onto_self():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (7, 9)
    bad_move(board, old, new, 1)

    new = (6, 8)
    bad_move(board, old, new, 1)

    old = (6, 9)
    new = (8, 9)
    bad_move(board, old, new, 2)

    new = (6, 8)
    bad_move(board, old, new, 2)


def test_to_big_a_move():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (4, 9)
    bad_move(board, old, new, 1)

    new = (3, 9)
    bad_move(board, old, new, 1)

    old = (6, 9)
    new = (4, 9)
    bad_move(board, old, new, 2)

    new = (3, 9)
    bad_move(board, old, new, 2)

def test_move_off_board():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (9, 0)
    new = (9, -1)
    bad_move(board, old, new, 1)

    old = (9, 0)
    new = (10, 0)
    bad_move(board, old, new, 1)

    old = (9, 9)
    new = (9, 10)
    bad_move(board, old, new, 1)

    old = (9, 0)
    new = (9, -1)
    bad_move(board, old, new, 2)

    old = (9, 0)
    new = (10, 0)
    bad_move(board, old, new, 2)

    old = (9, 9)
    new = (9, 10)
    bad_move(board, old, new, 2)

def test_move_op_peice():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (3, 9)
    new = (4, 9)
    bad_move(board, old, new, 2)

    old = (3, 9)
    new = (4, 9)
    bad_move(board, old, new, 1)

def test_move_on_mountain():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,12,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,3,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 2)
    new = (5, 2)
    bad_move(board, old, new, 1)

    old = (6, 2)
    new = (5, 2)
    bad_move(board, old, new, 2)

def test_move_flag():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,11,9,10,8,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (5, 9)
    bad_move(board, old, new, 1)

    old = (6, 9)
    new = (5, 9)
    bad_move(board, old, new, 2)

def test_move_bomb():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 0)
    new = (5, 0)
    bad_move(board, old, new, 1)

    old = (6, 0)
    new = (5, 0)
    bad_move(board, old, new, 2)

def test_basic_scout_move():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    old = (6, 9)
    new = (4, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

def test_basic_scout_not_diag():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (4, 8)
    bad_move(board, old, new, 1)

    old = (6, 9)
    new = (4, 8)

    bad_move(board, old, new, 2)

def test_basic_scout_not_jumping_player_2():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)


    old = (6, 0)
    new = (4, 0)

    bad_move(board, old, new, 2)

def test_basic_scout_not_jumping_player_1():
    board = Board()
    a_start_state = [1,8,12,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,11,12,12,12,12,12,2]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 0)
    new = (4, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)


    old = (6, 9)
    new = (4, 9)

    bad_move(board, old, new, 1)



def test_all_valid_moves():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    one_moves = board.get_valid_moves_list(1)
    for start,end in one_moves:
            assert board.is_valid_move(start, end, 1)

    two_moves = board.get_valid_moves_list(2)
    for start, end in two_moves:
        assert board.is_valid_move(start, end, 2)

    one_moves = board.get_valid_moves_set(1)
    for start,end in one_moves:
            assert board.is_valid_move(start, end, 1)

    two_moves = board.get_valid_moves_set(2)
    for start, end in two_moves:
        assert board.is_valid_move(start, end, 2)

def test_scout_attacking():
    board = Board()
    a_start_state = [1,8,12,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,11,12,12,12,12,12,2]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (3, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    old = (6, 9)
    new = (3, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

def test_p1_attacking_and_win():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,8,8,9,10,11,12,12,12,12,12,7]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot
    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[3][9] == piece_diplay_map[pieces.COLONEL.value]
    assert view_two[6][0] == piece_diplay_map[pieces.HIDDEN.value]

def test_p1_attacking_and_loose():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,8,7,9,10,11,12,12,12,12,12,8]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot
    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[3][9] == piece_diplay_map[pieces.HIDDEN.value]
    assert view_two[6][0] == piece_diplay_map[pieces.COLONEL.value]

def test_p2_attacking_and_loose():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,8,8,9,10,11,12,12,12,12,12,7]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 0)
    new = (5, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    old = new
    new = (4, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)
    print(view_one)
    print(view_two)

    #attack!!!
    old = new
    new = (3, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot
    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)
    print(view_one)
    print(view_two)

    assert view_one[6][9] == piece_diplay_map[pieces.COLONEL.value]
    assert view_two[3][0] == piece_diplay_map[pieces.HIDDEN.value]

def test_p2_attacking_and_win():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,8,7,9,10,11,12,12,12,12,12,8]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 0)
    new = (5, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    old = new
    new = (4, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    #attack!!!
    old = new
    new = (3, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[6][9] == piece_diplay_map[pieces.HIDDEN.value]
    assert view_two[3][0] == piece_diplay_map[pieces.COLONEL.value]

def test_p1_attacking_and_tie():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,8,9,10,11,12,12,12,12,12,8]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot
    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[3][9] == piece_diplay_map[pieces.EMPTY.value]
    assert view_two[6][0] == piece_diplay_map[pieces.EMPTY.value]

def test_p2_attacking_and_tie():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,8,9,10,11,12,12,12,12,12,8]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 0)
    new = (5, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    old = new
    new = (4, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    #attack!!!
    old = new
    new = (3, 0)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[6][9] == piece_diplay_map[pieces.EMPTY.value]
    assert view_two[3][0] == piece_diplay_map[pieces.EMPTY.value]

def test_p1_minner_attack_bomb():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,8,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,3,9,10,11,12,12,12,12,8,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot
    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[3][9] == piece_diplay_map[pieces.MINER.value]
    assert view_two[6][0] == piece_diplay_map[pieces.HIDDEN.value]

def test_p2_minner_attack_bomb():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,8,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,3,9,10,11,12,12,12,12,8,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)


    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[6][0] == piece_diplay_map[pieces.HIDDEN.value]
    assert view_two[3][9] == piece_diplay_map[pieces.MINER.value]

def test_p1_spy_attack_marshal():
    board = Board()
    a_start_state = [3,2,2,2,2,2,2,2,2,8,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,1,9,12,11,12,12,12,12,8,10]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot
    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[3][9] == piece_diplay_map[pieces.SPY.value]
    assert view_two[6][0] == piece_diplay_map[pieces.HIDDEN.value]

def test_p2_spy_attack_marshal():
    board = Board()
    a_start_state = [3,2,2,2,2,2,2,2,2,8,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,1,9,12,11,12,12,12,12,8,10]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)


    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[6][0] == piece_diplay_map[pieces.HIDDEN.value]
    assert view_two[3][9] == piece_diplay_map[pieces.SPY.value]

def test_p1_marshal_attack_spy():
    board = Board()
    a_start_state = [3,2,2,2,2,2,2,2,2,8,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,10,9,12,11,12,12,12,12,8,1]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot
    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[3][9] == piece_diplay_map[pieces.MARSHAL.value]
    assert view_two[6][0] == piece_diplay_map[pieces.HIDDEN.value]

def test_p2_marshal_attack_spy():
    board = Board()
    a_start_state = [3,2,2,2,2,2,2,2,2,8,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,12,7,10,9,12,11,12,12,12,12,8,1]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)


    old = (6, 9)
    new = (5, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)

    old = new
    new = (4, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)


    #attack!!!
    old = new
    new = (3, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)
    #p1 should be victorious
    #in both views the p1 peice should be in this spot

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    assert view_one[6][0] == piece_diplay_map[pieces.HIDDEN.value]
    assert view_two[3][9] == piece_diplay_map[pieces.MARSHAL.value]

def test_p1_flag_cap():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,12,12,12,12,12,12,11]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (3, 9)


    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)
    assert board.get_winner() == 1


def test_p2_flag_cap():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,12,12,12,12,12,12,11]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (6, 9)
    new = (3, 9)

    assert board.is_valid_move(old, new, 2)
    assert board.move(old, new, 2)
    assert board.get_winner() == 2


def test_get_full_board():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,12,12,12,12,12,12,11]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)


    print(board.get_full_view())


def test_get_player_positions_in_persp():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,12,12,12,12,12,12,11]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    pl1_ps1 = board.all_players_peice_positions(1,1)
    pl2_ps1 = board.all_players_peice_positions(2,1)

    pl1_ps2 = board.all_players_peice_positions(1,2)
    pl2_ps2 = board.all_players_peice_positions(2,2)

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    for (i,j) in pl1_ps1:
        assert(view_one[i][j] != piece_diplay_map[pieces.HIDDEN.value])
        assert(view_one[i][j] != piece_diplay_map[pieces.MOUNTAIN.value])
        assert(view_one[i][j] != piece_diplay_map[pieces.EMPTY.value])

    for (i,j) in pl2_ps1:
        assert(view_one[i][j] == piece_diplay_map[pieces.HIDDEN.value])

    for (i,j) in pl2_ps2:
        assert(view_two[i][j] != piece_diplay_map[pieces.HIDDEN.value])
        assert(view_two[i][j] != piece_diplay_map[pieces.MOUNTAIN.value])
        assert(view_two[i][j] != piece_diplay_map[pieces.EMPTY.value])

    for (i,j) in pl1_ps2:
        assert(view_two[i][j] == piece_diplay_map[pieces.HIDDEN.value])


def test_get_moved_positions_no_moves():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,12,12,12,12,12,12,11]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)


    pl1_ps1 = board.all_moved_peice_positions(1,1)
    pl2_ps1 = board.all_moved_peice_positions(2,1)
    pl1_ps2 = board.all_moved_peice_positions(1,2)
    pl2_ps2 = board.all_moved_peice_positions(2,2)

    assert pl1_ps1 == set()
    assert pl2_ps1 == set()
    assert pl1_ps2 == set()
    assert pl2_ps2 == set()

def test_get_reveled_positions_no_moves():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,12,12,12,12,12,12,11]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)


    pl1_ps1 = board.get_players_revealed_peice_positions(1,1)
    pl2_ps1 = board.get_players_revealed_peice_positions(2,1)
    pl1_ps2 = board.get_players_revealed_peice_positions(1,2)
    pl2_ps2 = board.get_players_revealed_peice_positions(2,2)

    assert pl1_ps1 == set()
    assert pl2_ps1 == set()
    assert pl1_ps2 == set()
    assert pl2_ps2 == set()


