def run_tests(solution_module):
    f = solution_module.candy
    # single child
    assert f([0]) == 1
    # all same rating — each gets 1
    assert f([1, 1, 1]) == 3
    # strictly increasing
    assert f([1, 2, 3]) == 6
    # strictly decreasing
    assert f([3, 2, 1]) == 6
    # valley shape
    assert f([1, 3, 2, 2, 1]) == 7
