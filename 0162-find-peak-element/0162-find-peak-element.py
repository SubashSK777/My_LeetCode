class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l  = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[r] > nums[r - 1]:
            return r

        while l < r:
            m = (l + r) // 2

            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m

            if nums[m] < nums[m + 1]:
                l = m + 1

            else:
                r = m - 1

        return l
        