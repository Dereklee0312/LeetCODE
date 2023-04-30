# Author: Derek Lee
# Start Date: 10-02-2023
# End Date:
# Link: https://leetcode.com/problems/island-perimeter/
# Difficulty: Easy
#
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:
#
# Input: grid = [[1]]
# Output: 4
# Example 3:
#
# Input: grid = [[1,0]]
# Output: 4
#
#
# Constraints:
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


# TODO: Add solution explanation
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cache = []
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    for row, col in offsets:
                        new_pos = (i + row, j + col)
                        if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(
                            grid[0]
                        ):
                            neighbour = grid[new_pos[0]][new_pos[1]]
                            if neighbour == 1 and (new_pos, (i, j)) not in cache:
                                cache.append((new_pos, (i, j)))
                                cache.append(((i, j), new_pos))
                                perimeter -= 2
        return perimeter

    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter
