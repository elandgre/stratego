from player import Player
from board import Board
from config import *
import time
from ai.random_searcher import RandomSearcher
from ai.random_starter import RandomStarter
from ai.basicAI import BasicAI
from ai.reachable_ai import ReachableAI

class Engine:
    def __init__(self, player1_config=None, player2_config=None, time_per_move=None):
        if not player1_config :
            player1_config = {
                Settings.AI.value : True,
                Settings.START_TYPE.value : StartType.RANDOM.value,
                Settings.START_PARAMS.value : [],
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value : AIType.NONE.value,
                Settings.AI_PARAMS.value : []
            }

        if not player2_config :
            player2_config = {
                Settings.AI.value : True,
                Settings.START_TYPE.value : StartType.RANDOM.value,
                Settings.START_PARAMS.value : [],
                Settings.SEARCH_TYPE.value : SearchType.RANDOM.value,
                Settings.SEARCH_PARAMS.value : [],
                Settings.AI_TYPE.value :  AIType.NONE.value,
                Settings.AI_PARAMS.value : []
            }

        if not time_per_move:
            time_per_move = 10

        self.player1 = None
        self.player2 = None

        if player1_config[Settings.AI.value]:
            #init the ai for player one
            self.player1 = Player(self, self._setup_ai(player1_config, time_per_move))
        else :
            self.player1 = Player(self)


        if player2_config[Settings.AI.value]:
            #init the ai for palyer one
            self.player2 = Player(self, self._setup_ai(player2_config, time_per_move))
        else:
            self.player2 = Player(self)

        self.num_moves = 0
        self.board = Board()
        self.player1_turn = True

    def _setup_ai(self, config, time_per_move):
        starter = None
        searcher = None
        evaluator = None

        #parse and create the start state
        if config[Settings.START_TYPE.value] == StartType.RANDOM.value :
            starter = RandomStarter(time.time())
        else:
            raise NotImplementedError

        #parse and create the searcher
        if config[Settings.SEARCH_TYPE.value] == SearchType.RANDOM.value :
            searcher = RandomSearcher(config[Settings.SEARCH_PARAMS.value])
        elif config[Settings.SEARCH_TYPE.value] == SearchType.NONE.value :
            searcher = None
        elif config[Settings.SEARCH_TYPE.value] == SearchType.GREEDY.value :
            searcher = None
        elif config[Settings.SEARCH_TYPE.value] == SearchType.FULL.value :
            #fill in the full search type
            raise NotImplementedError
        elif config[Settings.SEARCH_TYPE.value] == SearchType.STOCASTIC.value :
            #fill in the stocastic search type
            raise NotImplementedError
        else:
            raise NotImplementedError

        #parse and create the evaluator
        if config[Settings.AI_TYPE.value] == AIType.NONE.value :
            ai = BasicAI(self, time.time(), time_per_move, starter, None, searcher)
        elif config[Settings.AI_TYPE.value] == AIType.INVINCLBLE.value :
            raise NotImplementedError
        elif config[Settings.AI_TYPE.value] == AIType.REACHABLE.value :
            ai = ReachableAI(self,time.time(),time_per_move,starter, config[Settings.AI_PARAMS.value])
        else:
            raise NotImplementedError

        return ai

    def setup_board(self):
        invalid_state = True
        while invalid_state:
            states = self.player1.get_starting_state()
            if self.board.add_player(states,1):
                invalid_state = False
            else:
                print("invalid list of starting states")
        invalid_state = True
        while invalid_state:
            states = self.player2.get_starting_state()
            if self.board.add_player(states,2):
                invalid_state = False
            else:
                print("invalid list of starting states")

    def get_board(self, player):
        return self.board.get_player_view(player)

    def make_move(self, player1_turn):
        self.player1_turn = player1_turn
        invalid_move = True
        if self.player1_turn:
            if self.player1.is_human():
                print(self.board.get_player_view(1))
        else:
            if self.player2.is_human():
                print(self.board.get_player_view(2))
        while invalid_move:
            if self.player1_turn:
                print("player 1")
                start,end = self.player1.get_move()
                if(start == None and end == None):
                    print "empty"
                    return self.player1_turn
                if self.player1.is_human():
                    start = start[0],9-start[1]
                    end = end[0],9-end[1]

                if self.board.move(start,end,1):
                    self.player1_turn = False
                    invalid_move = False
                self.num_moves += 1
                return self.player1_turn
            else:
                print("player 2")
                start,end = self.player2.get_move()
                if(start == None and end == None):
                    print "empty"
                    return self.player1_turn
                    break
                if(self.player2.is_human()) :
                    start = 9-start[0],start[1]
                    end = 9-end[0],end[1]


                if self.board.move(start,end,2):
                    self.player1_turn = True
                    invalid_move = False
                self.num_moves += 1
                return self.player1_turn

    def run(self):
        self.setup_board()
        self.player1_turn = True
        while not self.board.get_winner():
            self.player1_turn = self.make_move(self.player1_turn)
        return self.board.get_winner()

    def get_state(self):
        if self.player1_turn:
            return self.board.get_player_view(1)
        else:
            return self.board.get_player_view(2)

    def get_valid_moves(self):
        if self.player1_turn:
            return self.board.get_valid_moves_list(1)
        else:
            return self.board.get_valid_moves_list(2)

    def get_num_moves(self):
        return self.num_moves

    def is_first_move(self):
        return self.num_moves < 2

    def get_oponents_peices(self):
        #TODO: set of PIECE POSITION
        return set()

    def get_my_peices(self):
        #set of PIECE POSITION
        #may not be needed
        return set()

    def get_oponents_moved_peices(self):
        #TODO: set of PIECE POSITION
        return set()

    def get_my_moved_peices(self):
        #set of PIECE POSITION
        #may not be needed
        return set()

    def get_oponents_revealed_peices(self):
        #TODO: set of PIECE POSITION revealed
        return set()

    def get_my_revealed_peices(self):
        #set of PIECE POSITION revealed
        #may not be needed
        return set()

    def get_peice_at(self, pos):
        if self.player1_turn:
            return self.board.get_piece_at_position(pos, 1)
        else:
            return self.board.get_piece_at_position(pos, 2)



#    def get_all_next_moves(self):
#        def next_moves(board):
#            return []

#    def get_p_percent_next_moves(self, p):
#        def next_moves(board):
#            return []





