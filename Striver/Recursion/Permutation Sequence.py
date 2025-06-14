class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        
        st = '123456789'
        st_arr =[]

        for i in range(n):
            st_arr.append(st[i])
        res = []
        def fun(index,temp):
            if index == n:
                res.append(''.join(temp))
                return
            
            for i in range(index,n):
                temp[i],temp[index] = temp[index],temp[i]
                fun(index+1,temp)
                temp[i],temp[index] = temp[index],temp[i]
        
        fun(0,st_arr)
        res.sort()
        return res[k-1]