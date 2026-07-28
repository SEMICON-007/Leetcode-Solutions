# 628. Maximum Product of Three Numbers

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6

# solution:

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        way1 = nums[0] * nums[1] * nums[2]
        way2 = max(nums) * nums[-1] * nums[-2]
        return max(way1, way2)
