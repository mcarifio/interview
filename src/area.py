#!/usr/bin/env python3
'''
Problem posed:

Given a 2D integer array, where each element can be 1 (represents white) or 0 (represents black). 
Write a function which calculates the largest contiguous white area.

0 0 1 0
1 1 1 0
1 0 0 0
1 1 0 0

yields 7

I didn't complete this during the interview process. Finished it about an hour later. 

'''




# Return an array of False for the grid indicating a cell hasn't been counted.
# Make a new one of these every time you start a counting episode.
def none_counted(grid):
    return [[False for i in range(len(grid))] for i in range(len(grid))]

# Compute the largest contiguous area in an n x n grid. For a cell (i,j) the four
# cells (i - 1, j) or left, (i + 1, j) or right, (i, j - 1) or above and (i, j + 1) or
# below are considered contiguous cells to be checked. Don't do the diagonals.
def largest_white_area(grid):
    max_area = 0 # no areas found yet
    grid_size = len(grid) # iteration bounds

    # for each element in the grid
    for i in range(grid_size):
        for j in range(grid_size):
            # if there's a 1, start counting
            if 1 == grid[i][j]:
                # Create a grid of counted cells. False means not counted, True means count.
                # This prevents double counting and endless recursion
                counted = none_counted(grid) # initially none seen
                # Generate the area of this cell
                area = cell_area(grid, i, j, counted)
                # If this area is largest seen so far, remember it
                if area > max_area: 
                    max_area = area
                    
    # computed the area of each cell, return the largest seen
    return max_area        

# computes the area of grid at [row][col] with supporting grid counted.
# counted remembers if a cell has been counted.
def cell_area(grid, row, col, counted):
    
    # off the grid left or right
    if row < 0 or row >= len(grid):
        return 0
    
    # off the grid above or below
    if col < 0 or col >= len(grid):
        return 0

    # already counted this cell, don't count again
    if counted[row][col]:
        return 0
    
    # shouldn't count this cell
    if 0 == grid[row][col]: 
        return 0

    # Counting my neighbors, remember I've been counted
    counted[row][col] = True
    return 1 + cell_area(grid, row - 1, col, counted) + \
               cell_area(grid, row + 1, col, counted) + \
               cell_area(grid, row, col - 1, counted) + \
               cell_area(grid, row, col + 1, counted)
     
    
    
if __name__ == '__main__':
    
    grid0 = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],  [0, 0, 0, 0] ]
    grid4 = [ [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0],  [1, 1, 0, 0] ]
    grid7 = [ [0, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0],  [1, 1, 0, 0] ]
    grid16 = [ [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],  [1, 1, 1, 1] ]
    
    assert(largest_white_area(grid0) == 0)
    assert(largest_white_area(grid4) == 4)
    assert(largest_white_area(grid7) == 7)
    assert(largest_white_area(grid16) == 16)

    
    