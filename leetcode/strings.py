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

print(uniqueMorseCodes(["gin", "zen", "gig", "msg"]))