from stack import Stack

class Tree:
    def __init__(self, root, subtrees):
        self.root = root
        self.subtrees = subtrees

    def __str__(self):
        return self.print()

    def print(self,depth=0):
        if not self.root:
            return ''

        else:
            string_rep = depth*" " + str(self.root) + '\n'

            for subtrees in self.subtrees:
                string_rep += subtrees.print(depth+1)

            return string_rep

    def __contains__(self, item):
        if not self.root:
            return None

        else:
            if self.root == item:
                return True

            for subtree in self.subtrees:
                if item in subtree:
                    return True

            return False

    def __len__(self):
        """
        Return the count of items in the tree.
        """

        if not self.root:
            return 0

        else:
            count = 1

            for subtree in self.subtrees:
                count += len(subtree)

            return count

    def height(self):
        """
        Return the height of the tree.
        """

        if not self.root:
            return 0

        else:
            heights = []

            for subtree in self.subtrees:
                heights.append(subtree.height()+1)

            return max(heights)


    def num_positives(self):
        """Return the number of positive numbers in this n-ary tree."""

        if not self.root:
            return 0

        else:
            counter = 0
            if self.root > 0:
                counter += 1

            for subtree in self.subtrees:
                counter += subtree.num_positives()

            return counter

    def leaves(self):
        if not self.root:
            return []

        if self.subtrees == []:
            return [self.root]

        else:
            leaves = []
            for subtree in self.subtrees:
                leaves.extend(subtree.leaves())

            return leaves


    def post_order_traversal(self):
        if not self.root:
            return []
        else:
            elements = []
            for subtree in self.subtrees:
                elements.extend(subtree.post_order_traversal())

            elements.append(self.root)

            return elements

    def post_order_iterative(self):
        """post order traversal iterative."""

        if not self.root:
            return []

        else:
            stack, output = [self],[]

            while stack:
                root = stack.pop()

                if root:
                    output.append(root.root)

                for children in root.subtrees:
                    stack.append(children)

            return output[::-1]



class BinarySearchTree:
    def __init__(self, root):
        if root:
            self.root = root
            self.left = BinarySearchTree(None)
            self.right = BinarySearchTree(None)

        else:
            self.root = None
            self.left = None
            self.right = None

    def is_leaf(self):
        return not self.left.root and not self.right.root

    def is_empty(self):
        return self.root is None

    def print_recursive(self, depth=0):
        if not self.root:
            return ""

        else:
            s = " "*depth
            s += str(self.root) + "\n"
            if self.next:
                s += "next:"  + str(self.next.root) + "\n"
            s += self.left.print_recursive(depth+1)
            s += self.right.print_recursive(depth+1)

            return s

    def __str__(self):
        return self.print_recursive(1)

    def in_order(self):
        """Return a list of the traversal"""
        if not self.root:
            return []
        else:
            items =[]
            items.extend(self.left.in_order())
            items.append(self.root)
            items.extend(self.right.in_order())

            return items

    def height(self):
        """Return the heigth of the binary search tree, defined as
        the maximum """

        if not self.root:
            return 0

        else:
            heights = []
            heights.append(self.left.height()+1)
            heights.append(self.right.height()+1)

            return max(heights)

    def get_max(self):
        """Return the maximum item from the binary search tree."""

        if not self.root:
            return 0

        else:
            if self.right.is_empty():
                return self.root

            return self.right.get_max()

    def range_sum(self, left, right):
        """give the sum of all values that are within this range."""

        if not self.root:
            return 0
        else:
            items = []

            if left > self.root:
                items.append(self.right.range_sum(left, right))

            elif right < self.root:
                items.append(self.left.range_sum(left, right))

            else:
                items.append(self.root)
                items.append(self.left.range_sum(left, right))
                items.append(self.right.range_sum(left, right))

            return sum(items)

    def size(self):
        """return the size of tree."""

        if self.root is None:
            return 0

        else:
            size = 1
            size += self.left.size()
            size += self.right.size()

            return size

    def breadth_first_search(self):
        """do a breadth first traversal"""

        queue = [self]
        items = []
        while queue:
            tree = queue.pop(0)
            if tree.root:
                items.append(tree.root)
                queue.append(tree.left)
                queue.append(tree.right)

        return items

    def levels(self):
        """
        return the levels in a list.
        """

        queue = [self]
        levels = []

        while queue:
            current_level = []

            for x in range(len(queue)):
                tree = queue.pop(0)
                if tree.root:
                    current_level.append(tree.root)
                    queue.append(tree.left)
                    queue.append(tree.right)

            if len(current_level) > 0:
                levels.append(current_level)

        return levels

    def diameter(self):
        if not self.root:
            return 0

        else:
            return 1 + self.left.height() + self.right.height()

    def minimum_depth(self):
        if not self.root:
            return 0

        else:
            return min([self.left.minimum_depth()+1, self.right.minimum_depth()+1])

    def invert(self):
        '''invert the binary tree.'''

        if self.root:
            self.left, self.right = self.right, self.left
            self.left.invert()
            self.right.invert()


    def average_of_levels(self):
        queue = [self]
        averages = []
        while queue:
            trees_in_level = 0
            sum_of_level = 0
            for x in range(len(queue)):
                cur_tree = queue.pop(0)
                if cur_tree.root:
                    trees_in_level += 1
                    sum_of_level += cur_tree.root
                    queue.append(cur_tree.left)
                    queue.append(cur_tree.right)

            if trees_in_level > 0:
                averages.append(sum_of_level/trees_in_level)

        return averages

    def insert(self, item):
        if not self.root:
            self.root = item
            self.left = BinarySearchTree(None)
            self.right = BinarySearchTree(None)

        else:
            if item >= self.root:
                self.right.insert(item)

            else:
                self.left.insert(item)

    def lowest_common_ancestor(self, l, q):
        '''find the lowest common ancestor of these 2 nodes.'''

        if l <= self.root <= q:
            return self.root

        else:
            if q < self.root:
                return self.left.lowest_common_ancestor(l, q)

            else:
                return self.right.lowest_common_ancestor(l,q)




