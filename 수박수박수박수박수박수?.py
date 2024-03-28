
import time


@profile
def solution(n):
    words = ["수" if num % 2 == 0 else "박" for num in range(10000)]
    answer = "".join(words[:n])
    return answer

@profile
def solution2(n):
    words = "수박" * (n // 2 + 1)
    answer = words[:n]
    return answer


if __name__ == "__main__":
    start_time = time.time()
    print(solution2(100))
    end_time = time.time()
    print(end_time - start_time)

    start_time = time.time()
    print(solution(100))
    end_time = time.time()
    print(end_time - start_time)
