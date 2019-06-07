def isUnique(s):
    """Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures."""
    counter = 0
    for characters in s:
        if characters in s[counter+1:]:
            return False

        counter += 1

    return True

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

print(urlify(" Mr John Smith    "))