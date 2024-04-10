def solution(x):
    str_x = str(x)
    sum_value = sum(map(int, str_x))
    return True if x % sum_value == 0 else False


if __name__ == "__main__":
    result = solution(10)
    print(result)