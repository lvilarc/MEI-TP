def run_tests(solution_module):
    f = solution_module.isMatch
    assert f('aa', 'a') is False
    assert f('aa', 'a*') is True
    assert f('ab', '.*') is True
    assert f('aab', 'c*a*b') is True
    assert f('mississippi', 'mis*is*p*.') is False
