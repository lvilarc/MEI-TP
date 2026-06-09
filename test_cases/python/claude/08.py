def run_tests(solution_module):
    f = solution_module.getPermutation
    # n=3, k=6 — last permutation
    assert f(3, 6) == '321'
    # n=2, first permutation
    assert f(2, 1) == '12'
    # n=2, last permutation
    assert f(2, 2) == '21'
    # n=4, k=1 — lexicographically first
    assert f(4, 1) == '1234'
    # n=4, k=24 — lexicographically last
    assert f(4, 24) == '4321'
