class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        
        adj = [[] for i in range(V)]
        
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        visited = [0] * V
        low = [None] * V
        ins = [None] * V
        time = 1
        def dfs(i,p):
            
            visited[i] = 1
            nonlocal time
            low[i] = time
            ins[i] = time
            time += 1
            for ele in adj[i]:
                if visited[ele] == 0:
                    dfs(ele,i)
                if ele != p:
                    low[i] = min(min(low[ele],ins[ele]),low[i])
        
        
        for e in range(V):
            
            if visited[e] == 0:
                dfs(e,-1)
                
        if low[c] > ins[d] or low[d] > ins[c]:
            return 1
        return 0