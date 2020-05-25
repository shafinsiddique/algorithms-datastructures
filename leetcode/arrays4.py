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
        total_product *= elements

    for elements in arr:
        output.append(total_product/elements)

    return output


def product_of_array_without_divison(arr):
    """
    same q as above but try to do it without division.
    This approach calculates the product for each element to its left, and to its right.
    and then calculates the overall product without that element.
    """
    left_products = []
    cur_product = 1
    last_value = 1
    for x in range(len(arr)):
        new_prod = cur_product*last_value
        left_products.append(new_prod)
        last_value = arr[x]
        cur_product = new_prod
    right_products= [0]*len(arr)
    cur_product = 1
    last_value = 1
    for x in range(len(arr)-1,-1,-1):
        new_prod = cur_product*last_value
        right_products[x] = new_prod
        last_value = arr[x]
        cur_product = new_prod

    output = []
    for x in range(len(arr)):
        output.append(left_products[x] * right_products[x])

    return output

def odd_even(arr):
    """partition the arr in such a way such that all even elements come before alll
    the odd elements."""

    curr_even = 0
    last_odd = len(arr)-1

    while curr_even < last_odd:
        if arr[curr_even] % 2 != 0:
            arr[curr_even], arr[last_odd] = arr[last_odd], arr[curr_even]
            last_odd -= 1

        else:
            curr_even += 1

def dutch_partitioning_problem(arr, pivot):
    """partition the array such that all elements less than the pivot appear first, followed
    by elements equaling the pivot and then finally elements greater than pivot.
    """

    # first pass, bring all small elements to front..

    small = 0

    for x in range(len(arr)):
        if arr[x] < pivot:
            arr[x], arr[small] = arr[small],arr[x]
            small += 1

    larger = l
    for x in range(len(arr)-1,-1,-1):
        if arr[x] < pivot:
            break

        elif arr[x] > pivot:
            arr[x], arr[larger] = arr[larger], arr[x]
            larger -=1

def array_partition_1(arr):
    """given an array of 2n elements, find the maximum sum that can found by summing up
    min (a, b) such that a and b are elements of arr."""

    sorted_arr = sorted(arr)
    sum = 0
    for x in range(0, len(arr), 2):
        sum += sorted_arr[x]

    return sum

def majority_element(arr):
    elements_counter = {}

    for elements in arr:
        if elements in elements_counter:
            elements_counter[elements] += 1

        else:
            elements_counter[elements] = 1


    max_key = None
    max_counter = None

    for elements in arr:
        if max_key:
            if elements_counter[elements] > max_counter:
                max_counter = elements_counter[elements]
                max_key = elements

        else:
            max_key = elements
            max_counter = elements_counter[elements]

    return max_key

def plus_one(arr):
    """given an arr of integers, add 1 to it."""

    output_reversed = []
    carried = 1
    for x in range(len(arr)-1,-1,-1):
        sum_number = arr[x] + carried

        if sum_number > 10:
            carried = 1
            output_reversed.append(sum_number % 10)

        else:
            carried = 0
            output_reversed.append(sum_number)
    output = []
    for x in range(len(output_reversed)-1,-1,-1):
        output.append(output_reversed[x])

    return output

def merge_two_sorted_arrays(arr1, arr2):
    arr1_counter = 0
    arr2_counter = 0
    merged = []
    while arr1_counter < len(arr1) and arr2_counter < len(arr2):
        if arr1[arr1_counter] < arr2[arr2_counter]:
            merged.append(arr1[arr1_counter])
            arr1_counter += 1

        else:
            merged.append(arr2[arr2_counter])
            arr2_counter += 1

    return merged + arr1[arr1_counter:] + arr2[arr2_counter:]


def move_zeroes(arr):
    """move all zeroes to the end."""

    zero = len(arr)-1
    non_zero = 0

    while non_zero < zero:
        if arr[non_zero] == 0:
            arr[non_zero], arr[zero] = arr[zero], arr[non_zero]
            zero -=1 # since we know that element is now a zero.

        else:
            non_zero += 1 # since we know this element is not a zero.

