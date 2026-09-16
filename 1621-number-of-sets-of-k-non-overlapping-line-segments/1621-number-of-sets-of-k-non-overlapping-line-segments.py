class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        N = n + k - 1
        R = 2 * k

        # dp[i][j] = C(i, j)
        dp = [[0] * (R + 1) for _ in range(N + 1)]

        # C(i, 0) = 1
        for i in range(N + 1):
            dp[i][0] = 1

        # Pascal's Triangle
        for i in range(1, N + 1):
            for j in range(1, min(i, R) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

        return dp[N][R]