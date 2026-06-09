class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Empty list starts with no head

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        """String representation: 1 -> 2 -> 3 -> None"""
        nodes, current = [], self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        nodes.append("None")
        return " -> ".join(nodes)

def reverse_iterative(self):
    prev, curr = None, self.head
    while curr:
        next_node   = curr.next   # Save next node
        curr.next   = prev        # Reverse the link
        prev        = curr        # Advance prev
        curr        = next_node   # Advance curr
    self.head = prev              # New head is the old tail
    
ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)

print("Original:  ", ll)          # 1 -> 2 -> 3 -> 4 -> 5 -> None

ll.reverse_iterative()
print("Reversed:  ", ll)          # 5 -> 4 -> 3 -> 2 -> 1 -> None