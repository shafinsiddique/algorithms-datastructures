import math
from stack import Stack


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, item):
        new_node = Node(item)
        if self.first is None:
            self.first = new_node

        else:
            new_node.next = self.first
            self.first = new_node

    def append(self, item):
        new_node = Node(item)
        if self.first is None:
            self.first = new_node

        else:
            curr = self.first

            while curr.next is not None:
                curr = curr.next

            curr.next = new_node

    def __str__(self):
        curr = self.first
        output = ""
        while curr:
            output += str(curr.item) + " "
            curr = curr.next

        return output

    def remove_by_index(self, index):
        curr = self.first
        counter = 0

        if index == 0:
            if curr:
                self.first = self.first.next

            else:
                raise IndexError
        else:
            while curr.next and counter < index-1:
                curr = curr.next
                counter += 1

            if not curr.next:
                raise IndexError

            else:
                curr.next = curr.next.next

    def __contains__(self, item):
        curr = self.first

        while curr:
            if curr.item == item:
                return True

        return False

    def remove_duplicates(self):
        items = set()
        curr = self.first
        while curr and curr.next:
            items.add(curr.item)
            if curr.next.item in items:
                curr.next = curr.next.next

            curr = curr.next

    def __len__(self):
        counter = 0
        curr = self.first

        while curr:
            counter += 1
            curr = curr.next

        return counter

    def middle_element(self):
        mid_point = len(self)//2
        curr = self.first
        for x in range(mid_point):
            curr = curr.next

        return curr.item

    def reverse(self):
        l = LinkedList()
        curr = self.first

        while curr:
            l.add(curr.item)
            curr = curr.next

        self.first = l.first

    def reverse2(self):
        node = None

        curr = self.first

        while curr:
            new_node = Node(curr.item)
            if node:
                new_node.next = node
                node = new_node

            else:
                node = new_node
            curr = curr.next
        self.first = node

    def reverse_recursive(self):
        reverse_rec(self, self.first, None)

    def delete_item(self, item):
        if self.first:
            if item == self.first.item:
                self.first = self.first.next

            else:
                curr = self.first

                while curr.next and curr.next.item != item:
                    curr = curr.next

                if curr.next:
                    curr.next = curr.next.next

def reverse_rec(linky, node, reversed_node):
    if node:
        new_node = Node(node.item)
        if reversed_node:
            new_node.next = reversed_node

        reverse_rec(linky, node.next, new_node)

    else:
        linky.first = reversed_node



def merge(linky1, linky2):
    """Merge 2 sorted linked lists"""
    merged_list = LinkedList()
    curr1 = linky1.first
    curr2 = linky2.first
    while curr1 and curr2:
        if curr1.item  <= curr2.item:
            merged_list.append(curr1.item)
            curr1 = curr1.next

        else:
            merged_list.append(curr2.item)
            curr2 = curr2.next

    lastNode = merged_list.first
    while lastNode.next:
        lastNode = lastNode.next

    if curr1:
        lastNode.next = curr1

    else:
        lastNode.next = curr2

    return merged_list

def merge_n(linky1,linky2):
    merged = LinkedList()
    curr1 = linky1.first
    curr2 = linky2.first

    while curr1 and curr2:
        if curr1.item <= curr2.item:
            merged.add(curr1.item)
            curr1 = curr1.next

        else:
            merged.add(curr2.item)
            curr2 = curr2.next

    if curr1:
        while curr1:
            merged.add(curr1.item)
            curr1 = curr1.next


    else:
        while curr2:
            merged.add(curr2.item)
            curr2 = curr2.next

    merged.reverse()

    return merged

def convert_binary_to_decimal(linky: LinkedList):
    starting = len(linky)-1
    curr = linky.first
    decimal = 0
    while curr:
        decimal += curr.item * math.pow(2, starting)
        starting -= 1
        curr = curr.next

    return decimal

def has_cycle(linky):
    """Given a linked list, determine if it has a cycle in it."""

    nodes = set()
    curr = linky.first

    while curr:
        if id(curr) in nodes:
            return True

        nodes.add(id(curr))
        curr = curr.next

    return False

def intersection_node(linky1,linky2):
    """Find the intersection node between the two linked lists."""

    curr = linky1.first
    nodes = set()
    while curr:
        nodes.add(id(curr))
        curr = curr.next

    curr2 = linky2.first
    while curr2:
        if id(curr2) in nodes:
            return curr2

    return -1


