import string


def alphabet_position(text):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
               "o","p","q","r","s","t","u","v","w","x","y","z"]
    positions = []
    text = text.replace(" ","")
    for punc in string.punctuation:
        text = text.replace(punc, "")
    for letter in text.lower():
        positions.append(str(int(alphabet.index(letter))+1))

    positions = " ".join(positions)
    return positions


print(alphabet_position("The sunset sets at twelve o' clock."))