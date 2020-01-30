def isUnique(s):
    """Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures."""
    counter = 0
    for characters in s:
        if characters in s[counter+1:]:
            return False

        counter += 1

    return True

def permutations(string):
    """Create all permutations of a string with non-repeating characters
    """
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string.replace(char, ""))]
    return permutation_list

def isPermutation(s,s2):
    """Given two strings, write a method to decide if one is a permutation of another."""

    for characters in s:
        if s.count(characters) != s2.count(characters):
            return False

    return True

def urlify(s):
    s = s.rstrip()
    """Replace all characters in s with %20."""
    finalstring = ""
    for characters in s:
        if characters == " ":
            finalstring += "%20"

        else:
            finalstring += characters
    return finalstring

def isPalindrome(s):
    return s[:] == s[::-1]

def palindrome_permutation(s):
    """Given a string, determine if it is a permutation of a palindrome."""

    for permutation in permutations(s):
        if isPalindrome(permutation):
            return True

    return False

def rotateArray(l):
    """Given an n x n matri, rorate it by 90 degrees."""

    rotatedArray = []

    for x in range(len(l[0])):
        row = []
        for y in range(len(l)):
            row.append(l[y][x])

        rotatedArray.insert(0, row)

    for tiems in rotatedArray:
        l.pop(0)
        l.append(tiems)

def zeroMatrix(l):
    """Zero Matrix."""
    rowsToZero  = []
    colsToZero =  []
    for x in range(len(l)):
        for y in range(len(l[0])):
            if l[x][y] == 0:
                if x not in rowsToZero:
                    rowsToZero.append(x)
                if y not in colsToZero:
                    colsToZero.append(y)

    for rows in rowsToZero:
        for x in range(len(l[rows])):
            l[rows][x] = 0


    for cols in colsToZero:
        for x in range(len(l)):
            l[x][cols] = 0

def isUnique2(s: str):
    """Implement an algorithm to determine if a string has all unique characters.

    What if you can't use addiitonal data strucutres??"""

    for x in range(len(s)):
        if s[x] in s[x+1:]:
            return False

    return True

def isUnqiue3(s: str):
    items = {}

    for item in s:
        if item in items:
            return False

        else:
            items[item] = None

    return True

def checkPermutation(s1, s2):
    """
    Given two strings, write an algorithm to determine if one is a permutation of the other.

    return true if s1 is a permutation of s2.
    """

    items = {}

    for letter in s2:
        if letter in items:
            items[letter] += 1

        else:
            items[letter] = 0
    items2 = {}
    for letter in s1:
        if letter in items2:
            items2[letter] += 1

        else:
            items2[letter] = 0

    return items == items2

def urlify2(s: str):
    """Write a method to replaces all spaces in a string with %20."""

    newString = s.strip()

    newString = newString.replace(" ", "%20")

    return newString

def oneDeleteAway(s1, s2):
    """

    Return true if 's1' is ONE DELETE AWAY FROM 's2.'

    S1 is one delete away if it has one element greater than s1 and if that element is taken away,
    the two strings match.
    """
    if len(s1) == len(s2) + 1:
        for x in range(len(s1)):
            newString = ""

            for y in range(len(s1)):
                if y != x:
                    newString += s1[y]

            if newString == s2:
                return True
    return False

def oneReplaceAway(s1, s2):
    if len(s1) == len(s2):
        for x in range(len(s1)):
            if s1[:x] + s2[x] + s1[x+1:] == s2:
                return True


    return False
def oneInsertionAway(s1, s2):
    """Return true if 's1' is ONE INSERTION AWAY from 's2'

    's1' is insertion away if len of s1 is one less than the len of s2."""

    if len(s1) == len(s2) - 1:
        if s1 == "" or s1[0] != s2[0]:
            return s2[0] + s1 == s2
        else:
            counter = 0

            while counter < len(s1) and s1[counter] == s2[counter]:
                counter += 1

            if counter == len(s1):
                return s1 + s2[-1] == s2

            else:
                return s1[:counter] + s2[counter] + s1[counter:] == s2

    return False



def oneAway(s1, s2):
    """Three types of edits can be made on strings.

    Replace, delete and insert character.

    Return true if s1 and s2 are either one or 0 edits away."""

    if s1 == s2:
        return True

    else:
        if len(s1) < len(s2):
            return oneInsertionAway(s1, s2)

        elif len(s1)  > len(s2):
            return oneDeleteAway(s1, s2)

        else:
            return oneReplaceAway(s1, s2)

def stringCompression(s):
    """

    implement a method to perform basic string compression using the counts of repeated characters.

    """

    newString = ""
    compareOld = ""
    counter = 0

    while counter < len(s):
        char = s[counter]
        compareOld += char + "1"

        charCounter = counter + 1

        while charCounter < len(s) and s[charCounter] == s[counter]:
            charCounter += 1


        newString += char + str(charCounter-counter)

        counter = charCounter

    if compareOld == newString:
        return s

    return newString

def rotateMatrix(nums: list):
    """Write a method to rotate the image by 90 degrees."""

    rotated = []

    for x in range(len(nums)-1,-1,-1):
        rotated.append([lists[x] for lists in nums])

    return rotated

def rotateMatrixInPlace(matrix: list):
    """

    Rotate the matrix in-place.

    """
    column = len(matrix)-1
    for x in range(len(matrix)):
        list = matrix[x]

        list[0],list[-1] = list[-1],list[0] # first swap the first and last element.

        for y in range(x+1, len(matrix)):
            list[y],matrix[y][column] = matrix[y][column],list[y] # then swap the other elements.

        column -= 1


def clearRowAndColumn(matrix, row, column):
    for x in range(len(matrix[row])): #### clear Row.
        matrix[row][x] = 0

    for arrays in matrix:
        arrays[column] =0



def zeroM(matrix: list):
    """

    Write an algorithm such that if an element in an MxM matrix is 0, its entire row
    and columns are set to 0.

    """
    rows = []
    cols = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0 and x not in rows and y not in cols:
                clearRowAndColumn(matrix, x, y)
                rows.append(x)
                cols.append(y)

                break


def rbc(a, b):
    x = a
    y = b

    while (x != y):
        if (x > y):
            x = x - y

        else:
            y = y - x

    return x

print(rbc(2475, 875))