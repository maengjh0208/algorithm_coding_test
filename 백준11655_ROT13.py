def function():
    origin_words = input()

    alphabet = {
        "a": "n",
        "A": "N",
        "b": "o",
        "B": "O",
        "c": "p",
        "C": "P",
        "d": "q",
        "D": "Q",
        "e": "r",
        "E": "R",
        "f": "s",
        "F": "S",
        "g": "t",
        "G": "T",
        "h": "u",
        "H": "U",
        "i": "v",
        "I": "V",
        "j": "w",
        "J": "W",
        "k": "x",
        "K": "X",
        "l": "y",
        "L": "Y",
        "m": "z",
        "M": "Z",
        "n": "a",
        "N": "A",
        "o": "b",
        "O": "B",
        "p": "c",
        "P": "C",
        "q": "d",
        "Q": "D",
        "r": "e",
        "R": "E",
        "s": "f",
        "S": "F",
        "t": "g",
        "T": "G",
        "u": "h",
        "U": "H",
        "v": "i",
        "V": "I",
        "w": "j",
        "W": "J",
        "x": "k",
        "X": "K",
        "y": "l",
        "Y": "L",
        "z": "m",
        "Z": "M"
    }

    encoded_words = []
    for i in origin_words:
        if i in alphabet.keys():
            encoded_words.append(alphabet[i])
        else:
            encoded_words.append(i)

    print("".join(encoded_words))


if __name__ == "__main__":
    function()