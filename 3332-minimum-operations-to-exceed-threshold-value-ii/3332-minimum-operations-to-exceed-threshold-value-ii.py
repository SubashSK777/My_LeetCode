class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        
        while len(nums) > 1 and nums[0] < k:
            num1 = heapq.heappop(nums)
            num2 = heapq.heappop(nums)
            heapq.heappush(nums, num1 * 2 + num2)
            ans += 1
        
        return ans