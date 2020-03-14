from linked_list import LinkedList
def how_many_smaller_numbers(arr):
    """given an arr, for each element in the arr, return how
    many elements are smaller than it."""

    sorted_arr = sorted(arr)

    first_occuring_index_dict = {}

    for x in range(len(sorted_arr)):
        if sorted_arr[x] not in first_occuring_index_dict:
            first_occuring_index_dict[sorted_arr[x]] = x

    items_smaller_dict = {}
    for x in range(len(sorted_arr)):
        items_smaller_dict[sorted_arr[x]] = len(sorted_arr[:first_occuring_index_dict[sorted_arr[x]]])

    output = []
    for elements in arr:
        output.append(items_smaller_dict[elements])

    return output


def decompress_run_length_encoding(arr):
    output = []
    for x in range(0, len(arr),2):
        freq, val =  arr[x], arr[x+1]

        for y in range(freq):
            output.append(val)

    return output

def replace_elements_with_greatest(arr):
    """given an arr, replace elements with the greatest on its right side.
    """
    curr_max = -1
    for x in range(len(arr)-1,-1,-1):
        arr[x], curr_max = curr_max, max(curr_max,arr[x])


    return arr

def high_five(arr):
    """Given a list of scores of different students,
    return the average score of each student's top five scores
    in the order of each student's id."""

    student_grade_dict = {}
    ids = set()
    for grades in arr:
        id = grades[0]
        if id in student_grade_dict:
            if student_grade_dict[id][1] < 5:
                student_grade_dict[id][0] += grades[1]
                student_grade_dict[id][1] += 1
                student_grade_dict[id][2] = student_grade_dict[id][0]/student_grade_dict[id][1]
        else:
            student_grade_dict[id] = [grades[1],1, grades[1]]
        ids.add(grades[0])

    sorted_ids = sorted(list(ids))
    output = []
    for ids in sorted_ids:
        output.append([ids, student_grade_dict[ids][2]])

    return output

def n_unique_integers_summing_zero(n):
    '''output any list of n unique integers summing to 0.'''

    if n == 1:
        return [0]

    else:
        if n % 2 == 0:
            output = []
            curr_number = 1
            while len(output) < n:
                output.append(curr_number)
                output.append(-curr_number)
                curr_number += 1

        else:
            output = n_unique_integers_summing_zero(n-1)
            output.append(0)

        return output

