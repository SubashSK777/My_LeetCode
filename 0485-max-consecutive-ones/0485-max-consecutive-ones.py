class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_count = (max_count if max_count > count else count)
                count = 0
                
        max_count = (max_count if max_count > count else count)

        return max_count
            


        