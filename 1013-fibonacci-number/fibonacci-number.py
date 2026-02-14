class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        prev2, prev = 0, 1
        for i in range(2, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        return prev