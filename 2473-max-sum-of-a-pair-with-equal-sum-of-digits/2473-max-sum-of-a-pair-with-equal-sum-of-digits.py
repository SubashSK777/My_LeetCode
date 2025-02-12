class Solution:
    def getSum(self, n: int) -> int:
        return sum(int(digit) for digit in str(n))

    def maximumSum(self, nums: list[int]) -> int:
        num_map = defaultdict(list)
        for num in nums:
            digit_sum = self.getSum(num)
            heapq.heappush(num_map[digit_sum], -num)

        max_sum = -1
        for heap in num_map.values():
            if len(heap) < 2:
                continue
            max_sum = max(max_sum, -heapq.heappop(heap) - heapq.heappop(heap))

        return max_sum