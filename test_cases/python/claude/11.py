def run_tests(solution_module):
    f = solution_module.minWindow
    # t is single char repeated — needs both
    assert f('aab', 'ab') == 'ab'
    # no valid window
    assert f('abc', 'd') == ''
    # t longer than s
    assert f('a', 'aa') == ''
    # entire string is minimum window
    assert f('bca', 'abc') == 'bca'
    # window shrinks from wider match
    assert f('acbbaca', 'aba') == 'baca'
