class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:
            s_i = ''.join(sorted(i))

            if s_i not in map:
                map[s_i] = []
            
            map[s_i].append(i)

        return list(map.values())