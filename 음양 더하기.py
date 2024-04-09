def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        answer = answer + absolute if sign is True else answer - absolute

    return answer


if __name__ == "__main__":
    result = solution(absolutes=[4, 7, 12], signs=[True, False, True])

    print(result)
    print(result == 9)