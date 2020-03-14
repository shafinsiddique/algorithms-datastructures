from linked_list import LinkedList
from stack import Stack
def two_sum(arr, target):
    """Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    """

    arr_dict = {}

    for x in range(len(arr)):
        arr_dict[arr[x]] =x

    for x in range(len(arr)):
        if target - arr[x] in arr_dict:
            if arr_dict[target-arr[x]] != x:
                return [x,arr_dict[target-arr[x]]]

def longest_substring_without_repeating(str):
    counter = 0
    substr_lens = []
    while counter < len(str):
        chars_set = set()
        chars_set.add(str[counter])

        runner = counter + 1

        while runner < len(str) and str[runner] not in chars_set:
            chars_set.add(str[runner])
            runner += 1

        substr_lens.append(len(chars_set))
        counter = runner

    return max(substr_lens)

def longest_palindromic_substring(str):
    palindromic_lens = []
    for x in range(len(str)):
        for y in range(len(str),x, -1):
            print(str[x:y])
            if x == 0:
                if str[x:y] == str[y::-1]:
                    palindromic_lens.append(len(str[x:y]))
            else:
                if str[x:y] == str[y:x:-1]:
                    palindromic_lens.append(len(str[x:y]))

    return max(palindromic_lens)

def container_with_most_water(heights):
    areas = []
    for x in range(len(heights)):
        x1 = x+1
        for y in range(x-1, -1, -1):
            if heights[y] >= heights[x]:
                x1 = y+1

        x2 = x+1
        for y in range(x+1, len(heights)):
            if heights[y] >= heights[x]:
                x2 = y+1

        areas.append(heights[x]*(x2-x1))


    return max(areas)


def container_with_most_water_optimized(heights):
    max_area = 0
    l_pointer = 0
    r_pointer = len(heights)-1

    while l_pointer < r_pointer:
        min_height = min([heights[l_pointer],heights[r_pointer]])
        max_area = max([max_area, min_height*(r_pointer-l_pointer)])

        if heights[l_pointer] < heights[r_pointer]:
            l_pointer += 1
        else:
            r_pointer -= 1

    return max_area

def two_sum_for(arr, target):
    """Given an arr arr, find elements a,b such that a + b  = target."""

    has_set = set(arr)

    for elements in arr:
        if target - elements in has_set:
            return [elements, target-elements]
    return None
def three_sum(arr):
    """given an array nums of n integers, are there elements a,b,c in arr
    such that a+b+c = 0

    unoptimized.
    """

    results = []
    results_set = []
    for x in range(len(arr)):
        sol = two_sum_for(arr[x+1:], 0-arr[x])
        if sol:
            sol.insert(0, arr[x])
            if set(sol) not in results_set:
                results.append(sol)
                results_set.append(set(sol))

    return results

def remove_nth_node_from_linked_list(linky,n):
    """Remove the nth node from linky, assuming n is always valid."""
    length_of_list = len(linky)
    index_to_remove = length_of_list - n

    counter = 0
    curr = linky.first

    while counter < index_to_remove-1:
        curr = curr.next
        counter += 1

    curr.next = curr.next.next

def remove_nth_node_one_pass(linky, n):
    """"Remove the nth node from the end from a linky in one pass."""
    curr = linky.first

    while curr:
        temp = curr
        for x in range(n):
            temp = temp.next

        if not temp.next:
            curr.next = curr.next.next
            break
        curr = curr.next

def valid_parentheses(paren_str):
    """Given a str of parentheses, return if it is valid."""
    stack = Stack()
    valid_map = {"}":"{",")":"(","]":"["}
    for items in paren_str:
        if items == "(" or items == "{" or items == "[":
            stack.push(items)

        else:
            if stack.is_empty():
                return False

            if stack.pop() != valid_map[items]:
                return False

    if not stack.is_empty:
        return False

    return True

def merge_linkys(linky1, linky2):
    merged_list = LinkedList()
    curr1 = linky1.first
    curr2 = linky2.first

    while curr1 and curr2:
        if curr1.item < curr2.item:
            merged_list.add(curr1.item)
            curr1 = curr1.next

        else:
            merged_list.add(curr2.item)
            curr2 = curr2.next

    if curr1:
        while curr1:
            merged_list.add(curr1.item)
            curr1 = curr1.next

    else:
        while curr2:
            merged_list.add(curr2.item)
            curr2 = curr2.next

    merged_list.reverse()

    return merged_list




l = LinkedList()
l.append(1)
l.append(2)
l.append(4)
l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)
print(merge_linkys(l,l2))
