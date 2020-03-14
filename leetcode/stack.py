class BinarySearchTree:
    def __init__(self, root):
        if root:
            self.root = root
            self.left = BinarySearchTree(None)
            self.right = BinarySearchTree(None)

        else:
            self.root = None
            self.left = None
            self.right = None

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()


    def is_empty(self):
        return self.root is None

    def print_recursive(self, depth=0):
        if not self.root:
            return ""

        else:
            s = " "*depth
            s += str(self.root) + "\n"
            s += self.left.print_recursive(depth+1)
            s += self.right.print_recursive(depth+1)

            return s

    def __str__(self):
        return self.print_recursive(1)
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

class MinStack:
    def __init__(self):
        self._items =[]
        self._mins =[]

    def isEmpty(self):
        return self._items == []

    def push(self,item):
        self._items.append(item)
        if self._mins == []:
            self._mins.append(item)

        else:
            if item < self._mins[-1]:
                self._mins.append(item)

    def pop(self):
        if not self.isEmpty():
            if self._items.pop() == self._mins[-1]:
                self._mins.pop()

    def min(self):
        return self._mins[-1]

class SetOfStacks:
    def __init__(self, limit):
        self.set_of_stacks = []
        self.limit = limit

    def push(self, item):
        if self.set_of_stacks == []:
            self.set_of_stacks.append([item])

        else:
            if len(self.set_of_stacks[-1]) > self.limit:
                self.set_of_stacks.append([item])

            else:
                self.set_of_stacks[-1].append(item)

    def pop(self):
        if self.set_of_stacks != []:
            self.set_of_stacks[-1].pop()
            if self.set_of_stacks[-1] == []:
                self.set_of_stacks.pop()


class QueueWithStack:
    def __init__(self):
        self.original_stack = Stack()

    def queue(self, item):
        self.original_stack.push(item)

    def dequeue(self):
        temp_stack = Stack()
        while not self.original_stack.is_empty():
            temp_stack.push(self.original_stack.pop())

        while not temp_stack.is_empty():
            self.original_stack.push(temp_stack.pop())




def remove_adjacent_duplicates(string):
    s = Stack()

    for chars in string:
        if s.is_empty():
            s.push(chars)

        else:
            if s.peek() != chars:
                s.push(chars)

            else:
                s.pop()

    return "".join(s._items)

def baseball_game(arr):
    """Given a baseball game, record the point."""
    points = Stack()

    for items in arr:
        if items.isdigit():
            points.push(int(items))
        elif items == "+":
            last_round = points.pop()
            second_last_round = points.pop()
            points.push(second_last_round)
            points.push(last_round)
            points.push(last_round + second_last_round)

        elif items == "D":
            last_round = points.pop()
            points.push(last_round)
            points.push(last_round*2)

        else:
            points.pop()

    return sum(points._items)

def next_greater_element(nums1, nums2):
    """Given two arrays nums 1 and nums  where nums1 is a subset of nums2, find the
    next greater element of each element in nums 1 in nums2.

    o(N^2) solution."""

    nums2_dict = {}

    for x in range(len(nums2)):
        nums2_dict[nums2[x]] = x

    elements = []
    for x in range(len(nums1)):
        next_greater = -1

        for y in range(nums2_dict[nums1[x]], len(nums2)):
            if nums2[y]>nums1[x]:
                next_greater = nums2[y]
                break

        elements.append(next_greater)
    return elements


def next_greater_element_optimized(arr1, arr2):
    next_greater_dict = {}
    item_stack = Stack()

    for elements in arr2:
        if item_stack.is_empty():
            item_stack.push(elements)

        else:
            if elements > item_stack.peek():
                while not item_stack.is_empty():
                    next_greater_dict[item_stack.pop()] = elements

                item_stack.push(elements)

    return next_greater_dict


def backspace_string_comparison(str1, str2):
    """Given two strings, return True if they are the same when
    entered into text editor."""
    str1_stack = Stack()
    for elements in str1:
        if elements == "#":
            str1_stack.pop()
        else:
            str1_stack.push(elements)

    str2_stack = Stack()
    for elements in str2:
        if elements == "#":
            str2_stack.pop()

        else:
            str2_stack.push(elements)

    while not str1_stack.is_empty() and not str2_stack.is_empty():
        if str1_stack.pop() != str2_stack.pop():
            return False

    if not str1_stack.is_empty():
        return False

    elif not str2_stack.is_empty():
        return False

    else:
        return True

def minimum_add_to_make_parenthesis_valid(string):
    """
    return the minimum number of paranthesis required to make the string
    valid.
    """

    parenthesis_stack = Stack()
    elements_to_add = 0
    for chars in string:
        if chars == "(":
            parenthesis_stack.push("(")

        else:
            if parenthesis_stack.is_empty():
                elements_to_add += 1

            else:
                parenthesis_stack.pop()

    while not parenthesis_stack.is_empty():
        parenthesis_stack.pop()
        elements_to_add += 1

    return elements_to_add

def binary_tree_inorder_traversal(bst):
    """do a in order traversal of BST iteratively.
    """
    items = []
    node_stack = Stack()
    curr = bst

    while curr.root != None or not node_stack.is_empty():
        while curr.root:
            node_stack.push(curr)
            curr = curr.left

        curr = node_stack.pop()
        items.append(curr.root)
        curr = curr.right

    return items

def score_of_valid_parenthesis(parenthesis_str):
    score = 0
    cur_index = 0
    temp_stack = Stack()
    while cur_index < len(parenthesis_str)-1:
        if parenthesis_str[cur_index] == "(":
            beginning_bracket = cur_index
            if parenthesis_str[cur_index + 1] == ")":
                score += 1
                cur_index += 2

            else:
                temp_stack.push("(")
                cur_index += 1
                while not temp_stack.is_empty():
                    if parenthesis_str[cur_index] == ")":
                        temp_stack.pop()

                    else:
                        temp_stack.push("(")

                    cur_index += 1
                print(cur_index-1)
                score += 2*(score_of_valid_parenthesis(parenthesis_str[beginning_bracket:cur_index-1]))

    return score

def pushed_and_popped(pushed, popped):
    """given two seperate arrays, return true if they can be the result of push and pop operations."""

    temp_stack = Stack()
    popped_index = 0
    for items in pushed:
        temp_stack.push(items)

        while not temp_stack.is_empty() and temp_stack.peek() == popped[popped_index]:
            temp_stack.pop()
            popped_index += 1


    return popped_index == len(popped)


def k_adjacent_duplicate_removal(string,k):
    """remove k number of adjacent duplicates."""

    chars_stack = Stack()

    for chars in string:
        dups_counter = 1
        while not chars_stack.is_empty() and chars_stack.peek() == chars:
            chars_stack.pop()
            dups_counter += 1

        if dups_counter >= k:
            for x in range(dups_counter-k):
                chars_stack.push(chars)
        else:
            for x in range(dups_counter):
                chars_stack.push(chars)

        # print(chars_stack._items)

    return "".join(chars_stack._items)

if __name__ == "__main__":
    print(k_adjacent_duplicate_removal("pbbcggttciiippooaais",2))


