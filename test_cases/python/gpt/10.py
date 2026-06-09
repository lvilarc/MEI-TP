def run_tests(solution_module):
    f = solution_module.fullJustify
    assert f(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16) == ['This    is    an', 'example  of text', 'justification.  ']
    assert f(['What', 'must', 'be', 'acknowledgment', 'shall', 'be'], 16) == ['What   must   be', 'acknowledgment  ', 'shall be        ']
    assert f(['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'], 20)[0] == 'Science  is  what we'
    assert f(['a'], 1) == ['a']
    assert f(['longword'], 8) == ['longword']
