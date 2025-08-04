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
        print(line)
    print()

def calculate_fitness(board):
    """
    Calculates the fitness score of a board.
    Returns: 28 - number of attacking pairs.
    """
    attacking_pairs = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            #same row
            if board[i] == board[j]:
                attacking_pairs += 1

            #same major diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1
    return 28 - attacking_pairs



if __name__ == "__main__":
    board = generate_random_board()
    print("Random board:", board)
    print_board(board)
    fitness = calculate_fitness(board)
    print("Fitness score:", fitness)