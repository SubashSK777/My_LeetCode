class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_val = 0
        current_sum = 0

        for i in range(k):
            current_sum += nums[i]

        avg_sum = current_sum / k

        max_val = avg_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] 
            current_sum -= nums[i - k]

            avg_sum = current_sum / k

            max_val = max(avg_sum, max_val)

        return max_val
        