def merge(bst1, bst2):
    if bst1.root and bst2.root:
        merged = BinarySearchTree(bst1.root + bst2.root)
        merged.left = merge(bst1.left, bst2.left)
        merged.right = merge(bst1.right, bst2.right)

        return merged

    elif bst1.root:
        return bst1

    else:
        return bst2


def arr_to_bst(arr):
    bst = BinarySearchTree(None)
    for items in arr:
        bst.insert(items)

    return bst

def two_sum(bst, target):
    if not bst.root:
        return []

    else:
        items = bst.in_order()
        left_pointer = 0
        right_pointer = len(items)-1

        while left_pointer < right_pointer:
            sum = items[left_pointer] + items[right_pointer]
            if sum == target:
                return [items[left_pointer],items[right_pointer]]

            elif sum > target:
                right_pointer -=1

            else:
                left_pointer += 1


def is_same(bst1, bst2):
    '''given two bsts, check if theyre the same.'''

    if not bst1.root and not bst2.root:
        return True

    else:
        if bst1.root and bst2.root and bst1.root == bst2.root:
            if is_same(bst1.left, bst2.left) and is_same(bst1.right, bst2.right):
                return True

        return False


def bottom_left_tree_value(tree):
    """given a binary tree, """

    queue = [tree]
    left_most_value = tree.root
    while queue:
        for x in range(len(queue)):
            tree_in_level = queue.pop(0)
            if x == 0:
                left_most_value = tree_in_level.root

            if tree_in_level.left.root:
                queue.append(tree_in_level.left)

            if tree_in_level.right.root:
                queue.append(tree_in_level.right)
    return left_most_value

def bst_to_sorted_linked_list(bst):
    """
    Given a sorted binary search tree.
    """

    if bst.is_leaf():
        bst.next = None
        return bst

    elif bst.left.root and bst.right.root:
        left_list = bst_to_sorted_linked_list(bst.left)
        curr = left_list
        while curr and curr.next:
            curr = curr.next

        curr.next = bst
        right_list = bst_to_sorted_linked_list(bst.right)
        bst.next = right_list

        return left_list

    elif bst.left.root:
        left_list = bst_to_sorted_linked_list(bst.left)
        curr = left_list
        while curr.next:
            curr = curr.next

        curr.next = bst
        bst.next = None

        return left_list

    elif bst.right.root:
        bst.next = bst_to_sorted_linked_list(bst.right)
        return bst



def print_bst_sorted_list(bst):
    curr = bst
    while curr.root and curr.next:
        print(curr.root, end=" ")
        curr = curr.next


def sum_of_nodes_with_even_grandparents(bst):
    if not bst.root or bst.is_leaf():
        return 0

    else:
        sum_of_nodes = 0
        if bst.root % 2 == 0:
            if bst.left.root:
                if bst.left.left.root:
                    sum_of_nodes += bst.left.left.root

                if bst.left.right.root:
                    sum_of_nodes += bst.left.right.root

            if bst.right.root:
                if bst.right.left.root:
                    sum_of_nodes += bst.right.left.root

                if bst.right.right.root:
                    sum_of_nodes += bst.right.right.root

        sum_of_nodes += sum_of_nodes_with_even_grandparents(bst.left)
        sum_of_nodes += sum_of_nodes_with_even_grandparents(bst.right)

        return sum_of_nodes

def deepest_leaves_sum(bst):
    """return the sum of the leaves from the deepest leaves."""
    queue = [bst]
    levels = []
    while queue:
        current_level = []

        for x in range(len(queue)):
            cur_tree = queue.pop(0)

            if cur_tree.left.root:
                queue.append(cur_tree.left)

            if cur_tree.right.root:
                queue.append(cur_tree.right)

            current_level.append(cur_tree.root)

        levels.append(current_level)

    return sum(levels[-1])

