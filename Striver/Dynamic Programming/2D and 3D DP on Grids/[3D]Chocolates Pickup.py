# https://www.geeksforgeeks.org/problems/chocolates-pickup/1
# memorization
class Solution:
    def solve(self, n, m, grid):
        # Code here
        
        dp = [[[None for i in range(m)] for j in range(m)] for k in range(n)]
        def fun(i,j1,j2):
            
            if j1 >= m or j2 >= m or j1 < 0 or j2 < 0:
                return float('-inf')
            
            if i == n-1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            if dp[i][j1][j2] is not None:
                return dp[i][j1][j2]
            
            maxi = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    
                    if j1 == j2:
                        maxi = max(maxi, grid[i][j1] + fun(i+1,x+j1,y+j2))
                    else:
                        maxi = max(maxi, grid[i][j1] + grid[i][j2] + fun(i+1,x+j1,y+j2))
            dp[i][j1][j2] = maxi
            return maxi
        
        return fun(0,0,m-1)
