from collections import deque
def valid(i,j,n,m):
	
    
    if i >= 0 and j >= 0 and i < n and  j < m:
        return True
    return False
    
    
class Solution:
	
        def orangesRotting(self, mat):
            
            
            #Code here
            
            n = len(mat)
            m = len(mat[0])
            q = deque()
            for r in range(n):
                for c in range(m):
                    if mat[r][c] == 2:
                        q.append([r,c,0])
            
            
            ans = 0
            ne = [[-1,0],[1,0],[0,-1],[0,1]]
            while q:
                
                r,c,d = q.popleft()
                
                ans = max(ans,d)
                
                for n_r,n_c in ne:
                    row = n_r + r
                    col = n_c + c
                    if valid(row,col,n,m) and mat[row][col] == 1:
            
                        mat[row][col] = 2
                        q.append([row,col,d+1])
        # print(mat)
            for r in range(n):
                for c in range(m):
                    if mat[r][c] == 1:
                        return -1 
            return ans 