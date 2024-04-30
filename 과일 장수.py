# p(상자에 담긴 사과 중 가장 낮은 점수) * m(상자에 담긴 사과 개수) : 사과 한 상자 가격

def solution(k, m, score):
    score.sort()

    p = 0  # 임의 값 설정
    result = 0  # 최대 이익

    for _ in range(len(score) // m):
        for _ in range(m):
            p = score.pop()

        result += p * m

    return result


if __name__ == "__main__":
    result = solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
    print(result)
