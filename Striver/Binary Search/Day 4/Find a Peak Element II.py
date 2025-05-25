class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        N = len(mat)
        M = len(mat[0])

        def findMax(i):
            mx = -1
            x = -1
            for j in range(N):

                if mat[j][i] > mx:
                    mx = mat[j][i]
                    x = j
            return mx,x

        low = 0
        high = M-1

        while low <= high:

            mid = (low + high)//2

            mx,i = findMax(mid)

            left = mat[i][mid-1] if mid -1 >= 0 else -1
            right = mat[i][mid+1] if mid + 1 < M else -1

            if left < mat[i][mid] > right:
                return [i,mid]
            elif left > mat[i][mid]:
                high = mid - 1
            else:
                low = mid + 1