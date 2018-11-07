from utils.constants import *
import random

def minimax(player, state, alpha, beta, depth, limit, next_states, evaluator):
    if(depth == limit): return evaluator(state, player)
    else:
        children = next_states(state, player)
        if(children == []): return evaluator(state, player)
        else:
            if(player == 1):
                v = -float('Inf')
                for child in children:
                    child_v = minimax(2, child, alpha, beta, depth-1, limit, next_states, evaluator)
                    v = max(v, child_v)
                    if(v >= beta): return v
                    alpha = min(alpha, v)
            else:
                v = float('Inf')
                for child in children:
                    child_v = minimax(1, child, alpha, beta, depth-1, limit, next_states, evaluator)
                    v = min(v, child_v)
                    if(v <= alpha): return v
                    beta = max(beta, v)
            return v

def minimax_search(state, limit, next_states, evaluator, player):
    return minimax(player, state, -float('Inf'), float('Inf'), 0, limit, next_states, evaluator)


def get_random_start():
    placements = []

    for piece in starting_piece_counts:
        for piece_count in range(starting_piece_counts[piece]):
            placements.append(piece_map[piece])

    random.shuffle(placements)
    return placements