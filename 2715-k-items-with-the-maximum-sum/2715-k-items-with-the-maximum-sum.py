class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
   
        sum = 0
        if numOnes >= k :
            return k
        else :
            sum += numOnes
            k -= numOnes
        if numZeros >= k :
            return sum
        else :
            k -= numZeros
        if numNegOnes >= k:
            sum -=k
            return sum
            

                