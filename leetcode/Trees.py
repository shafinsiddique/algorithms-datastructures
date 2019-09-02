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


bst = BST.BinarySearchTree(7)
left = BST.BinarySearchTree(3)
left._left = BST.BinarySearchTree(2)
left._right = BST.BinarySearchTree(5)
right = BST.BinarySearchTree(11)
right._left = BST.BinarySearchTree(9)
right._right = BST.BinarySearchTree(13)
bst._left = left
bst._right = right
print(bst)
print(rangeSumofBST(bst, 3, 7))