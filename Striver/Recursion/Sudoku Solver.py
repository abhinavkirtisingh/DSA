class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        N = len(board)
        def safeS(num,i,j):
            
            for x in range(9):
                if board[x][j] == num or board[i][x] == num:
                    return False
            
                if board[3 * (i//3) + (x//3)][3 * (j//3) + (x%3)] == num:
                    return False
            return True
        
        
        def solveS():

            for i in range(N):
                for j in range(N):

                    if board[i][j] == '.':

                        for num in '123456789':
                            if safeS(num,i,j):
                                board[i][j] = num
                                if solveS():
                                    return True
                                board[i][j] = "."       
                        return False
            return True
        solveS()
        return board