class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        combo = []
        
        def combinationSumUtil(ind, combo, target):
            if target == 0:
                ans.append(combo.copy())
                return
            for i in range(ind, n):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue 
                if candidates[i] > target:
                    break
                combo.append(candidates[i])
                combinationSumUtil(i+1, combo, target - candidates[i])
                combo.pop()
        candidates.sort()
        combinationSumUtil(0, combo, target)   
        return ans