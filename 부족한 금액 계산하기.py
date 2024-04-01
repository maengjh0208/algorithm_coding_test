# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 놀이기구 첫 이용로: price, N번째 이용로: N * price
# 놀이기구를 count번 탈 경우, 얼마가 모자라는지 return. 금액이 부족하지 않을경우 0 return


def solution(price: int, money: int, count: int):
    total_price = int((count * (count + 1) / 2) * price)

    if money >= total_price:
        return 0
    else:
        return total_price - money


if __name__ == "__main__":
    result = solution(3, 20, 4)

    print(result)
    print(result == 10)  # 정답