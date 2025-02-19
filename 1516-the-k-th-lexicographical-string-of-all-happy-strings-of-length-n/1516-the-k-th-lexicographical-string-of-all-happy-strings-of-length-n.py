class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        strs = []
        letters = ['a', 'b', 'c']

        def dfs(s):
            if len(s) == n:
                strs.append(s)
                return
            
            for letter in letters:
                if not s or s[-1] != letter:
                    dfs(s + letter)
        
        dfs("")
        strs.sort()
        return strs[k - 1] if k <= len(strs) else ""