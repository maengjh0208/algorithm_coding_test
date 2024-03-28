def function():
    # N: 분해합
    N = int(input())

    # ex) 자연수 M 의 분해합 = M + M의 각 자릿수 합
    # M의 각 자릿수 합이 가장 큰 경우는 모든 자릿수가 9로 이뤄진 경우이다
    start = N - (N // 10 + 1) * 9
    start = 0 if start < 0 else start

    for M in range(start, N):

        temp = 0  # 각 자릿수 합
        for i in str(M):
            temp += int(i)

        if M + temp == N:
            print(M)
            break
    else:
        print("0")


if __name__ == "__main__":
    function()