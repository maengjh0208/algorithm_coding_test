def check(s):
    stack = []
    for c in s:
        if stack and (
                (c == "]" and stack[-1] == "[") or (c == ")" and stack[-1] == "(") or (c == "}" and stack[-1] == "{")):
            stack.pop()
        else:
            stack.append(c)

    return False if stack else True


def solution(s):
    count = 0
    for i in range(len(s)):
        count += check(s[i:] + s[:i])

    return count


if __name__ == "__main__":
    result = solution("[](){}")
    print(result)
