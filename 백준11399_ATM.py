def function():
    # 입력값 받기 N: 사람수 / times: 각 사람이 돈을 인출하는데 걸리는 시간
    N = int(input())
    times = list(map(int, input().split()))

    # 정렬
    times.sort()

    times_sum = 0
    for i in range(N):
        times_sum += (N - i) * times[i]

    print(times_sum)


if __name__ == "__main__":
    function()