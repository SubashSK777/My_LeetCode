class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0

        max_sum = -math.inf

        for i in range(k):
            summ += nums[i]

        max_sum = (max_sum if max_sum > summ else summ)

        for i in range(k ,len(nums)):
            summ += nums[i]
            summ -= nums[i - k]

            max_sum = (max_sum if max_sum > summ else summ)

        return max_sum / k




        