class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        n = len(maze)
        def valid(i,j):
            if i >= 0 and j >= 0 and i < n and j < n and maze[i][j] == 1:
                return True
            return False
        ans = []
        pos = [[1,0,'D'],[0,-1,'L'],[0,1,'R'],[-1,0,'U']]
        visited = [[0 for i in range(n)] for i in range(n)]
        def fun(i,j,st):
            if i == n-1 and j == n-1:
                ans.append(st)
                return
            visited[i][j] = 1
            for x,y,d in pos:
                if valid(i+x,j+y) and visited[i+x][j+y] == 0:
                     fun(i+x,j+y,st+d)
            visited[i][j] = 0
        fun(0,0,'')
        return ans