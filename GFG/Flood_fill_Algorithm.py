from collections import deque

class Solution:
	def floodFill(self, image, sr, sc, newColor):
		
	    
            #Code here
            pq = deque()
            oldColor = image[sr][sc]
            pq.append([sr,sc])
            n = len(image)
            m = len(image[0])
            visited = [[0 for i in range(m)] for i in range(n)]
            neb = [[0,1],[1,0],[-1,0],[0,-1]]
            
            def valid(row,col):
                if row >= 0 and col >= 0 and row < n and col < m:
                    return True
                return False
                
            
            while pq:
                r,c = pq.popleft()
                visited[r][c] = 1
                image[r][c] = newColor
                for n_r,n_c in neb:
                    row = n_r + r
                    col = n_c + c
                    if valid(row,col) and visited[row][col] == 0 and image[row][col] == oldColor:
                        pq.append([row,col])
            return image