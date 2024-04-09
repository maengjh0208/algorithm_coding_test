

def solution(number, limit, power):
    # 약수 개수 리스트
    number_of_divisors = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(1, number // i + 1):
            number_of_divisors[i * j] += 1

    # 철 합산
    sum_value = 0
    for i in range(1, number + 1):
        count = number_of_divisors[i]
        sum_value = sum_value + count if count <= limit else sum_value + power

    return sum_value


if __name__ == "__main__":
    result = solution(5, 3, 2)
    print(result)