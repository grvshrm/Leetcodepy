class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        n = len(nums)
        max_reach = 0
        for i, step in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + step)
            if max_reach >= n-1:
                break
        return True