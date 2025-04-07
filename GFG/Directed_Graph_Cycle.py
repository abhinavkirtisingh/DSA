class Solution:
    def isCycle(self, V, edges):
        # code here
        
        visited = [0 for i in range(V)]
        
        adj = [[] for i in range(V) ]
        
        for e1,e2 in edges:
            adj[e1].append(e2)
        
        def dfs(i,s):
            if i in s:
                return True
            visited[i] = 1
            s.add(i)
            for ele in adj[i]:
                if visited[ele] == 1 and dfs(ele,s):
                    return True
            s.remove(i)
            return False
        s = set()
        for i in range(V):
            if visited[i] == 0 and dfs(i,s):
                return True
        return False