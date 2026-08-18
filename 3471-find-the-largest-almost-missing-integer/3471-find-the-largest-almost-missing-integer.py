class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in range(len(nums)-k+1):
            w = set(nums[i:i+k])
            for num in w:
                freq[num] = freq.get(num,0)+1
        
        m = -1
        for key,val in freq.items():
            if val == 1:
                m = max(m,key)
        return m

