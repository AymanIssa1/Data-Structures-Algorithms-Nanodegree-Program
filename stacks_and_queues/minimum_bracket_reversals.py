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


def minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    for brackets in input_string:
        if stack.is_empty():
            stack.push(brackets)
        else:
            top = stack.top()
            if top != brackets:
                if top == '{':
                    stack.pop()
                    continue
            stack.push(brackets)

    ls = list()
    count = 0
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        ls.append(first)
        ls.append(second)
        if first == '}' and second == '}':
            count += 1
        elif first == '{' and second == '}':
            count += 2
        elif first == '{' and second == '{':
            count += 1

    return count


def minimum_bracket_reversals2(input_string):
    opening_bracket_count = 0
    closing_bracket_count = 0
    for bracket in input_string:
        if bracket == '{':
            opening_bracket_count += 1
        else:
            closing_bracket_count += 1

    return int(abs(opening_bracket_count - closing_bracket_count) / 2)


print(minimum_bracket_reversals('}}}}'))
print(minimum_bracket_reversals2('}}}}'))

print(minimum_bracket_reversals('}{}}'))
print(minimum_bracket_reversals2('}{}}'))
