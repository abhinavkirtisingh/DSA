class Solution:
	def isCycle(self, V, edges):
          
            #Code here
            
            
            graph = [[] for i in range(V)]
            
            
            
            for x,y in edges:
                graph[x].append(y)
                graph[y].append(x)
            vis = [False] * V
            cycle = False
            
            def dfs(v,p,tr):
                tr.add(v)
                vis[v] = True
                nonlocal cycle
                # print(v)
                for ele in graph[v]:
                    if ele != p and ele in tr:
                        cycle = True
                        return
                    if vis[ele] == False:
                        tr.add(ele)
                        dfs(ele,v,tr)
                
                    
                    
                
            
            for v in range(V):
                tr = set()
                if vis[v] == False:
                                
                    dfs(v,-1,tr)
                
            return cycle
            