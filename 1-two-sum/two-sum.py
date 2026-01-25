from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hmap = dict()
        for i in range(len(nums)):
            if target-nums[i] in hmap:
                ans = [i, hmap[target-nums[i]]]
            else:
                hmap[nums[i]] = i
        return ans
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ind_nums = defaultdict(list)
#         for i in range(len(nums)):
#             ind_nums[nums[i]].append(i)
#         sorted_nums = list(sorted(nums))
#         i, j = 0, len(nums)-1
#         ans = list()
#         while i < j:
#             curr_sum = sorted_nums[i]+sorted_nums[j]
#             if curr_sum == target:
#                 ans = [ind_nums[sorted_nums[i]][0], ind_nums[sorted_nums[j]][0]] if sorted_nums[i] != sorted_nums[j] else ind_nums[sorted_nums[i]]
#                 break
#             elif curr_sum < target:
#                 i+=1
#             else:
#                 j-=1
#         return ans