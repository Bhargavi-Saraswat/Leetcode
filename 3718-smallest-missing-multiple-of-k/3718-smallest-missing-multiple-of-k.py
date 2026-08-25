class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        m = float('inf')
        c = 0
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = True
        for i in range(1,len(nums)+2):
            if k*i not in freq:
                c = k*i
                m = min(m,c)
        return m