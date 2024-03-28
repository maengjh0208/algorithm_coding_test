def function():
    board = input().split(".")

    for i in range(len(board)):
        if len(board[i]) % 2 != 0:
            print("-1")
            return

        n = len(board[i]) // 4
        m = len(board[i]) % 4

        board[i] = "AAAA" * n if m == 0 else "AAAA" * n + "BB"

    print(".".join(board))


if __name__ == "__main__":
    function()