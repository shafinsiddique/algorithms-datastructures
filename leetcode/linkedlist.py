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


l = LinkedList()
l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.add(50)
l.add(60)
print(l)
reverse(l)
reverseRecursive(l)
print(l)