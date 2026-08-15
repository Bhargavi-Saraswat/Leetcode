class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        c = 0
        length = 0
        for right in range(len(nums)-1):
            if nums[right] == nums[right+1]:
                continue
            elif nums[right+1]-nums[right] == 1:
                c+=1
            else:
                length = max(c,length)
                c = 0
        return max(length,c)+1
