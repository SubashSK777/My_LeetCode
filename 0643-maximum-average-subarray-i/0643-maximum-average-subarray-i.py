class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_val = 0
        max_val = float(-inf)
        avg_val = 0
        n = len(nums)

        for i in range(k):
            curr_val += nums[i]

        avg_val = curr_val / k
        max_val = (max_val if max_val > avg_val else avg_val)

        for i in range(k, n):
            curr_val += nums[i]
            curr_val -= nums[i - k]
            avg_val = curr_val / k
            max_val = (max_val if max_val > avg_val else avg_val)

        return max_val

        