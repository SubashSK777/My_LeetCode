class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        # Reverse queries to use pop() efficiently
        q = queries[::-1]
        
        delta = [0] * (n + 1)
        current_sum = 0
        
        for i, num in enumerate(nums):
            # Update current sum with delta effect
            current_sum += delta[i]
            
            # Keep accepting queries until we satisfy the constraint
            while q and current_sum < num:
                start, end, val = q.pop()
                
                if end >= i:
                    if start <= i:
                        # Direct effect on current position
                        current_sum += val
                    else:
                        # Future effect
                        delta[start] += val
                    
                    # Mark the end of effect
                    delta[end + 1] -= val
            
            # If we still can't satisfy this position, return -1
            if current_sum < num:
                return -1
        
        return m - len(q)