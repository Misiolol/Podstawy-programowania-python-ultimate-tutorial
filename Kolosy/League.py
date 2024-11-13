from collections import Counter

def winner(match):
    t1, t2, s1, s2 = match.split(":")
    s1, s2 = int(s1), int(s2)
    if s1>s2:
        return t1
    if s2>s1:
        return t2
    else:
        return 0
    
def played_matches(matches):
    help = []
    for match in matches:
        t1, t2, s1, s2 = match.split(":")
        help.append(t1)
        help.append(t2)
    return Counter(help)
        
def solution(team_names, team_matches, team_wins, needed_wins):
    solutions = []
    for team in team_names:
        found = False
        for n in team_matches.keys():
            if n == team:
                found = True
                left_matches = len(team_names) - 1 - team_matches[team]
                if left_matches + team_wins[team] >= needed_wins:
                    solutions.append(team)
        if not found:
            left_matches = len(team_names) - 1
            if left_matches >= needed_wins:
                solutions.append(team)
    return solutions
                

def main():
    number_of_teams, number_of_played_matches, needed_wins = map(int, input().split())

    team_names = [input() for _ in range(number_of_teams)]
    matches = [input() for _ in range(number_of_played_matches)]
    team_matches = played_matches(matches)
    
    winners = []
    for match in matches:
        winners.append(winner(match))
    team_wins = Counter(winners)
    
    #print(team_matches)
    #print(team_wins)
    
    
    for team in sorted(solution(team_names, team_matches, team_wins, needed_wins)):
        print(team)
    
  
  
main()  
    
    
    
