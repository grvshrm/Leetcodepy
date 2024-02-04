class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        currSum = 1
        carry = 0
        while i >= 0:
            currSum = currSum + digits[i] + carry
            carry = currSum//10
            digits[i] = currSum%10
            currSum = 0
            i -= 1
        if carry == 1:
            digits.insert(0, carry)
        return digits
            
            
        