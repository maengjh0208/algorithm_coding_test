def solution(x, n):
    return [x * i for i in range(1, n + 1)]


if __name__ == "__main__":
    result = solution(2, 5)
    print(result)