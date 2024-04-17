def solution(numbers, target):
    possible_numbers = [numbers[0], -numbers[0]]

    for num in numbers[1:]:
        next_possible_numbers = []
        for i in possible_numbers:
            next_possible_numbers.append(i + num)
            next_possible_numbers.append(i - num)

        possible_numbers = next_possible_numbers

    return possible_numbers.count(target)


if __name__ == "__main__":
    result = solution(numbers=[4, 1, 2, 1], target=4)
    print(result)
