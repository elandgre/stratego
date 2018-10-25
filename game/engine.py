from player import Player
from board import Board
from config import *
from time import time

class Engine:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        if player1_config[Settings.AI.value]:
            #init the ai for player one
            self.player1 = _setup_ai(player1_config)
        else :
            self.player1 = Player(self)


        if player2_config[Settings.AI.value]:
            #init the ai for palyer one
            self.player2 = _setup_ai(player2_config)
        else:
            self.player2 = Player(self)


        self.board = Board()
        self.player1_turn = True

    def _setup_ai(config):
        starter = None
        searcher = None
        evaluator = None

        #parse and create the start state
        if config[Settings.START_TYPE.value] == StartType.RANDOM.value :
            #fill in the random start state
            raise Exception('not impmented')
        else:
            raise Exception('not impmented')

        #parse and create the searcher
        if config[Settings.SEARCH_TYPE.value] == SearchType.RANDOM.value :
            #fill in the random search type
            raise Exception('not impmented')
        elif config[Settings.SEARCH_TYPE.value] == SearchType.FULL.value :
            #fill in the full search type
            raise Exception('not impmented')
        elif config[Settings.SEARCH_TYPE.value] == SearchType.STOCASTIC.value :
            #fill in the stocastic search type
            raise Exception('not impmented')
        else:
            raise Exception('not impmented')

        #parse and create the evaluator
        if config[Settings.EVALUATION_TYPE.value] == SearchType.FLAG_ATTACK.value :
            raise Exception('not impmented')
        elif config[Settings.EVALUATION_TYPE.value] == SearchType.FLAG_DEFENCE.value :
            raise Exception('not impmented')
        elif config[Settings.EVALUATION_TYPE.value] == SearchType.STRATEGIC_DEFENCE.value :
            raise Exception('not impmented')
        elif config[Settings.EVALUATION_TYPE.value] == SearchType.MIXED.value :
            raise Exception('not impmented')
        else:
            raise Exception('not impmented')

        return BasicAI(self, time.now(), TIME_PER_MOVE, starter, evaluator, searcher )

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
            self.player2.get_starting_state()
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
                    new_start = start[0],9-start[1]
                    new_end = end[0],9-end[1]
                    if self.board.move(new_start,new_end,1):
                        self.player1_turn = False
                        invalid_move = False
                else:
                    print("player 2")
                    start,end = self.player2.get_move()
                    new_start = 9-start[0],start[1]
                    new_end = 9-end[0],end[1]
                    if self.board.move(new_start,new_end,2):
                        self.player1_turn = True
                        invalid_move = False
        return self.board.get_winner()

    def get_state(self):
        if self.player1_turn:
            return self.board.get_player_view(1)
        else:
            return self.board.get_player_view(2)

    def get_valid_moves(self):
        if self.player1_turn:
            self.board(get_valid_moves,1)
        else:
            self.board(get_valid_moves,2)
