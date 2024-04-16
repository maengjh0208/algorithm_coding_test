# n: 처음 갖고 있는 병사 수, k: 무적권 횟수, enemy: 매 라운드마다 공격해오는 적의 수 리스트
# 최대 몇 라운드까지 막을 수 있는지 리턴
from heapq import heappop, heappush


def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)

    round = 0

    queue = []
    for i in range(k):
        heappush(queue, enemy[i])

    for num in enemy[k:]:
        if queue[0] < num:
            if n >= queue[0]:
                n -= heappop(queue)
                heappush(queue, num)
                round += 1
            else:
                break
        else:
            if n >= num:
                n -= num
                round += 1
            else:
                break

    round += k
    return round


if __name__ == "__main__":
    result = solution(7, 3, [4, 2, 4, 5, 3, 3, 1])

    print(result)
