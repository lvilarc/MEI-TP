def run_tests(solution_module):
    f = solution_module.isMatch
    # multiple ? chars
    assert f('abc', '???') is True
    # star at the end consumes remainder
    assert f('abcdef', 'abc*') is True
    # consecutive stars behave like one
    assert f('abc', '***') is True
    # empty string, empty pattern
    assert f('', '') is True
    # star cannot match if pattern requires more
    assert f('ab', 'a*c') is False
