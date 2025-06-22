# https://leetcode.com/problems/coin-change-ii/submissions/1672260500/

#memorization
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[None for i in range(amount+1)] for j in range(N)]
        def fun(index,target):
            if index == 0:
                if target%coins[0] == 0:
                    return 1
                else:
                    return 0
            if dp[index][target] is not None:
                return dp[index][target]
            nottake = fun(index-1,target)
            take = 0
            if coins[index] <= target:
                take = fun(index,target - coins[index])
            dp[index][target] = take + nottake
            return dp[index][target]
        return fun(N-1,amount)

# space optimized tabulation
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [0 for i in range(amount+1)]

        for t in range(amount+1):
            if t%coins[0] == 0:
                dp[t] = 1           
        
        
        for index in range(1,N):
            for target in range(amount+1):
                nottake = dp[target]
                take = 0
                if coins[index] <= target:
                    take = dp[target - coins[index]]
                dp[target] = take + nottake

        return dp[-1]