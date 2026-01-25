class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reverse = 0
        while num > 0:
            if reverse !=0:
                reverse = reverse * 10
            reverse = reverse + num%10
            num = num // 10
        return x == reverse
