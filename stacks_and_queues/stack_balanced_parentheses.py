# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def equation_checker(equation):
    stack = Stack()

    for char in equation:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() != '(':
                return False

    return stack.size() == 0

print(equation_checker("((32+8)∗(5/2))/(2+6))"))