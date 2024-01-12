class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for i in range(0, len(intervals)):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            elif intervals[i][1] > ans[-1][1]:
                ans[-1][1] = intervals[i][1]
        return ans