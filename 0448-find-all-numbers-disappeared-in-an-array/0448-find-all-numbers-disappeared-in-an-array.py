class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        res = []
        
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                res.append(i)

        return res
        