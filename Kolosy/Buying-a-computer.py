def best_pc(user, computers):
    suitable_pc = []
    for computer in computers:
        suitable = True
        for req in user:
            name, val = req.split(":")
            if name == "cpu": idx = 1
            if name == "gpu": idx = 2
            if name == "disc": idx = 3
            if name == "ram": idx = 4            
            if int(computer[idx]) < int(val):
                suitable = False
        if suitable:
            suitable_pc.append(computer)
            
    suitable_pc.sort(key=lambda x: (int(x[5]), x[0]))
    return suitable_pc[0][0]
            

def main(): 
    n = int(input())
    computers = []
    for _ in range(n):
        row = list(input().split())
        computers.append(row)
    k = int(input())
    users = []
    for _ in range(k):
        row = list(input().split())
        users.append(row)
    sol = []
    for user in users:
        sol.append(best_pc(user, computers))
    
    for i in range(len(sol)):
        print(sol[i])
        
main()