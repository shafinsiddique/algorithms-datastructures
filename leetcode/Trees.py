from dataStructures import BST
from dataStructures import tree

def rangeSumofBST(binarySearchTree: BST.BinarySearchTree, start, end):
    """LeetCode Question ID #938."""

    if binarySearchTree.isEmpty():
        return 0

    else:
        s = 0

        if start <= binarySearchTree._root <= end:
            s += binarySearchTree._root
            s += rangeSumofBST(binarySearchTree._left, start, end)
            s += rangeSumofBST(binarySearchTree._right, start, end)
        else:
            s += rangeSumofBST(binarySearchTree._right, start, end)

        return s

def merge(bst1: BST.BinarySearchTree, bst2: BST.BinarySearchTree):
    """Merge two binary trees."""

    if bst1.isEmpty() and bst2.isEmpty():
        return BST.BinarySearchTree(None)

    elif bst1.isEmpty():
        return bst2

    elif bst2.isEmpty():
        return bst1

    else:
        newTree = BST.BinarySearchTree(bst1._root + bst2._root)

        newTree._left = merge(bst1._left, bst2._left)

        newTree._right = merge(bst1._right, bst2._right)

        return newTree

def search(bst: BST.BinarySearchTree, item):
    """Search in a Binary Search Tree."""

    if bst.isEmpty():
        return

    else:
        if item < bst._root:
            return search(bst._left, item)

        elif item == bst._root:
            return bst

        else:
            return search(bst._right, item)

def preOrderTraversal(tree: BST.BinarySearchTree):
    if tree.isEmpty():
        return []

    else:
        values = [tree._root]
        values.extend(preOrderTraversal(tree._left))
        values.extend(preOrderTraversal(tree._right))

        return values

def unvaluedBinaryTree(tree: BST.BinarySearchTree):
    if tree.isEmpty() or tree.isSizeOne():
        return True

    elif tree._left.isEmpty():
        return tree._root == tree._right._root

    elif tree._right.isEmpty():
        return tree._root == tree._left._root

    else:
        if tree._root != tree._left._root or tree._root != tree._right._root:
            return False

        if not unvaluedBinaryTree(tree._left) or not unvaluedBinaryTree(tree._right):
            return False

        return True






bst1 = BST.BinarySearchTree(1)
left = BST.BinarySearchTree(1)
left._left = BST.BinarySearchTree(1)
right = BST.BinarySearchTree(1)

bst1._left = left
bst1._right = right

bst2 = BST.BinarySearchTree(1)
left1 = BST.BinarySearchTree(1)
left1._right = BST.BinarySearchTree(1)
right1 = BST.BinarySearchTree(1)
right1._right = BST.BinarySearchTree(1)
bst2._left = left1
bst2._right = right1

bt = merge(bst1, bst2)
print(bt)
print(unvaluedBinaryTree(bst2))
