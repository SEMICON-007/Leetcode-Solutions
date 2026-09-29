class Solution:
    def minCost(self, n: int) -> int:
        cost=0
        while n>1:
            a=n-1
            b=1
            cost+=a*b
            n-=1
        return cost

                
        