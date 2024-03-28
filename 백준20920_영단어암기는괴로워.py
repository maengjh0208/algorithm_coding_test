import collections
import sys


def function():
    # N: 단어 개수 / M : 외울 단어의 길이 기준
    N, M = map(int, input().split())

    words = [sys.stdin.readline().rstrip() for _ in range(N)]

    words_count = collections.Counter([i for i in words if len(i) >= M])

    sorted_words = sorted(words_count)
    sorted_words.sort(key=len, reverse=True)
    sorted_words.sort(key=words_count.__getitem__, reverse=True)

    print(sorted_words)

    print(sorted_words.)


    # for i in sorted(words_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    #     sys.stdout.write(i[0] + "\n")


if __name__ == "__main__":
    function()