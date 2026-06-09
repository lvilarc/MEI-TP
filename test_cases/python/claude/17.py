def run_tests(solution_module):
    f = solution_module.minCut
    # single char — already palindrome
    assert f('a') == 0
    # already a palindrome
    assert f('aba') == 0
    # two different chars
    assert f('ab') == 1
    # classic example
    assert f('aab') == 1
    # all same chars — zero cuts
    assert f('aaaa') == 0
