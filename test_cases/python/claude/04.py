def run_tests(solution_module):
    f = solution_module.findSubstring
    # example from problem statement
    assert sorted(f('barfoothefoobarman', ['foo', 'bar'])) == [0, 9]
    # single word
    assert sorted(f('aaaa', ['aa'])) == [0, 1, 2]
    # no match at all
    assert f('xyz', ['abc']) == []
    # word longer than remaining string
    assert f('ab', ['ab', 'ab']) == []
    # words cover entire string exactly
    assert sorted(f('abcabc', ['abc', 'abc'])) == [0]
