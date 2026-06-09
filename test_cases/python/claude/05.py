def run_tests(solution_module):
    f = solution_module.longestValidParentheses
    # all open — no valid pairs
    assert f('(((') == 0
    # nested valid
    assert f('(())') == 4
    # multiple separated valid segments, longest is 4
    assert f('()(()') == 2
    # entire string is valid
    assert f('()()') == 4
    # single close bracket
    assert f(')') == 0
