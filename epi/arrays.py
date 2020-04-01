def partition(nums: list):
    """Partition the array.

    O(n) time and O(N) space.
    """
    smaller = []
    equal = []
    larger =[]
    pivot = nums[0]
    for items in nums:
        if items < pivot:
            smaller.append(items)

        elif items == pivot:
            equal.append(items)

        else:
            larger.append(items)

    return smaller + equal + larger

