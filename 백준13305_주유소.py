import sys


def function():
    N = int(input())
    road_lengths = list(map(int, sys.stdin.readline().split()))
    oil_prices = list(map(int, sys.stdin.readline().split()))

    # 각 구간별 최소 주유 금액
    temp = []

    min_price = oil_prices[0]
    for i in range(len(oil_prices)):
        min_price = oil_prices[i] if oil_prices[i] < min_price else min_price
        temp.append(min_price)

    # 총 주유 금액
    total_price = 0

    for i in range(len(road_lengths)):
        total_price += road_lengths[i] * temp[i]

    print(total_price)


if __name__ == "__main__":
    function()