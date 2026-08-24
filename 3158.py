# 3158. Find the XOR of Numbers Which Appear Twice
# You are given an array nums, where each number in the array appears either once or twice.

# Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.


# Example 1:

# Input: nums = [1,2,1,3]

# Output: 1

# Explanation:

# The only number that appears twice in nums is 1.

# Example 2:

# Input: nums = [1,2,3]

# Output: 0

# Explanation:

# No number appears twice in nums.

# solution:

from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = []
        ans = 0
        for num in nums:
            if num in seen:
                ans ^= num
            else:
                seen.append(num)
        return ans
