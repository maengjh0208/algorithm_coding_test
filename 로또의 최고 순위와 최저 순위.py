def solution(lottos, win_nums):
    lotto_count = 0
    scores = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    for num in lottos:
        if num != 0 and num in win_nums:
            lotto_count += 1

    return [scores[lotto_count + lottos.count(0)], scores[lotto_count]]


if __name__ == "__main__":
    result = solution(
        lottos=[44, 1, 0, 0, 31, 25],
        win_nums=[31, 10, 45, 1, 6, 19],
    )

    print(result)
