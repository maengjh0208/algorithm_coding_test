def solution(players, callings):
    players_location = dict()

    # location = 0
    # for player in players:
    #     players_location[player] = location
    #     location += 1

    players_location = {player: idx for idx, player in enumerate(players)}

    for calling_player in callings:
        calling_player_location = players_location[calling_player]
        forward_player = players[calling_player_location - 1]

        # 선수들 위치 변경
        players[calling_player_location] = forward_player
        players[calling_player_location - 1] = calling_player

        players_location[calling_player] -= 1
        players_location[forward_player] += 1

    return players


if __name__ == "__main__":
    players = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]

    result = solution(players, callings)
    print(result == ["mumu", "kai", "mine", "soe", "poe"])