class Solution:
    def myPow(self, num: float, n: int) -> float:
        ans = 1
        pow = n
        if pow < 0:
            pow = -1 * pow
        while(pow):
            if pow % 2:
                ans = ans * num
                pow = pow - 1
            else:
                num = num * num
                pow = pow >> 1
        if n < 0:
            ans = 1 / ans
        return ans