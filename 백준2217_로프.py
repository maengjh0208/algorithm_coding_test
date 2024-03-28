import sys


def function():
    # 각 로프별 중량(kg)
    weight = []
    for _ in range(int(input())):
        weight.append(int(sys.stdin.readline().rstrip()))

    weight.sort(reverse=True)

    # 최대 가능 중량
    max_weight = 0
    for i in range(len(weight)):
        temp = (i + 1) * weight[i]

        max_weight = temp if temp > max_weight else max_weight

    print(max_weight)


if __name__ == "__main__":
    function()