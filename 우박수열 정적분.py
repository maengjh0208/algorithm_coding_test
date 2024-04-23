def solution(k, ranges):
    # 콜라츠 추측 리스트
    collatz_list = [k]
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1

        collatz_list.append(k)

    # 콜라츠 추측 누적 넓이 구하기
    collatz_area_list = [0]
    for i in range(len(collatz_list) - 1):
        area = (collatz_list[i] + collatz_list[i + 1]) / 2
        collatz_area_list.append(collatz_area_list[-1] + area)

    width = len(collatz_list) - 1
    result = []
    for a, b in ranges:
        b = width + b
        area = collatz_area_list[b] - collatz_area_list[a] if a <= b else -1

        result.append(area)

    return result


if __name__ == "__main__":
    result = solution(k=5, ranges=[[0, 0], [0, -1], [2, -3], [3, -3]])

    print(result)
