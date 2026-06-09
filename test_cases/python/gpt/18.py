def run_tests(solution_module):
    f = solution_module.candy
    assert f([1, 0, 2]) == 5
    assert f([1, 2, 2]) == 4
    assert f([1]) == 1
    assert f([1, 3, 4, 5, 2]) == 11
    assert f([5, 4, 3, 2, 1]) == 15
