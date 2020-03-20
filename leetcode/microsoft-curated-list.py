from stack import Stack
from linked_list import LinkedList,Node

def largest_container_with_water(arr):
    """given an arr of heights, find the largest container ."""

    l_counter = 0
    r_counter = len(arr) - 1
    max_height = 0
    while l_counter < r_counter:
        min_of_the_two = min([arr[l_counter], arr[r_counter]])
        max_height = max([max_height, min_of_the_two * (r_counter - l_counter)])

        if arr[r_counter] < arr[l_counter]:
            r_counter -= 1

        else:
            l_counter += 1

    return max_height


def warm_temperatures(arr):
    temperature_stack = Stack()
    temperature_dict = {}
    for x in range(len(arr)):
        if temperature_stack.is_empty():
            temperature_stack.push([x, arr[x]])

        else:
            counter = 1
            while not temperature_stack.is_empty() and arr[x] > temperature_stack.peek()[1]:
                temperature_dict[temperature_stack.pop()[0]] = counter
                counter += 1

            temperature_stack.push([x, arr[x]])

    days = []

    for x in range(len(arr)):
        if x in temperature_dict:
            days.append(temperature_dict[x])

        else:
            days.append(0)

    return days


def run_length_decoding(string):
    '''given an encoded string, return its decoded version.'''
    decoded = ""
    curr_point = 0

    while curr_point < len(string):
        if string[curr_point]!="]":
            if string[curr_point].isdigit():
                number = ""
                while string[curr_point]!="[":
                    number += string[curr_point]
                    curr_point += 1

                starting_bracket = curr_point
                bracket_stack = Stack()
                bracket_stack.push("[")
                curr_point += 1
                while not bracket_stack.is_empty():
                    if string[curr_point] == "[":
                        bracket_stack.push("[")

                    elif string[curr_point] == "]":
                        bracket_stack.pop()

                    curr_point += 1
                decoded += int(number)*run_length_decoding(string[starting_bracket+1:])

            else:
                decoded += string[curr_point]

                curr_point += 1
        else:
            curr_point += 1
    return decoded


def bottom_left_tree_value(tree):
    """given a binary tree, """

    queue = [tree]
    left_most_value = tree.root
    while queue:
        for x in range(len(queue)):
            tree_in_level = queue.pop(0)
            if x == 0:
                left_most_value = tree_in_level.root

            if tree_in_level.left.root:
                queue.append(tree_in_level.left)

            if tree_in_level.right.root:
                queue.append(tree_in_level.right)
    return left_most_value


def longest_palindrome_in_s(string):
    '''given a string, find the longest palindromic substring.'''

    for x in range(len(string)):
        for y in range(len(string), x, -1):
            substring = string[x:y]
            reversed_substring = string[y-1:x-1:-1]
            if substring == reversed_substring:
                return substring


def longest_substring_without_repeating_characters(string):
    '''given a string, find the longest subtstring
    without repeating characters.'''
    max_without_repeating = 0
    index = 0

    while index < len(string):
        elements_in_current_subs = set()
        elements_in_current_subs.add(string[index])

        second_counter = index + 1
        while second_counter < len(string) and string[second_counter] not in elements_in_current_subs:
            elements_in_current_subs.add(string[second_counter])
            second_counter += 1

        max_without_repeating = max([max_without_repeating, len(elements_in_current_subs)])
        index = second_counter

    return max_without_repeating


def maximum_width_of_binary_tree(bst):
    """return the maximum of the binary tree."""

    queue = [bst]
    widths = []

    while queue:
        widths.append(len(queue))
        for x in range(len(queue)):
            cur_tree = queue.pop(0)
            queue.append(cur_tree.left)
            queue.append(cur_tree.right)

    return max(widths)


def two_sum(arr, target):
    '''given an arr, return the indices of 2 elements such that they
    add up to target.'''

    sorted_arr = sorted(arr)
    l_pointer = 0
    r_pointer = len(arr)-1

    while l_pointer < r_pointer:
        if sorted_arr[l_pointer] + sorted_arr[r_pointer] == target:
            return [l_pointer, r_pointer]

        elif sorted_arr[l_pointer] + sorted_arr[r_pointer] < target:
            l_pointer += 1

        else:
            r_pointer += 1


def is_palindrome(string):
    processed_string = ""

    for chars in string:
        if chars.isalnum():
            processed_string += chars.lower()

    reversed_string = ""
    for x in range(len(processed_string)-1,-1,-1):
        reversed_string += processed_string[x]

    return processed_string == reversed_string


