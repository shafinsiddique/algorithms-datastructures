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

l2 = LinkedList()
l2.append(1)
l2.append(1)
l2.append(1)
l2.append(1)
l2.append(4)
l1 = LinkedList()
node = Node(1)
node1 = Node(2)
node2 = Node(3)
node.next =node1
node1.next = node2
node2.next = node
l1._first = node
print(detectCycle(l1, 0))
