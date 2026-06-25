from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums.count(num) == 2 and num not in ans:
                ans.append(num)
        return sorted(ans)
