def run_tests(solution_module):
    f = solution_module.minCut
    assert f('aab') == 1
    assert f('a') == 0
    assert f('ab') == 1
    assert f('racecar') == 0
    assert f('banana') == 1
