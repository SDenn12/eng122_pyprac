### Task must return the alphabetic positions of inputted text
```python
# MY SOLUTION:
import string


def alphabet_position(text):
    # defines the letters in the alphabet
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
               "o","p","q","r","s","t","u","v","w","x","y","z"]
    positions = []
    
    # removes the spaces
    text = text.replace(" ","")
    
    # removes all punctuation
    for punc in string.punctuation:
        text = text.replace(punc, "")
    
    #
    for letter in text.lower():
        positions.append(str(int(alphabet.index(letter))+1))

    positions = " ".join(positions)
    return positions


print(alphabet_position("The sunset sets at twelve o' clock."))
# returns 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11

# BEST SOLUTION
def alphabet_position_(s):
    # ord retrieves the ascii number of the character (subtracting from ascii
    # and adding 1 gives the alphabet position). This cycles for all characters
    # as long as they are in the alphabet.
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
```
### Counting duplicates
```python
# My Solution
def duplicate_count(text):
    stored = {}
    count = 0
    for letter in text.lower():
        if letter.isalpha() and letter not in stored.keys() or letter.isdigit() and letter not in stored.keys():
            stored[letter] = 1
        elif letter.isalpha() and letter in stored.keys() or letter.isdigit() and letter in stored.keys():
            stored[letter] += 1
        else:
            pass
    print(stored)
    for value in stored.values():
        if value > 1:
            count += 1
        else:
            pass
    return count

# BEST SOLUTION
def duplicate_count(text):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# sets cant contain duplicates. means for loop gives a 'list' of the unique characters. Then runs through the list
# of unique characters and appends them if the count is greater than 2.
```
### Swap characters in a string in python
```python
# MY SOLUTION
def DNA_strand(dna):
    # swap letters a for t and c for g
    return "".join([c.replace("A","1").replace("T","2").replace("C","3").replace("G","4")
                   .replace("1", "T").replace("2", "A").replace("3", "G").replace("4", "C") 
                    for c in dna])

# BEST SOLUTIONS
#1
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
#2
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])
```
### combine two strings, only presenting distinct characters and sorting them
```python
def longest(s1, s2):
    return ''.join(sorted(list(set(s1 + s2))))
```
### moves the zeros to the end in a list
```python
def move_zeros(lst):
    for i in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)
    return lst
```