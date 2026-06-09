def run_tests(solution_module):
    f = solution_module.longestValidParentheses
    assert f('(()') == 2
    assert f(')()())') == 4
    assert f('') == 0
    assert f('()(())') == 6
    assert f('))))') == 0
