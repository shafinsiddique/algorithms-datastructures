def stock_market(arr):
    max_profit = 0

    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if arr[y] > arr[x]:
                max_profit = max([arr[y]-arr[x], max_profit])

    return max_profit

def stock_market_one_pass(arr):
    """do the stock market question in one pass."""
    global_min = arr[0]
    max_profit = 0

    for items in arr:
        if items < global_min:
            global_min = items

        elif items - global_min > max_profit:
            max_profit = items - global_min

    return max_profit


def pivot_index(arr):
    """write an algorithm to find the pivot index of an arr."""

    left_sum = 0
    right_sum = 0
    leftsums = []
    rightsums = []
    for x in range(len(arr)):
        left_sum += arr[x]
        right_sum += arr[len(arr)-1-x]
        leftsums.append(left_sum)
        rightsums.append(right_sum)

    for x in range(len(arr)):
        if x == 0:
            if rightsums[-2] == 0:
                return x

        else:
            if leftsums[x-1] == rightsums[-2-x]:
                return x

def distinct_character_in_string(string):
    """return the index of the first non repeating character."""
    char_dict = {}
    for chars in string:
        if chars in char_dict:
            char_dict[chars] += 1

        else:
            char_dict[chars] = 1

    for x in range(len(string)):
        if char_dict[string[x]] == 1:
            return x

    return -1

def maximum_product_with_three_factors(arr):
    '''stupid q.'''

    sorted_array = sorted(arr, reverse=True)

    return sorted_array[0]*sorted_array[1]*sorted_array[2]


def maximum_product_linear(arr):
    """Assuming arr len >= 3"""
    sorted_first_part = sorted(arr[:3], reverse=True)

    first_num = sorted_first_part[0]
    second_num = sorted_first_part[1]
    third_num = sorted_first_part[2]

    for x in range(3, len(arr)):
        if arr[x] > first_num:
            first_num, second_num, third_num = arr[x], first_num, second_num

        elif arr[x] > second_num:
            second_num, third_num = arr[x], second_num

        elif arr[x] > third_num:
            third_num = arr[x]

    return first_num*second_num*third_num

def third_largest_number(arr):
    """Given an arr, return the third last number."""

    largest, second_largest, third_last = 0, 0, 0

    for nums in arr:
        if nums > largest:
            largest, second_largest, third_last = nums, largest, second_largest

        elif nums > second_largest:
            second_largest, third_last = nums, second_largest

        elif nums > third_last:
            third_last = nums

    if len(arr) >= 3:
        return third_last

    elif len(arr) >= 2:
        return second_largest

    else:
        return largest

def distinct_emails(addresses):
    """Given a list of email addresses, return the number of unique emails."""
    unique_emails = set()
    for email in addresses:
        index_of_at = email.index("@")
        local_name = (email[:index_of_at]).replace('.',"")
        local_name = local_name[:local_name.index("+")]
        domain_name = email[index_of_at:]
        unique_emails.add(local_name +domain_name)

    return len(unique_emails)

def move_zeroes(arr):
    '''given an arr, move all the zeroes to the end.'''

    curr_index = 0

    for x in range(len(arr)):
        if arr[x] != 0:
            arr[curr_index] = arr[x]
            curr_index += 1

    for x in range(curr_index, len(arr)):
        arr[x] = 0

def three_sum(arr):
    '''given an arr and a target, return 3 numbers that add up to target.'''

    arr_dict = {}
    for x in range(len(arr)):
        arr_dict[arr[x]] = x
    items = []
    items_set = set()
    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if -arr[x]-arr[y] in arr_dict and arr_dict[-arr[x]-arr[y]] > y:
                items_set.add((arr[x],arr[y],-arr[x]-arr[y]))

    return items_set



print(three_sum([-1, 0, 1, 2, -1, -4]))