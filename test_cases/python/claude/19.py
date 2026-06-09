def run_tests(solution_module):
    f = solution_module.wordBreak
    # no solution
    assert f('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) == []
    # word reuse with multiple splits
    assert sorted(f('aaaa', ['a', 'aa'])) == sorted(['a a a a', 'a a aa', 'a aa a', 'aa a a', 'aa aa'])
    # classic example
    assert sorted(f('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog'])) == sorted(['cat sand dog', 'cats and dog'])
    # word reuse
    assert sorted(f('aaa', ['a', 'aa'])) == sorted(['a a a', 'a aa', 'aa a'])
    # single char word
    assert f('a', ['a']) == ['a']
