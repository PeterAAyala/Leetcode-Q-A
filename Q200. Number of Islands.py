"""
Q200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        searched = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        numIslands = 0
        
        def DFS(row: int, col: int) -> int:
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1" or searched[row][col]:
                return
            searched[row][col] = True
            DFS(row+1, col)
            DFS(row-1, col)
            DFS(row, col+1)
            DFS(row, col-1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not searched[row][col] and grid[row][col] == "1":
                    DFS(row, col)
                    numIslands += 1
                #if searched[row][col]:
                #    continue
        return numIslands
                
                   
        