def run_tests(solution_module):
    f = solution_module.isMatch
    assert f('aa', 'a') is False
    assert f('aa', '*') is True
    assert f('cb', '?a') is False
    assert f('adceb', '*a*b') is True
    assert f('', '*') is True
