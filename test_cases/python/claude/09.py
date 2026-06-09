def run_tests(solution_module):
    f = solution_module.isNumber
    # positive decimal
    assert f('+3.14') is True
    # exponent with sign
    assert f('3e+7') is True
    # double sign is invalid
    assert f('--6') is False
    # just a dot is invalid
    assert f('.') is False
    # integer string
    assert f('123') is True
