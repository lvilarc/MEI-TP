def run_tests(solution_module):
    f = solution_module.maxProfit
    assert f([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert f([1, 2, 3, 4, 5]) == 4
    assert f([7, 6, 4, 3, 1]) == 0
    assert f([1]) == 0
    assert f([2, 1, 2, 0, 1]) == 2
