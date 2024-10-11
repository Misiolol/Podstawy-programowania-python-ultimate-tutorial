n = int(input())

grid = []
for i in range(n):
    grid.append([int(cell) for cell in list(input())])

#! Function to explore the island starting from the given cell (row, col)
def exploreIsland(row, col):
#~ Use a stack to store the cells to visit (Depth First Search)
    stack = [(row, col)]
    
    while stack:
        current_row, current_col = stack.pop()

        #? Check if the cell is within bounds and part of the island 
        if 0 <= current_row < n and 0 <= current_col < n and grid[current_row][current_col] == 1:
            #! Mark the current cell as visited by changing it from 1 to 0
            grid[current_row][current_col] = 0
            
            #! Add neighboring cells (left, right, up, down) to the stack to explore them
            stack.append((current_row, current_col - 1))  # left neighbor
            stack.append((current_row, current_col + 1))  # right neighbor
            stack.append((current_row - 1, current_col))  # upper neighbor
            stack.append((current_row + 1, current_col))  # lower neighbor


num_islands = 0
        

for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            num_islands += 1
            exploreIsland(row, col)


print(num_islands)
