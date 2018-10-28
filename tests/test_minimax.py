from utils.search_utils import *

def next_states_func(d):
    def f(state, player):
        return d[state]
    return f

def eval_func(d):
    def f(state, player):
        return d[state]
    return f

def test_0_limit():
    next_s = next_states_func({
        'a' : ['b', 'c', 'd'],
        'b' : ['e', 'f'],
        'c' : ['f'],
        'd' : ['e'],
        'e' : [],
        'f' : ['g']
        })

    eval_f = eval_func({
        'a' : 5,
        'b' : 4,
        'c' : 3,
        'd' : 4,
        'e' : 3,
        'f' : 1,
        'g' : 0
        })

    minimax_search('a', 0, next_s, eval_f, 0)
