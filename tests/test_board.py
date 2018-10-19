from game.board import *

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

def test_simple_move():
    #tests simple valid move
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (3, 0)
    new = (4, 0)

    old_view_one = board.get_player_view(1)

    assert board.is_valid_move(old, new, 1)
    assert board.move(old, new, 1)

    view_one = board.get_player_view(1)
    assert old_view_one[9-old[0]][9-old[1]] == view_one[9-new[0]][9-new[1]]
    assert view_one[9-old[0]][9-old[1]] == 0

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
    old = (3, 0)
    new = (2, 0)
    bad_move(board, old, new, 1)

    new = (3, 1)
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
    old = (3, 0)
    new = (5, 0)
    bad_move(board, old, new, 1)

    new = (6, 0)
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

    old = (0, 0)
    new = (0, -1)
    bad_move(board, old, new, 1)

    old = (0, 0)
    new = (-1, 0)
    bad_move(board, old, new, 1)

    old = (0, 9)
    new = (0, 10)
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
    old = (3, 0)
    new = (4, 0)
    bad_move(board, old, new, 2)

    old = (6, 9)
    new = (5, 9)
    bad_move(board, old, new, 1)

def test_move_on_mountain():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,12,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,3,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (3, 7)
    new = (4, 7)
    bad_move(board, old, new, 1)

    old = (6, 2)
    new = (5, 2)
    bad_move(board, old, new, 2)

def test_move_flag():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,11,9,10,8,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (3, 0)
    new = (4, 0)
    bad_move(board, old, new, 1)

    old = (6, 9)
    new = (5, 9)
    bad_move(board, old, new, 2)

def test_move_bomb():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (3, 9)
    new = (4, 9)
    bad_move(board, old, new, 1)

    old = (6, 0)
    new = (5, 0)
    bad_move(board, old, new, 2)

def test_basic_scout_move():
    board = Board()
    a_start_state = [1,8,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,2,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)
    old = (3, 0)
    new = (5, 0)
    print(board.get_player_view(1))
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
    old = (3, 0)
    new = (5, 1)
    bad_move(board, old, new, 1)

    old = (6, 9)
    new = (4, 8)

    bad_move(board, old, new, 2)

def test_all_valid_moves():
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    one_moves = board.get_valid_moves(1)
    for start in one_moves.keys():
        for end in one_moves[end]:
            assert board.is_valid_move(start, end, 1)

    two_moves = board.get_valid_moves(2)
    for start in two_moves.keys():
        for end in two_moves[end]:
            assert board.is_valid_move(start, end, 2)

#TODO: test scout moves
#TODO: test attacking moves
#TODO: test special moves




