# 각 문자열을 작성하기 위해 키를 최소 몇번씩 눌러야 하는지 배열에 담아 리턴
# 작성이 불가능한 경우는 -1로 저장
INF = 1000


def solution(keymap, targets):
    # 알파벳: (최소 누르는 횟수, keymap 인덱스)
    alphabets = {i: INF for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    for keys in keymap:
        for idx, key in enumerate(keys):
            alphabets[key] = min(alphabets[key], idx + 1)

    result = []
    for target in targets:
        count = 0
        for key in target:
            if alphabets[key] == INF:
                result.append(-1)
                break
            else:
                count += alphabets[key]
        else:
            result.append(count)

    return result


if __name__ == "__main__":
    result = solution(
        keymap=["ABACD", "BCEFD"],
        targets=["ABCD", "AABB"],
    )
    print(result)
