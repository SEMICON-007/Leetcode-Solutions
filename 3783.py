class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        a = n
        while a > 0:
            rev = rev * 10 + (a % 10)
            a = a // 10
        return abs(n - rev)
