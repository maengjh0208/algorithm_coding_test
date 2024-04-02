def solution(t, p):
    int_p = int(p)
    len_p = len(p)
    count = 0

    for i in range(len(t) - len_p + 1):
        if int(t[i : i + len_p]) <= int_p:
            count += 1

    return count


if __name__ == "__main__":
    result = solution("500220839878", "7")

    print(result)
    print(result == 8)