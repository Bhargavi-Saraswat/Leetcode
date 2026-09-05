class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # prefixMax[i] = max(nums[0..i])
        prefixMax = [0] * n
        prefixMax[0] = nums[0]

        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])

        # suffixMin[i] = min(nums[i..n-1])
        suffixMin = [0] * n
        suffixMin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])

        # Find the first stable index
        for i in range(n):
            if prefixMax[i] - suffixMin[i] <= k:
                return i

        return -1