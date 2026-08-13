class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        v = len(nums)//2
        for key,val in freq.items():
            if val>v:
                return key
        return 0