def function():
    # T : 테스트 개수
    T = int(input())

    for _ in range(T):
        # H : 층 수 / W : 한층 당 방 개수 / N : N번 째 손님
        H, W, N = map(int, input().split())

        # X : 손님이 배정 받은 층 수 / Y : 손님이 배정 받은 방 번호
        X = N % H
        Y = N // H + 1

        if X == 0:
            X = H
            Y -= 1

        if Y < 10:
            print(f"{X}0{Y}")
        else:
            print(f"{X}{Y}")


if __name__ == "__main__":
    function()