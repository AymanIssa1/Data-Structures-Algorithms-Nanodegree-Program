# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skip_i_delete_j(head, i, j):
    if i == 0:
        return None

    if j == 0:
        return head

    if head is None or j < 0 or i < 0:
        return head

    current = head
    previous = None

    while current:
        # skip (i - 1) nodes
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next

        previous = current
        current = current.next

        # delete next j nodes
        for _ in range(j):
            if current is None:
                break
            current = current.next

        # connect the previous.next to current
        previous.next = current

    return head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data)
        head = head.next


print_linked_list(skip_i_delete_j(create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 2, 3))
