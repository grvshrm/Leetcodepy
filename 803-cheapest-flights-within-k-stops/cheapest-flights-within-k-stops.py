import heapq as hq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, wt in flights:
            adj[u].append([v, wt])
        dist = [float("inf")] * n
        dist[src] = 0
        pq = [(0, src, 0)]
        while pq:
            st, u, dis = hq.heappop(pq)
            if st > k:
                continue
            for v, wt in adj[u]:
                if dis + wt < dist[v]:
                    dist[v] = dis + wt
                    hq.heappush(pq, (st + 1, v, dist[v]))
        ans = dist[dst] if dist[dst] < float("inf") else -1
        return ans

                
            