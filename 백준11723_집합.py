import sys

def function():
    N = int(input())

    S = []

    for _ in range(N):
        command = sys.stdin.readline().split()

        if command[0] == "all":
            S = [i for i in range(1, 21)]
        elif command[0] == "empty":
            S = []
        else:
            num = int(command[1])

            if command[0] == "add" and num not in S:
                S.append(num)
            elif command[0] == "remove" and num in S:
                S.remove(num)
            elif command[0] == "toggle":
                if num in S:
                    S.remove(num)
                else:
                    S.append(num)
            elif command[0] == "check":
                sys.stdout.write("1\n" if num in S else "0\n")


if __name__ == "__main__":
    function()