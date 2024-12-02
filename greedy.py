
def update_probabilities(grid, hits, misses):
    probabilities = [[1 for _ in range(len(grid))] for _ in range(len(grid))]
    for i, j in hits:
        probabilities[i][j] = 0  # Hit already resolved
    for i, j in misses:
        probabilities[i][j] = 0  # Can't place ships here
    return probabilities

def greedy_algorithm(grid, ships, hits, misses):
    probabilities = update_probabilities(grid, hits, misses)
    moves = 0
    while any("S" in row for row in grid):  # Continue until all ships are sunk
        max_prob = max(max(row) for row in probabilities)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if probabilities[i][j] == max_prob:
                    if grid[i][j] == "S":
                        hits.append((i, j))
                        grid[i][j] = "H"  # Hit
                    else:
                        misses.append((i, j))
                        grid[i][j] = "M"  # Miss
                    moves += 1
                    probabilities = update_probabilities(grid, hits, misses)
                    break
    return moves
