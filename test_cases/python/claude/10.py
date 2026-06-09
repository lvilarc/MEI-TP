def run_tests(solution_module):
    f = solution_module.fullJustify
    # single word line — left justified
    assert f(['hello'], 5) == ['hello']
    # last line is left-justified
    result = f(['a', 'b', 'c'], 5)
    assert result[-1] == 'a b c'
    # two words, last line — left justified with trailing space
    assert f(['ab', 'cd'], 6) == ['ab cd ']
    # three words fit in one line
    assert f(['x', 'y', 'z'], 5) == ['x y z']
    # exact fit — no padding needed
    assert f(['abc'], 3) == ['abc']
