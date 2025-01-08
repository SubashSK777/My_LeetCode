class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for i in nums:
            if i in res:
                return True
            else:
                res.add(i)
        return False