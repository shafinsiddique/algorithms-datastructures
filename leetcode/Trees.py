from dataStructures.BST import BinarySearchTree
from dataStructures import tree

def rangeSumofBST(binarySearchTree: BinarySearchTree, start, end):
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

def merge(bst1: BinarySearchTree, bst2: BinarySearchTree):
    """Merge two binary trees."""

    if bst1.isEmpty() and bst2.isEmpty():
        return BinarySearchTree(None)

    elif bst1.isEmpty():
        return bst2

    elif bst2.isEmpty():
        return bst1

    else:
        newTree = BinarySearchTree(bst1._root + bst2._root)

        newTree._left = merge(bst1._left, bst2._left)

        newTree._right = merge(bst1._right, bst2._right)

        return newTree

def search(bst:BinarySearchTree, item):
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

def preOrderTraversal(tree: BinarySearchTree):
    if tree.isEmpty():
        return []

    else:
        values = [tree._root]
        values.extend(preOrderTraversal(tree._left))
        values.extend(preOrderTraversal(tree._right))

        return values

def unvaluedBinaryTree(tree: BinarySearchTree):
    """A binary tree is unvalued if all its values are equal. Return if
    a given tree is an unvalued binary tree."""
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

def maximumDepth(tree: tree.Tree):
    """Find the height of the tree."""

    if tree.isEmpty():
        return 0

    else:
        heights = []

        for subtrees in tree._subtrees:
            heights.append(subtrees.height() + 1)

        return max(heights)



def getAllValuesFromBST(bst: BinarySearchTree):
    """Return all values of the bst in sorted order"""

    if bst.isEmpty():
        return []

    else:
        values = []

        values.extend(getAllValuesFromBST(bst._left))
        values.append(bst._root)
        values.extend(getAllValuesFromBST(bst._right))

        return values
def increasingOrderSearchTree(bst: BinarySearchTree):
    """Rearrange it in order so that each tree has no left subtree and only one right subtree."""

    values = getAllValuesFromBST(bst)
    newTree = BinarySearchTree(0)
    newTreeAlias = newTree

    for value in values:
        t = BinarySearchTree(value)
        newTreeAlias._right = t
        newTreeAlias = t

    return newTree._right

def getLeafs(bst: BinarySearchTree):
    if bst.isEmpty():
        return []

    elif bst.isSizeOne():
        return [bst._root]

    else:
        leaves = []

        leaves.extend(getLeafs(bst._left))
        leaves.extend(getLeafs(bst._right))

        return leaves
def leafValueSequence(bst: BinarySearchTree, bst1: BinarySearchTree):
    """Return if the leaf value lists of two binary search trees are the same."""

    return getLeafs(bst) == getLeafs(bst1)

def getValuesInRange(bst: BinarySearchTree, start, end ):
    if bst.isEmpty():
        return []

    else:
        values = []

        if not start <= bst._root <= end:
            values.extend(getValuesInRange(bst._right, start, end))
        else:
            values.append(bst._root)

            values.extend(getValuesInRange(bst._left, start, end))
            values.extend(getValuesInRange(bst._right, start, end))

        return values
def trim_bst(bst: BinarySearchTree, start, end):
    values = getValuesInRange(bst, start, end)
    newTree = BinarySearchTree(values.pop(0))
    for value in values:
        newTree.insert(value)

    bst._root = newTree._root
    bst._left = newTree._left
    bst._right = newTree._right

def helper(bst: BinarySearchTree, start, end):
    if not bst._root:
        return BinarySearchTree(None)

    if bst._root > end:
        return helper(bst._left, start, end)

    elif bst._root < start:
        return helper(bst._right, start, end)

    else:
        bst._left = helper(bst._left, start, end)
        bst._right = helper(bst._right, start, end)

        return bst

def trim_bst2(bst: BinarySearchTree, start, end):
    return helper(bst, start, end)


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
print(trim_bst2(bst, 5,7))

