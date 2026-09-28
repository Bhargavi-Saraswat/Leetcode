class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        c = 0
        l = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i+1] - nums[i] == 1:
                c+=1
            else:
                l = max(c,l)
                c = 0
        return max(c,l)+1