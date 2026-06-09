def run_tests(solution_module):
    f = solution_module.isMatch
    # zero repetitions via star
    assert f('b', 'a*b') is True
    # empty string matched by star
    assert f('', 'a*') is True
    # dot matches any char
    assert f('a', '.') is True
    # complex: star eliminates prefix
    assert f('aab', 'c*a*b') is True
    # fails without enough chars
    assert f('ab', 'a') is False