def insert_into_bst(bst, item):
    if not bst.root:
        bst.root = item
        bst.left = BinarySearchTree(None)
        bst.right = BinarySearchTree(None)

    else:
        if item < bst.root:
            insert_into_bst(bst.left, item)

        else:
            insert_into_bst(bst.right, item)


def maximum_binary_tree(arr):
    if len(arr) > 0:

        index_dict = {}
        for x in range(len(arr)):
            index_dict[arr[x]] = x

        maximum_element = max(arr)
        index_of_max = index_dict[maximum_element]
        tree = BinarySearchTree(maximum_element)
        tree.left = maximum_binary_tree(arr[:index_of_max])
        tree.right = maximum_binary_tree(arr[index_of_max+1:])

        return tree


    else:
        return BinarySearchTree(None)

def validate_bst(bst):
    """return true if bst is a valid bst."""
    if not bst.root or bst.is_leaf():
        return True

    elif bst.left.root and bst.right.root:
        if bst.left.root > bst.root or bst.right.root < bst.root:
            return False

        if not validate_bst(bst.left) or not validate_bst(bst.right):
            return False

        return True

    elif bst.left.root:
        if bst.left.root > bst.root:
            return False

        if not validate_bst(bst.left):
            return False

        return True

    else:
        if bst.right.root < bst.root:
            return False

        if not validate_bst(bst.right):
            return False

        return True

def largest_bst_subtree(bst):
    """return the largest subtree from a binary tree."""

    return max([bst.left.size(),bst.right.size()])


def maximum_width_of_binary_tree(bst):
    """return the maximum of the binary tree."""

    queue = [bst]
    widths = []

    while queue:
        widths.append(len(queue))
        for x in range(len(queue)):
            cur_tree = queue.pop(0)
            if cur_tree.root and not cur_tree.is_leaf():
                queue.append(cur_tree.left)
                queue.append(cur_tree.right)

    return max(widths)

def iterative_depth_first_search(bst):
    if not bst.root:
        return []
    else:
        curr = bst
        output, stack = [],[]

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            cur_tree = stack.pop()

            if cur_tree.root != None:
                output.append(cur_tree.root)

            curr = cur_tree.right

        return output

def levels(bst):
    queue = [bst]
    levels =[]

    while queue:
        level = []

        for x in range(len(queue)):
            cur_tree = queue.pop(0)
            if cur_tree.root != None:
                level.append(cur_tree.root)
                queue.append(cur_tree.left)
                queue.append(cur_tree.right)

        if level != []:
            levels.append(level)

    return levels

def zigzag_levels(bst):
    '''return the zigzag traversal'''
    queue = [bst]
    levels = []
    reverse = False
    while queue:
        level = []

        for x in range(len(queue)):
            cur_tree = queue.pop(0)
            if cur_tree.root != None:
                level.append(cur_tree.root)
                queue.append(cur_tree.left)
                queue.append(cur_tree.right)

        if level:
            if reverse:
                levels.append(level[::-1])
                reverse = False
            else:
                reverse = True
                levels.append(level)

    return levels

def populate_next_node_in_bst(bst):
    queue = [bst]

    while queue:
        cur_level = []
        for x in range(len(queue)):
            cur_tree = queue.pop(0)

            if cur_tree.root is not None:
                cur_level.append(cur_tree)
                queue.append(cur_tree.left)
                queue.append(cur_tree.right)
        if cur_level:
            for x in range(len(cur_level)-1):
                cur_level[x].next = cur_level[x+1]
            cur_level[-1].next = None



b = BinarySearchTree(8)
b.left = BinarySearchTree(3)
b.left.left = BinarySearchTree(1)
b.left.right = BinarySearchTree(6)
b.left.right.left = BinarySearchTree(4)
b.left.right.right = BinarySearchTree(7)
b.right = BinarySearchTree(10)
b.right.right = BinarySearchTree(14)
b.right.right.left = BinarySearchTree(13)
# print(maximum_width_of_binary_tree(b))
#
b2 = BinarySearchTree(1)
b2.left = BinarySearchTree(3)
b2.left.left = BinarySearchTree(5)
b2.left.right = BinarySearchTree(3)
b2.right = BinarySearchTree(2)
b2.right.right = BinarySearchTree(9)
# print(levels(b))
populate_next_node_in_bst(b)
print(b)
# print(b)
# print(b.lowebsst_common_ancestor(1,6))
#
# bs1 = BinarySearchTree(1)
# bs1.left = BinarySearchTree(2)
# bs1.right = BinarySearchTree(3)
# bs2 = BinarySearchTree(1)
# bs2.left = BinarySearchTree(2)
# bs2.right = BinarySearchTree(4)
