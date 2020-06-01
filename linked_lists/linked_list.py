class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)


def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.block)
        current_node = current_node.next


print_linked_list(head)


def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)

    return head


def create_linked_list_better(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next

    return head


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = Node
        self.previous = Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
