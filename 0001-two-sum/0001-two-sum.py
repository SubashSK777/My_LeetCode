class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nummap:
                return[nummap[complement], i]
            nummap[num] = i

        return []
        