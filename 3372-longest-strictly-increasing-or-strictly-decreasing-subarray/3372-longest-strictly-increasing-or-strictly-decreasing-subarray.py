class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        max_count = 0

        #increasing order
        left = 0
        for right in range(1, n):
            if nums[right] <= nums[right - 1]:
                left = right
            max_count = max_count if max_count > (right - left + 1) else (right - left + 1)

        left = 0
        for right in range(1, n):
            if nums[right] >= nums[right - 1]:
                left = right
            max_count = max_count if max_count > (right - left + 1) else (right - left + 1)

        return max_count