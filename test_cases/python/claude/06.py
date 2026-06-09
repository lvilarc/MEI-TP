def run_tests(solution_module):
    f = solution_module.firstMissingPositive
    # consecutive from 1 — next is n+1
    assert f([1, 2, 3]) == 4
    # negatives and zero only
    assert f([-1, -2, 0]) == 1
    # duplicates present
    assert f([2, 2, 2]) == 1
    # single element equal to 1
    assert f([1]) == 2
    # large gap
    assert f([100, 200, 300]) == 1
