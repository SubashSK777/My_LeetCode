class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        count = 0
        
        for i in range (len(nums)):
            for j in range (len(nums)):
                if i < j:
                    if nums[i] + nums[j] < target:
                        count += 1
        return count
        