class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1
        
        return count if (nums[n - 2] == 1 and nums[n - 1] == 1) else -1