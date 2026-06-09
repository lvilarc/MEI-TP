def run_tests(solution_module):
    f = solution_module.findMedianSortedArrays
    # both arrays same length, even total
    assert abs(f([1, 2], [3, 4]) - 2.5) < 1e-9
    # one empty array, odd total
    assert abs(f([], [2, 3, 5]) - 3.0) < 1e-9
    # arrays with negative values
    assert abs(f([-3, -1], [-2, 0]) - (-1.5)) < 1e-9
    # single element each
    assert abs(f([3], [4]) - 3.5) < 1e-9
    # all same values
    assert abs(f([2, 2], [2, 2]) - 2.0) < 1e-9
