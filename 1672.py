from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_list = []

        for i in range(len(accounts)):

            wealth_list.append(sum(accounts[i]))
        return max(wealth_list)


solution = Solution()
print(solution.maximumWealth([[1, 2, 3], [3, 2, 1]]))
