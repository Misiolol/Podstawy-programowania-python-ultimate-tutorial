
def row_remove(matrix, idx):
    new_matrix = [row for i, row in enumerate(matrix) if i != idx]
    return new_matrix

def column_remove(matrix, idx):
      return [row[:idx] + row[idx+1:] for row in matrix]


def main():    
    k = int(input())
    base_matrix = [list(input().split()) for _ in range(k)]
    second_matrix = [list(input().split()) for _ in range(k-1)]
    for i in  range(k):
        for j in range(k):
            new_matrix = column_remove(row_remove(base_matrix, i), j)
            if new_matrix == second_matrix:
                return 1
    return 0

if main():
    print("True")
else:
    print("False")
    
