def run_tests(solution_module):
    f = solution_module.getPermutation
    assert f(3, 3) == '213'
    assert f(4, 9) == '2314'
    assert f(3, 1) == '123'
    assert f(1, 1) == '1'
    assert f(5, 120) == '54321'
