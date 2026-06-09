class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    values = []
    for node in lists:
        while node:
            values.append(node.val)
            node = node.next
    dummy = ListNode()
    cur = dummy
    for value in sorted(values):
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next
