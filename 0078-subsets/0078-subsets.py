class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def subsetUtil(i, cur):
            if i >= n:
                ans.append(cur[:])
                return
            cur.append(nums[i])
            subsetUtil(i+1, cur)
            cur.pop()
            subsetUtil(i+1, cur)
        
        subsetUtil(0, [])
        return ans