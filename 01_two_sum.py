# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# solution:

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_pairs = [(0, 0)] * len(nums)
        for i in range(len(nums)):
            sorted_pairs[i] = (nums[i], i)

        # sorted_pairs=sorted([(num,idx) for (idx,num) in enumerate(nums)])

        sorted_pairs.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            pair_sum = sorted_pairs[left][0] + sorted_pairs[right][0]
            if pair_sum == target:
                break
            elif pair_sum > target:
                right -= 1
            else:
                left += 1
        return [sorted_pairs[left][1], sorted_pairs[right][1]]
