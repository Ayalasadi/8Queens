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

def generate_population(size):
    """Generates a list of random boards."""
    return [generate_random_board() for _ in range(size)]

def evaluate_population(population):
    """
    Returns a list of (board, fitness) tuples.
    """
    return [(board, calculate_fitness(board)) for board in population]

def normalize_fitness(fitness_list):
    """
    Given a list of fitness values, returns a list of normalized fitness scores.
    """
    total = sum(fitness_list)
    if total == 0:
        return [0 for _ in fitness_list]
    return [f / total for f in fitness_list]


if __name__ == "__main__":
    #create population
    population = generate_population(10)

    #evaluate fitness
    evaluated = evaluate_population(population)

    #extract fitness scores
    fitness_scores = [fit for _, fit in evaluated]

    #normalize them
    normalized_scores = normalize_fitness(fitness_scores)

    #print each board with fitness and normalized probability
    for i, (board, fit) in enumerate(evaluated):
        print(f"Board {i+1}: {board}")
        print_board(board)
        print(f"Fitness: {fit}, Normalized: {normalized_scores[i]:.4f}\n")
    board = generate_random_board()
    print("Random board:", board)
    print_board(board)
    fitness = calculate_fitness(board)
    print("Fitness score:", fitness)