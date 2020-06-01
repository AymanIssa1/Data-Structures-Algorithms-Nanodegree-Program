class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def reverse_stack(stack):
    reverse_stack = Stack()

    while not stack.is_empty():
        reverse_stack.push(stack.pop)

    return reverse_stack


def reverse_stack2(stack):
    holder_stack = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)
    _reverse_stack_recursion(stack, holder_stack)


def _reverse_stack_recursion(stack, holder_stack):
    if holder_stack.is_empty():
        print("Empty")
        return
    popped_element = holder_stack.pop()
    print("just popped " + str(popped_element))
    _reverse_stack_recursion(stack, holder_stack)
    print("just pushing " + str(popped_element))
    stack.push(popped_element)


def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack2(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)
