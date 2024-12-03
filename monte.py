import random

def update_probabilities(grid, hits, misses):
    size = len(grid)
    probabilities = [[1 for _ in range(size)] for _ in range(size)]

    # Adjust probabilities based on hits and misses
    for i, j in hits:
        probabilities[i][j] = 0  # Hit already resolved
    for i, j in misses:
        probabilities[i][j] = 0  # Can't place ships here

    return probabilities

def monte_carlo_algorithm(grid, hits, misses, simulations=100):
    size = len(grid)
    moves = 0
    visited = [[False for _ in range(size)] for _ in range(size)]

    # Helper function to check if a cell is valid and not visited
    def is_valid_cell(i, j):
        return 0 <= i < size and 0 <= j < size and not visited[i][j] and grid[i][j] != "M"

    # Initialize probabilities
    probabilities = update_probabilities(grid, hits, misses)

    # Run simulations to make moves based on probabilities
    while any("S" in row for row in grid):  # Continue until all ships are found
        max_prob = max(max(row) for row in probabilities)
        candidates = [(i, j) for i in range(size) for j in range(size) if probabilities[i][j] == max_prob and not visited[i][j]]

        if not candidates:
            break  # No more valid moves left

        # Pick a random candidate with the highest probability
        current_position = random.choice(candidates)
        row, col = current_position
        visited[row][col] = True
        moves += 1

        # Mark the cell as hit or miss
        if grid[row][col] == "S":
            hits.append((row, col))
            grid[row][col] = "H"
        else:
            misses.append((row, col))
            grid[row][col] = "M"
        

        # Update the probabilities
        probabilities = update_probabilities(grid, hits, misses)

    return moves
