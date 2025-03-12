class Solution:
    def maximumCount(self, nums):
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the first positive number
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        # Now, 'left' is the index of the first positive number
        positive_count = n - left

        # Find the last negative number using binary search
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
        # Now, 'right' is the index of the last negative number
        negative_count = right + 1

        # Return the maximum count of positive and negative integers
        return max(positive_count, negative_count)