class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = max(arr)
        return arr.index(peak)
        