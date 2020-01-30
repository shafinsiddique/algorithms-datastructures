from dataStructures.BST import BinarySearchTree
from dataStructures.LinkedList import LinkedList
from dataStructures.LinkedList import Node
import sys
def twoSum(nums, target):
    """Given an array of integers, return the indices such
    that they add up to a certain target, you can assume it exists."""

    # using two pointer technique.
    # n log n efficiency.
    nums = sorted(nums)

    i = 0
    j = len(nums)-1

    while i != j:
        if nums[i] + nums[j] == target:
            return [i, j]

        elif nums[i] + nums[j] > target:
            j -=1
        else:
            i += 1

def reverseString(s):
    """Reverse the string."""
    newString = ""

    for x in range(len(s)-1,-1,-1):
        newString += s[x]

    return newString

def reverseArray(arr: list):
    """Reverse the given array."""
    midpoint = len(arr)//2
    backwards = -1
    for x in range(midpoint):
        arr[x], arr[backwards] = arr[backwards],arr[x]

        backwards-=1

def maximumDepth(bst: BinarySearchTree):
    """Find the maximum depth of binary search tree."""

    if bst.isEmpty():
        return 0

    else:
        leftHeight = maximumDepth(bst._left) + 1
        rightHeight = maximumDepth(bst._right) + 1

        return max([leftHeight, rightHeight])

def singleNumber(arr: list):
    """Given a non empty array of numbers, every element appears twice except
    for one. Find that element."""

    arr = sorted(arr)

    for x in range(1, len(arr)-1):
        if arr[x] != arr[x+1] and arr[x] != arr[x-1]:
            return arr[x]

def singleNumber2(arr: list):
    """
    Hash table approach.
    """

    values = {}

    for items in arr:
        try:
            values.pop(items)
        except:
            values[items] = 1


    return values.popitem()[0]

def fizzBuzz(n):
    """Fizzbuzz test"""

    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")

        elif x % 3 == 0:
            print("Fizz")

        elif x % 5 == 0:
            print("buzz")

        else:
            print(str(x))

def reverseLinkedList(linky: LinkedList):
    """Reverse the linked list."""

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


def reverseNodes(linky: LinkedList, node: Node):
    """Reverse the nodes."""

    if node is None:
        return

    if node.next is None:
        linky._first = node

    else:
        reverseNodes(linky, node.next)
        node.next.next = node
        node.next = None


def reverseLinkyRecursive(linky: LinkedList):
    """Reverse the linked list recursively."""

    if linky._first is None:
        return

    else:
        return reverseNodes(linky, linky._first)


def wordChain():
    line = int(sys.stdin.readline())
    words =[]
    for x in range(line):
        words.append(sys.stdin.readline().replace("\n",""))

    counter = 1

    currentLastString = words[0][-1]

    for x in range(1, len(words)):
        if words[x][0] == currentLastString:
            counter += 1
            currentLastString = words[x][-1]
        else:
            break

    return counter


def fibonnacciLike(n):
    """f1 = 1, f2 = 2"""

    if n == 1:
        return 1

    elif n == 2:
        return 2

    else:
        return fibonnacciLike(n-1) + fibonnacciLike(n-2)
