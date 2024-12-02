import time
from exact import exact_algorithm
from greedy import greedy_algorithm
from monte import monte_carlo_algorithm


# Helper function to generate datasets
def generate_dataset(size, ships):
    grid = [["-" for _ in range(size)] for _ in range(size)]
    ship_sizes = ships

    # Example of a fixed placement pattern
    placements = [
        (0, 0, "horizontal", 2),  # Place a 2-cell ship at the top left, horizontal
        (2, 2, "vertical", 3),    # Place a 3-cell ship starting at (2, 2), vertical
        (4, 4, "horizontal", 1)   # Place a 1-cell ship at (4, 4), horizontal
    ]

    for row, col, direction, size in placements:
        if direction == "horizontal":
            for i in range(size):
                grid[row][col + i] = "S"
        elif direction == "vertical":
            for i in range(size):
                grid[row + i][col] = "S"

    return grid, ship_sizes

# Example usage:
grid, ship_sizes = generate_dataset(5, [2, 3, 1])
for row in grid:
    print(" ".join(row))

# Define datasets
datasets = [
    {"size": 5, "ships": [2, 3]},       # Small dataset for exact algorithm
    {"size": 10, "ships": [2, 3, 4]},  # Medium dataset
    {"size": 15, "ships": [3, 4, 5]},  # Large dataset
]

# Algorithms to test
algorithms = {
    "Exact Algorithm": exact_algorithm,
    "Greedy Algorithm": greedy_algorithm,
    "Monte Carlo Algorithm": monte_carlo_algorithm,
}

# Run experiments
for dataset in datasets:
    print(f"\nDataset: {dataset['size']}x{dataset['size']}, Ships: {dataset['ships']}")
    grid, ships = generate_dataset(dataset["size"], dataset["ships"])

    for name, algorithm in algorithms.items():
        runtimes = []
        results = []
        for _ in range(1):  # Run each algorithm 5 times
            grid_copy = [row[:] for row in grid]  # Create a fresh copy of the grid
            hits, misses = [], []  # Initialize empty hits and misses
            
            start_time = time.time()
            
            if name == "Monte Carlo Algorithm":
                result = algorithm(grid_copy, hits, misses, simulations=100)
            else:
                result = algorithm(grid_copy, ships, hits, misses)
            
            end_time = time.time()
            runtimes.append(end_time - start_time)
            results.append(result)
            # Print final grid state for verification
            print(f"\nFinal grid state after running {name}:")
            for row in grid_copy:
                print(' '.join(row))

        # Report results
        avg_runtime = sum(runtimes) / len(runtimes)
        print(f"  {name}: Avg Runtime = {avg_runtime:.4f}s")
