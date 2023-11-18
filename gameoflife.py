import numpy as np

def game_of_life(board):
    n, m = len(board), len(board[0])
    new_board = np.copy(board)

    def count_neighbors(i, j):
        neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
        return sum(board[x][y] for x, y in neighbors if 0 <= x < n and 0 <= y < m)

    for i in range(n):
        for j in range(m):
            live_neighbors = count_neighbors(i, j)
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[i][j] = 0
            else:
                if live_neighbors == 3:
                    new_board[i][j] = 1

    return new_board

# Test the function
board = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
])

print("Initial board:")
print(board)

for _ in range(10):
    board = game_of_life(board)
    print("\nNext generation:")
    print(board)