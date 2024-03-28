def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f"김서방은 {i}에 있다"

    return f"김서방은 {seoul.index('Kim')}에 있다"


if __name__ == "__main__":
    print(solution(["Jane", "Kim"]))