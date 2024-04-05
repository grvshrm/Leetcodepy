class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        combo = []
        
        def combinationSumUtil(ind, combo, target):
            if ind == n:
                if target == 0:
                    ans.append(combo.copy())
                return
            if candidates[ind] <= target:
                combo.append(candidates[ind])
                combinationSumUtil(ind, combo, target - candidates[ind])
                combo.pop()
            combinationSumUtil(ind+1, combo, target)
        combinationSumUtil(0, combo, target)   
        return ans