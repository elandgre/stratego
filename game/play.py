from engine import Engine
from config import FRONTEND
def play():
    e = Engine(1000)
    winner = e.run()
    print("after {} moves".format(e.get_num_moves()))
    print "THE WINNER IS ..."
    print "player " + str(winner)
    print e.get_value(1, 100, -1, 500)

if __name__ == "__main__":
    play()