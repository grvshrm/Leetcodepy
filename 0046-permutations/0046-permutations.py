class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        l, r = 0, n-1
        ans = []
        def permuteUtil(nums, l, r):
            if l == r:
                ans.append(nums[:])
                return
            for i in range(l, r+1):
                nums[l], nums[i] = nums[i], nums[l]
                permuteUtil(nums, l+1, r)
                nums[l], nums[i] = nums[i], nums[l]
        permuteUtil(nums, l, r)
        return ans