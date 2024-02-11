class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currCnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currCnt += 1
            else:
                currCnt = 0
            maxOnes = max(maxOnes, currCnt)
        return maxOnes