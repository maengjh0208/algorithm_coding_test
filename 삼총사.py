# 문제링크: school.programmers.co.kr/learn/courses/30/lessons/131705
# 학생들이 각자 정수 번호를 갖는다.
# 학생 3명의 정수 번호를 더했을 때 0이 되면 삼총사

from itertools import combinations


def solution(number: list):
    count = 0

    for p in combinations(number, 3):
        if sum(p) == 0:
            count += 1

    return count


if __name__ == "__main__":
    result = solution([-2, 3, 0, 2, -5])

    print(result)
    print(result == 2)