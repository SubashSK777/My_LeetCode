class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        count = [0] * (n * n + 1)
        
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        a, b = -1, -1
        
        for num in range(1, n * n + 1):
            if count[num] == 2:
                a = num
            elif count[num] == 0:
                b = num
                
        return [a, b]
        