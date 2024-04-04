class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        l, r = 0, n-1
        ans = []
        def permuteUtil(nums, l):
            if l == n-1:
                ans.append(nums[:])
                return
            for i in range(l, n):
                nums[l], nums[i] = nums[i], nums[l]
                permuteUtil(nums, l+1)
                nums[l], nums[i] = nums[i], nums[l]
        permuteUtil(nums, l)
        return ans