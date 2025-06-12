class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def safe(ans,row,col):
            for x in range(col,-1,-1):
                if ans[row][x] == 'Q':
                    return False
            x,y = row,col

            while x >= 0 and y >= 0:
                if ans[x][y] == 'Q':
                    return False
                x-=1
                y-=1
            x,y = row,col
            while x < n and y >= 0:
                if ans[x][y] == 'Q':
                    return False
                x += 1
                y -= 1
            return True


        final = []
        def solveQ(ans,col):
            
            if col == n:
                temp = []
                for i in range(n):
                    temp.append(''.join(ans[i]))
                final.append(temp.copy())
                return
            
            for row in range(n):
                
                if safe(ans,row,col):
                    ans[row][col] = 'Q'
                    solveQ(ans,col+1)                        
                    ans[row][col] = '.'
        ans = [['.' for i in range(n)] for j in range(n)]
        solveQ(ans,0)  
        return final


        