from engine import Engine

def play():
    e = Engine()
    winner = e.run()
    print("after {} moves".format(e.get_num_moves()))
    print "THE WINNER IS ..."
    print "player " + str(winner)

if __name__ == "__main__":
    play()