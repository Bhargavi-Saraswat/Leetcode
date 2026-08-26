class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)
        if len(ones) < k:
            return ""
        ans = ""
        min_len = float('inf')
        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]
            curr = s[left:right + 1]
            curr_len = right - left + 1
            if curr_len < min_len:
                min_len = curr_len
                ans = curr
            elif curr_len == min_len:
                ans = min(ans, curr)
        return ans