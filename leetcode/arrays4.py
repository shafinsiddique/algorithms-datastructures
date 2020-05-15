def two_sum(arr, target):
    """given an arr and a target, return indices of two elements that add up to
    target.

    guaranteed to have a solution."""
    elements_dict = {}

    for x in range(len(arr)):
        elements_dict[arr[x]] = x

    for x in range(len(arr)):
        if target - arr[x] in elements_dict and elements_dict[target-arr[x]] != x:
            return [arr[x], target-arr[x]]

def best_time_to_buy_and_sell_stock(arr):
    """the intuition behind this algorithm is that you want the min element on the left
    hand side and the max element on the right hand side. Such when u subtract,
    you get profit. The apporoach im thinking of is you keep a min variable keeping tracking
    of each new minimum. This is because whenever we find a value lower than our current_min,
    we have the possibility that there might be number to its right that
    gives us a greater profit."""

    min = arr[0]
    max_profit = 0

    for x in range(1, len(arr)):
        if arr[x] < min:
            min = arr[x]

        else:
            if arr[x] - min > max_profit:
                max_profit = arr[x] - min

    return max_profit


def three_sum_equality(arr1, arr2):
    arr1_element_count = {}
    arr_2_element_count = {}
    for x in range(3):
        if arr1[x] in arr1_element_count:
            arr1_element_count[arr1[x]] += 1

        else:
            arr1_element_count[arr1[x]] = 1

        if arr2[x] in arr_2_element_count:
            arr_2_element_count[arr2[x]] += 1

        else:
            arr_2_element_count[arr2[x]] = 1

    return arr1_element_count == arr_2_element_count



def three_sum(arr):
    '''given an arr, return the indices of three indices that sum up to 0.

    the intuition behind this problem is that two sum finds TWO integers that add up to
    a value. 0 = X + Y + Z. If we have x fixed, we can do a check to find if there's
    two values that sum to 0-x.

    x + y + z = 0

    y + z = 0-x.'''
    solutions = []
    for x in range(len(arr)):
        two_sum_result = two_sum(arr[:x] + arr[x+1:], 0-arr[x])

        if two_sum_result:
            list_of_values = [arr[x], two_sum_result[0], two_sum_result[1]]

            unique = True

            for sets in solutions:
                if three_sum_equality(list_of_values, sets):
                    unique = False
            if unique:
                solutions.append(list_of_values)

    return solutions


def product_of_array_except_self(arr):
    """given an array arr, return an output array such that output[i] = product of all
    elements in arr except ar[i].

    The simple O(N) time approach would be to use division.

    """

    total_product = 1
    output = []
    for elements in arr:
        print(elements)
        total_product *= elements

    for elements in arr:
        output.append(total_product/elements)

    return output


print(product_of_array_except_self([1,2,3,4]))

