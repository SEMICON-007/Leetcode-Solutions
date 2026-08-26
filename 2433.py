# 2433. Find The Original Array of Prefix Xor

# You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.

# It can be proven that the answer is unique.


# Example 1:

# Input: pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
# Explanation: From the array [5,7,2,3,2] we have the following:
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

# solution:

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        ans = [0] * len(pref)
        ans[0] = pref[0] ^ 0

        for i in range(len(pref) - 1):
            ans[i + 1] = pref[i] ^ pref[i + 1]

        return ans
