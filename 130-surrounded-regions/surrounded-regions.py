class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(index: tuple(int)):
            nonlocal vis, board, m, n
            r, c = index
            vis[r][c] = 1
            for dr, dc in zip([0, 0, 1, -1], [-1, 1, 0, 0]):
                i,  j = r+dr, c+dc
                if 0 <= i < m and 0 <= j < n and not vis[i][j] and board[i][j] == 'O':
                    dfs((i, j))

        for i in range(m):
            if board[i][0] == 'O':
                dfs((i, 0))
            if board[i][n-1] == 'O':
                dfs((i, n-1))
        for j in range(n):
            if board[0][j] == 'O':
                dfs((0, j))
            if board[m-1][j] == 'O':
                dfs((m-1, j))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not vis[i][j]:
                    board[i][j] = 'X'

        
        


        