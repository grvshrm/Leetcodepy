class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        n = len(piles)
        while low <= high:
            mid = (low + high)//2
            if self.isPossible(piles, mid, h):
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def isPossible(self, piles: List[int], k: int, h: int) -> bool:
        cnt = 0
        for pile in piles:
            cnt += ceil(pile/k)
        return cnt <= h
            
            
        