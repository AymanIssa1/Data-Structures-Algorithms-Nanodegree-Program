class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.block
            node = node.next

    def __repr__(self):
        return str([v for v in self])


def reverse(linked_list):
    new_list = LinkedList()
    prev_node = None

    current_node = linked_list.head
    while current_node:
        new_node = Node(current_node.block)
        new_node.next = prev_node
        prev_node = new_node

    new_list.head = prev_node

    return new_list


def iscircular(linked_list):
    if linked_list.head is None:
        return False

    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if slow_runner == fast_runner:
            return True

    return False
