class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        arr = []
        for i in range(len(nums)):
            if nums[i] > 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(nums)//2):
            for j in range(2):
                if j%2 == 0:
                    arr.append(arr1[i])
                else:
                    arr.append(arr2[i])
        return arr
            