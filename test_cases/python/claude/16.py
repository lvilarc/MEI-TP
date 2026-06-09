def run_tests(solution_module):
    f = solution_module.ladderLength
    # endWord not reachable
    assert f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == 0
    # direct one-step
    assert f('a', 'b', ['b']) == 2
    # standard example
    assert f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5
    # endWord not in list
    assert f('abc', 'xyz', ['abc']) == 0
    # one-step direct transformation
    assert f('ab', 'cb', ['bb', 'cb']) == 2
