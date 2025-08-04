import random

def generate_random_board():
    """Generates a random board with one queen per column."""
    board = list(range(8))  #list of 8 items: [0,1,2,...,7]
    random.shuffle(board)
    return board

def print_board(board):
    """Prints the board as 8x8 with Qs and dots."""
    for row in range(8):
        line = ""
        for col in range(8):
            if board[col] == row:
                line += "Q "
            else:
                line += ". " 
        print()
    print()


if __name__ == "__main__":
    board = generate_random_board()
    print("Random board:", board)
    print_board(board)