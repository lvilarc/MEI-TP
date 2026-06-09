def _norm(paths):
    return sorted(tuple(path) for path in paths)

def run_tests(solution_module):
    f = solution_module.findLadders
    assert _norm(f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])) == _norm([['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']])
    assert f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == []
    assert f('a', 'c', ['a', 'b', 'c']) == [['a', 'c']]
    assert _norm(f('red', 'tax', ['ted', 'tex', 'red', 'tax', 'tad', 'den', 'rex', 'pee'])) == _norm([['red', 'ted', 'tad', 'tax'], ['red', 'ted', 'tex', 'tax'], ['red', 'rex', 'tex', 'tax']])
    assert f('lost', 'cost', ['most', 'fost', 'cost', 'lost']) == [['lost', 'cost']]
