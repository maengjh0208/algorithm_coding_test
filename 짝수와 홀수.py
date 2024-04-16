def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    result = solution(3)
    print(result)