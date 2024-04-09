import heapq


def solution(operations: list) -> list:
    """
    operations 설명
    I 숫자: 숫자 추가
    D -1: 최솟값 제거
    D 1: 최댓값 제거
    """
    max_heap = []  # 숫자가 클수록 우선순위 높음
    min_heap = []  # 숫자가 작을수록 우선순위 높음

    for operation in operations:
        oper, num = operation.split()
        num = int(num)

        # 숫자 추가
        if oper == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        # 숫자 제거
        elif max_heap and oper == "D":
            # 최솟값 제거
            if num == -1:
                x = -heapq.heappop(min_heap)

                max_heap.remove(x)
                heapq.heapify(max_heap)

            # 최댓값 제거
            elif num == 1:
                x = -heapq.heappop(max_heap)

                min_heap.remove(x)
                heapq.heapify(min_heap)

    max_value, min_value = 0, 0
    if max_heap:
        max_value = -heapq.heappop(max_heap)
        min_value = heapq.heappop(min_heap)

    return [max_value, min_value]


if __name__ == "__main__":
    result = solution(["I 1", "I 2", "D 1", "D -1", "I 3", "I 4", "D 1"])

    print(result)