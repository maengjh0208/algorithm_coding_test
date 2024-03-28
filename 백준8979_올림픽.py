import sys


def function():
    # N: 국가 수 / K: 등수를 알고 싶은 국가
    N, K = map(int, input().split())

    # 각 국가별 메달 정보 list[list] : [[국가번호, 금메달 개수, 은메달 개수, 동메달 개수], ...]
    medals = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 정렬
    medals.sort(key = lambda x : (-x[1], -x[2], -x[3]))

    rank = 1
    for i in range(len(medals)):
        if i > 0 and medals[i][1:] != medals[i-1][1:]:
            rank = i + 1

        if medals[i][0] == K:
            print(rank)
            break


if __name__ == "__main__":
    function()
