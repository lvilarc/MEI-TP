def _make(values, node_cls):
    dummy = node_cls()
    cur = dummy
    for value in values:
        cur.next = node_cls(value)
        cur = cur.next
    return dummy.next

def _list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

def run_tests(solution_module):
    f = solution_module.mergeKLists
    N = solution_module.ListNode
    assert _list(f([_make([1, 4, 5], N), _make([1, 3, 4], N), _make([2, 6], N)])) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert _list(f([])) == []
    assert _list(f([None])) == []
    assert _list(f([_make([-3, -1], N), _make([-2, 0, 2], N)])) == [-3, -2, -1, 0, 2]
    assert _list(f([_make([1], N), _make([0], N), _make([2], N)])) == [0, 1, 2]
