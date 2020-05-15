def odd_even(arr):
    """arrange the elements in such a way such that all even elements come before
    all odd elements."""

    currend_even = 0
    currend_odd = len(arr)-1

    while currend_even < currend_odd:
        if arr[currend_even] % 2 == 0:
            currend_even += 1
        else:
            arr[currend_even], arr[currend_odd] = arr[currend_odd], arr[currend_even]
            currend_odd -= 1

def partitioning(arr, pivot):
    """return a partioning, such that all elements less than pivot appear first, followed
    by elements equal to pivot, followed by elements greater than pivot.

    The initial solution is pretty intuitive.

    Iterate through the arrays, have 3 seperate arrays - lessThan,equalTo,greaterThan.

    Simply concatanate the 3 arrays at the end.

    This approach leads to o(n) runtime and o(n) space.

    See below for another approach using O(1) space but at an increased runtime."""

    smaller, equal, bigger = [],[],[]

    for elements in arr:
        if elements < pivot:
            smaller.append(elements)

        elif elements == pivot:
            equal.append(elements)

        else:
            bigger.append(elements)

    return smaller + equal + bigger

def partioning_constant_space(arr, pivot):
    """This approach takes o(1) space but o(n^2) time. Definitely not the most optimal solution
    but definitely interesting to know."""

    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if arr[y] < pivot:
                arr[x],arr[y] = arr[y],arr[x]
                break

    for x in range(len(arr)-1, -1, -1):
        if arr[x] < pivot:
            break

        for y in range(x):
            if arr[y] > pivot:
                arr[x],arr[y] = arr[y], arr[x]


l = [1,2,4,9,6,8,2,1]

partioning_constant_space(l, 8)
print(l)

