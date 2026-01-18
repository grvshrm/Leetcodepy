class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        missing_num = 0
        for num in nums:
            missing_num ^= num
        for num in  range(n):
            missing_num ^= num
        return missing_num
