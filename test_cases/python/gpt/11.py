def run_tests(solution_module):
    f = solution_module.minWindow
    assert f('ADOBECODEBANC', 'ABC') == 'BANC'
    assert f('a', 'a') == 'a'
    assert f('a', 'aa') == ''
    assert f('aa', 'aa') == 'aa'
    assert f('ab', 'b') == 'b'
