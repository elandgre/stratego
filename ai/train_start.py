from ls_startstate_trainer import LSStartStateTrainer

def train():
    start = [2,3,12,2,3,12,11,12,3,3,4,12,4,7,8,5,12,5,6,4,5,4,12,1,9,2,7,7,8,2,6,2,2,5,2,6,3,10,2,6]
    LSStartStateTrainer(start)

if __name__ == "__main__":
    train()