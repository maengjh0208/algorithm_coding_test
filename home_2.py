def solution(target: str, typed: str) -> bool:
    target_location = 0
    target_length = len(target)
    result = True

    for i in range(len(typed)):
        if target_location < target_length and typed[i] == target[target_location]:
            target_location += 1
        else:
            target_location -= 1
            if typed[i] == target[target_location]:
                target_location += 1
            else:
                result = False
                break

    return result


if __name__ == "__main__":
    result = solution("bucketplace", "buckeetpladce")
    print(result)