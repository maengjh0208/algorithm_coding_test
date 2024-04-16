def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


if __name__ == "__main__":
    result = solution(["abce", "abcd", "cdx"], 2)
    print(result)
