class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """maxSum = float('-inf')
        n = len(nums)
        currSum = 0
        for i in range(n):
            currSum += nums[i]
            if currSum < 0:
                currSum = 0
            if maxSum < currSum:
                maxSum = currSum
        return maxSum (returns 0 even if arr contains only -ve nums)"""
        maxSum, currSum = nums[0], nums[0]
        n = len(nums)
        for i in range(1, n):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum