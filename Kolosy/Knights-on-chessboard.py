def count_knight_attacks(board, n):
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    count = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 's':
                for dx, dy in moves:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 's':
                        count += 1

    print(count)


def main():
    k = int(input())
    chsboard = [list(input().strip()) for _ in range(k)]
    count_knight_attacks(chsboard, k)

main()
