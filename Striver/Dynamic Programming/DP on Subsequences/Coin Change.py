# https://leetcode.com/problems/coin-change/
# memorization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)
        dp = [[None for i in range(amount+1)] for j in range(N)]
        def fun(index,target):

            if index == 0:
                if target%coins[index] == 0:
                    return target//coins[index]
                else:
                    return float('inf')
            if dp[index][target] is not None:
                return dp[index][target] 
            
            nottake = fun(index-1,target)
            take = float('inf')
            if coins[index] <= target:
                take = 1 + fun(index, target - coins[index])
            dp[index][target] = min(take,nottake)
            return dp[index][target]
            
        ans =  fun(N-1,amount)
        
        if ans == float('inf'):
            return -1
        else:
            return ans
# tabulation
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)
        dp = [[0 for i in range(amount+1)] for j in range(N)]
        
        for t in range(amount+1):
            if t%coins[0] == 0:
                dp[0][t] = t//coins[0]
            else:
                dp[0][t] = float('inf')
        
        for index in range(1,N):
            for target in range(amount+1):
                nottake = dp[index-1][target]
                take = float('inf')
                if coins[index] <= target:
                    take = 1 + dp[index][target - coins[index]]
                dp[index][target] = min(take,nottake)
        
        return -1 if dp[N-1][amount] == float('inf') else dp[N-1][amount]
        
# space optimized
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)
        dp = [0 for i in range(amount+1)]
        
        for t in range(amount+1):
            if t%coins[0] == 0:
                dp[t] = t//coins[0]
            else:
                dp[t] = float('inf')
        
        for index in range(1,N):
            for target in range(amount+1):
                nottake = dp[target]
                take = float('inf')
                if coins[index] <= target:
                    take = 1 + dp[target - coins[index]]
                dp[target] = min(take,nottake)
        
        return -1 if dp[-1] == float('inf') else dp[-1]

