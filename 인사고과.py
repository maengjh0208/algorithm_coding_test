# 점수 종류 2개 있음 (근무 태도 점수, 동료 평가 점수)
# 다른 임의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 존재한다면 해당 사원은 인센티브 못받음
# 그 외 사원은 두 점수의 합이 높은 순으로 석차를 내서 인센티브 차등 지급
# 동석차 수 만큼 다음 석차는 건너뜀 (ex 1등이 2명이라면 2등 없이 다음 석차는 3등)
# 완호(scores의 첫번째 값)의 등수를 리턴. 인센티브 못받는 경우엔 -1 리턴

def solution(scores: list):
    target = scores[0]

    scores.sort(key=lambda x: (-x[0], x[1]))
    new_scores = [scores[0]]  # 인센티브 받는 사원 리스트

    # 인센티브 받는 사원 골라내기
    max_b = scores[0][1]
    for i in range(1, len(scores)):
        if scores[i][1] < max_b:
            # 완호가 인센티브 못받는 경우 -1 리턴
            if target == scores[i]: return -1
        else:
            new_scores.append(scores[i])
            max_b = max(max_b, scores[i][1])

    # 점수 합이 큰 순서대로 정렬
    new_scores.sort(key=lambda x: -sum(x))

    rank = 1
    for i in range(len(new_scores)):
        if i != 0 and sum(new_scores[i - 1]) > sum(new_scores[i]):
            rank = i + 1

        # 완호의 등 수 리턴
        if target == new_scores[i]:
            return rank


if __name__ == "__main__":
    result = solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]])
    print(result)
