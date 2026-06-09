def run_tests(solution_module):
    f = solution_module.isNumber
    assert f('0') is True
    assert f('e') is False
    assert f('.') is False
    assert f('-.9') is True
    assert f('99e2.5') is False
