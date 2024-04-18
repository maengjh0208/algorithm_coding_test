from collections import defaultdict


def solution(clothes):
    clothes_count = defaultdict(int)

    for _, cloth_type in clothes:
        clothes_count[cloth_type] += 1

    combination_count = 1
    for value in clothes_count.values():
        combination_count *= value + 1

    return combination_count - 1


if __name__ == "__main__":
    result = solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
    print(result)
