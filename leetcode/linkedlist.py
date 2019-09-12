from dataStructures.LinkedList import LinkedList, Node

def length(linky: LinkedList):
    curr = linky._first
    counter = 0

    while curr:
        counter += 1
        curr = curr.next

    return counter

def getMiddle(linky: LinkedList):
    """Return the middle node of the linked list."""

    middle = length(linky) // 2
    curr = linky._first
    for x in range(middle):
        curr = curr.next

    return curr.item

def reverse(linky: LinkedList):
    """Reverse Linkedlist."""

    if linky._first is None:
        return

    else:
        node = Node(linky._first.item)
        curr = linky._first.next

        while curr:
            newNode = Node(curr.item)
            newNode.next = node
            node = newNode
            curr = curr.next

        linky._first = node

def reverseRecursive(linky: LinkedList):
    reverseR(linky, linky._first)

def reverseR(linky, curr: Node):
    if curr is None:
        return

    elif curr.next is None:
        linky._first = curr

    else:
        reverseR(linky, curr.next)
        curr.next.next = curr
        curr.next = None

def deleteNode(linky: LinkedList, item):
    """Delete from linkedlist given item."""


    if (linky and linky._first.item == item):
        linky._first = linky._first.next

    else:
        curr = linky._first

        while curr.next and curr.next.item != item:
            curr = curr.next

        if not curr.next:
            raise ValueError

        else:
            curr.next = curr.next.next

def deleteIndex(linky: LinkedList, index):
    """Delete from linkedlist given index."""

    if linky._first is None:
        raise IndexError

    else:
        if index == 0:
            linky._first = linky._first.next

        else:
            counter = 0
            curr = linky._first

            while curr.next and counter < index - 1:
                curr = curr.next
                counter += 1

            if not curr.next:
                raise IndexError

            else:
                curr.next = curr.next.next

def delete(node: Node):
    """
    Delete a node from a linked list given only that node.

    """
    node.item = node.next.item
    node.next = node.next.next


def merge(l1: LinkedList, l2: LinkedList):
    """Merge two sorted linked lists."""
    curr = l1._first
    curr2 = l2._first
    merged = LinkedList()
    mergedCurr = merged._first
    while curr and curr2:
        if curr.item < curr2.item:
            n = Node(curr.item)
            curr = curr.next

        else:
            n = Node(curr2.item)
            curr2 = curr2.next

        if mergedCurr is None:
            merged._first = n
            mergedCurr = n

        else:
            mergedCurr.next = n
            mergedCurr = n


    if not curr:

        mergedCurr.next = curr2

    else:
        mergedCurr.next = curr

    return merged

def deleteDuplicates(linky: LinkedList):
    """Given a sorted linked lists, delete all duplicates such that each element appear
    only once."""

    curr = linky._first

    while curr and curr.next:
        if curr.item == curr.next.item:
            curr.next = curr.next.next
        else:
            curr = curr.next


def detectCycle(linky: LinkedList, pos):
    """Detect cycle in linkedlist."""
    if pos  < 0:
        return False

    else:
        curr = linky._first
        counter = 0
        detectCycle.node = None
        while curr:
            if counter == pos:
                detectCycle.node = curr

            if detectCycle.node and curr.next == detectCycle.node:
                return True

            curr = curr.next
            counter += 1


        return False

def isPalindrome(linky: LinkedList):
    """Return whether a given linked list is a palindrome.

    For O(1) space,

    get to the middle of the node.

    reverse the 2nd half of the linked list.

    check if first half equals second half."""


    linky2 = LinkedList()

    curr = linky._first

    while curr:
        node = Node(curr.item)
        node.next = linky2._first
        linky2._first = node
        curr = curr.next

    curr = linky._first
    curr2 = linky2._first

    while curr:
        if curr.item != curr2.item:
            return False

        curr = curr.next
        curr2 = curr2.next

    return True

def removeElements(linky: LinkedList, item):
    """Remove all elements from linked lists that have the val item.

    o(n) time, O(1) space."""

    curr = linky._first
    while curr.item == item:
        linky._first = curr.next
        curr = linky._first


    while curr.next:
        if curr.next.item == item:
            curr.next = curr.next.next

        else:
            curr = curr.next

def getIntersection(linky1: LinkedList, linky2: LinkedList):
    """Writew a program to find the node at whcih the intersection
    of two singly linked lists begin."""

    len1 = length(linky1)
    len2 = length(linky2)
    curr = linky1._first
    curr2 = linky2._first
    if len1 > len2:
        for x in range(len1-len2):
            curr = curr.next

    else:
        for x in range(len2 - len1):
            curr2 = curr2.next

    while curr and curr2:
        if curr == curr2:
            return curr.item

        curr = curr.next
        curr2 = curr2.next

    return None

def nextGreaterNode(linky: LinkedList):
    nums = []
    curr  = linky._first

    while curr:
        max = 0

        curr2 = curr.next

        while curr2:
            if curr2.item > max:
                max = curr2.item

            curr2 = curr2.next

        nums.append(max)

        curr = curr.next

    return nums

def nextGNode(linky: LinkedList):
    """
    list of next greater integer for each element.
    """
    stack = []
    curr = linky._first
    values = {}
    results = []
    while curr:
        item = curr.item

        if not stack or stack[-1] > item:
            stack.append(item)
            values[item] = 0
            curr = curr.next


        else:
            values[stack.pop()] = item

    curr2 = linky._first

    while curr2:
        results.append(values[curr2.item])
        curr2 = curr2.next

    return results

def components(linky: LinkedList, G: list):
    """Return the number of connected components in G,
    where two values are connected if they appear consecutively in the linked list.
"""

    gDict = {}

    for items in G:
        gDict[items] = None

    counter = 0
    curr = linky._first

    while curr.next:
        if curr.item in gDict and curr.next.item in gDict:
            counter += 1




        curr = curr.next

    return counter

l1 = LinkedList()
l2 = LinkedList()

l1.append(0)
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(3)

g = [0,3,1,4]

print(components(l1, g))