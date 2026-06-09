def _norm(paths):
    return sorted(tuple(p) for p in paths)

def run_tests(solution_module):
    f = solution_module.findLadders
    # endWord not in wordList
    assert f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']) == []
    # direct one-step transformation
    assert _norm(f('a', 'b', ['a', 'b'])) == _norm([['a', 'b']])
    # two shortest paths
    assert _norm(f('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])) == _norm([
        ['hit', 'hot', 'dot', 'dog', 'cog'],
        ['hit', 'hot', 'lot', 'log', 'cog']
    ])
    # beginWord equals endWord is excluded by constraints, use unreachable
    assert f('abc', 'xyz', ['def']) == []
    # minimal two-step path
    assert _norm(f('ab', 'cb', ['ab', 'bb', 'cb'])) == _norm([['ab', 'cb']])
