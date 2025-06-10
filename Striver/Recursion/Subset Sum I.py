class Solution:
	def subsetSums(self, arr):
		# code here
		ans = []
		N = len(arr)
		def fun(temp,index,sm):
		    if index == N:
		        ans.append(sm)
		        return
		    
		    
		    fun(temp,index+1, sm + arr[index])
		    fun(temp,index+1,sm)
		   
        fun([],0,0)
        
        return ans