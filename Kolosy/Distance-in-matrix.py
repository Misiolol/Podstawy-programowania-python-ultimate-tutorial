def find_min_distance(matrix):
    matrix_size = len(matrix)
    
    one_positions = []
    for row_index in range(matrix_size):
        for col_index in range(matrix_size):
            if matrix[row_index][col_index] == 1:
                one_positions.append((row_index + 1, col_index + 1))
    
    minimum_distance = 999999999999
    
    
    for first_pos_index in range(len(one_positions)):
        for second_pos_index in range(first_pos_index + 1, len(one_positions)):
            row1, col1 = one_positions[first_pos_index]
            row2, col2 = one_positions[second_pos_index]
            
            if row2 % row1 == 0 and col2 % col1 == 0:
                distance = abs(row1 - row2) + abs(col1 - col2)
            else:
                distance = 1000
            
            minimum_distance = min(minimum_distance, distance)
    
    return minimum_distance


def main():
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    print(find_min_distance(matrix))
    
main()