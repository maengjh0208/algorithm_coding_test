def solution(n):
    answer = 0
    while n != 0:
        answer += n % 10
        n //= 10

    return answer


result = solution(123)
print(result)
