class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in map:
                return[map[complement], i]
            else:
                map[nums[i]] = i
        return []
   