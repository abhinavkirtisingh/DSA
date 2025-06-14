class Solution:
    def partition(self, s: str) -> List[List[str]]:


        n = len(s)
        def isPalindrom(st):
                n = len(st)
                l = 0
                r = n-1

                while l < r:

                    if st[l] != st[r]:
                        return False
                    l+=1
                    r-=1
                return True
            
        ans = []
        def fun(temp,index):
            if index == n:
                ans.append(temp.copy())
                return
            x = ''
            for ele in range(index,n):
                x += s[ele]
                if isPalindrom(x):
                    temp.append(x)
                    fun(temp,ele+1)
                    temp.pop()
        fun([],0)
        return ans