def best_time_to_buy_and_sell_stock_ii(arr):
    """
    the algorithm I am thinking of for this question is for now a brute force approach.

    algorithm :

    - iterate through the array, consider buying for that day.
    - find the next greater element that has a lower element after it.
        - if no lower element, simply find the max between this element and the end
        of the array. break the loop.

        - if lower element, use the next greater element.

    - if no greater element, profit is 0 for the day and move to the next element.
    """

    profits = []
    current_index = 0

    while current_index < len(arr):
        buy_price = arr[current_index]
        next_greater_element, lower_after_next_greater_element = None, None
        iterator = current_index + 1

        while iterator < len(arr):
            if next_greater_element:
                if arr[iterator] < arr[next_greater_element]:
                    lower_after_next_greater_element = iterator
                    break
            else:
                if arr[iterator] > arr[current_index]:
                    next_greater_element = iterator

            iterator += 1

        if next_greater_element:
            if lower_after_next_greater_element:
                sell_price = max(arr[current_index+1:lower_after_next_greater_element])
                current_index = lower_after_next_greater_element

            else:
                sell_price = max(arr[current_index+1:])
                current_index = len(arr)

            profits.append(sell_price - buy_price)

        else:
            profits.append(0)
            current_index += 1

    return sum(profits)


def best_time_to_buy_and_sell_stock_II_optimized(arr):
    """this is optimized approach of buy and sell stock II. In O(n) time and space.

    The algorithm Im thinking of is:

    - initially, set the buy price to the first element (if no first element,
    0 profit overall, return 0)
    - iterate through the array trying to find a sell price for the current buy price we just
    in.
    - if we find an element that is greater than our buy price, we declare that as a
    potential sell price. Notice that I said potential sell price and not just sell price.
    This is because there might be an element after the potential sell price
    that is greater than the current sellprice.  We will have a determined sell price
    when we find an element after the sell price that is LOWER than the current sell price.
    that is when we sell the stock and buy it at the new price we just found.
    - Before we have sold our stock or found a potential sell price, if we see an element
    that is lower than the current buy price, we set our new price to that amount.
    this is because any profit we could have made at the earlier price, we are guaranteed
    to make more now that we have an even lower price.
    """
    if arr == []:
        return 0

    buy_price = arr[0]
    potential_sell_price = None
    curr_index = 0
    profits = []

    while curr_index < len(arr):
        if not potential_sell_price: # no potential sell price for the price we bought at, try to find a sell price.
            if arr[curr_index] > buy_price:
                potential_sell_price = arr[curr_index]
            else: # found a price lower than current buy price.
                buy_price = arr[curr_index]

        else: # there is a potential sell price, we either confirm to sell or try to find a better price.
            if arr[curr_index] < potential_sell_price: # found a price lower than the sell price.
                # we can confirm the previous sale and buy at a new price.
                profits.append(potential_sell_price - buy_price)
                potential_sell_price = None
                buy_price = arr[curr_index]

            elif arr[curr_index] > potential_sell_price: # found an even better sell price.
                # since this is greater, we can ensure greater profit.
                potential_sell_price = arr[curr_index]

        curr_index += 1

    if potential_sell_price:
        profits.append(potential_sell_price - buy_price)

    return sum(profits)


def remove_duplicates_from_sorted_array(arr):
    """
    remove duplicates from sorted array.

    The algorithm I am thinking of is that we start iterating through the array,
    and keep a variable keeping track of the last valid element, so that we have something
    to compare the current element with.

    initially, when we start the loop, our variable to compare with is the first element.

    however, before comparing any element, we should see if there's a None element in the
    list that we previously set. If there is, first we place the current element in that None
    spot in the list, and make the current element None.

    """

    if len(arr) > 1:
        element_to_compare_with = 0
        none_element = None

        for x in range(1, len(arr)):
            current_valid_index = x
            if none_element: # handle the case, first we have to make a swap with the none
                # element.
                arr[none_element] = arr[x]
                current_valid_index = none_element
                arr[x] = None

            if arr[current_valid_index] == arr[element_to_compare_with]:
                arr[current_valid_index] = None
                none_element = current_valid_index

            else:
                element_to_compare_with += 1

                if none_element:
                    none_element += 1


def find_all_duplicates_in_array(arr):
    """tricky algorithm.

    the key idea is that for any index i in arr, arr[i]-1 is a valid index.

    we iterate through the array. We check the index of arr[x] - 1.
    because thats a valid index. if that index is negative, it means there was another
    element with that value, therefore duplicate.

    """
    output = []

    for x in range(len(arr)):
        index_to_check = abs(arr[x])-1

        if arr[index_to_check] < 0:
            output.append(index_to_check+1)
        else:
            arr[index_to_check] = -arr[index_to_check]

    return output

