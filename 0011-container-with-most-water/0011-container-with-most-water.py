class Solution:
    def maxArea(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        max_val = 0

        while(l < r):
            curr_val = min(arr[l], arr[r]) * (r - l)
            max_val = max(curr_val, max_val)
            
            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1
            
        
        return max_val
        