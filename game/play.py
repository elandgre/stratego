from engine import Engine
from config import FRONTEND
def play():
    all_wins = []
    ai1 = {'ai parameters': [1, 0, 0, 0, 0, 0, 1, 1, -1, 1, 0, -1, 1, 0, 0, 1, 0, -1, 0, 1, 0, 0, 0, 0, -1, -1, 1, 0, 0, 1, 0, 1, 1, 1, -1, 1, -1, 0, 1, -1, 1, -1, 0, 0, 0, -1, -1, -1, 0, 1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 1, -1, 0, 0, 1, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -1, -1, 1, 0, 1, 0, 1, 0, -1, -1, -1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 'eval_type': 'reachable', 'search_parmeters': [], 'FILENAME': 'train/good_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}
    ai2 = {'ai parameters': [-0.8071999597000045, 0.14082462182940536, -0.7603731881329097, 0.12750473491157677, 0.2831446004522624, 0.36397186789709246, 0.6164866708441277, 0.443941322557174, -0.9879041769967224, 0.7454435014094059, 0.843800172498504, -0.4589268902722091, -0.7654114477446744, -0.5584312826387791, -0.2907695097063754, -0.6619474886694041], 'eval_type': 'piece_based_add', 'search_parmeters': [], 'FILENAME': 'train/good_piece_based_add.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}


    # standard
    #{'ai parameters': [1, 0, 0, 0, 0, 0, 1, 1, -1, 1, 0, -1, 1, 0, 0, 1, 0, -1, 0, 1, 0, 0, 0, 0, -1, -1, 1, 0, 0, 1, 0, 1, 1, 1, -1, 1, -1, 0, 1, -1, 1, -1, 0, 0, 0, -1, -1, -1, 0, 1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 1, -1, 0, 0, 1, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -1, -1, 1, 0, 1, 0, 1, 0, -1, -1, -1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 'eval_type': 'reachable', 'search_parmeters': [], 'FILENAME': 'train/good_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}

    #mul
    #{'ai parameters': [-1, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], 'eval_type': 'piece_based_mull', 'search_parmeters': [], 'FILENAME': 'train/good_piece_based_mul.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}


    #mod
    #{'ai parameters': [-1, 1, 0, 0, 0, 0, -1, 1, -1, 0, 1, -1, -1, 1, 0, -1, 0, 0, 1, 1, 0], 'eval_type': 'modified_reachable', 'search_parmeters': [], 'FILENAME': 'train/good_modified_reachable.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}

    #add
    #{'ai parameters': [-0.8071999597000045, 0.14082462182940536, -0.7603731881329097, 0.12750473491157677, 0.2831446004522624, 0.36397186789709246, 0.6164866708441277, 0.443941322557174, -0.9879041769967224, 0.7454435014094059, 0.843800172498504, -0.4589268902722091, -0.7654114477446744, -0.5584312826387791, -0.2907695097063754, -0.6619474886694041], 'eval_type': 'piece_based_add', 'search_parmeters': [], 'FILENAME': 'train/good_piece_based_add.txt', 'params_for_start_state': [], 'type_of_start_state': 'champion', 'is an ai': True, 'type_of_search': 'no searcher'}

    wins1 = 0
    wins2 = 0
    ties = 0
    for i in range(100):
        e = Engine(1000, ai1, ai2)
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