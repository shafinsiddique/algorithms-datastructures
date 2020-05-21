def next_greater_permutation(arr):
    """
    Algorithm:

    Find the first i from the right such that arr[i] > arr[i-1].

    swap arr[i-1] with the smallest element in arr[i:] that is greater than arr[i-1].
    Let's call that element n.

    notice how even after the swap everything in arr[i:] is still in descending order.
    to the order.

    Somply reverse arr[i:]

    """
    index = 0
    for index in range(len(arr) - 1, -1, -1):
        if index > 0:
            if arr[index] > arr[index - 1]:
                break
    # find the smallest element greater than arr[index-1]

    if index > 0:
        index_of_smallest_element = index

        for x in range(index, len(arr)):
            if arr[x] > arr[index - 1] and arr[x] < arr[index_of_smallest_element]:
                index_of_smallest_element = x
        # swap.
        arr[index_of_smallest_element], arr[index - 1] = arr[index - 1], \
                                                         arr[index_of_smallest_element]
    # reverse everything from index to len(arr)
    backwards = len(arr) - 1
    for x in range((index - len(arr)) // 2):
        arr[index + x], arr[backwards] = arr[backwards], arr[index + x]
        backwards -= 1