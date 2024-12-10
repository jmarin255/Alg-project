def is_valid_placement(grid, row, col, size, direction):
    """Check if a ship of given size and direction can be placed at (row, col)."""
    if direction == "horizontal":
        if col + size > len(grid):  # Check out-of-bounds
            return False
        for i in range(size):
            if grid[row][col + i] != "-":
                return False
    elif direction == "vertical":
        if row + size > len(grid):  # Check out-of-bounds
            return False
        for i in range(size):
            if grid[row + i][col] != "-":
                return False
    return True

def place_ship(grid, row, col, size, direction):
    """Place a ship on the grid."""
    if direction == "horizontal":
        for i in range(size):
            grid[row][col + i] = "S"
    elif direction == "vertical":
        for i in range(size):
            grid[row + i][col] = "S"

def remove_ship(grid, row, col, size, direction):
    """Remove a ship from the grid."""
    if direction == "horizontal":
        for i in range(size):
            grid[row][col + i] = "-"
    elif direction == "vertical":
        for i in range(size):
            grid[row + i][col] = "-"

def backtrack(grid, ships):
    """Recursive backtracking function to place ships."""
    if not ships:  # Base case: All ships are placed successfully
        return True

    size = ships[0]  # Take the first ship size to place
    for row in range(len(grid)):
        for col in range(len(grid)):
            for direction in ["horizontal", "vertical"]:
                if is_valid_placement(grid, row, col, size, direction):
                    place_ship(grid, row, col, size, direction)
                    if backtrack(grid, ships[1:]):  # Recur for the remaining ships
                        return True
                    remove_ship(grid, row, col, size, direction)  # Backtrack

    return False  # No valid placement found

def exact_algorithm(grid, ships, hits, misses):
    """Main function for the exact algorithm using backtracking."""
    moves = 0

    # Create a copy of the grid for the backtracking process
    grid_copy = [row[:] for row in grid]

    # Start the backtracking process on the grid copy
    if backtrack(grid_copy, ships):
        print("Optimal solution found.")
    else:
        print("No solution found.")
        return None

    # Keep track of whether we have found all the ships
    ships_found = False

    # Apply the results from the backtracking to the original grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid_copy[i][j] == "S":
                # Check if the original grid at the same location also has a ship
                if grid[i][j] == "S":
                    hits.append((i, j))
                    grid[i][j] = "H"  # Mark the original grid as hit
                    moves += 1
                else:
                    misses.append((i, j))
                    grid[i][j] = "M"  # Mark the original grid as miss
                    moves += 1
            elif grid[i][j] == "-":
                # If the cell in the original grid is empty, mark it as a miss
                misses.append((i, j))
                grid[i][j] = "M"
                moves += 1

            # Stop marking further cells once all ships are found
            if not any("S" in row for row in grid):
                ships_found = True
                break
        if ships_found:
            break

    return moves
