def solution(numbers):
    result = []
    for number in numbers:
        binary_numbers = ["0"] + list(bin(number)[2:])
        length = len(binary_numbers)

        for i in range(length - 1, -1, -1):
            if binary_numbers[i] == "0":
                binary_numbers[i] = "1"
                if i != length - 1 and binary_numbers[i + 1] == "1":
                    binary_numbers[i + 1] = "0"

                break

        result.append(int("0b" + "".join(binary_numbers), 2))

    return result


if __name__ == "__main__":
    result = solution([2, 7])
    print(result)
