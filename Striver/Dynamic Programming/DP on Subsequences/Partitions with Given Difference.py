#https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1
# refer count subset with sum k problem
from typing import List

def perfectSum(arr, target):
        N = len(arr)
        dp = [0 for i in range(target+1)]
        
        if arr[0] == 0:
            dp[0] = 2
        else:
            dp[0] = 1
        if arr[0] != 0 and arr[0] <= target:
            dp[arr[0]] = 1
        
        for index in range(1,N):
            for T in range(target,-1,-1):
                nottake = dp[T]
                take = 0
                if arr[index] <= T:
                    take = dp[T - arr[index]]
                dp[T] = take + nottake
        return dp[target]
class Solution:
    def countPartitions(self, arr, d):
        # code here
        sm = sum(arr)
        if sm - d < 0 or (sm - d)%2:
            return 0
        return perfectSum(arr,(sm - d)//2)
            
        
