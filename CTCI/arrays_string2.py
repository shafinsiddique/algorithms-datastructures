def check_removal(larger_string, smaller_string):
    """

    """
    for x in range(len(larger_string)):
        if x == 0:
            if larger_string[1:] == smaller_string:
                return True

        else:
            if larger_string[:x] + larger_string[x+1:] == smaller_string:
                return True

    return False

def check_replace(string1, string2):
    """Assume len(string1) == len(string2) """

    for x in range(len(string1)):
        if string1[x] != string2[x]:
            if string1[:x] + string2[x] + string1[x+1:] == string2:
                return True

    return False


def one_away(string1, string2):
    """Given two strings, return True if they are one away: which means
    """

    if len(string1) == len(string2) + 1:
        return check_removal(string1, string2)

    elif len(string2) == len(string1) + 1:
        return check_removal(string2, string1)

    elif len(string1) == len(string2):
        if string1 == string2:
            return True

        return check_replace(string1, string2)

    return False


def string_compression(string1):
    """implememnt a method to perform basic string compression using the counts
    of repeated characters."""

    compressed_string = ""
    curr_char = ""
    curr_char_count = 0
    for x in range(len(string1)):
        if x == len(string1)-1:
            compressed_string += curr_char + str(curr_char_count + 1)

        else:
            if string1[x] != string1[x+1]:
                compressed_string += string1[x] + str(curr_char_count + 1)

                curr_char = string1[x+1]
                curr_char_count = 0
            else:
                curr_char = string1[x]
                curr_char_count += 1
    return compressed_string

def rotate_matrix(matrix):
    """matrix rotation o(n) space."""
    rotated = []

    for x in range(len(matrix)-1,-1,-1):
        rotated.append([row[x] for row in matrix])
    return rotated

def zero_matrix(matrix):
    """Write an algorithm such that if an element in MxN matrix is 0, its
    entire row and columns are set to 0."""

    rows = set()
    cols = set()

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if x in rows or y in cols:
                matrix[x][y] = 0

    return matrix

print(zero_matrix([[1,2,3,0],[4,5,6,0]]))