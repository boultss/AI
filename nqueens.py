def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\n")

def is_safe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, N):
    if col >= N:
        print_solution(board, N)  # Print the board when a solution is found
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen

            res = solve_n_queens(board, col + 1, N) or res  # Recur to place the rest of the queens

            board[i][col] = 0  # Backtrack and remove the queen

    return res

def solve(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board, 0, N):
        print("No solution exists")
    else:
        print(f"Solutions for {N}-Queens problem are displayed above.")

# Run the N-Queens Solver
N = int(input("Enter the number of queens (N): "))
solve(N)
