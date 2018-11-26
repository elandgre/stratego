from game.player import Player
from game.engine import Engine

def test_contructor():
    #simple test to make sure that the constructor runs
    engine = Engine()
    player = Player(True, engine)

def test_get_start_state_doesnt_fail():
    #simple test to make sure that the get_start_state runs
    engine = Engine()
    player = Player(True, engine)
    player.get_starting_state()

def test_is_human():
    engine = Engine()
    player = Player(True, engine)
    assert player.is_human()