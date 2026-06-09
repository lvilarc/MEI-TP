def run_tests(solution_module):
    f = solution_module.firstMissingPositive
    assert f([1, 2, 0]) == 3
    assert f([3, 4, -1, 1]) == 2
    assert f([7, 8, 9, 11, 12]) == 1
    assert f([1, 1]) == 2
    assert f([1, 2, 3, 4, 5]) == 6
