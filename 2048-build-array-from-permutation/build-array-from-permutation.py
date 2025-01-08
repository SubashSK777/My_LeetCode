class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums1 = 0
        output = []
        n = len(nums)
        for i in range(n):
            output.append(nums[nums[i]])
        return output
        