def merge_intervals(intervals):
    """given a collection of intervals, merge all overlapping intervals."""

    merged_intervals = []

    if intervals:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals.append(intervals[0])

        for x in range(1, len(intervals)):
            if merged_intervals[-1][0]<=intervals[x][0]<=merged_intervals[-1][1]:
                merged_intervals[-1][1] = intervals[x][1]

            else:
                merged_intervals.append(intervals[x])

    return merged_intervals


def container_with_most_water(arr):
    """
    The intutition behind this algorithm is that we will have two pointers,
    looking at the area.
    later we move the pointer with the lower height. This is because the greater
    the height, the greater the area."""

    l_pointer = 0
    r_pointer = len(arr)-1
    area = 0

    while l_pointer < r_pointer:
        min_height = min(arr[l_pointer], arr[r_pointer])
        area = max([(r_pointer - l_pointer)*min_height, area])

        if arr[l_pointer] == min_height:
            l_pointer += 1

        else:
            r_pointer -= 1

    return area

def three_sum_closest(arr, target):
    """3sum closest problem, find 3 elements that are the closest to target."""
    result = arr[0]+arr[1]+arr[2]
    arr = sorted(arr)
    for x in range(len(arr)):
        l_pointer = x+1
        r_pointer = len(arr)-1

        while l_pointer < r_pointer:
            cur_sum = arr[x] + arr[l_pointer] + arr[r_pointer]

            if cur_sum > target:
                r_pointer -=1

            else:
                l_pointer += 1

            if abs(target - cur_sum) < abs(target - result):
                result = cur_sum

    return result

def two_sum_sorted(arr, target):
    """given a sorted array, find two elements that add up to target."""

    l_pointer = 0
    r_pointer = len(arr) - 1

    while l_pointer < r_pointer:
        if arr[l_pointer] + arr[r_pointer] == target:
            return [arr[l_pointer], arr[r_pointer]]

        elif arr[l_pointer] + arr[r_pointer] > target:
            r_pointer -= 1

        else:
            l_pointer += 1

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
    for index in range(len(arr)-1,-1,-1):
        if index > 0:
            if arr[index] > arr[index-1]:
                break
    # find the smallest element greater than arr[index-1]

    if index > 0:
        index_of_smallest_element = index

        for x in range(index, len(arr)):
            if arr[x] > arr[index-1] and arr[x] < arr[index_of_smallest_element]:
                index_of_smallest_element = x
        # swap.
        arr[index_of_smallest_element], arr[index-1] = arr[index-1],\
                                                   arr[index_of_smallest_element]
    # reverse everything from index to len(arr)
    backwards = len(arr)-1
    for x in range((index-len(arr))//2):
        arr[index + x], arr[backwards] = arr[backwards], arr[index+x]
        backwards -= 1


def find_pivot_point(arr, left, right):
    midpoint = left + (right - left) // 2

    if left < right:
        if arr[midpoint] > arr[right]:
            return find_pivot_point(arr, midpoint + 1, right)

        return find_pivot_point(arr, left, midpoint-1)

    return left

def binary_search(arr, left, right, target):
    if left < right:
        midpoint = left + (right - left) // 2
        if arr[midpoint] == target:
            return midpoint

        elif target < arr[midpoint]:
            return binary_search(arr, left, midpoint, target)

        return binary_search(arr, midpoint, right, target)

    return -1

def search_in_rotated_array(arr, target):
    """given a sorted array that is rotated, find the target.

    intutition: can we use binary search to find the smallest element in the array.?

    """

    pivot_index = find_pivot_point(arr, 0, len(arr)-1)

    # use the pivot index to find the element. look at the pivot index and see if the elemnt falls between pivot to end of array.
    # if it does, perform a binary search on the right hand side, else perform a bianery search on the left hand side.

    if arr[pivot_index] <= target <= arr[-1]:
        return binary_search(arr, pivot_index, len(arr)-1, target)

    return binary_search(arr, 0, pivot_index, target)

def binary_search_imp(arr, start, end, target):
    if start < end:
        pivot = start + (end - start)//2

        if arr[pivot] == target:
            return pivot

        elif target < arr[pivot]:
            return binary_search_imp(arr, start, pivot-1, target)

        return binary_search_imp(arr, pivot+1, end, target)

    return -1

def bs_search(arr, target):
    return binary_search_imp(arr, 0, len(arr), target)

print(bs_search([1,3,9,21,22,29,30,31], 9))