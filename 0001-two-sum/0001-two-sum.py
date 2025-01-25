class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        n = len(map)

        for i, value in enumerate(nums):
            complement = target - value
            if complement in map:
                return [i, map[complement]]
            map[value] = i
        return []        