class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}

        for n in nums:
            if n in freq:
                return True
            freq[n] = 1

        return False

        