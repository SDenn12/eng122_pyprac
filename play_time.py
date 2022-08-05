# import string
#
#
# def alphabet_position(text):
#     alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
#                "o","p","q","r","s","t","u","v","w","x","y","z"]
#     positions = []
#     text = text.replace(" ","")
#     for punc in string.punctuation:
#         text = text.replace(punc, "")
#     for letter in text.lower():
#         positions.append(str(int(alphabet.index(letter))+1))
#
#     positions = " ".join(positions)
#     return positions
#
#
# print(alphabet_position("The sunset sets at twelve o' clock."))

# BEST SOLUTION
# def alphabet_position_(s):
#     # ord retrieves the ascii number of the character (subtracting from ascii
#     # and adding 1 gives the alphabet position). This cycles for all characters
#     # as long as they are in the alphabet.
# #   return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
# def duplicate_count(text):
#     stored = {}
#     count = 0
#     for letter in text.lower():
#         if letter.isalpha() and letter not in stored.keys() or letter.isdigit() and letter not in stored.keys():
#             stored[letter] = 1
#         elif letter.isalpha() and letter in stored.keys() or letter.isdigit() and letter in stored.keys():
#             stored[letter] = 2
#         else:
#             pass
#     print(stored)
#     for value in stored.values():
#         if value > 1:
#             count += 1
#         else:
#             pass
#     return count


def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


print(duplicate_count("abcde"))
print(duplicate_count("aabBcde"))