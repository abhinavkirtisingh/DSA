import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adj = [[] for i in range(V)]
        
        for e1,e2,d in edges:
            adj[e1].append([d,e2])
        visited = [0] * V
        dis = [float('inf')] * V
        pq = [[0,src]]
        dis[src] = 0
        
        while pq:
            d, node = heapq.heappop(pq)
            if visited[node] == 1:
                continue
            visited[node] = 1
            for nxt_d, nxt_node in adj[node]:
                if d + nxt_d < dis[nxt_node]:
                    dis[nxt_node] = d + nxt_d
                if visited[nxt_node] == 0:
                    heapq.heappush(pq,[dis[nxt_node], nxt_node])
        return dis