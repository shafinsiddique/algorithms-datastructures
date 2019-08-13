class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self._first = None

    def add(self, item):
        n = Node(item)
        n.next = self._first
        self._first = n


    def __str__(self):
        curr = self._first
        s = ""

        while curr is not None:
            s += str(curr.item) + " "

            curr = curr.next

        return s

    def append(self, item):
        n = Node(item)

        curr = self._first

        if curr is None:
            self._first = n

        else:
            while curr.next is not None:
                curr = curr.next

            curr.next = n

    def popFirst(self):
        if self._first is None:
            raise IndexError
        else:
            self._first = self._first.next

l = LinkedList()
l.add(2)
l.add(3)
l.add(4)
l.append(7)
l.append(8)
l.popFirst()
print(l)

