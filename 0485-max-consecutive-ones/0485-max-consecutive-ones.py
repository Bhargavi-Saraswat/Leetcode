class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==1:
            if nums[0] != 1:
                return 0
            else:
                return 1
        maxOne = 0
        c = 0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                maxOne = max(maxOne,c)
            else:
                c = 0
        return maxOne