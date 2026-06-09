def run_tests(solution_module):
    f = solution_module.findMin
    # fully sorted, no rotation
    assert f([1, 2, 3, 4, 5]) == 1
    # all same values
    assert f([3, 3, 3]) == 3
    # rotated with duplicates
    assert f([2, 2, 2, 0, 1]) == 0
    # single element
    assert f([7]) == 7
    # minimum is last element after rotation
    assert f([3, 4, 5, 1, 2]) == 1
