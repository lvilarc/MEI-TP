def run_tests(solution_module):
    f = solution_module.wordBreak
    assert sorted(f('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog'])) == sorted(['cats and dog', 'cat sand dog'])
    assert sorted(f('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple'])) == sorted(['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple'])
    assert f('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) == []
    assert f('', ['a']) == ['']
    assert sorted(f('aaaa', ['a', 'aa'])) == sorted(['a a a a', 'aa a a', 'a aa a', 'a a aa', 'aa aa'])
