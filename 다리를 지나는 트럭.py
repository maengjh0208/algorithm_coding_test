# link : https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    time = 0
    bridge = deque([])
    truck_weights = deque(truck_weights)
    bridge_weight = 0

    while truck_weights or bridge:
        time += 1

        # 잔재 시간이 bridge_length - 1초가 된 트럭 제거 & 현재 다리 위 총 트럭 무게 업데이트
        if bridge and bridge[0][1] == bridge_length - 1:
            truck_weight, _ = bridge.popleft()
            bridge_weight -= truck_weight

        # 현재 다리위에 있는 트럭의 잔재 시간 1초씩 늘려 주기
        for state in bridge:
            state[1] += 1

        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            truck_weight2 = truck_weights.popleft()

            bridge_weight += truck_weight2
            bridge.append([truck_weight2, 0])

    return time


if __name__ == "__main__":
    result = solution(100, 100, [10])
    print(result)