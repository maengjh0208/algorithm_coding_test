def solution(word):
    vowels = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    value = [625, 125, 25, 5, 1]

    result = 0
    for idx, c in enumerate(word):
        result += sum(vowels[c] * i for i in value[idx:]) + 1

    return result


if __name__ == "__main__":
    result = solution("EIO")
    print(result)