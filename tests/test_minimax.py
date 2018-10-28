from utils.search_utils import *

def next_states_func(d):
    def f(state, player):
        return d[state]
    return f

def eval_func(d):
    def f(state, player):
        return d[state]
    return f

basic_next_s = next_states_func({
    'a' : ['b', 'c'],
    'b' : ['d', 'e'],
    'c' : ['f', 'g'],
    'd' : ['h', 'i'],
    'e' : ['j', 'k'],
    'f' : ['l', 'm'],
    'g' : ['n', 'o'],
    'h' : [],
    'i' : [],
    'j' : [],
    'k' : [],
    'l' : [],
    'm' : [],
    'n' : [],
    'o' : []
})

basic_eval_f = eval_func({
    'a' : 0,
    'b' : 2,
    'c' : 1,
    'd' : 4,
    'e' : 2,
    'f' : 2,
    'g' : 2,
    'h' : 5,
    'i' : 1,
    'j' : 1,
    'k' : 1,
    'l' : 1,
    'm' : 1,
    'n' : 0,
    'o' : 0
})

def test_0_limit():
    assert 0 == minimax_search('a', 0, basic_next_s, basic_eval_f, 0)

def test_goal():
    assert 5 == minimax_search('h', 2, basic_next_s, basic_eval_f, 0)

def test_full():
    assert 1 == minimax_search('a', 3, basic_next_s, basic_eval_f, 0)