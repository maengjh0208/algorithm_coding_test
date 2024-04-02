# 입력된 수가 짝수라면 2로 나눈다..
# 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
# 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
# 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환한다.

def solution(num):
    count = 0

    while num != 1:
        count += 1

        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1

        if count == 500 and num != 1:
            return -1

    return count


if __name__ == "__main__":
    result = solution(6)

    print(result)
    print(result == 8)