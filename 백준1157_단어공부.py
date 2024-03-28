import collections


def function():
    word = input().lower()

    word_dict = collections.Counter(word)

    # 가장 자주 등장한 알파벳 단어 리스트 (최대 2개 알파벳 단어 구하기)
    most_common_list = word_dict.most_common(2)

    # 가장 많이 사용된 알파벳 단어 여러개인 경우 '?' 출력
    if len(most_common_list) > 1 and most_common_list[0][1] == most_common_list[1][1]:
        print("?")
    # 그 외, 가장 많이 사용된 알파벳 단어를 대문자로 출력
    else:
        print(most_common_list[0][0].upper())


if __name__ == "__main__":
    function()