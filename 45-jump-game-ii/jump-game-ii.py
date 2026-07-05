class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, n = 0, 0, len(nums)
        jumps = 0
        while r < n-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(i + nums[i], farthest)
            l = r+1
            r = farthest
            jumps += 1
        return jumps