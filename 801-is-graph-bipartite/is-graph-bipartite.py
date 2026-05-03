from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * (n)
        for i in range(n):
            if color[i] == -1:
                if not self.is_bipartite_graph(graph, i, color, n):
                    return False
        return True

    def is_bipartite_graph(self, graph, start, color, n):
        q = deque()
        color[start] = 0
        q.append(start)
        while q:
            i = q.popleft()
            for neighbor in graph[i]:
                if color[neighbor] == -1:
                    color[neighbor] = int(not color[i])
                    q.append(neighbor)
                elif color[neighbor] == color[i]:
                    return False
        return True