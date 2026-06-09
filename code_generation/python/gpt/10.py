from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional, Iterable


@dataclass
class Node:
    value: Any
    next: Optional["Node"] = None


class LinkedList:
    def __init__(self, values: Iterable[Any] = ()) -> None:
        self.head: Optional[Node] = None

        for value in values:
            self.append(value)

    def append(self, value: Any) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def reverse(self) -> None:
        previous: Optional[Node] = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def to_list(self) -> list[Any]:
        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def __repr__(self) -> str:
        return " -> ".join(map(str, self.to_list())) or "Empty"


# Example usage
linked_list = LinkedList([1, 2, 3, 4, 5])

print(linked_list)
# 1 -> 2 -> 3 -> 4 -> 5

linked_list.reverse()

print(linked_list)
# 5 -> 4 -> 3 -> 2 -> 1