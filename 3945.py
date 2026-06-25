from typing import List


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = 0
        score = 0
        a = n
        digit = []
        while a > 0:
            digit.append(a % 10)
            a = a // 10
        for i in range(10):
            freq = digit.count(i)
            score += i * freq
        return score
