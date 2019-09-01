class Tree:
    def __init__(self, root, subtrees):
        self._root = root
        self._subtrees = subtrees

    def __str__(self):
        return self._print()

    def _print(self, depth=0):
        if self._root is None:
            return ""

        else:
            s = depth*" " + str(self._root) + '\n'

            for subtrees in self._subtrees:
                s+= subtrees._print(depth+1)

            return s

    def __contains__(self, item):
        if self._root == item:
            return True

        else:
            for subtrees in self._subtrees:
                if subtrees.__contains__(item):
                    return True

            return False

    def __len__(self):
        if self._root is None:
            return 0

        else:
            count = 1

            for subtrees in self._subtrees:
                count += len(subtrees)

            return count

    def num_positives(self):
        if self._root is None:
            return 0

        else:
            count = 0
            if self._root > 0:
                count += 1

            for subtrees in self._subtrees:
                count += subtrees.num_positives()

            return count

    def maximum(self):
        """Return the maximum item stored in this tree."""

        if self._root is None:
            return 0

        else:
            values = [self._root]

            for subtrees in self._subtrees:
                values.append(subtrees.maximum())

            return max(values)

    def height(self):
        """return the height of this tree."""

        if self._root is None:
            return 0

        elif self._subtrees == []:
            return 1

        else:
            heights = []

            for subtrees in self._subtrees:
                heights.append(subtrees.height() + 1)

            return max(heights)

    def leaves(self):
        """Return a list of all leaves."""

        if self._root is None:
            return []

        elif self._subtrees == []:
            return [self._root]

        else:
            leaves = []

            for subtrees in self._subtrees:
                leaves.extend(subtrees.leaves())

            return leaves

    def sum(self):
        """Return sum of tree."""

        if self._root is None:
            return 0

        else:
            sum = self._root

            for subtrees in self._subtrees:
                sum += subtrees.sum()

            return sum

    def average(self):
        """Return average of all the values in the tree. We need length and sum."""

        if len(self) == 0:
            return 0

        else:
            return self.sum()/len(self)

    def delete_root(self):
        """To delete root of the subtree, take the right most subtree"""

        if self._subtrees == []:
            self._root = None

        else:
            rightmostsubtree = self._subtrees.pop()
            self._root = rightmostsubtree._root

            self._subtrees.extend(rightmostsubtree._subtrees)

    def leftmostleaf(self):
        if self._subtrees == []:
            temp = self._root
            self._root = None

            return temp

        else:
            return self._subtrees[0].leftmostleaf()



    def delete_root2(self):
        """Find the left most leaf, and make that the root of the tree."""

        if self._subtrees == []:
            self._root = None
        else:
            leftmostleaf = self.leftmostleaf()

            self._root = leftmostleaf

    def delete_item(self, item):
        """Delete the given item from the tree."""


print("hello world.")

t = Tree(1, [Tree(2,[]), Tree(9,[Tree(4,[])])])
print(t)
t.delete_root2()
print(t)