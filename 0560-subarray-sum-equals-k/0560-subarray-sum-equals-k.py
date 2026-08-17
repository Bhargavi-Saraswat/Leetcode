class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        s = 0
        freq = {0:1}
        for num in nums:
            s += num
            if s-k in freq:
                c+=freq[s-k]
            freq[s] = freq.get(s,0)+1
        return c