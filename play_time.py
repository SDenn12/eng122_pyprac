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
#             stored[letter] += 1
#         else:
#             pass
#     print(stored)
#     for value in stored.values():
#         if value > 1:
#             count += 1
#         else:
#             pass
#     return count


# def duplicate_count(s):
#     # sets cant contain duplicates. means for loop gives a 'list' of the unique characters. Then runs through the list
#     # of unique characters and appends them if the count is greater than 2.
#     return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
#

# print(duplicate_count("abcde"))
# print(duplicate_count("aabBcde"))

# def DNA_strand(dna):
#     # swap letters a for t and c for g
#     return "".join([c.replace("A","1").replace("T","2").replace("C","3").replace("G","4").replace("1", "T").replace("2", "A").replace("3", "G").replace("4", "C") for c in dna])
#
#         #.replace("1", "T").replace("2", "A").replace("3", "G").replace("4", "C")
# print(DNA_strand("ATAT"))
# def longest(s1, s2):
#     # your code
#     return ''.join(sorted(list(set(s1 + s2))))
#
#
# print(longest("asdf", "hgdf"))

def move_zeros(lst):
    return [lst.remove(0).append(0) for c in lst.count(0)]