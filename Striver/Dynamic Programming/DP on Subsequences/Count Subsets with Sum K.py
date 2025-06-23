# if arr[i] != 0
class Solution:
    def perfectSum(self, arr, target):
        N = len(arr)
        dp = [[None for i in range(target+1)] for j in range(N)]
        
        def fun(index, T):
            if T == 0:
                return 1
            if index == 0:
                if T == arr[0]:
                    return 1
                return 0
            if dp[index][T] is not None:
                return dp[index][T]
            
            nottake = fun(index - 1, T)
            take = 0
            if arr[index] <= T:
                take = fun(index - 1, T - arr[index])
            dp[index][T] = take + nottake
            return dp[index][T]
        
        return fun(N - 1, target)

# if arr[i] == 0
# memorization
class Solution:
    def perfectSum(self, arr, target):
        N = len(arr)
        dp = [[None for i in range(target+1)] for j in range(N)]
        
        def fun(index, T):
            
            if index == 0:
                if T == 0 and arr[0] == 0:
                    return 2
                if T == 0 or T == arr[0]:
                    return 1
                return 0
            if dp[index][T] is not None:
                return dp[index][T]
            
            nottake = fun(index - 1, T)
            take = 0
            if arr[index] <= T:
                take = fun(index - 1, T - arr[index])
            dp[index][T] = take + nottake
            return dp[index][T]
        
        return fun(N - 1, target)

#tabulation 
class Solution:
    def perfectSum(self, arr, target):
        N = len(arr)
        dp = [[0 for i in range(target+1)] for j in range(N)]
        
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1
        
        for index in range(1,N):
            for T in range(target+1):
                nottake = dp[index - 1][T]
                take = 0
                if arr[index] <= T:
                    take = dp[index - 1][T - arr[index]]
                dp[index][T] = take + nottake
        return dp[N-1][target]

#space optimized
class Solution:
    def perfectSum(self, arr, target):
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