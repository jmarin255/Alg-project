import random

def update_probabilities(grid, hits, misses):
    """Update the probabilities grid based on current hits and misses."""
    probabilities = [[1 for _ in range(len(grid))] for _ in range(len(grid))]
    for i, j in hits:
        probabilities[i][j] = 0  # Hit already resolved
    for i, j in misses:
        probabilities[i][j] = 0  # Can't place ships here
    return probabilities

def greedy_algorithm(grid, ships, hits, misses):
    """Greedy algorithm that selects cells based on their probabilities of containing a ship."""
    size = len(grid)
    moves = 0
    probabilities = [[1 for _ in range(size)] for _ in range(size)]  # Initial equal probabilities
    visited = set()

    # Start with a random cell initially
    row, col = random.randint(0, size - 1), random.randint(0, size - 1)

    while any("S" in row for row in grid):  # Continue until all ships are found
        if (row, col) not in visited:
            visited.add((row, col))
            
            # Check the status of the selected cell
            if grid[row][col] == "S":
                hits.append((row, col))
                grid[row][col] = "H"  # Mark as hit
            else:
                misses.append((row, col))
                grid[row][col] = "M"  # Mark as miss

            moves += 1
            probabilities = update_probabilities(grid, hits, misses)  # Update probabilities based on new hits/misses

            # Find the cell with the highest probability for the next move
            max_prob = max(max(row) for row in probabilities)
            candidates = [(i, j) for i in range(size) for j in range(size) if probabilities[i][j] == max_prob and (i, j) not in visited]

            if candidates:
                row, col = random.choice(candidates)  # Choose a random candidate with the highest probability
            else:
                break  # No more candidates left, exit the loop

    return moves
