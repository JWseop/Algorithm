# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# Lv.1
# 문제: 달리기 경주

def solution(players, callings):
    player_dict = {player: index for index, player in enumerate(players)}

    for call in callings:
        if player_dict[call] != 0:
            i = player_dict[call]
            # Swap players in list
            players[i-1], players[i] = players[i], players[i-1]
            # Update player positions in the dictionary
            player_dict[players[i-1]], player_dict[players[i]] = player_dict[players[i]], player_dict[players[i-1]]

    return players