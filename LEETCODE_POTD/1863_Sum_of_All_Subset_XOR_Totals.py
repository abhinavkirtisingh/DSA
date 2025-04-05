class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        n = len(nums)
        ans = []
        def fun(i,temp):
            if i == n:
                
                ans.append(temp.copy())
                return 
            temp.append(nums[i])
            fun(i+1,temp)
            temp.pop()
            fun(i+1,temp)
        fun(0,[])
        res = 0
        for i in ans:
            x = 0
            for ele in i:
                x ^= ele
            res += x
        return res