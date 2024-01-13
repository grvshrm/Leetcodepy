class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = []
        elm1, elm2, cnt1, cnt2 = 0, 0, 0, 0
        n = len(nums)
        for i in range(n):
            if cnt1 == 0 and nums[i] != elm2:
                cnt1 += 1
                elm1 = nums[i]
            elif cnt2 == 0 and nums[i] != elm1:
                cnt2 += 1
                elm2 = nums[i]    
            elif nums[i] == elm1:
                cnt1 += 1
            elif nums[i] == elm2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for i in nums:
            if i == elm1:
                cnt1 += 1
            elif i == elm2:
                cnt2 += 1
        if cnt1 > n //3:
            major.append(elm1)
        if cnt2 > n // 3:
            major.append(elm2)
        return major