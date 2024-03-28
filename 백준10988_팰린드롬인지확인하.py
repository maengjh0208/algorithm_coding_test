def function():
    # 거꾸로 했을때에도 동일한 단어가 되면 팰린드롬 단어이다.
    # 팰린드롬 단어이면 1, 아니면 0 출력

    word = input()  # 소문자로만 이뤄진 단어 입력

    if word == word[::-1]:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    function()