class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        
        for i in range(len(arr)):
            if arr[i] in hm:
                hm[arr[i]] += 1
            else:
                hm[arr[i]] = 1

        res = set()

        for i in hm.values():
            res.add(i)

        return len(res) == len(set(arr))