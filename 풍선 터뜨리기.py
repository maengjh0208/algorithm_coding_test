def solution(a):
    if len(a) in (1, 2):
        return len(a)

    # 양쪽 끝에 있는 숫자는 최후까지 남기는 것이 가능
    count = 2

    # 왼쪽 부터 순차적으로 최솟값 구하기
    left_min_value = a[0]
    left_min_value_list = [0]  # 0번째 인덱스 값과 마지막 인덱스 값은 어차피 비교대상이 아니므로 어떤 숫자가 들어가더라도 상관 없음
    for i in a[1:]:
        left_min_value_list.append(left_min_value)
        left_min_value = min(left_min_value, i)

    # 오른쪽 부터 순차적으로 최솟값 구하기
    right_min_value = a[-1]
    right_min_value_list = [0]  # 0번째 인덱스 값과 마지막 인덱스 값은 어차피 비교대상이 아니므로 어떤 숫자가 들어가더라도 상관 없음
    for i in a[-1::-1]:
        right_min_value_list.append(right_min_value)
        right_min_value = min(right_min_value, i)

    right_min_value_list = right_min_value_list[::-1]

    # 최후까지 남기는 것이 가능한 풍선 개수 구하기
    for idx in range(1, len(a) - 1):
        if a[idx] < left_min_value_list[idx] or a[idx] < right_min_value_list[idx]:
            count += 1

    return count


if __name__ == "__main__":
    result = solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33])
    print(result)
