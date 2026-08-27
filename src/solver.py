#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Iterating through row offsets (-1, 0, 1) and col offsets (-1, 0, 1)
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Skiping the target cell itself
            if i == 0 and j == 0:
                continue
            
            # Calculating the neighbor's coordinates
            neighbor_row = row + i
            neighbor_col = col + j
            
            # Checking if the neighbor is within the bounds of the grid
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                # Adding to count if the cell is alive (assuming alive = 1 or True)
                if grid[neighbor_row][neighbor_col]:
                    alive_count += 1

    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Creating a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Iterating through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Find out how many live neighbors the current cell has
            neighbors = count_neighbors(grid, r, c)
            
            # Applying the 4 Rules of Life
            if grid[r][c] == 1:
                # Rule 2: Survival (2 or 3 neighbors -> lives)
                if neighbors == 2 or neighbors == 3:
                    next_grid[r][c] = 1
                # Rules 1 & 3: Underpopulation (<2) or Overpopulation (>3) -> dies
                # (Since next_grid is already filled with 0s, we don't need an else statement)
            else:
                # Rule 4: Reproduction (exactly 3 neighbors -> becomes a live cell)
                if neighbors == 3:
                    next_grid[r][c] = 1

    return next_grid
