import random

# Create an empty board
board = [" " for _ in range(9)]

# Player and computer notation
player_symbol = 'X'
computer_symbol = "O"

# Function to draw tic tac toe board
def draw_board():
    print("-------------")
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print("-------------")
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print("-------------")
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print("-------------")

# Function to validate winner
def check_winner(symbol):
    # Check horizontal line
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == symbol:
            return True
    # Check vertical line
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == symbol:
            return True
    # Check for diagonal
    if board[0] == board[4] == board[8] == symbol or board[2] == board[4] == board[6] == symbol:
        return True
    return False

# Function to take player's turn
def players_turn():
    position = int(input("Enter a number from 1-9: ")) -1
    if board[position] == ' ':
        board[position] = player_symbol
        draw_board()
        if check_winner(player_symbol):
            print("Congratulations! You win!")
        else:
            computer_turn()
    else:
        print("Position already taken. Try again.")
        players_turn()

# Function to take computer's turn
def computer_turn():
    available_moves = [i for i in range(9) if board[i] == ' ']
    if len(available_moves) > 0:
        position = random.choice(available_moves)
        board[position] = computer_symbol
        draw_board()
        if check_winner(computer_symbol):
            print("You lose!")
        else:
            players_turn()
    else:
        print("It's a tie.")

# Main function
def main():
    print("+---------------+")
    print("| TIC TAC TOE   |")
    print("+---------------+")
    draw_board()
    players_turn()

if __name__ == "__main__":
    main()
