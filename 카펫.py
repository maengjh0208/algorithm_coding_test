def solution(brown: int, yellow: int) -> list:
    # 가로:x, 세로:y
    x_y_multiplication = brown + yellow
    x_y_addition = (brown + 4) / 2

    for x in range(x_y_multiplication - 2, 0, -1):
        if x_y_multiplication % x == 0:
            y = x_y_multiplication / x

            if x + y == x_y_addition:
                return [int(x), int(y)]


if __name__ == "__main__":
    result = solution(10, 2)
    print(result)