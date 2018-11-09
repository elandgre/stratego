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


#[2, 3, 12, 2, 8, 3, 5, 12, 3, 3, 4, 12, 4, 7, 12, 11, 5, 6, 12, 4, 5, 4, 12, 6, 9, 1, 10, 3, 8, 2, 6, 2, 2, 5, 2, 2, 7, 7, 2, 6]