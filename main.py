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

def select_parents(population, normalized_scores):
    """
    Randomly selects two parents based on normalized fitness probabilities.
    Returns: (parent1, parent2)
    """
    parents = random.choices(population, weights=normalized_scores, k=2)
    return parents[0], parents[1]

def crossover(parent1, parent2):
    """
    Performs single-point crossover between two parents.
    Returns two children.
    """
    point = random.randint(1, 7)  #must be between 1 and 7
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(board, mutation_rate=0.05):
    """
    Mutates the board with a given probability.
    Randomly changes the row of one queen.
    """
    if random.random() < mutation_rate:
        col = random.randint(0, 7)  #pick random column
        new_row = random.randint(0, 7)
        while new_row == board[col]:  #make sure to actually change it
            new_row = random.randint(0, 7)
        board[col] = new_row
    return board

def breed(population, normalized_scores, mutation_rate=0.05):
    """
    Selects two parents and returns two children after crossover and mutation.
    """
    parent1, parent2 = select_parents(population, normalized_scores)
    child1, child2 = crossover(parent1, parent2)
    child1 = mutate(child1, mutation_rate)
    child2 = mutate(child2, mutation_rate)
    return child1, child2

def genetic_algorithm(pop_size=100, generations=1000, mutation_rate=0.05):
    """
    Runs the full genetic algorithm.
    Returns the best board and fitness history.
    """
    population = generate_population(pop_size)
    best_fitness = 0
    best_board = None
    fitness_history = []

    for gen in range(generations):
        evaluated = evaluate_population(population)
        fitness_scores = [fit for _, fit in evaluated]
        normalized_scores = normalize_fitness(fitness_scores)

        #track best and average fitness
        gen_best = max(fitness_scores)
        gen_avg = sum(fitness_scores) / len(fitness_scores)
        fitness_history.append((gen_avg, gen_best))

        if gen_best > best_fitness:
            best_fitness = gen_best
            best_board = evaluated[fitness_scores.index(gen_best)][0]

        #stop early if perfect solution is found
        if best_fitness == 28:
            print(f"Perfect solution found at generation {gen}")
            break

        #breed new population
        new_population = []
        while len(new_population) < pop_size:
            child1, child2 = breed(
                [board for board, _ in evaluated],
                normalized_scores,
                mutation_rate
            )
            new_population.extend([child1, child2])
        population = new_population[:pop_size]

    return best_board, best_fitness, fitness_history


# ------------------------- TESTING BLOCK -------------------------

if __name__ == "__main__":
    population_size = 10
    mutation_rate = 0.1

    #generate and evaluate initial population
    population = generate_population(population_size)
    evaluated = evaluate_population(population)
    fitness_scores = [fit for _, fit in evaluated]
    normalized_scores = normalize_fitness(fitness_scores)

    #print initial population with fitness info
    print("Initial Population:")
    for i, (board, fit) in enumerate(evaluated):
        print(f"Board {i+1}: {board}")
        print_board(board)
        print(f"Fitness: {fit}, Normalized: {normalized_scores[i]:.4f}\n")

    #test breeding process
    print("--- Breeding Test ---")
    child1, child2 = breed(
        [board for board, _ in evaluated],
        normalized_scores,
        mutation_rate
    )

    print("Child 1 (mutated):", child1)
    print_board(child1)
    print("Child 2 (mutated):", child2)
    print_board(child2)

# ------------------------- RUN GA BLOCK -------------------------
    print("\nRunning Genetic Algorithm...")
    best_board, best_fitness, fitness_history = genetic_algorithm(
        pop_size=100,
        generations=500,
        mutation_rate=0.05
    )

    print("\nBest Board Found:")
    print_board(best_board)
    print(f"Best Fitness: {best_fitness}")

    print("\nFitness Progress (every 50 generations):")
    for i in range(0, len(fitness_history), 50):
        avg_fit, best_fit = fitness_history[i]
        print(f"Gen {i}: Avg = {avg_fit:.2f}, Best = {best_fit}")