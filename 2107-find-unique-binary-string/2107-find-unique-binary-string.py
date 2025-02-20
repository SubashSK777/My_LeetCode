class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = set(nums)

        def dfs(str_num):
            if len(str_num) == n:
                return str_num not in s, str_num
            
            l_found, l_str = dfs(str_num + "0")
            if l_found:
                return True, l_str
            
            r_found, r_str = dfs(str_num + "1")
            return r_found, r_str
        
        return dfs("")[1]