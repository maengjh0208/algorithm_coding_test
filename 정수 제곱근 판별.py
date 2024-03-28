import math


def solution(n: int) -> int:
    square_root = math.sqrt(n)

    if square_root - int(square_root) == 0:
        return (int(square_root) + 1) ** 2
    else:
        return -1


if __name__ == "__main__":
    result = solution(121)
    print(result)