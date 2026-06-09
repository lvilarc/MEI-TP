def run_tests(solution_module):
    f = solution_module.numDistinct
    assert f('rabbbit', 'rabbit') == 3
    assert f('babgbag', 'bag') == 5
    assert f('', 'a') == 0
    assert f('abc', '') == 1
    assert f('aaaaa', 'aa') == 10
