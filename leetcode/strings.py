"""This section consists of leetcode easy questions from the Strings Section."""
def toLowerCase(s: str) -> str:
    """THis function returns a string in all lowercase."""

    return s.lower()

def uniqueMorseCodes(l: list) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.",
             "--.","....","..",".---","-.-",".-..",
             "--","-.","---",".--.","--.-",".-.","...",
             "-","..-","...-",".--","-..-","-.--","--.."]

    converted = []
    for strs in l:
        translation = ""

        for characters in strs:
            # print(ord(characters)-96-1)
            translation+= morse[ord(characters)-96-1]

        converted.append(translation)

    final_list = []

    for words in converted:
        if words not in final_list:
            final_list.append(words)

    return len(final_list)


def unique_email_address(e: list) -> int:
    mailing_list = []

    for emails in e:
        # can be optimized here if we write an if statement.
        localname = emails[:emails.index("@")-1]

        temp_email = ""

        for chars in localname[:localname.index("+")-1]:
            if chars != ".":
                temp_email += chars

        temp_email += emails[emails.index("@"):]

        if temp_email not in mailing_list:
            mailing_list.append(temp_email)

    return len(mailing_list)

def robot_return_to_origin(moves: str) -> bool:
    x = 0
    y = 0

    for move in moves:
        if move == "R":
            x += 1

        elif move == "L":
            x -= 1

        elif move == "U":
            y += 1

        else:
            y -= 1

    return x == 0 and y == 0


def reverse_words_in_string(s):
    """Given a string, reverse the words in the string, while preserving
    the whitespaces."""

    words_wo_sp = s.split(" ")
    reversed_words = []
    for words in words_wo_sp:
        reversed = ""

        for x in range(len(words)-1,-1,-1):
            reversed += words[x]

        reversed_words.append(reversed)

    final_string = ""

    for w in reversed_words:
        final_string += w
        final_string += " "

    return final_string


def _isvowel(c) -> bool:
    vowels = ["a","e","i","o","u", "A","E","I","O","U"]

    return c in vowels

def goat_latin(s):
    sentence = s.split(" ")
    translatedsentence = ""
    for x in range(len(sentence)):
        translatedword = ""
        if _isvowel(sentence[x][0]):
            translatedword += sentence[x] + "ma"


        else:
            translatedword += sentence[x][1:] + sentence[x][0] + "ma"

        translatedword += "a"*x + " "

        translatedsentence += translatedword

    return translatedsentence

def _isnumberlog(s):
    """Return true if it is a number log."""

    ignore_id = s.split(" ")

    for logs in ignore_id[1:]:
        if not logs.isdigit():
            return False

    return True

def bubble_sort_letter(unordered_letter_logs):
    """Sort the unordered letter logs."""


    for x in range(len(unordered_letter_logs)-1): # Probs should use helper method ehre.
        for y in range(x+1, len(unordered_letter_logs)):
            if unordered_letter_logs[x][1:] > unordered_letter_logs[y][1:]:
                unordered_letter_logs[x], unordered_letter_logs[y] = \
                unordered_letter_logs[y], unordered_letter_logs[x]

            elif unordered_letter_logs[x][1:] == unordered_letter_logs[y][1:]:
                if unordered_letter_logs[x] > unordered_letter_logs[y]:
                    unordered_letter_logs[x], unordered_letter_logs[y] = \
                        unordered_letter_logs[y], unordered_letter_logs[x]



def reorder_log_files(logs: list) -> list:
    """Given a list of logs, return them in the proper order."""

    number_logs = []
    unordered_letter_logs = []


    for log in logs:
        if _isnumberlog(log):
            number_logs.append(log)

        else:
            unordered_letter_logs.append(log)

    bubble_sort_letter(unordered_letter_logs)
    unordered_letter_logs.extend(number_logs)

    return unordered_letter_logs

def _getsubsequence(s):
    subsequences = []

    for x in range(len(s)):
        for y in range(len(s), x, -1):
            subsequences.append(s[x:y])

    return subsequences

def lowest_uncommon_subsequence(s1, s2):
    """return the length of the longest uncommon subsequence"""

    s1_sub = _getsubsequence(s1)
    s2_sub = _getsubsequence(s2)

    uncommon_subs = []

    for subs in s1_sub:
        if subs not in s2_sub:
            uncommon_subs.append(subs)

    for subs in s2_sub:
        if subs not in s1_sub:
            uncommon_subs.append(subs)

    lengths = [len(subs) for subs in uncommon_subs]

    return max(lengths)

def ransom_note(s1, s2):
    for characters in s1:
        if characters in s2:
            index = s2.index(characters)

            temp_string = ""

            for x in range(len(s2)):
                if x != index:
                    temp_string += s2[x]


            s2 = temp_string

        else:
            return False

    return True

def grouped_together(s):
    for x in range(len(s)-1):
        if s[x] != s[x+1]:
            if s[x] in s[x+1:]:
                return False

    return True
def _checkequality(s):
    onecount = 0
    zerocount = 0


    for chars in s:
        if chars == "1":
            onecount += 1

        else:
            zerocount += 1

    return onecount == zerocount
def _getsubstrings(s):
    equal_substrings = []

    for x in range(len(s)):
        for y in range(len(s),x,-1):
            substring = s[x:y]
            if _checkequality(substring) and grouped_together(substring):

                equal_substrings.append(substring)

    return equal_substrings


def count_binary_substrings(s):
    """Given a string, count the number of substrings that have equal number of
    consecutive 1 and 0s."""

    return len(_getsubstrings(s))


def attendancerecord(s):
    """Given an attendance record, return whether the student is eligible
    for an award.
    """

    if s.count("A") > 1:
        return False

    else:
        for x in range(len(s)-2):
            if s[x] == "L" and s[x+1] == "L" and s[x+2] == "L":
                return False

    return True


def longpressedname(name, typed):
    if name == typed:
        return True

    else:
        currentindex = 0
        for y in range(len(name)-1):
            if name[y] == typed[currentindex]:
                if name[y] == name[y+1]:
                    currentindex += 1
                else:

                    for x in range(currentindex, len(typed)):
                        if typed[x] != name[y]:
                            currentindex = x
                            break

            else:
                return False

        return True


def swap(s, i, j):
    swapped = ""

    for x in range(len(s)):
        if x == i:
            swapped += s[j]

        elif x == j:
            swapped += s[i]

        else:
            swapped += s[x]

    return swapped
def buddystrings(s1, s2):
    """Given two strings,
    return true if and only if we can swap two letters in A so that a equals B.

    """

    for x in range(len(s1)-1):
        for y in range(x+1, len(s1)):

            swapped = swap(s1, x, y)

            if swapped == s2:
                return True

    return False


def atoi(s):
    s = s.strip()

    if s[0] != '-' and s[0]!='+' and not s[0].isdigit():
        return 0

    else:
        converted = ''

        for characters in s:
            if characters != "+" and characters != "-" and \
                    not characters.isdigit():
                break

            converted += characters

        converted = int(converted)

        if converted < -2**31:
            return -2**31

        elif converted >= 2**31 - 1:
            return 2**31 - 1

        else:
            return converted


print(atoi("-91283472332"))