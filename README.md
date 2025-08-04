# 8-Queens Genetic Algorithm

This project implements a genetic algorithm in Python to solve the classic 8-Queens problem: placing eight queens on a chessboard such that no two queens attack each other. The solution is approached using population-based search with selection, crossover, and mutation operations.

## Overview

- **Encoding**: Each candidate solution (board) is represented as a list of 8 integers. Each index represents a column, and the value at that index represents the row position of the queen in that column.
- **Fitness Function**: The fitness score is calculated as the number of non-attacking queen pairs (maximum of 28). Conflicts are detected along rows and diagonals.
- **Genetic Operators**:
  - **Selection**: Parents are selected using roulette-wheel selection based on normalized fitness scores.
  - **Crossover**: Single-point crossover is used to produce offspring.
  - **Mutation**: A low-probability mutation alters the row position of a randomly chosen queen.

## Parameter Tuning

Experiments were conducted using different population sizes and mutation rates. Larger population sizes and moderate mutation rates (around 0.05) led to more consistent convergence to optimal solutions.

| Population Size | Mutation Rate | Best Fitness |
|-----------------|----------------|--------------|
| 10              | 0.01–0.1       | 26–27        |
| 100             | 0.05           | 28           |
| 500             | 0.01–0.1       | 28           |

## Visualization

A plot of average and best fitness over generations is generated using matplotlib. It shows the improvement in population fitness as the algorithm progresses.

## Sample Output

Perfect solution found at generation 34

Best Board:
. . . . Q . . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . . . Q . .
Q . . . . . . .
. . . Q . . . .
. . . . . . . Q

## How to Run 

### Clone and Set Up
- **Clone and enter the project folder**
git clone https://github.com/Ayalasadi/8Queens.git
cd 8Queens

-**Create and activate virtual environment**
python3 -m venv venv
source venv/bin/activate

-**install dependencies**
pip install -r requirements.txt

-**Run main genetic algorithm**
python3 main.py

-**Run experiments or plots**
python3 experiments.py
python3 plot_fitness.py

### Run the Genetic Algorithm
python3 main.py

### Run Parameter Experiments
python3 experiments.py

### Plot Fitness Curve
python3 plot_fitness.py

### Dependencies
- Python 3.10+
- matplotlib