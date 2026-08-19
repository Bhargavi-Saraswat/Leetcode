class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNo = float('inf')
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[left]<=nums[mid]:
                minNo = min(minNo,nums[left])
                left = mid+1
            else:
                minNo = min(minNo,nums[mid])
                right = mid-1
        return minNo