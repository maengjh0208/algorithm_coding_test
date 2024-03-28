def solution(s: str):
    int_list = [int(i) for i in s.split()]
    big = max(int_list)
    small = min(int_list)

    return f"{small} {big}"



if __name__ == "__main__":
    print(solution("1 2 3 4"))