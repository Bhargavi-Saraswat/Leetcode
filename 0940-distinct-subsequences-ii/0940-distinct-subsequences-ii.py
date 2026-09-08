class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # dp[i] = number of distinct subsequences
        # using first i characters, including empty subsequence
        dp = [0] * (n + 1)
        dp[0] = 1

        # last[c] = position where character c last appeared
        last = [-1] * 26

        for i in range(1, n + 1):
            ch = ord(s[i - 1]) - ord('a')

            # Add current character to every existing subsequence
            dp[i] = 2 * dp[i - 1]

            # Remove duplicates caused by previous occurrence
            if last[ch] != -1:
                dp[i] -= dp[last[ch] - 1]

            dp[i] %= MOD

            # Current character's latest position
            last[ch] = i

        # Remove the empty subsequence
        return (dp[n] - 1) % MOD