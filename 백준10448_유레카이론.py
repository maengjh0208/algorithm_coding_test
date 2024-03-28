import sys


def function():
    # 각 삼각수마다 필요한 점 개수
    triangle_list = []
    for i in range(1, 45):
        triangle_list.append(int(i * (i + 1) / 2))

    # 1 ~ 1000 이하의 자연수에 대하여 3개의 삼각수로 표현되는 경우 "1", 아니면 "0"
    temp = ["0" for _ in range(1001)]

    for i in range(len(triangle_list)):
        for j in range(len(triangle_list)):
            for k in range(len(triangle_list)):
                num = triangle_list[i] + triangle_list[j] + triangle_list[k]
                if num > 1000:
                    continue
                else:
                    temp[num] = "1"

    for _ in range(int(input())):
        print(temp[int(sys.stdin.readline().rstrip())])


if __name__ == "__main__":
    function()