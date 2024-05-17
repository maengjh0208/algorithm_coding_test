def solution(happiness: list) -> int:
    # 이거 이렇게 풀면 안됨 ..
    N = len(happiness)
    happiness_value = [1 if num > 8 else -1 for num in happiness]
    result = [0] * N

    count = 0
    value = 0
    for i in range(N):
        if happiness_value[i] < 0 or (i > 0 and happiness_value[i - 1]):
            continue

        for j in range(i, N):
            if value + happiness_value[j] == 0:
                result[i] = count
                value = 0
                count = 0
                break
            else:
                value += happiness_value[j]
                count += 1
                if j == N - 1:
                    result[i] = count

    return max(result)


if __name__ == "__main__":
    result = solution(
        [6, 10, 3, 9, 4, 10, 3, 9, 3, 10, 6]
    )

    print(result)