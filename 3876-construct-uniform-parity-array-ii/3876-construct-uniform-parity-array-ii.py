class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)

        # If minimum is odd, we can make every element odd
        if mn % 2 == 1:
            return True

        # If minimum is even, every element must already be even
        return all(x % 2 == 0 for x in nums1)