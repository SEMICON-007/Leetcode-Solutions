from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        sum_extra_candies = 0
        for i in range(len(candies)):
            sum_extra_candies = candies[i] + extraCandies
            if sum_extra_candies >= max(candies):
                result.append(True)
            else:
                result.append(False)

        return result
