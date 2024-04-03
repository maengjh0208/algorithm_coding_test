def solution(s):
    s = list(s)
    return "".join(sorted(s, reverse=True))


if __name__ == "__main__":
    result = solution("Zbcdefg")

    print(result)
    print(result == "gfedcbZ")