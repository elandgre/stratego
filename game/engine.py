from player import Player
from board import Board
from config import *
import time
from ai.random_searcher import RandomSearcher
from ai.random_starter import RandomStarter
from ai.basicAI import BasicAI

class Engine:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        if player1_config[Settings.AI.value]:
            #init the ai for player one
            self.player1 = Player(self, self._setup_ai(player1_config))
        else :
            self.player1 = Player(self)


        if player2_config[Settings.AI.value]:
            #init the ai for palyer one
            self.player2 = Player(self, self._setup_ai(player2_config))
        else:
            self.player2 = Player(self)


        self.board = Board()
        self.player1_turn = True

    def _setup_ai(self, config):
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
        elif config[Settings.SEARCH_TYPE.value] == SearchType.FULL.value :
            #fill in the full search type
            raise NotImplementedError
        elif config[Settings.SEARCH_TYPE.value] == SearchType.STOCASTIC.value :
            #fill in the stocastic search type
            raise NotImplementedError
        else:
            raise NotImplementedError

        #parse and create the evaluator
        if config[Settings.EVALUATION_TYPE.value] == EvaluationType.NONE.value :
            evaluator = None
        elif config[Settings.EVALUATION_TYPE.value] == EvaluationType.FLAG_ATTACK.value :
            raise NotImplementedError
        elif config[Settings.EVALUATION_TYPE.value] == EvaluationType.FLAG_DEFENCE.value :
            raise NotImplementedError
        elif config[Settings.EVALUATION_TYPE.value] == EvaluationType.STRATEGIC_DEFENCE.value :
            raise NotImplementedError
        elif config[Settings.EVALUATION_TYPE.value] == EvaluationType.MIXED.value :
            raise NotImplementedError
        else:
            raise NotImplementedError

        return BasicAI(self, time.time(), TIME_PER_MOVE, starter, evaluator, searcher )

    def run(self):
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
        self.player1_turn = True
        while not self.board.get_winner():
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
                        break
                    if self.player1.is_human():
                        start = start[0],9-start[1]
                        end = end[0],9-end[1]

                    if self.board.move(start,end,1):
                        self.player1_turn = False
                        invalid_move = False
                else:
                    print("player 2")
                    start,end = self.player2.get_move()
                    if(start == None and end == None):
                        print "empty"
                        break
                    if(self.player2.is_human()) :
                        start = 9-start[0],start[1]
                        end = 9-end[0],end[1]


                    if self.board.move(start,end,2):
                        self.player1_turn = True
                        invalid_move = False
            self.board.check_win()
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

    def get_all_next_moves(self):
        def next_moves(board):
            return []

    def get_p_percent_next_moves(self, p):
        def next_moves(board):
            return []





