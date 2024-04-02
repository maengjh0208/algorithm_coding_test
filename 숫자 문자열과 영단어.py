import time


def convert_string_to_number(s: str) -> tuple:
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": '4',
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for i in range(3, len(s) + 1):
        if s[:i] in numbers.keys():
            return numbers[s[:i]], i


def solution(s: str) -> int:
    start = 0
    number_list = []

    for i in range(len(s)):
        if i < start:
            continue

        # 숫자인지 확인
        if s[i].isdigit():
            number_list.append(s[i])
        else:
            result = convert_string_to_number(s[i : i + 5])

            number_list.append(result[0])
            start = i + result[1]

    return int("".join(number_list))





def solution2(s):
    num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
               "eight": "8", "nine": "9"}
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


import time

# solution 메서드 시간 체크
start_time = time.time()
solution("one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10")
print(time.time() - start_time)

# solution2 메서드 시간 체크
start_time = time.time()
solution2("one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10one4seveneightone4seveneight23four5six71zerotwozero3123twotwothree10")
print(time.time() - start_time)

