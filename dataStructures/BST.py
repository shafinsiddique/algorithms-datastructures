class BinarySearchTree:
    def __init__(self, root):
        if root is None:
            self._root = None
            self._left = None
            self._right = None

        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def __str__(self):
        return self.print()

    def print(self, depth=0):
        if self.isEmpty():
            return ""

        else:
            s = depth*" " + str(self._root) + "\n"

            s += self._left.print(depth+1)

            s += self._right.print(depth + 1)

            return s

    def isEmpty(self):
        return self._root is None

    def isSizeOne(self):
        return self._left.isEmpty() and self._right.isEmpty()

    def __contains__(self, item):
        if self.isEmpty():
            return False

        else:
            if item < self._root:
                return item in self._left

            elif item == self._root:
                return True

            else:
                return item in self._right

    def maximum(self):
        """Return the maximum number in this BST."""

        if self.isEmpty():
            return 0

        elif self.isSizeOne():
            return self._root

        else:
            return self._right.maximum()

    def count(self, item):
        """Return the total count of the 'item' in the tree."""

        if self.isEmpty():
            return 0

        else:
            counter = 0

            if item < self._root:
                counter += self._left.count(item)

            elif item == self._root:
                counter += 1
                counter += self._left.count(item)
                counter += self._right.count(item)

            else:
                counter += self._right.count(item)

            return counter

    def items(self):
        """Return all of the items in the BST in sorted order."""

        if self.isEmpty():
            return []


        else:
            values = []
            values.extend(self._left.items())
            values.append(self._root)
            values.extend(self._right.items())

            return values

    def smaller(self, item):
        """Return all of the items in the BST that are strictly smaller than item"""

        if self.isEmpty():
            return []

        else:
            values = []
            values.extend(self._left.smaller(item))

            if self._root < item:
                values.append(self._root)

            values.extend(self._right.smaller(item))

        return values

    def extractMax(self):
        if self._right.isEmpty():
            temp = self._root
            self.deleteRoot()
            return temp

        else:
            return self._right.extractMax()


    def deleteRoot(self):
        if self.isEmpty():
            return

        elif self._left.isEmpty():
            self._root, self._left, self._right = self._right._root, self._right._left, \
                                                  self._right._right

        elif self._right.isEmpty():
            self._root, self._left, self._right = self._left._root, self._left._left, \
                                                  self._left._right


        else:
            self._root = self._left.extractMax()

    def height(self):
        """Return the height of the tree."""

        if self.isEmpty():
            return 0

        elif self.isSizeOne():
            return 1

        else:
            leftHeight = self._left.height() + 1
            rightHeight = self._right.height() + 1

            return max([leftHeight, rightHeight])

    def insert(self, item):
        """Insert the given item to the BST while maintaining BST property."""

        if self.isEmpty():
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

        else:
            if item < self._root:
                return self._left.insert(item)

            else:
                return self._right.insert(item)

    def itemsInRange(self, start, end):
        if self.isEmpty():
            return []

        else:
            values = []
            values.extend(self._left.itemsInRange(start, end))
            if start <= self._root <= end:
                values.append(self._root)

            values.extend(self._right.itemsInRange(start, end))

            return values

    def rotate_right(self):
        rightBST = BinarySearchTree(self._root)
        rightBST._left = self._left._right
        rightBST._right = self._right

        leftBst = self._left._left


        self._root, self._left, self._right = self._left._root, leftBst, rightBST

    def preOrderTraversal(self):
        if self.isEmpty():
            return
        print(self._root)
        self._left.preOrderTraversal()
        self._right.preOrderTraversal()

    def inOrderTraversal(self):
        if self.isEmpty():
            return

        else:
            self._left.inOrderTraversal()
            print(self._root)
            self._right.inOrderTraversal()


bst = BinarySearchTree(7)
left = BinarySearchTree(3)
left._left = BinarySearchTree(2)
left._right = BinarySearchTree(5)
right = BinarySearchTree(11)
right._left = BinarySearchTree(9)
right._right = BinarySearchTree(13)
bst._left = left
bst._right = right
print(bst)
bst.rotate_right()
bst.preOrderTraversal()
print()
bst.inOrderTraversal()