from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        Q = deque()
        vis = [[0 for _ in range(n)] for _ in range(m)]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    Q.append([i, j, 0])
                    vis[i][j] = 1
        row_del = [-1, 0, 0, 1]
        col_del = [0, -1, 1, 0]
        while Q:
            r, c, dis = Q.popleft()
            ans[r][c] = dis
            for ind in range(4):
                i, j = r + row_del[ind], c + col_del[ind]
                if i >= 0 and i < m and j >= 0 and j < n and not vis[i][j]:
                    Q.append([i, j, dis+1])
                    vis[i][j] = 1
        return ans



        