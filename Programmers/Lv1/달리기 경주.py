def solution(players, callings):
    idx = {i: player for i, player in enumerate(players)}
    p = {player: i for i, player in enumerate(players)}
    for i in callings:
        ni = p[i]
        front = ni - 1
        front_player = idx[front]
        p[i], p[front_player] = front, ni
        idx[ni], idx[front] = front_player, i
    return list(idx.values())


solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
