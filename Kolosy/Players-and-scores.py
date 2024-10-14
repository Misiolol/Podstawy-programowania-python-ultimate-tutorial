N = int(input())
scores = []
players = set()
for _ in range(N):
    current_match = list(input().split()) 
    scores.append(current_match)
    name = current_match[0].split(":")[0]
    name2 = current_match[1].split(":")[0]
    players.add(name)
    players.add(name2)

players = list(players)
solution_array = []

for _ in range(len(players)):
    solution_array.append([players[_], int(0), int(0)])

#* print(scores)
#* print(solution_array)
for _ in range(0, len(scores)):
    name, score = scores[_][0].split(":")
    name2, score2 = scores[_][1].split(":")
    for i  in range(len(solution_array)):
        if solution_array[i][0] == name:
            index = i
    for i  in range(len(solution_array)):
        if solution_array[i][0] == name2:
            index2 = i
    if int(score) > int(score2):
        solution_array[index][1]+=1
        #print(solution_array[index2][0])
    if int(score2) > int(score):
        solution_array[index2][1]+=1
    solution_array[index][2]+=int(score)
    solution_array[index2][2]+=int(score2)

sorted_solution_array = sorted(solution_array, key=lambda x:(-x[1], -x[2], x[0]))
#print (sorted_solution_array)

for i in range(len(players)):
    print(sorted_solution_array[i][0])







#!print(solution_array)

