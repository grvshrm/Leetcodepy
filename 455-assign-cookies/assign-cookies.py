class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # DP - TLE
        # g.sort()
        # s.sort()
        # n, m = len(g), len(s)
        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(n - 1, -1, -1):
        #     for j in range(m - 1, -1, -1):
        #         skip_cookie = dp[i][j + 1]
        #         take_cookie = 0
        #         if s[j] >= g[i]:
        #             take_cookie = 1 + dp[i + 1][j + 1]
        #         dp[i][j] = max(skip_cookie, take_cookie)
        # return dp[0][0]
        g.sort()
        s.sort()
        student_index = 0
        cookie_index = 0

        while student_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[student_index]:
                student_index += 1
            cookie_index += 1
        return student_index