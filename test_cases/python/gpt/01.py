def run_tests(solution_module):
    f = solution_module.findMedianSortedArrays
    assert abs(f([1, 3], [2]) - 2.0) < 1e-9
    assert abs(f([1, 2], [3, 4]) - 2.5) < 1e-9
    assert abs(f([], [1]) - 1.0) < 1e-9
    assert abs(f([-5, -3, -1], [-4, -2, 0]) - (-2.5)) < 1e-9
    assert abs(f([-1000000, 1000000], [-1000000, 1000000]) - 0.0) < 1e-9
