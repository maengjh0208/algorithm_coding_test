def solution(s):
    idx = -1
    answer = []

    for c in s:
        if c == " ":
            idx = -1
        else:
            idx += 1
            c = c.upper() if idx % 2 == 0 else c.lower()

        answer.append(c)

    return "".join(answer)


if __name__ == "__main__":
    result = solution("try hello world")
    print(result)