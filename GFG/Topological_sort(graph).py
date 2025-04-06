class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        
        
        adj = [[] for i in range(V)]
        
        for e1,e2 in edges:
            adj[e1].append(e2)
        
        visited = [0 for i in range(V)]
        ans = []
        def dfs(i):
    
            visited[i] = 1
            
            for e in adj[i]:
                if visited[e] == 0:
                    dfs(e)
                    
            ans.append(i)
        
        for i in range(V):
            if visited[i] == 0:
                dfs(i)
        return ans[::-1]