def run_tests(solution_module):
    f = solution_module.findSubstring
    assert f('barfoothefoobarman', ['foo', 'bar']) == [0, 9]
    assert f('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']) == []
    assert f('barfoofoobarthefoobarman', ['bar', 'foo', 'the']) == [6, 9, 12]
    assert f('', ['a']) == []
    assert f('aaaaaaaaaaaa', ['aa', 'aa', 'aa']) == [0, 1, 2, 3, 4, 5, 6]
