class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x%10 == 0:
            return False
        num = x
        reverse = 0
        while num != 0:
            if reverse !=0:
                reverse = reverse * 10
            reverse = reverse + num%10
            num = num // 10
        print(x)
        print(reverse)
        return x == reverse
