def solution(s, n):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_case_dict = {c: idx for idx, c in enumerate(upper_case)}

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    lower_case_dict = {c: idx for idx, c in enumerate(lower_case)}

    result = []
    for c in s:
        if not c.isalpha():
            result.append(c)
        elif c.islower():
            result.append(lower_case[(lower_case_dict[c] + n) % 26])
        else:
            result.append(upper_case[(upper_case_dict[c] + n) % 26])

    return "".join(result)


if __name__ == "__main__":
    result = solution("AB", 1)
    print(result)
