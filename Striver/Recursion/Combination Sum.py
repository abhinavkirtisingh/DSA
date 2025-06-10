class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        ans = []
        def subSum(arr,index,sm):

            if sm >= target or index == N:
                if sm == target:
                    ans.append(list(arr))
                return

            sm += candidates[index]
            arr.append(candidates[index])
            subSum(arr,index,sm)
            arr.pop()
            sm -= candidates[index]
            subSum(arr,index+1,sm)

        subSum([],0,0)
        return ans
