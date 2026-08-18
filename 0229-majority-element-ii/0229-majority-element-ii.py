class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v = len(nums)//3
        freq = {}
        arr = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        for key,val in freq.items():
            if val > v:
                arr.append(key)
        return arr