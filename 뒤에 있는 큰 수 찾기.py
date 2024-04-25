def solution(numbers):
    stack = []  # 자신보다 뒤에 큰 숫자가 없는 numbers의 인덱스만 stack에 남는다.
    result = [-1] * len(numbers)  # 초기 세팅

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]

        stack.append(i)

    return result


if __name__ == "__main__":
    result = solution([9, 1, 5, 3, 6, 2])
    print(result)
