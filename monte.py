



def simulate_placement(grid, hits, misses):
    # Simulate random placement consistent with hits/misses
    simulation_grid = [row[:] for row in grid]
    for i, j in hits:
        simulation_grid[i][j] = "H"
    for i, j in misses:
        simulation_grid[i][j] = "M"
    return simulation_grid

def monte_carlo_algorithm(grid, hits, misses, simulations=100):
    moves = 0
    while any("S" in row for row in grid):
        expected_hits = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
        for _ in range(simulations):
            simulation = simulate_placement(grid, hits, misses)
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if simulation[i][j] == "S":
                        expected_hits[i][j] += 1
        max_hits = max(max(row) for row in expected_hits)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if expected_hits[i][j] == max_hits:
                    if grid[i][j] == "S":
                        hits.append((i, j))
                        grid[i][j] = "H"
                    else:
                        misses.append((i, j))
                        grid[i][j] = "M"
                    moves += 1
                    break
    return moves