# import _Functions

move_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def can_king_escape(board, king_position, move_directions, rooks_positions):
    for dx, dy in move_directions:
        new_row, new_col = king_position[0] + dx, king_position[1] + dy
        
        if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row][new_col] == 'o':
            if is_rook_attacking(rooks_positions, new_row, new_col) == False:
                return True
    return False

def is_rook_attacking(rooks_positions, row, col):
    for rook in rooks_positions:
        if rook[0] == row or rook[1] == col:
            return True
    return False

def change_rooks_around_king(board):
    global move_directions
    
    king_position = None
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                king_position = (i, j)
                break
        if king_position:
            break

    if king_position:
        k_row, k_col = king_position
        
        for dx, dy in move_directions:
            new_row, new_col = k_row + dx, k_col + dy
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == 'w':
                    board[new_row][new_col] = 'o'
    return board

def solution(board):
    global move_directions
    
    king_position = (0, 0)
    rooks_positions = []
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                king_position = (i, j)
            elif board[i][j] == 'w':
                rooks_positions.append((i, j))

    king_under_attack = is_rook_attacking(rooks_positions, king_position[0], king_position[1])
    
    if king_under_attack:
        if can_king_escape(board, king_position, move_directions, rooks_positions):
            return "game goes on"
        else:
            return "mat"
    else:
        if can_king_escape(board, king_position, move_directions, rooks_positions):
            return "game goes on"
        else:
            return "pat"
    

def main():
    board = []
    for _ in range(8):
        row_input = input()
        board_row = []
        for char in row_input:
            board_row.append(char)
        board.append(board_row)
    board = change_rooks_around_king(board)
    print(solution(board))
    
main()
