class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                return True
            freq[num] = True
        return False