# 서로 다른 인덱스에 있는 두개의 수를 뽑아 더해서 만들 수 있는 모든 수를 오름차순으로 리턴

def solution(numbers):
    numbers.sort()
    answer = set()

    for i in range(len(numbers) - 1):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        for j in range(i + 1, len(numbers)):
            add_value = numbers[i] + numbers[j]
            if add_value not in answer:
                answer.add(add_value)

    return sorted(list(answer))


if __name__ == "__main__":
    result = solution([2, 1, 3, 4, 1])
    print(result)