"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        a = b = c = 0
        for i in range(1,n):
            dp[i] = min(dp[a]*2, dp[b]*3, dp[c]*5)
            if dp[i] == dp[a]*2: a += 1
            if dp[i] == dp[b]*3: b += 1
            if dp[i] == dp[c]*5: c += 1
        return dp[-1]
