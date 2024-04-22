def solution(n, m, section):
    count = 1
    end = section[0] + m

    for i in section[1:]:
        if end > i:
            continue

        count += 1
        end = i + m

    return count


if __name__ == "__main__":
    result = solution(8, 4, [2, 3, 6])
    print(result)