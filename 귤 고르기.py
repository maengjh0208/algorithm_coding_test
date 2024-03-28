def solution(k, tangerine):
    size_value = dict()
    for size in tangerine:
        if size in size_value:
            size_value[size] += 1
        else:
            size_value[size] = 1

    size_list = sorted(size_value.values(), reverse=True)

    count = 0
    for size in size_list:
        k -= size
        count += 1
        if k <= 0:
            break

    return count


if __name__ == "__main__":
    result = solution(6, [1, 3, 2, 5, 4, 5, 2, 3])

    print(result)  # 3
