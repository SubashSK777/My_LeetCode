class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0

        
        for num in digits:
            res += num
            res *= 10
        res //= 10
        res += 1
        
        return list(int(i) for i in str(res))



        


        
        