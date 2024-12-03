import time
from exact import exact_algorithm
from greedy import greedy_algorithm
from monte import monte_carlo_algorithm


# Helper function to generate datasets
def generate_dataset(size, placements):
    grid = [["-" for _ in range(size)] for _ in range(size)]

    for row, col, direction, ship_size in placements:
        if direction == "horizontal":
            if col + ship_size <= size:  # Ensure the ship fits horizontally
                for i in range(ship_size):
                    grid[row][col + i] = "S"
        elif direction == "vertical":
            if row + ship_size <= size:  # Ensure the ship fits vertically
                for i in range(ship_size):
                    grid[row + i][col] = "S"
    return grid


# Define datasets with specific placements
datasets = [
    {
        "size": 5,
        "placements": [
            (0, 0, "horizontal", 2),  # Place a 2-cell ship at (0, 0) horizontally
            (2, 2, "vertical", 3),    # Place a 3-cell ship at (2, 2) vertically
            (4, 4, "horizontal", 1),  # Place a 1-cell ship at (4, 4) horizontally
        ],
    },
    {
        "size": 10,
        "placements": [
            (1, 1, "horizontal", 3),  # Place a 3-cell ship at (1, 1) horizontally
            (5, 5, "vertical", 4),    # Place a 4-cell ship at (5, 5) vertically
            (8, 8, "horizontal", 2),  # Place a 2-cell ship at (8, 8) horizontally
        ],
    },
    {
        "size": 15,
        "placements": [
            (0, 0, "horizontal", 4),  # Place a 4-cell ship at (0, 0) horizontally
            (7, 7, "vertical", 5),    # Place a 5-cell ship at (7, 7) vertically
            (12, 12, "horizontal", 3),  # Place a 3-cell ship at (12, 12) horizontally
        ],
    },
]

# Algorithms to test
algorithms = {
    "Exact Algorithm": exact_algorithm,
    "Greedy Algorithm": greedy_algorithm,
    "Monte Carlo Algorithm": monte_carlo_algorithm,
}

# Run experiments
for dataset in datasets:
    size = dataset["size"]
    placements = dataset["placements"]

    print(f"\nDataset: {size}x{size}, Placements: {placements}")
    grid = generate_dataset(size, placements)

    print("\nOriginal Grid: ")
    for row in grid:
        print(" ".join(row))

    for name, algorithm in algorithms.items():
        runtimes = []
        results = []
        for _ in range(1):  # Run each algorithm once
            grid_copy = [row[:] for row in grid]  # Create a fresh copy of the grid
            hits, misses = [], []  # Initialize empty hits and misses

            start_time = time.time()

            if name == "Monte Carlo Algorithm":
                result = algorithm(grid_copy, hits, misses, simulations=100)
            else:
                result = algorithm(grid_copy, [p for _, _, _, p in placements], hits, misses)

            end_time = time.time()
            runtimes.append(end_time - start_time)
            results.append(result)

            # Print final grid state for verification
            print(f"\nFinal grid state after running {name}:")
            for row in grid_copy:
                print(" ".join(row))

        # Report results
        avg_runtime = sum(runtimes) / len(runtimes)
        print(f"  {name}: Avg Runtime = {avg_runtime:.4f}s")

