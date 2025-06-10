class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        ans = []
        candidates.sort()
        def fun(index,ds,total):
            if total == target:
                ans.append(ds.copy())
                return
            if total > target or index == N:
                return

            ds.append(candidates[index])
            fun(index+1, ds, total + candidates[index])
            ds.pop()

            while index + 1 < N and candidates[index] == candidates[index+1]:
                index += 1
            fun(index+1,ds,total)
        
        fun(0,[],0)
        return ans
        