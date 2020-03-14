from linked_list import LinkedList
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self, item):
        self.items.pop(0)

    def is_empty(self):
        return self.items == []

