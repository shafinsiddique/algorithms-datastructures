class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

def binary_operation(operation: str):
    """precondition: <operation> is valid."""
    operators = Stack()
    items = Stack()

    for elements in operation:
        if elements == "(":
            pass

        elif elements == "*" or elements == "-" or elements == "/" or elements == "+":
            operators.push(elements)

        elif elements == ")":
            curr_operation = operators.pop()
            first_element = items.pop()
            second_element = items.pop()

            if (curr_operation == "*"):
                new_element = first_element * second_element

            elif curr_operation == "+":
                new_element = first_element + second_element

            elif curr_operation == "-":
                new_element = second_element / first_element

            else:
                new_element = second_element - first_element

            items.push(new_element)
        else:
            items.push(int(elements))

    return items.pop()

print(binary_operation("((2*4)*2)"))




