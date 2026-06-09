def run_tests(solution_module):
    f = solution_module.isScramble
    # identical strings
    assert f('abc', 'abc') is True
    # length 1, same char
    assert f('a', 'a') is True
    # length 1, different char
    assert f('a', 'b') is False
    # known scramble
    assert f('great', 'rgeat') is True
    # known non-scramble
    assert f('abcde', 'caebd') is False
