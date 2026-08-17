class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        summ = 0
        maxSum = float('-inf')
        for num in nums:
            summ += num
            maxSum = max(summ,maxSum)
            if summ<0:
                summ = 0
        return maxSum