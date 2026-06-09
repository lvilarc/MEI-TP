def _to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def _make(vals, node_cls):
    dummy = node_cls()
    cur = dummy
    for v in vals:
        cur.next = node_cls(v)
        cur = cur.next
    return dummy.next

def run_tests(solution_module):
    f = solution_module.mergeKLists
    N = solution_module.ListNode
    # single list passthrough
    assert _to_list(f([_make([1, 2, 3], N)])) == [1, 2, 3]
    # two lists with negative values
    assert _to_list(f([_make([-2, -1], N), _make([-3, 0], N)])) == [-3, -2, -1, 0]
    # lists with duplicates
    assert _to_list(f([_make([1, 1], N), _make([1, 1], N)])) == [1, 1, 1, 1]
    # empty list inside k lists
    assert _to_list(f([None, _make([5], N)])) == [5]
    # k=0
    assert _to_list(f([])) == []
