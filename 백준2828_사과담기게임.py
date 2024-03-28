def function():
    # N: 스크린 크기 / M: 바구니 크기
    N, M = map(int, input().split())

    # j: 떨어지는 사과 개수
    j = int(input())

    # 떨어지는 사과 위치 순서대로
    apple_locations = [int(input()) for _ in range(j)]

    basket_left = 1             # 바구니 왼쪽 위치
    basket_right = 1 + (M - 1)  # 바구니 오른쪽 위치

    count = 0  # 총 이동 횟수

    for apple in apple_locations:
        # 사과가 이미 바구니 위치에 있는 경우
        if basket_left <= apple <= basket_right:
            continue

        # 바구니가 사과 왼쪽에 있는 경우
        if apple < basket_left:
            diff = basket_left - apple

            basket_left -= diff
            basket_right -= diff
            count += diff

        # 바구니가 사과 오른쪽에 있는 경우
        if basket_right < apple:
            diff = apple - basket_right

            basket_left += diff
            basket_right += diff
            count += diff

    print(count)


if __name__ == "__main__":
    function()