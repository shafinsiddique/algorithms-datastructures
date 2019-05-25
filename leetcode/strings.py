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



print(goat_latin("I speak Goat Latin"))