# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer n.

# Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

# Let sum be the sum of digits in x.

# Return an integer representing the value of x * sum.


# Example 1:

# Input: n = 10203004

# Output: 12340

# Explanation:

# The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
# The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
# Therefore, the answer is x * sum = 1234 * 10 = 12340.
# Example 2:

# Input: n = 1000

# Output: 1

# Explanation:

# The non-zero digit is 1, so x = 1 and sum = 1.
# Therefore, the answer is x * sum = 1 * 1 = 1.

# solution:


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum_digits = 0
        x = 0
        rev = 0
        while n > 0:
            sum_digits += n % 10
            if n % 10 != 0:
                x = x * 10 + n % 10
            n = n // 10
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
        return rev * sum_digits


solution = Solution()
print(solution.sumAndMultiply(12203))
