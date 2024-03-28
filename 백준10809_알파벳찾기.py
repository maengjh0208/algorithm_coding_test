def function():
    word = input()

    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    print(" ".join([str(word.find(i)) for i in alphabets]))


if __name__ == "__main__":
    function()