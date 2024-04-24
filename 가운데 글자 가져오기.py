def solution(s):
    middle = len(s) // 2

    if len(s) % 2 != 0:
        return s[middle]
    else:
        return s[middle - 1: middle + 1]


if __name__ == "__main__":
    result = solution("qwer")
    print(result)