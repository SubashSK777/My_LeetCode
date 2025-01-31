class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        dicti = {"(":")", "{":"}", "[":"]"}

        for i in s:
            if i in dicti:
                res.append(i)
            else:
                if len(res) != 0 and i == dicti[res[-1]]:
                    res.pop()
                else:
                    return False
        if len(res) == 0:
            return True
        return False
        