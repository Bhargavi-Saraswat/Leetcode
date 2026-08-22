class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        s = 0
        p = 1
        while x!=0:
            d = x%10
            s+=d
            p*=d
            x = x//10
        return n%(s+p) == 0