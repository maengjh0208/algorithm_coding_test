import sys

def function():
    player_name = dict()

    for _ in range(int(input())):
        name = sys.stdin.readline().strip()

        alphabet = name[0]
        if alphabet not in player_name.keys():
            player_name[alphabet] = 1
        else:
            player_name[alphabet] += 1

    five_players = []
    for key, value in player_name.items():
        if value > 4:
            five_players.append(key)

    if five_players:
        print("".join(sorted(five_players)))
    else:
        print("PREDAJA")


if __name__ == "__main__":
    function()