def flip_and_invert(row):
    back_pointer = len(row)-1
    for x in range(len(row)//2):
        row[x],row[back_pointer] = row[back_pointer],row[x]
        back_pointer -=1


def flip_and_invert_image(matrix):
    """flip and invert matrix"""

    for x in range(len(matrix)):
        flip_and_invert(matrix[x])

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 1:
                matrix[x][y] = 0

            else:
                matrix[x][y] = 1
    return matrix


def squares_of_sorted_arr2(arr):
    """return the squares of a sorted order in increasing order also in increasing order."""

    last_negative = 0
    while last_negative < len(arr) and arr[last_negative] < 0:
        last_negative += 1

    left_pointer = last_negative - 1
    right_pointer = last_negative
    output = []
    while left_pointer >= 0 and right_pointer < len(arr):
        if arr[left_pointer]*arr[left_pointer] < arr[right_pointer]*arr[right_pointer]:
            output.append(arr[left_pointer]*arr[left_pointer])
            left_pointer -= 1

        else:
            output.append(arr[right_pointer]*arr[right_pointer])
            right_pointer += 1

    while left_pointer >= 0:
        output.append(arr[left_pointer]*arr[left_pointer])
        left_pointer -= 1

    while right_pointer < len(arr):
        output.append(arr[right_pointer]*arr[right_pointer])
        right_pointer += 1

    return output


def binary_search_fixed_point(arr, item, start, end):
    """given an arr and an item, find the first occurence of the item."""

    if start > end:
        return -1

    else:
        midpoint = start + ((end-start)//2)

        if arr[midpoint] == item:
            occurence = midpoint
            earlier_occurence = binary_search_fixed_point(arr,item,start,midpoint-1)

            if earlier_occurence == -1:
                return occurence

            else:
                return earlier_occurence

        elif item < arr[midpoint]:
            return binary_search_fixed_point(arr, item, start, midpoint-1)

        return binary_search_fixed_point(arr, item, midpoint+1, end)

def height_checker(heights):
    """how many students are not in the right place?"""

    sorted_heights = sorted(heights)

    counter = 0

    for x in range(len(heights)):
        if heights[x] != sorted_heights[x]:
            counter += 1

    return counter

def array_partition(arr):
    """return sum of maximum pair min(a,b)."""

    sorted_arr = sorted(arr)
    sum = 0
    for x in range(0,len(sorted_arr),2):
        sum += arr[x]

    return sum

def majority_element(arr):
    '''return the majority element.'''

    element_count = {}

    for elements in arr:
        if elements in element_count:
            element_count[elements] += 1
            if element_count[elements] > len(arr)//2:
                return elements

        else:
            element_count[elements] = 1

def move_all_zeroes(arr):
    """given an arr, move all zeroes to the end. must do it in place."""

    current_pos = 0

    for x in range(len(arr)):
        if arr[x] != 0:
            arr[current_pos] = arr[x]
            current_pos += 1


    for x in range(current_pos, len(arr)):
        arr[x] = 0

    return arr

def plus_one(arr):
    '''given an arr of integers, representing a digit, return a new list of one added to that number,'''
    carried = 0
    sum_list = []
    sum_linky = LinkedList()

    for x in range(len(arr)-1, -1, -1):
        if x == len(arr)-1:
            num = arr[x] + 1

            if num == 10:
                sum_linky.add(0)
                carried = 1

            else:
                sum_linky.add(num)

        else:
            sum_linky.add(arr[x]+carried)
            carried = 0

    curr = sum_linky.first
    while curr:
        sum_list.append(curr.item)
        curr = curr.next

    return sum_list


def merge_sorted_arrays(arr, arr2):
    '''given two sroted arrays, merge the two'''

    c1 = 0
    c2 = 0
    output = []
    while c1 < len(arr) and c2 < len(arr2):
        if arr[c1] < arr2[c2]:
            output.append(arr[c1])
            c1 += 1

        else:
            output.append(arr2[c2])
            c2 += 1
    if c1 == len(arr):
        return output + arr2[c2:]

    else:
        return output + arr[c1:]

def in_same_line(starting_interval, ending_interval):
    return ending_interval[0] - starting_interval[1] <= 0

def merge_overlapping_intervals(intervals):
    '''given an arr of intervals, merge all overlapping intervals.'''

    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    merged_intervals = [intervals_sorted[0]]

    for x in range(1, len(intervals_sorted)):
        if in_same_line(merged_intervals[-1],intervals_sorted[x]):
            starting = merged_intervals.pop()
            merged_intervals.append([starting[0], intervals_sorted[x][1]])

        else:
            merged_intervals.append(intervals_sorted[x])

    return merged_intervals


def three_sum_closest(arr, target):
    '''given an array and a target, give 3 numbers which are the closest to target.'''

    sorted_arr = sorted(arr)
    current_result = arr[0] + arr[1] + arr[2]

    for x in range(len(arr)):
        l_pointer = x+1
        r_pointer = len(arr)-1

        while l_pointer < r_pointer:
            curr_sum = sorted_arr[x] + sorted_arr[l_pointer] + sorted_arr[r_pointer]

            if curr_sum < target:
                l_pointer += 1

            else:
                r_pointer -=1

            if abs(curr_sum - target) < abs(current_result - target):
                current_result = curr_sum

    return current_result


if __name__ == "__main__":
    # print(merge_sorted_arrays([1,2,3,8,9],[2,5,6,7]))
    print(three_sum_closest([-1, 2, 1, -4], 1))