class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        if N == 1:
            return 0
        prev = 0
        mn = prices[0]
        cur = None
        for i in range(1,N):
            cur = max(prices[i] - mn,prev)
            prev = cur
            mn = min(mn,prices[i])
        return cur
        