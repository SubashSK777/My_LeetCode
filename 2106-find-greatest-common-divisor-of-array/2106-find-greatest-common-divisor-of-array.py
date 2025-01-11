class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = max(nums)

        mini = min(nums)

        return gcd(maxi, mini)
        