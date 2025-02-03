class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        max_len = 1

        if n == 1:
            return 1

        left = 0
        for right in range(1, n):
            if nums[right - 1] >= nums[right]:
                left = right
            else:
                max_len = max(max_len, right - left + 1)

        left = 0
        for right in range(1, n):
            if nums[right - 1] <= nums[right]:
                left = right
            else:
                max_len = max(max_len, right - left + 1)

        return max_len


        