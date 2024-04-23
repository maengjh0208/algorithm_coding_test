"""
문자열 x 이진변환 방법
1. 문자열 x에서 숫자 0 모두 제거
2. x의 길이를 2진법으로 변경

문자열 x가 "1"이 될 때까지 반복
이진 변환 횟수, 변환 과정에서 제거된 모든 0의 갯수를 리스트 형태로 리턴
"""


def solution(s: str) -> list:
    convert_count = 0
    deleted_zero_count = 0
    while s != "1":
        zero_count = s.count("0")
        deleted_zero_count += zero_count
        convert_count += 1

        s = bin(len(s) - zero_count)[2:]

    return [convert_count, deleted_zero_count]


if __name__ == "__main__":
    result = solution("110010101001")
    print(result)
