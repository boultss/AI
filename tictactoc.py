import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("\n")

# Function to check if any player has won
def check_winner(board):
    win_states = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    if ["X", "X", "X"] in win_states:
        return 1  # AI (Maximizer) wins
    elif ["O", "O", "O"] in win_states:
        return -1  # Opponent (Minimizer) wins
    elif " " not in board:
        return 0  # Draw
    return None  # Game not finished

# Minimax function
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner is not None:
        return winner  # Return score for the board state

    if is_maximizing:  # AI's turn (Maximizer)
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "  # Undo move
                best_score = max(best_score, score)
        return best_score
    else:  # Opponent's turn (Minimizer)
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "  # Undo move
                best_score = min(best_score, score)
        return best_score

# Function to find the best move for AI
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "  # Undo move
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Main function to play the game
def play_game():
    board = [" "] * 9  # Empty Tic-Tac-Toe board
    print("Welcome to Tic-Tac-Toe! AI (X) vs You (O)")
    print_board(board)

    while True:
        # Player move (O)
        user_move = int(input("Enter your move (0-8): "))
        if board[user_move] != " ":
            print("Invalid move! Try again.")
            continue
        board[user_move] = "O"
        print_board(board)

        # Check if player wins or draws
        if check_winner(board) == -1:
            print("You win! 🎉")
            break
        elif check_winner(board) == 0:
            print("It's a draw! 🤝")
            break

        # AI move (X)
        print("AI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move] = "X"
        print_board(board)

        # Check if AI wins or draws
        if check_winner(board) == 1:
            print("AI wins! 🤖")
            break
        elif check_winner(board) == 0:
            print("It's a draw! 🤝")
            break

# Run the game
play_game()
