def print_board(board):
    """Renders the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board):
    """Checks if there is a winner on the board."""
    # Winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    return None


def check_draw(board):
    """Checks if the board is full (a draw)."""
    return " " not in board


def play_game():
    """Main game loop."""
    # Initialize the board with empty spaces
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1 through 9 from top-left to bottom-right.")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get and validate user input
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
            if board[move] != " ":
                print("That space is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        # Place the move on the board
        board[move] = current_player
        
        # Check for a winner
        winner = check_win(board)
        if winner:
            print_board(board)
            print(f"Congratulations! Player {winner} wins! 🎉")
            break
            
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break
            
        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()