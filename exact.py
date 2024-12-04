def is_valid_placement(grid, row, col, size, direction):
    #Check if a ship of given size and direction can be placed at (row, col).
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





def remove_ship(grid, row, col, size, direction):
    #Remove a ship from the grid.
    if direction == "horizontal":
        for i in range(size):
            grid[row][col + i] = "-"
    elif direction == "vertical":
        for i in range(size):
            grid[row + i][col] = "-"


def backtrack(grid, ships):
    #Recursive backtracking function to place ships.
    if not ships:  # Base case: All ships are placed successfully
        return True

    size = ships[0]  # Take the first ship size to place
    for row in range(len(grid)):
        for col in range(len(grid)):
            for direction in ["horizontal", "vertical"]:
                if is_valid_placement(grid, row, col, size, direction):
                    if backtrack(grid, ships[1:]):  # Recur for the remaining ships
                        return True
                    remove_ship(grid, row, col, size, direction)  # Backtrack

    return False  # No valid placement found


def exact_algorithm(grid, ships, hits, misses):
    #Main function for the exact algorithm using backtracking.
    moves = 0
    
    # Start the backtracking process
    if backtrack(grid, ships):
        print("Optimal solution found.")
    
    # Mark hits and misses
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "S":
                hits.append((i, j))
                grid[i][j] = "H"
            else:
                misses.append((i, j))
                grid[i][j] = "M"
            moves += 1
            
            # Stop if all ships have been found and marked as hits
            if not any("S" in row for row in grid):
                break

    return moves

   
