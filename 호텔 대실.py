# 한 번 사용한 객실은 퇴실 시간 기준으로 10분간 청소 후 다음 손님을 받을 수 있다.
# 필요한 최소 객실의 수를 리턴
from heapq import heappush, heappop


def add_10_minutes(out_time: int) -> int:
    out_time += 10

    if out_time % 100 >= 60:
        out_time += 40

    return out_time


def solution(book_time: list) -> int:
    for idx in range(len(book_time)):
        start = book_time[idx][0].split(":")
        end = book_time[idx][1].split(":")

        book_time[idx][0] = int(start[0]) * 100 + int(start[1])
        book_time[idx][1] = int(end[0]) * 100 + int(end[1])

    book_time.sort()

    heap = [add_10_minutes(book_time[0][1])]
    max_room = 1

    for start, end in book_time[1:]:
        if heap[0] <= start:
            heappop(heap)
            heappush(heap, add_10_minutes(end))
        else:
            heappush(heap, add_10_minutes(end))
            max_room = max(max_room, len(heap))

    return max_room


if __name__ == "__main__":
    result = solution(
        [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
    )

    print(result)
