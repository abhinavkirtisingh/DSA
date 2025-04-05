from collections import deque



class Solution:
    def numIslands(self, grid):
        # code here
        
        q = deque()
        ROW = len(grid)
        COL = len(grid[0])
        visited = [[0 for i in range(COL)] for j in range(ROW)]
        
        def valid(r,c):
            if r >= 0 and c >= 0 and r < ROW and c < COL:
                return True
            return False
        neb = [[0,1],[-1,0],[1,0],[0,-1],[-1,1],[1,1],[-1,-1],[1,-1]]
        
        def dfs(r,c):
            
            visited[r][c] = 1
            for nr,nc in neb:
                n_r = nr + r
                n_c = nc + c
                if valid(n_r,n_c) and visited[n_r][n_c] == 0 and grid[n_r][n_c] == 'L':
                    dfs(n_r,n_c)
        islands = 0
        for r in range(ROW):
            for c in range(COL):
                if visited[r][c] == 0 and grid[r][c] == 'L':
                    islands += 1
                    dfs(r,c)
        return islands        
                    