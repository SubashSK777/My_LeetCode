class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        n = len(nums)
        for i in range (n):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i
        