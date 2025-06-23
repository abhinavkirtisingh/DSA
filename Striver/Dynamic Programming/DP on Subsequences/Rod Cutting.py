# https://www.geeksforgeeks.org/problems/rod-cutting0840/1
# memorization (tle)
class Solution:
    def cutRod(self, price):
        #code here
        N = len(price)
        dp = [[None for i in range(N+1)] for j in range(N)]
        def fun(index,size):
            if index == 0:
                return price[0] * size
            if dp[index][size] is not None:
                return dp[index][size]
            nottake =  fun(index-1,size)
            take = 0
            if size - index > 0:
                take = price[index] + fun(index,size - (index +1))
            dp[index][size] = max(take,nottake) 
            return dp[index][size]
        return fun(N-1,N)

# tabulation(tle)
class Solution:
    def cutRod(self, price):
        #code here
        N = len(price)
        dp = [[0 for i in range(N+1)] for j in range(N)]
        
        for size in range(N+1):
            dp[0][size] = price[0] * size
        
        for index in range(1,N):
            for size in range(N+1):
                nottake =  dp[index-1][size]
                take = 0
                if size - index > 0:
                    take = price[index] + dp[index][size - (index +1)]
                dp[index][size] = max(take,nottake) 
                
        
        return dp[N-1][N]

#space optimized
class Solution:
    def cutRod(self, price):
        #code here
        N = len(price)
        dp = [0 for i in range(N+1)]
        
        for size in range(N+1):
            dp[size] = price[0] * size
        
        for index in range(1,N):
            for size in range(N+1):
                nottake =  dp[size]
                take = 0
                if size - index > 0:
                    take = price[index] + dp[size - (index +1)]
                dp[size] = max(take,nottake) 
                
        
        return dp[-1]