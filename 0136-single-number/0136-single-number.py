class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        least_common = count.most_common()[-1]

        return least_common[0]
        