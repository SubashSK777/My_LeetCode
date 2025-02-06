class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_count = defaultdict(int)
        counter = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                
                counter += 8 * (prod_count[prod])
                prod_count[prod] += 1

        return counter

        