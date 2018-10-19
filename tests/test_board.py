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

def test_op_hidden():
    #tests mountians are there
    board = Board()
    a_start_state = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,10,11,12,12,12,12,12,12]
    one = board.add_player(a_start_state,1)
    two = board.add_player(a_start_state,2)

    view_one = board.get_player_view(1)
    view_two = board.get_player_view(2)

    rows = [4,5]
    columns = [2,3,6,7]
    for i in rows:
        for j in columns:
            assert view_one[i][j] == MOUNTAIN
            assert view_two[i][j] == MOUNTAIN

