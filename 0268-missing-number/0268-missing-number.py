class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nat = (n *(n + 1)) // 2

        summ = sum(nums)

        return nat - summ