from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        num_pair = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] < target:
                    num_pair += 1
        return num_pair
