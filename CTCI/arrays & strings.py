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


def oneAway()

print(checkPermutation("abc","acb"))
print(urlify2("Mr John Smith         "))










