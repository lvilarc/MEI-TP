def run_tests(solution_module):
    f = solution_module.numDistinct
    # t not present in s
    assert f('abc', 'z') == 0
    # t equals s — only one way
    assert f('abc', 'abc') == 1
    # empty t — one way (empty subsequence)
    assert f('abc', '') == 1
    # classic example
    assert f('rabbbit', 'rabbit') == 3
    # repeated chars
    assert f('aaa', 'a') == 3
