from engine import Engine
from config import FRONTEND
def play():
    FRONTEND = False
    e = Engine(1000)
    winner = e.run()
    print("after {} moves".format(e.get_num_moves()))
    print "THE WINNER IS ..."
    print "player " + str(winner)

if __name__ == "__main__":
    play()