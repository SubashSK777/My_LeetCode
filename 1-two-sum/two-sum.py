class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in res:
                return [res[comp], i]
            else:
                res[nums[i]] = i
        return []