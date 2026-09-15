class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            pal[i][i] = True

        # Check palindromes of length 2 and more
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = maximum number of non-overlapping palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            # Option 1: don't choose a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Option 2: choose a palindrome s[j:i]
            for j in range(i):
                length = i - j

                if length >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]