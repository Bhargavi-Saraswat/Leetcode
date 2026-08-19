class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = [-1]*len(nums)
        stack = []
        n = len(nums)
        for i in range(2*n-1,-1,-1):
            j = i%n
            while stack and stack[-1]<=nums[j]:
                stack.pop()
            if i<n:
                if stack:
                    arr[j] = stack[-1]
            stack.append(nums[j])
        return arr
