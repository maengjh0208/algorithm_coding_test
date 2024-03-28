def solution(a, b):
    big = max(a, b)
    small = min(a, b)

    return int(big * (big + 1) / 2 - (small - 1) * small / 2)


if __name__ == "__main__":
    result = solution(3,5) # 12
    print(result)