class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = [-1]*len(nums1)
        freq = {}
        for i in range(len(nums2)):
            freq[nums2[i]] = i
        for i in range(len(nums1)):
            j = freq[nums1[i]]+1
            while j<len(nums2):
                if nums1[i]<nums2[j]:
                    arr[i] = nums2[j]
                    break
                j+=1
        return arr



