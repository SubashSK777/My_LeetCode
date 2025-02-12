class Solution:

    def sumDigits(self, num):
        return sum(int(digits) for digits in str(num))



    def maximumSum(self, nums: List[int]) -> int:
        h_map = {}
        max_sum = -1

        for num in nums:
            digit_sum = self.sumDigits(num)

            if digit_sum in h_map:
                max_sum = max(max_sum, h_map[digit_sum] + num)
                h_map[digit_sum] = max(h_map[digit_sum], num)
            else:
                h_map[digit_sum] = num

        return max_sum

        
        