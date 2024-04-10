
def compare_dict(want_dict: dict, discount_dict: dict) -> bool:
    for key in want_dict:
        if key not in discount_dict:
            return False

        if want_dict[key] != discount_dict[key]:
            return False

    return True


def solution(want: list, number: list, discount: list) -> int:
    want_dict = {w: n for w, n in zip(want, number)}

    discount_dict = {}
    for product in discount[:9]:
        if product in discount_dict:
            discount_dict[product] += 1
        else:
            discount_dict[product] = 1

    count = 0
    for idx in range(9, len(discount)):
        if discount[idx] in discount_dict:
            discount_dict[discount[idx]] += 1
        else:
            discount_dict[discount[idx]] = 1

        if compare_dict(want_dict, discount_dict):
            count += 1

        discount_dict[discount[idx - 9]] -= 1

    return count


if __name__ == "__main__":
    result = solution(
        want=["banana", "apple", "rice", "pork", "pot"],
        number=[3, 2, 2, 2, 1],
        discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"],
    )

    print(result)