def string_to_integer_atoi(string):
    '''convert string to integer.'''

    first_digit_index = 0
    while first_digit_index < len(string) and string[first_digit_index] == " ":
        first_digit_index += 1

    if string[first_digit_index] == "+" or string[first_digit_index] == "-":
        last_digit = first_digit_index+1
        while last_digit < len(string) and string[last_digit].isdigit():
            last_digit += 1

        return int(string[first_digit_index:last_digit])

    elif string[first_digit_index].isdigit():
        last_digit = first_digit_index
        while last_digit < len(string) and string[last_digit].isdigit():
            last_digit += 1

        return int(string[first_digit_index:last_digit])

    else:
        return "error"


def reverse_string(string):
    '''return the reversed string.'''

    reversed_string = ""

    for x in range(len(string)-1,-1,-1):
        reversed_string += string[x]

    return reversed_string


def reverse_list(arr):
    r_pointer = len(arr)-1
    for x in range(len(arr)//2):
        arr[x], arr[r_pointer] = arr[r_pointer],arr[x]

        r_pointer -= 1

    return arr


def reverse_items_in_string(string):
    reversed = ""
    cur_index = 0
    while cur_index < len(string):
        if string[cur_index]!= " ":
            word = ""
            while cur_index < len(string) and string[cur_index] != " ":
                word += string[cur_index]
                cur_index += 1

            if reversed == "":
                reversed = word

            else:
                reversed = word + " " + reversed

        else:
            cur_index += 1

    return reversed


def reverse_items_string_II(string):

    """do an in-place """
    curr_index = 0
    reversed= ""

    while curr_index < len(string):
        if string[curr_index]!= " ":
            word = ""
            while curr_index < len(string) and string[curr_index] != " ":
                word += string[curr_index]
                curr_index += 1

            if reversed == "":
                reversed = word

            else:
                reversed = word + " " + reversed

        else:
            curr_index += 1

    for x in range(len(reversed)):
        string[x] = reversed[x]

    return string


def valid_parenthesis(string):
    temp_stack = Stack()

    valid_dict=  {"]":"[","}":"{",")":"("}

    for chars in string:
        if chars in valid_dict:
            # we encountered a closing bracket
            if temp_stack.is_empty():
                return False

            if valid_dict[chars] != temp_stack.pop():
                return False

        else:
            temp_stack.push(chars)

    if not temp_stack.is_empty():
        return False

    return True


def group_anagrams(words):
    serialization_dict = {}
    for word in words:
        char_count = {}
        ser = ""
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        sorted_char_count = sorted(char_count.items(), key=lambda x: x[0])

        for tuples in sorted_char_count:
            ser += tuples[0] + str(tuples[1])

        if ser in serialization_dict:
            serialization_dict[ser].append(word)

        else:
            serialization_dict[ser] = [word]

    return list(serialization_dict.values())


def intersection_of_linkys(linky1, linky2):
    len1 = len(linky1)
    len2 = len(linky2)

    if len1 > len2:
        first = linky1.first
        second = linky2.first
        bigger = len1
        smaller = len2

    else:
        first = linky2.first
        second = linky1.first
        bigger = len2
        smaller = len1

    for x in range(bigger-smaller):
        first = first.next

    curr1 = first
    curr2 = second

    while curr1:
        if curr1 is curr2:
            return curr1.item
        curr1 = curr1.next
        curr2 = curr2.next


def best_time_to_buy_stock(arr):
    max_profit = 0
    min_value = max(arr)

    for x in range(len(arr)):
        if arr[x] < min_value:
            min_value = arr[x]

        elif arr[x] - min_value > max_profit:
            max_profit = arr[x]-min_value

    return max_profit


def is_palindrome_2(string):
    """given a string, determine if it is a palindrome, ignoring cases and  non alphanumeric cases."""

    processed_string = ""

    for chars in string:
        if chars.isalnum():
            processed_string += chars.lower()

    return processed_string == processed_string[::-1]


def string_to_integer(string):
    """convert the following string to integer."""

    processed_string = string.strip()
    starting = 0

    if processed_string[starting] == '-' or processed_string[starting] == '+':
        starting += 1

    while starting < len(processed_string) and processed_string[starting].isdigit():
        starting += 1

    if starting == 0:
        return -1

    else:
        return int(processed_string[0:starting])


def reverse_string_2(string):
    '''reverse the given string.'''

    reversed_string = ""

    for x in range(len(string)-1,-1,-1):
        reversed_string += string[x]


def reverse_words_in_string2(string):
    """reverse words in the string.

    the sky is blue

    blue is sky the."""

    cur_index = 0
    reversed = ""
    while cur_index < len(string):
        if string[cur_index]!= " ":
            word = ""
            while cur_index < len(string) and string[cur_index] != " ":
                word += string[cur_index]
                cur_index += 1


            if reversed == "":
                reversed = word

            else:
                reversed = word  + " " + reversed

        else:
            cur_index += 1

    return reversed


if __name__ == "__main__":
    pass