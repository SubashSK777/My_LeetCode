class Solution:
    def maxArea(self, height: List[int]) -> int:
        w_level = 0
        l = 0
        r = len(height) - 1
        maxi = 0

        while l < r:
            mini = height[l] if height[l] < height[r] else height[r]

            dist = r - l
            maxi = max(maxi, (mini * dist))

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxi



        