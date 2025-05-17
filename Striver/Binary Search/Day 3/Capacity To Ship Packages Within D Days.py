class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sm = sum(weights)
        if days == 1:
            return sm
        N = len(weights)
        

        def cdays(w):
            day = 1
            load = 0
            for ele in weights:
                if load + ele > w:
                    load = ele
                    day += 1
                else:
                    load += ele
            return day
        low = max(weights)
        high = sm + 1
        while low <= high:
            mid = (low+high)//2
            x = cdays(mid)
            if x > days:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
        





