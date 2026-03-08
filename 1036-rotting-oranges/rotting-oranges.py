from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        q = deque()
        total_oranges = 0
        total_time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total_oranges += 1
                    if grid[i][j] == 2:
                        q.append([i, j])
        rotten_oranges = 0
        while len(q) > 0:
            curr_rotten = len(q)
            rotten_oranges += curr_rotten
            while curr_rotten > 0:
                x, y  = q.popleft()
                for del_row, del_col in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                    x_new = x + del_row
                    y_new = y + del_col
                    if x_new >= 0 and x_new < m and y_new >= 0 and y_new < n and\
                    grid[x_new][y_new] == 1:
                        q.append([x_new, y_new])
                        grid[x_new][y_new] = 2
                curr_rotten -= 1
            if len(q) > 0:
                total_time += 1
        return total_time if (rotten_oranges == total_oranges) else -1