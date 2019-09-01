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


t = Tree(1, [Tree(2,[]), Tree(3,[Tree(4,[])])])
print(t.num_positives())