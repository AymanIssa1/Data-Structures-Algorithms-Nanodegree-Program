class Node:
    """LinkedListNode class to be used for this problem"""

    def __init__(self, data):
        self.data = data
        self.next = None


"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""


def swap_nodes(head, left_index, right_index):
    one_previous = head
    one_current = head

    two_previous = head
    two_current = head

    current = head

    i = 0
    while current:
        if i < left_index:
            one_previous = current
            one_current = current.next

        if i < right_index:
            two_previous = current
            two_current = current.next

        current = current.next
        i += 1

    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    one_previous.next = two_current

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
    print()


print_linked_list(swap_nodes(create_linked_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 3, 7))
