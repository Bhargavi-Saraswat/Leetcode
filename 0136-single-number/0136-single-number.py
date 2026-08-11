class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        c = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        for i in range(len(nums)):
            if freq.get(nums[i]) == 1:
                c = nums[i]
        return c