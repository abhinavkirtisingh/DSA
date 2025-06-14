class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        adj = [[] for i in range(v)]
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def isSafe(adj,colour,vertex,cIndex):
            
            for ele in adj[cIndex]:
                if vertex[ele] == colour:
                    return False
            return True
        
        
        
        vertex = [-1] * v
        def solveC(cIndex):
            if cIndex == v:
                return True
            
            
            for colour in range(m):
                
                if isSafe(adj,colour,vertex,cIndex):
                    vertex[cIndex] = colour
                    if solveC(cIndex+1):
                        return True
                    vertex[cIndex] = -1
            
            return False
        
        return solveC(0)