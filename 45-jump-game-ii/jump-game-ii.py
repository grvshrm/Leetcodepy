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

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         min_jumps = 0
#         curr_end = 0
#         farthest = 0
#         for i in range(n-1):
#             farthest = max(farthest, i + nums[i])
#             if i == curr_end:
#                 min_jumps += 1
#                 curr_end = farthest
#         return min_jumps