from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = ["1","2","3","4","5","6","7","8","9"]
        a = []
        b = []
        c = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num in digits:
                    if num in a:
                        return False
                    else:
                        a.append(num)
                num = board[j][i]
                if num in digits:
                    if num in b:
                        return False
                    else:
                        b.append(num)
                num = board[i//3*3 + j//3][i%3*3 + j%3]
                if num in digits:
                    if num in c:
                        return False
                    else:
                        c.append(num)
            a.clear()
            b.clear()
            c.clear()
        
        return True