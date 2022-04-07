"""
Q417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""
class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        m = len(heights[0])
        n = len(heights)
        pac_searched = [[False for x in range(m)] for y in range(n)]
        atl_searched = [[False for x in range(m)] for y in range(n)]
        result = []                  
        for i in range(n):
            self.DFS(i, 0, heights, pac_searched, n, m)
            self.DFS(i, m-1, heights, atl_searched, n, m)
        
        for j in range(m):
            self.DFS(0, j, heights, pac_searched, n, m)
            self.DFS(n-1, j, heights, atl_searched, n, m)
        
        for i in range(n):
            for j in range(m):
                if pac_searched[i][j] and atl_searched[i][j]:
                    result.append([i,j])
        return result
    
    def DFS(self, i, j, matrix, searched, n, m):
        searched[i][j] = True
        for direc in self.directions:
            x, y = direc[0] + i, direc[1] + j
            if x < 0 or x >= n or y < 0 or y >= m or searched[x][y] or matrix[x][y] < matrix[i][j] :
                continue
            self.DFS(x, y, matrix, searched, n, m)
    