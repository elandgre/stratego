from engine import Engine
from config import FRONTEND
from utils.constants import *
def play():
    all_wins = []
    ai1 = {
                Settings.AI.value : True,
                Settings.START_TYPE.value : StartType.SIMPLE.value,
                Settings.START_PARAMS.value : [4, 5, 6, 2, 3, 3, 7, 10, 6, 12, 2, 12, 4, 5, 1, 2, 2, 7, 5, 2, 6, 12, 2, 9, 12, 4, 12, 8, 3, 3, 3, 5, 8, 2, 6, 11, 12, 4, 7, 2],
                #[2, 2, 6, 6, 12, 4, 5, 8, 2, 3, 1, 4, 7, 2, 3, 8, 12, 5, 7, 2, 3, 11, 10, 6, 2, 5, 6, 4, 2, 4, 12, 12, 12, 3, 2, 3, 7, 9, 12, 5],
                #[7, 5, 5, 2, 3, 12, 6, 3, 4, 6, 1, 2, 12, 2, 4, 7, 4, 3, 8, 2, 12, 12, 6, 5, 6, 5, 3, 7, 10, 2, 2, 2, 8, 12, 4, 3, 2, 9, 11, 12],
                #[2, 12, 3, 4, 9, 2, 3, 6, 12, 2, 4, 3, 7, 12, 4, 2, 3, 5, 5, 12, 11, 4, 8, 1, 12, 2, 7, 7, 6, 3, 6, 5, 5, 12, 2, 6, 2, 10, 2, 8],
                #[7, 3, 3, 7, 3, 12, 4, 11, 12, 5, 2, 7, 4, 9, 12, 6, 2, 12, 3, 6, 2, 8, 6, 1, 3, 12, 4, 5, 2, 4, 5, 5, 2, 8, 2, 6, 2, 12, 2, 10],
                ##[11, 12, 7, 12, 4, 2, 3, 3, 12, 3, 4, 8, 4, 12, 12, 2, 6, 7, 5, 12, 5, 2, 1, 5, 3, 6, 7, 3, 8, 5, 6, 4, 2, 9, 2, 2, 2, 10, 2, 6],
                #[4, 2, 12, 3, 7, 12, 11, 12, 3, 3, 12, 3, 12, 8, 2, 5, 12, 4, 5, 6, 5, 4, 1, 4, 9, 2, 7, 7, 10, 6, 2, 6, 2, 5, 2, 3, 6, 8, 2, 2],
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value :  AIType.NONE.value,
                Settings.AI_PARAMS.value : []
            }


    ai2 = {
                Settings.AI.value : True,
                Settings.START_TYPE.value : StartType.CHAMPION.value,
                Settings.START_PARAMS.value : [],
                Settings.SEARCH_TYPE.value : SearchType.NONE.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value :  AIType.MODIFIED_REACHABLE.value,
                Settings.AI_PARAMS.value : [-1, 1, 0, 0, 0, 0, -1, 1, -1, 0, 1, -1, -1, 1, 0, -1, 0, 0, 1, 1, 0]
            }
    #radnom trained:
    #[69, 30, 1]
    #[62, 37, 1]


    #good trained
    #[57, 40, 3]
    #[60, 38, 2]
    #[71, 28, 1]
    #[67, 31, 2]



    #against champ random ai
    #[69, 29, 2] not random start
    #[75, 24, 1] random start

    #against champ standard ai
    #[59, 39, 2] not random start
    #[76, 22, 2] random start

    #against RANDOM standard ai
    #[73, 24, 3] not random start
    #[70, 28, 2] random start

    #AGAINST RANDOM GENERALIZED ai
    #[67, 28, 5] not random start
    #[64, 36, 0] random start

    #AGAINST champion GENERALIZED ai
    #[76, 23, 1] not random start
    #[70, 26, 4] random start




    #alt. eval function std
    #[0, 0, 0, 1, 0, -1, -1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0, -1, 1, -1, 1, -1, 1, 1, 0, 0, 1, -1, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, -1, 0, 1, 1, -1, -1, -1, 0, 0, 1, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 1, 0, 0, 1, 0, 1, -1, 0, 0, -1, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1, 1, 1, -1, -1, -1, -1, 1, 0, 0, 0]
    #[0, 1, 0, 0, 0, -1, -1, 0, 1, 1, 1, 1, -1, 0, -1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 0, -1, 1, -1, 0, 1, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 1, -1, 0, 0, 0, -1, 0, -1, 0, -1, 0, 1, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 1, 0, 1, 0, 0, -1, 0, 0, 0, -1, -1, -1, 1, 0, 0, 0, 1, 0, -1, -1, 1, 0, 0, 0, 1]

    #alt eval funciton mod
    #[-1, -1, 1, 0, 1, 1, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0]
    #[0, 1, 0, -1, 1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1, 0, 1, 1, 0, 0]
    #[0, 1, 0, -1, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1, 0, 1, 1, 0, 0]

    # standard
    #{'ai parameters': [1, 0, 0, 0, 0, 0, 1, 1, -1, 1, 0, -1, 1, 0, 0, 1, 0, -1, 0, 1, 0, 0, 0, 0, -1, -1, 1, 0, 0, 1, 0, 1, 1, 1, -1, 1, -1, 0, 1, -1, 1, -1, 0, 0, 0, -1, -1, -1, 0, 1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 1, -1, 0, 0, 1, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -1, -1, 1, 0, 1, 0, 1, 0, -1, -1, -1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 'eval_type': 'reachable', 'search_parmeters': [], 'FILENAME': 'train/good_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}

    #mul
    #{'ai parameters': [-1, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], 'eval_type': 'piece_based_mull', 'search_parmeters': [], 'FILENAME': 'train/good_piece_based_mul.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}


    #generalized
    #{'ai parameters': [-1, 1, 0, 0, 0, 0, -1, 1, -1, 0, 1, -1, -1, 1, 0, -1, 0, 0, 1, 1, 0], 'eval_type': 'modified_reachable', 'search_parmeters': [], 'FILENAME': 'train/good_modified_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}

    #add
    #{'ai parameters': [-0.8071999597000045, 0.14082462182940536, -0.7603731881329097, 0.12750473491157677, 0.2831446004522624, 0.36397186789709246, 0.6164866708441277, 0.443941322557174, -0.9879041769967224, 0.7454435014094059, 0.843800172498504, -0.4589268902722091, -0.7654114477446744, -0.5584312826387791, -0.2907695097063754, -0.6619474886694041], 'eval_type': 'piece_based_add', 'search_parmeters': [], 'FILENAME': 'train/good_piece_based_add.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}

    wins1 = 0
    wins2 = 0
    ties = 0
    for i in range(100):
        e = Engine(1000)
        #, ai2
        winner = e.run()
        if(winner == 1):
            wins1 +=1
        elif(winner == 0):
            ties += 1
        else:
            wins2 += 1
        print("after {} moves".format(e.get_num_moves()))
        print "THE WINNER IS ..."
        print "player " + str(winner)
        print e.get_value(1, 100, -1, 500)
    all_wins.append(wins1)
    all_wins.append(ties)
    all_wins.append(wins2)
    print("toal wins: {}".format(all_wins))

if __name__ == "__main__":
    play()


#[2, 3, 12, 2, 8, 3, 5, 12, 3, 3, 4, 12, 4, 7, 12, 11, 5, 6, 12, 4, 5, 4, 12, 6, 9, 1, 10, 3, 8, 2, 6, 2, 2, 5, 2, 2, 7, 7, 2, 6]