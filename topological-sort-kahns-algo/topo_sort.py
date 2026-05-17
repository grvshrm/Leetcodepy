from collections import defaultdict, deque

class Solution:
    def topoSort(self, V, edges):
        adj_list = defaultdict(list)
        indegree = [0] * V
        for u, v in edges:
            adj_list[u].append(v)
            indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        topo_sort = list()
        while(q):
            node = q.popleft()
            topo_sort.append(node)
            for nbr in adj_list[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        return topo_sort