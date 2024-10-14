N = int(input())

players = set()
input = []
for _ in range (N):
    cutternt_player = list(input().split())
    input.append(cutternt_player)
    for player in cutternt_player:
        name, points = player.split(":")
        players.add(name)
players_list = []
for _ in range(len(players)):
    players_list.append([players[_], 0, 0])

for i in range(0, input, 2):
    name, points = input[i].split(":")
    name2, points2 = input[i+1].split(":")
    if points > points2:
        



