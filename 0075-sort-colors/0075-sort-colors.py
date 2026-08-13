class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for left in range(len(nums)):
            for right in range(len(nums)-left-1):
                if nums[right]>nums[right+1]:
                    nums[right],nums[right+1] = nums[right+1],nums[right]
        