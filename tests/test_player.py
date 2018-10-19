from game.player import Player
from game.engine import Engine

def test_contructor():
    #simple test to make sure that the constructor runs
    engine = Engine()
    player = Player(engine)
