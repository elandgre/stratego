from ai.modifiedGbrtTrainer import *
ai_config = {
            Settings.AI.value : True,
            Settings.START_TYPE.value : StartType.CHAMPION.value,
            Settings.START_PARAMS.value : [],
            Settings.SEARCH_TYPE.value : SearchType.NONE.value,
            Settings.SEARCH_PARAMS.value : [],
            Settings.AI_TYPE.value :  AIType.PIECE_BASED_MUL.value,
            Settings.AI_PARAMS.value : []
        }

opponent_config = {
            Settings.AI.value : True, #should this be Ai or person
            Settings.START_TYPE.value : StartType.CHAMPION.value, #what kind of start state
            Settings.START_PARAMS.value : [], #any parameters for the stater
            Settings.SEARCH_TYPE.value : SearchType.RANDOM.value, #what kind of search is happening
            Settings.SEARCH_PARAMS.value : [], #any parameters for the search
            Settings.AI_TYPE.value : AIType.NONE.value, # what is the AI
            Settings.AI_PARAMS.value : [] #any params for the ai
        }

output_file = 'train/good_piece_based_mul.txt'

n_params = 16



res = run_and_plot(ai_config, opponent_config, output_file, n_params)
print("Print the results are in the average is {}".format(res))