def solution(storey):
    count = 0

    while True:
        storey, rest = storey // 10, storey % 10
        if rest > 5 or (rest == 5 and storey % 10 >= 5):
            count += 10 - rest
            storey += 1
        else:
            count += rest

        if storey == 0:
            break

    return count


if __name__ == "__main__":
    result = solution(555)
    print(result)
