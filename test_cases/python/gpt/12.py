def run_tests(solution_module):
    f = solution_module.isScramble
    assert f('great', 'rgeat') is True
    assert f('abcde', 'caebd') is False
    assert f('a', 'a') is True
    assert f('abc', 'bca') is True
    assert f('abcd', 'bdac') is False
