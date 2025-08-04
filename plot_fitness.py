import matplotlib.pyplot as plt
from main import genetic_algorithm

def plot_fitness_curve(pop_size=100, generations=300, mutation_rate=0.05):
    best_board, best_fitness, history = genetic_algorithm(
        pop_size=pop_size,
        generations=generations,
        mutation_rate=mutation_rate
    )

    avg_fitness = [avg for avg, _ in history]
    best_fitness = [best for _, best in history]
    gens = list(range(len(history)))

    plt.figure(figsize=(10, 6))
    plt.plot(gens, avg_fitness, label='Average Fitness', linewidth=2)
    plt.plot(gens, best_fitness, label='Best Fitness', linewidth=2)
    plt.xlabel('Generation')
    plt.ylabel('Fitness Score')
    plt.title(f'Fitness Over Time\nPop: {pop_size}, Mutation: {mutation_rate}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fitness_curve(pop_size=100, generations=300, mutation_rate=0.05)
