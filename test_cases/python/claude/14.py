def run_tests(solution_module):
    f = solution_module.maxProfit
    # single element — no transaction possible
    assert f([5]) == 0
    # all prices equal — no profit
    assert f([3, 3, 3]) == 0
    # one increasing run — one transaction covers it
    assert f([1, 2, 3, 4, 5]) == 4
    # two separate profitable windows
    assert f([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    # strictly decreasing — no profit
    assert f([5, 4, 3, 2, 1]) == 0
