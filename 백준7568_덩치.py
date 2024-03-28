import sys


def function():
    # 전체 사람 수
    N = int(input())

    deongchi = []
    for i in range(N):
        weight, hight = map(int, sys.stdin.readline().split())
        deongchi.append([i, weight, hight])

    # 정렬
    deongchi.sort(key=lambda x: (-x[1], -x[2]))

    # 순위 리스트 세팅
    score_list = [0 for _ in range(N)]

    for i in range(len(deongchi)):
        score = 1

        if i > 0:
            for j in range(i):
                if deongchi[j][1] > deongchi[i][1] and deongchi[j][2] > deongchi[i][2]:
                    score += 1

        score_list[deongchi[i][0]] = score

    print(" ".join(map(str, score_list)))


if __name__ == "__main__":
    function()