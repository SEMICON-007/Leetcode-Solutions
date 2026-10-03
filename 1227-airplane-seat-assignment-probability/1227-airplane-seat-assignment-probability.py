class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n==1:
            return float(n)
        else:
            return float(1/2)