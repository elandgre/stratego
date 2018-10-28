from engine import Engine

def play():
    e = Engine()
    winner = e.run()
    print "AND THE WINNER IS ..."
    print "player " + str(winner)

if __name__ == "__main__":
    play()