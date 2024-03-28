def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == "__main__":
    result = solution("1111")
    print(result)