def is_palindrome(linky):
    '''Given a singly linked list, determine if it is a palindrome.
    '''

    string_rep = ""
    curr = linky.first

    while curr:
        string_rep += str(curr.item)
        curr = curr.next

    for x in range(len(string_rep)//2):
        if string_rep[x]!= string_rep[-1-x]:
            return False

    return True

def remove_elements(linky, val):
    '''remove all elements from the linky with the val = val'''

    curr = linky.first

    while curr and curr.next:
        if curr.next.item == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    if linky.first:
        if linky.first.item == val:
            linky.first = linky.first.next


def sum_of_two_nums(linky, linky2):
    '''given two non empty linkys, sum up the two linkys and return the sum
    in a new linked list.'''
    curr = linky.first
    curr2 = linky2.first
    num1 = ""
    while curr:
        num1 += str(curr.item)
        curr = curr.next
    num1 = int(num1[::-1])
    num2 = ''
    while curr2:
        num2 += str(curr2.item)
        curr2 = curr2.next

    num2 = int(num2[::-1])

    sum_of_numbers = str(num1 + num2)

    sum_list = LinkedList()
    for nums in sum_of_numbers:
        sum_list.add(nums)

    return sum_list


def next_greater_node_in_linked_list(linky):
    '''given a linked list of nodes, return an array of integers for the next
    greater node.'''

    greater_stack = Stack()
    counter = 0
    curr = linky.first
    index_with_next_greater_dict = {}
    while curr:
        while not greater_stack.is_empty() and curr.item > greater_stack.peek()[1]:
            index_being_popped = greater_stack.pop()[0]
            index_with_next_greater_dict[index_being_popped] = curr.item

        greater_stack.push([counter, curr.item])
        counter += 1
        curr = curr.next

    output_list = []
    for x in range(counter):
        if x in index_with_next_greater_dict:
            output_list.append(index_with_next_greater_dict[x])

        else:
            output_list.append(0)

    return output_list


def odd_even_linked_list(linky):
    '''given a linked list, group all the odd elements together followed
    by the even elements.'''

    fast_node = linky.first.next
    slow_node = linky.first

    while fast_node and fast_node.next:
        temp = fast_node.next
        fast_node.next = fast_node.next.next
        temp.next = slow_node.next
        slow_node.next = temp

        fast_node  = fast_node.next
        slow_node = slow_node.next

def next_greater(linky):
    """given a linked list, for each node, get the next greater node. """

    curr = linky.first
    greater_stack = Stack()
    index_dict = {}
    curr_index = 0
    while curr:
        while not greater_stack.is_empty() and curr.item > greater_stack.peek()[1]:
            item = greater_stack.pop()
            index_dict[item[0]] = curr.item

        greater_stack.push((curr_index, curr.item))

        curr = curr.next
        curr_index += 1

    output_list = []

    for x in range(curr_index):
        if x in index_dict:
            output_list.append(index_dict[x])

        else:
            output_list.append(0)

    return output_list

def add_two_linked_lists(linky1, linky2):
    '''add the values in two linked lists
     and return the sum linked list.'''

    stack1 = Stack()
    curr = linky1.first
    counter1 = 0

    while curr:
        stack1.push(curr.item)
        curr = curr.next
        counter1 += 1

    curr2 = linky2.first
    stack2 = Stack()
    counter2 = 0
    while curr2:
        stack2.push(curr2.item)
        curr2 = curr2.next
        counter2 += 1

    if counter1 > counter2:
        bigger_stack = stack1
        smaller_stack = stack2

    else:
        bigger_stack = stack2
        smaller_stack = stack1

    carried = 0
    sum_list = LinkedList()
    while not smaller_stack.is_empty():
        number = bigger_stack.pop() + smaller_stack.pop() + carried

        if number > 10:
            carried = 1
            sum_list.add(number % 10)

        else:
            carried = 0
            sum_list.add(number)

    while not bigger_stack.is_empty():
        number = bigger_stack.pop() + carried

        if number > 10:
            carried = 1
            sum_list.add(number % 10)

        else:
            carried = 0
            sum_list.add(number)

    return sum_list


def osmosis(linky):
    head_node = None
    tail_node = None

    curr = linky.first

    while curr:
        if not head_node:
            head_node = Node(curr.item)
            tail_node = head_node

        else:
            if curr.item == tail_node.item:
                tail_node.item = tail_node.item*2

            else:
                tail_node.next = Node(curr.item)
                tail_node = tail_node.next

        curr = curr.next

    linky.first = head_node




if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(1)
    l.append(2)
    l.append(2)
    l.append(3)
    l.append(4)
    osmosis(l)
    print(l)

