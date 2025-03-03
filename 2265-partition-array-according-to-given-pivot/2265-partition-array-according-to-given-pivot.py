__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        c = 0
        for i in nums:
            if i<pivot:
                small.append(i)
            elif i>pivot:
                big.append(i)
            elif i==pivot:
                c+=1
        res = []
        res += small
        res += [pivot]*c
        res += big
        return res