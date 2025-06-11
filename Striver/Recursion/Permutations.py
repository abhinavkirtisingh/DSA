from collections import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        def fun(arr,index):
           
            if index == N:
                ans.append(list(arr))
                return


            for ele in range(N):

                if nums[ele] not in arr:
                    arr.append(nums[ele])
                    fun(arr,index+1)
                    arr.pop()
                    
                    
            
        fun([],0)
        return ans       


#APPROACH 2   
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        N = len(nums)

        def fun(arr,index):
            if index == N:
                ans.append(list(arr))
                return
            
            for ind in range(index,N):
                arr[ind],arr[index] = arr[index], arr[ind]
                fun(arr,index+1)
                arr[ind],arr[index] = arr[index], arr[ind]
        
        fun(nums,0)
        return ans     

        
        