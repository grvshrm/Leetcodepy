class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def subsetUtil(i, res):
            if i >= n:
                ans.append(res.copy())
                return
            res.append(nums[i])
            subsetUtil(i+1, res)
            res.pop()
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            subsetUtil(i+1, res)
        nums.sort()
        subsetUtil(0, [])
        return ans
                