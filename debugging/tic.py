#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    turn_count = 0  # Keep track of turns to detect a draw
    
    while not check_winner(board):
        if turn_count == 9:
            print_board(board)
            print("It's a draw!")
            return  # End the game if the board is full

        print_board(board)
        
        # 1. Handle Invalid Input (Letters, symbols)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue  # Skip the rest of the loop and ask again
            
        # 2. Handle Out-of-Bounds Input (Numbers outside 0-2)
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates out of bounds! Please enter 0, 1, or 2.")
            continue
            
        # 3. Handle Valid Moves
        if board[row][col] == " ":
            board[row][col] = player
            turn_count += 1
            
            # Check for a winner BEFORE switching players
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                return
                
            # Switch player only if no one won yet
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()