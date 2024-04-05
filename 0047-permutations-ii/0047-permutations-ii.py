from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        count = Counter(nums)
        perm = []
        def permuteUtil():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    permuteUtil()
                    perm.pop()
                    count[num] += 1                      
        permuteUtil()
        return ans
        