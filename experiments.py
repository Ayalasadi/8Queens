from main import genetic_algorithm
def run_parameter_experiments():
    population_sizes = [10, 100, 500]
    mutation_rates = [0.01, 0.05, 0.1]
    generations = 300

    print("Parameter Experiments:\n")
    for pop_size in population_sizes:
        for mut_rate in mutation_rates:
            print(f"Running: Pop Size = {pop_size}, Mutation Rate = {mut_rate}")
            best_board, best_fitness, history = genetic_algorithm(
                pop_size=pop_size,
                generations=generations,
                mutation_rate=mut_rate
            )
            print(f"Best Fitness: {best_fitness}\n")

if __name__ == "__main__":
    run_parameter_experiments()
