class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []
        for row in range(1, numRows + 1):
            ansRow = [1]
            ans = 1
            for col in range(1, row):
                ans = ans * (row - col)
                ans = ans // col
                ansRow.append(ans)
            pascalTriangle.append(ansRow)
        return pascalTriangle