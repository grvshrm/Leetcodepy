from collections import defaultdict, deque

class Solution:
    def isCyclic(self, V, edges):
        adj = defaultdict(list)
        indegree = [0] * V
        for i, j in edges:
            adj[i].append(j)
            indegree[j] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        cnt = 0
        while(q):
            node = q.popleft()
            cnt += 1
            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        return cnt != V