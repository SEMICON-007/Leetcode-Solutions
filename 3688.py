# 3688. Bitwise OR of Even Numbers in an Array

# You are given an integer array nums.

# Return the bitwise OR of all even numbers in the array.

# If there are no even numbers in nums, return 0.


# Example 1:

# Input: nums = [1,2,3,4,5,6]

# Output: 6

# Explanation:

# The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

# Example 2:

# Input: nums = [7,9,11]

# Output: 0

# Explanation:

# There are no even numbers, so the result is 0.

# solution:

from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        even = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even = even | nums[i]
                count += 1
        if count == 0:
            return count
        else:
            return even
