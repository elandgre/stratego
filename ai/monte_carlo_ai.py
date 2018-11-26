import numpy as np
from ai import AI

class MonteCarloCheatingAI(AI):
    def __init__(self,engine,start_time,time_per_move,starter,evaluator, max_depth, num_to_explore, player):
        super(MonteCarloCheatingAI, self).__init__(engine,start_time,time_per_move, starter)
        self.evaluator = evaluator
        self.max_depth = max_depth
        self.num_to_explore = num_to_explore
        self.max_player = player

    def get_starting_state(self):
        return self.starter.start()

    def get_move(self):
        print 'geting move'
        state = self.engine.get_state()
        valid_moves = self.engine.get_valid_moves()
        time = self.time_per_move
        evaluator = self.evaluator

        best_move = self.best_next(state, self.max_depth, self.max_player)

        print 'decided move'
        return best_move

    def best_next(self, state, max_depth, player):
        state = self.engine.board
        all_next_moves = state.get_valid_moves_list(player)
        best_eval = None
        best_move = None, None

        for (start, end) in all_next_moves:
            next_state = state.copy()
            next_state.move(start, end, player)

            next_player = 1
            if player == 1:
                next_player = 2

            next_eval = self.search(next_state, max_depth-1, next_player)

            if best_eval == None or best_eval < next_eval:
                best_eval = next_eval
                best_move = (start, end)

        return best_move

    def search(self, state, max_depth, player):
        if max_depth == 0 or state.get_winner():
            cur_moves = self.max_depth - max_depth + self.engine.get_num_moves()
            return self.evaluator(state, player, cur_moves, self.engine.get_max_moves(), self.time_per_move, 5)
        else :
            all_next_moves = state.get_valid_moves_list(player)

            total_moves = len(all_next_moves)
            n_select = min(total_moves, self.num_to_explore)

            ind = np.random.choice(total_moves, size=n_select, replace=False)

            select_next_moves = [all_next_moves[i] for i in ind]

            best_eval = None

            for (start, end) in select_next_moves:
                next_state = state.copy()
                next_state.move(start, end, player)

                next_player = 1
                if player == 1:
                    next_player = 2

                next_eval = self.search(next_state, max_depth-1, next_player)

                if self.max_player == player:
                    if best_eval == None or best_eval < next_eval:
                        best_eval = next_eval
                else:
                    if best_eval == None or best_eval > next_eval:
                        best_eval = next_eval

            return best_eval





