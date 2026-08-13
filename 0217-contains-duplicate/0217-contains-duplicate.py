class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            freq[nums[i]] = freq.get(nums[i],0)+1
        return False