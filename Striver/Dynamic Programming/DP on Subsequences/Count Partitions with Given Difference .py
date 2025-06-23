from typing import List


class Solution:
    def countPartitions(self, arr, d):
        # code here
        
        N = len(arr)
        sm = sum(arr)
        dp = [[None for i in range(sm+1)] for j in range(N)]
        def fun(index,T):
            
            if index < 0:
                if T - (sm-T) == d:
                    return 1
                return 0
            if dp[index][T] is not None:
                return dp[index][T]
            nottake = fun(index-1,T)
            take = fun(index-1, T + arr[index])
            dp[index][T] = take + nottake
            return dp[index][T]
        
        return fun(N-1,0)