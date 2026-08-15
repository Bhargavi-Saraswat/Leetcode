class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums)-2
        while pivot>=0 and nums[pivot]>=nums[pivot+1]:
            pivot-=1
        
        if pivot>=0:
            m = 0
            for right in range(len(nums)-1,pivot,-1):
                if nums[pivot]<nums[right]:
                    m = right
                    break
            nums[pivot],nums[m] = nums[m],nums[pivot]
        
        left = pivot+1
        right = len(nums)-1

        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
            