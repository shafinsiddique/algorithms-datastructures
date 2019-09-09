from dataStructures.BST import BinarySearchTree
from dataStructures.tree import Tree

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

def maximumDepth(tree: Tree):
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

def levelOrderTraversal(tree: Tree):
    """breadth first search is a Queue."""
    toVisit = [[tree]]
    roots = [[tree._root]]
    while toVisit:
        listOfTrees = toVisit.pop(0)
        newList = []
        newRoots = []
        for trees in listOfTrees:
            newList.extend(trees._subtrees)
            for subtrees in trees._subtrees:
                newRoots.append(subtrees._root)

        if newList == []:
            break
        else:
            roots.append(newRoots)
            toVisit.append(newList)

    return roots

def levelOrderTraversal2(tree: Tree):
    """breadth first search is a Queue. """

    toVisit = [[tree]]
    roots = [[tree._root]]

    while toVisit:
        listOfTrees = toVisit.pop(0)
        newTreesList = []
        newRoots = []
        for tree in listOfTrees:
            newTreesList.extend(tree._subtrees)

            for subtree in tree._subtrees:
                newRoots.append(subtree._root)

        if newTreesList:
            toVisit.append(newTreesList)
            roots.append(newRoots)

        else:
             break

    return roots

def averageOfLevelsInBinaryTree(bst: BinarySearchTree):
    toVisit = [[bst]]
    averages = []

    while toVisit:
        listOfTrees = toVisit.pop(0)
        newList =[]
        sum = 0
        for trees in listOfTrees:
            sum += trees._root

            if not trees._left.isEmpty():
                newList.append(trees._left)

            if not trees._right.isEmpty():
                newList.append(trees._right)

        averages.append(sum / len(listOfTrees))

        if newList == []:
            break

        else:
            toVisit.append(newList)

    return averages

def sumOfRootToLeaf(bst: BinarySearchTree):
    """For all leaves in the tree, return the sum of the values of the root to the leaf.
    """

    if bst.isEmpty():
        return 0

    elif bst.isSizeOne():
        return [bst._root]

    else:
        leftsum = sumOfRootToLeaf(bst._left)
        rightsum = sumOfRootToLeaf(bst._right)
        sum =  []
        for items in leftsum:
            sum.append(items + bst._root)

        for items in rightsum:
            sum.append(items + bst._root)

        return sum

def invertBinaryTree(bst: BinarySearchTree):
    """Invert this binary tree."""

    if bst.isEmpty() or bst.isSizeOne():
        return

    else:
        bst._left, bst._right = bst._right, bst._left

        invertBinaryTree(bst._left)
        invertBinaryTree(bst._right)

def twoSumIV(bst: BinarySearchTree, target):
    """Given a binary search tree, return True if there exists two numbers that add up to target."""

    if bst.isEmpty() or bst.isSizeOne():
        return False

    else:
        values = getAllValuesFromBST(bst)
        l = 0
        r = len(values)-1

        while l < r:
            if values[l] + values[r] == target:
                return True ### Remember this algorithm.

            elif values[l] + values[r] < target:
                l += 1

            else:
                r -= 1

        return False

def convertbsttoGreaterTree(bst: BinarySearchTree):
    if bst.isEmpty() or bst.isSizeOne():
        return

    else:
        convertbsttoGreaterTree(bst._left)
        convertbsttoGreaterTree(bst._right)

        if not bst._right.isEmpty():
            bst._root += bst._right._root


def treeToString(bst: BinarySearchTree):
    """"""
    if bst.isEmpty():
        return ""

    elif bst.isSizeOne():
        return str(bst._root)

    else:
        s = str(bst._root) + "("

        s += treeToString(bst._left) + ")" + "("

        s += treeToString(bst._right) + "))"

        return s

def maximumBinaryTree(nums: list):
    """Construct a maximum binary tree from the nums list."""

    if nums == []:
        return BinarySearchTree(None)

    else:
        maximumNumber = max(nums)
        maxIndex = nums.index(maximumNumber)
        bt = BinarySearchTree(maximumNumber)
        bt._left = maximumBinaryTree(nums[:maxIndex])
        bt._right = maximumBinaryTree(nums[maxIndex+1:])

        return bt

def insert(bst: BinarySearchTree, item):
    """Insert into a binary search tree."""

    if bst.isEmpty():
        bst._root = item

    else:
        if item < bst._root:
            return insert(bst._left, item)

        else:
            return insert(bst._right, item)

def listToBST(nums: list):
    """Construct a binary search tree that matches the given preorder traversal.

    """

    if nums == []:
        return BinarySearchTree(None)

    else:
        sortedList = sorted(nums)

        midPoint = len(sortedList) // 2

        bst = BinarySearchTree(sortedList[midPoint])

        bst._left = listToBST(sortedList[:midPoint])
        bst._right = listToBST(sortedList[midPoint+1:])

        return bst

def pruningBinaryTree(bst: BinarySearchTree):
    """Remove all subtrees that don't have 1."""

    if bst.isEmpty():
        return

    elif bst.isSizeOne():
        if bst._root == 0:
            bst._root = None
            bst._left = BinarySearchTree(None)
            bst._right = BinarySearchTree(None)

    else:
        pruningBinaryTree(bst._left)
        pruningBinaryTree(bst._right)

        if bst.isSizeOne():
            if bst._root == 0:
                bst._root = None
                bst._left = BinarySearchTree(None)
                bst._right = BinarySearchTree(None)


    

bst = BinarySearchTree(1)
left = BinarySearchTree(1)
left._left = BinarySearchTree(0)
left._right = BinarySearchTree(0)
right = BinarySearchTree(1)
right._left = BinarySearchTree(0)
right._right = BinarySearchTree(1)
bst._left = left
bst._right = right
pruningBinaryTree(bst)
print(bst)



# lt = Tree(2, [Tree(4, []), Tree(5, [])])
# rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
#                           Tree(10, [Tree(12,[])])])
# t = Tree(1, [lt, rt])


