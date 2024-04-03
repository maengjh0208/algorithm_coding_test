def solution(n: int) -> list:
    n = list(str(n))
    return list(map(int, n[::-1]))


if __name__ == "__main__":
    result = solution(12345)

    print(result)
    print(result == [5,4,3,2,1])