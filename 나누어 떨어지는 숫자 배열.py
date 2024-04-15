def solution(arr, divisor):
    answer = []

    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    return sorted(answer) if answer else [-1]


if __name__ == "__main__":
    result = solution([5, 9, 7, 10], 5)

    print(result)
