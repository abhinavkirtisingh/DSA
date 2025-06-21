# https://www.geeksforgeeks.org/problems/geeks-training/1
#memorization
class Solution:
    def maximumPoints(self, arr):
        # Code here
        N = len(arr)
        dp = [ [None for i in range(3)] for j in range(N)]
        def fun(index,prev):
            if index < 0:
                return 0
            ans = float('-inf')
            if prev != -1 and dp[index][prev] is not None:
                return dp[index][prev]
            
            for i in range(3):
                if prev != i:
                    ans = max(ans,arr[index][i] + fun(index-1,i))
            if prev != -1:
                dp[index][prev] = ans
            return ans
        return fun(N-1,-1)
        
# tabulation
class Solution:
    def maximumPoints(self, arr):
        # Code here
        N = len(arr)
        dp = [ [0 for i in range(4)] for j in range(N)]

        dp[0][0] = max(arr[0][1],arr[0][2])
        dp[0][1] = max(arr[0][0],arr[0][2])
        dp[0][2] = max(arr[0][0],arr[0][1])
        dp[0][3] = max(arr[0][0],arr[0][1],arr[0][2])
        
        for day in range(1,N):
            
            for last in range(4):
                
                for task in range(3):
                    
                    if last != task:
                        dp[day][last] = max(dp[day][last],dp[day-1][task] + arr[day][task])
        
        return dp[N-1][3]