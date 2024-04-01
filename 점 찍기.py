# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k: int, d: int) -> int:
    count = 0

    for y in range(0, d + 1, k):
        x = int((d ** 2 - y ** 2) ** (0.5))
        count += x // k + 1

    return count


if __name__ == "__main__":
    result = solution(1, 5)

    print(result)
    print(result == 26)