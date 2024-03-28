def function():
    money = int(input())

    # coin_5: 5원 개수 / coin_2: 2원 개수
    coin_5 = 0
    coin_2 = 0

    n = money // 5  # 몫

    for i in range(n + 1):
        if (money - (n - i) * 5) % 2 == 0:
            coin_5 = (n - i)
            coin_2 = (money - (n - i) * 5) // 2
            break

    total_coin_count = coin_5 + coin_2

    print(total_coin_count if total_coin_count != 0 else -1)


if __name__ == "__main__":
    function()