
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])
        low = 0
        high = (N*M) - 1

        while low <= high:

            mid = (low + high)//2
            row = mid//M
            col = mid%M
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        N = len(matrix)
        M = len(matrix[0])
        i = 0
        j = M-1
        
        while j >= 0 and i < N:
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j-=1
        return False
