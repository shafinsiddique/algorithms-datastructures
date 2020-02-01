class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

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

def valid_parentheses(string):
    s = Stack()
    format = {")":"(","}":'{',']':'['}
    for elements in string:
        if elements == "(" or elements == "{" or elements == "[":
            s.push(elements)

        else:
            if s.is_empty():
                return False

            if s.pop() != format[elements]:
                return False

    if s.is_empty():
        return True

    return False

def adjacentDuplicates(string):
    s = Stack()
    for elements in string:
        if s.is_empty():
            s.push(elements)

        elif s.peek() == elements:
            s.pop()

        else:
            s.push(elements)

    return ''.join(s._items)

print(adjacentDuplicates("ooo1aa"))


