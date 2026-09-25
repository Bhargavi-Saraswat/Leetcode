class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in freq:
                return [freq[diff],i]
            freq[nums[i]] = i
        return []