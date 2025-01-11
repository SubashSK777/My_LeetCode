class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        sum = 0

        if k <= numOnes:
            return k
        else:
            sum += numOnes
            k = k - numOnes

        if k <= numZeros:
            return sum
        else:
            k = k - numZeros
        
        if k <= numNegOnes:
            sum -= k
            return sum