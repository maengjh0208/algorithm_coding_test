import sys


def function():
    words = list(set(sys.stdin.readline().rstrip() for _ in range(int(input()))))

    words.sort(key=lambda x: (len(x), x))

    print("\n".join(words))


if __name__ == "__main__":
    function()