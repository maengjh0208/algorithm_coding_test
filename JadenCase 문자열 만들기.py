# s 구성 요소: 공백, 알파벳, 숫자
# 공백 문자가 연속해서 나올 수 있다.
def solution(s):
    words = []
    for idx, c in enumerate(s):
        if not c.isalpha():
            words.append(c)
        elif idx == 0 or (idx > 0 and s[idx - 1] == " "):
            words.append(c.upper())
        else:
            words.append(c.lower())

    return "".join(words)


if __name__ == "__main__":
    result = solution("3people unFollowed me")
    print(result)
