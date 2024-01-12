class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            start, end = 0, m - 1
            while(start <= end):
                matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                start += 1
                end -= 1