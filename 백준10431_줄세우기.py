import sys


def function():
    P = int(input())  # 테스트케이스 수

    for _ in range(P):
        i, *height_list = map(int, sys.stdin.readline().split())

        changes = 0
        for j in range(1, len(height_list)):
            for k in range(j):
                if height_list[j] < height_list[k]:
                    changes += 1

        print(f"{i} {changes}")


if __name__ == "__main__":
    function()