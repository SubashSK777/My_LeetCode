class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
       
        output = []
        n = len(nums)
        for i in range(n):
            output.append(nums[nums[i]])
        return output
        