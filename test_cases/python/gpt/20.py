def run_tests(solution_module):
    f = solution_module.findMin
    assert f([1, 3, 5]) == 1
    assert f([2, 2, 2, 0, 1]) == 0
    assert f([1]) == 1
    assert f([10, 1, 10, 10, 10]) == 1
    assert f([2, 2, 2, 2]) == 2
