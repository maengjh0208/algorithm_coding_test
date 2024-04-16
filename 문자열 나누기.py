def solution(s: str):
    count = 0  # 분리된 문자열 개수

    # 초기화 필요한 변수들 (start: 시작 문자, start_count: 시작 문자 개수, other_count: 시작 문자 제외한 나머지 문자 개수, change: 초기화 필요 여부)
    start = s[0]
    start_count = 1
    other_count = 0
    change = False

    for c in s[1:]:
        # 초기화
        if change:
            start = c
            start_count = 1
            other_count = 0
            change = False
            continue

        if c == start:
            start_count += 1
        else:
            other_count += 1

        if start_count == other_count:
            count += 1
            change = True

    # 마지막 문자열이 분해되지 않는 경우
    if start_count != other_count:
        count += 1

    return count


if __name__ == "__main__":
    result = solution("banana")
    print(result)
