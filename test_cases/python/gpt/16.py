def run_tests(solution_module):
    f = solution_module.ladderLength
    assert f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5
    assert f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == 0
    assert f('a', 'c', ['a', 'b', 'c']) == 2
    assert f('lost', 'cost', ['most', 'fost', 'cost', 'lost']) == 2
    assert f('talk', 'tail', ['talk', 'tons', 'fall', 'tail', 'gale', 'hall', 'negs']) == 0
