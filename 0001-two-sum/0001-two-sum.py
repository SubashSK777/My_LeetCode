class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hm:
                return [hm[comp], i]
            else:
                hm[nums[i]] = i

        return []