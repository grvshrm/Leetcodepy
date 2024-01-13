class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                major = nums[i]
            elif nums[i] == major:
                cnt += 1
            else:
                cnt -= 1
        cnt = 0
        for i in nums:
            if i == major:
                cnt += 1
        return major if cnt > n // 2 else -1
        