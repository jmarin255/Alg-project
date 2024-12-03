import random

def simulate_placement(grid, hits, misses):
    """
    Simulate the current state of the grid with hits and misses.
    """
    simulation_grid = [row[:] for row in grid]
    for i, j in hits:
        simulation_grid[i][j] = "H"
    for i, j in misses:
        simulation_grid[i][j] = "M"
    return simulation_grid

def monte_carlo_algorithm(grid, hits, misses, simulations=100):
    """
    Monte Carlo Algorithm for Battleship to simulate random moves and determine hits and misses.
    """
    size = len(grid)
    moves = 0
    
    # Keep track of visited cells
    visited = [[False for _ in range(size)] for _ in range(size)]
    
    # Helper function to check if a cell is valid and not visited
    def is_valid_cell(i, j):
        return 0 <= i < size and 0 <= j < size and not visited[i][j] and grid[i][j] != "M"
    
    # Start from a random initial cell
    start_row = random.randint(0, size - 1)
    start_col = random.randint(0, size - 1)
    current_position = (start_row, start_col)
    visited[start_row][start_col] = True

    while any("S" in row for row in grid):  # Continue until all ships are found
        row, col = current_position  # Ensure row and col are integers here

        # If current position is a ship, mark it as a hit
        if grid[row][col] == "S":
            hits.append((row, col))
            grid[row][col] = "H"
            visited[row][col] = True
            moves += 1

            # Check all four directions for the next move
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            random.shuffle(directions)  # Shuffle directions for random movement order

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if is_valid_cell(next_row, next_col):
                    current_position = (next_row, next_col)
                    visited[next_row][next_col] = True
                    break  # Move to the next valid neighboring cell and continue
            else:
                # If no valid neighboring cells, pick a random unvisited cell
                unvisited_cells = [(i, j) for i in range(size) for j in range(size) if not visited[i][j] and grid[i][j] == "S"]
                if unvisited_cells:
                    current_position = random.choice(unvisited_cells)
                    visited[current_position[0]][current_position[1]] = True
        else:
            # If the current position is a miss, mark it as "M"
            misses.append((row, col))
            grid[row][col] = "M"
            visited[row][col] = True
            moves += 1

            # Pick a random unvisited cell to continue
            unvisited_cells = [(i, j) for i in range(size) for j in range(size) if not visited[i][j] and grid[i][j] == "S"]
            if unvisited_cells:
                current_position = random.choice(unvisited_cells)
                visited[current_position[0]][current_position[1]] = True
            else:
                break  # Exit if no unvisited cells are available

        # Print the current grid state only after each move
        print("\nCurrent grid state:")
        for r in grid:
            print(' '.join(r))

    return moves
