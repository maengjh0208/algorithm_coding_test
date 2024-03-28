def function():
    # A : 1대 주차시 한 대당 이용 요금 / B : 2대 주차시 한 대당 이용 요금 / C : 3대 주차시 한 대당 이용 요금
    A, B, C = map(int, input().split())

    # 각 시간별 주차된 차량 수
    cars = [0 for _ in range(100)]

    for _ in range(3):
        arrival, left = map(int, input().split())

        for i in range(arrival, left):
            cars[i-1] += 1

    total_costs = 0
    for num in cars:
        if num == 1:
            total_costs += A
        elif num == 2:
            total_costs += B * 2
        elif num == 3:
            total_costs += C * 3
        else:
            pass

    print(total_costs)


if __name__ == "__main__":
    function()