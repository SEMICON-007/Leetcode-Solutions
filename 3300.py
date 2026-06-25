from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = [0] * len(nums)

        for i in range(len(nums)):
            digit_sum = 0
            while nums[i] > 0:
                digit_sum += nums[i] % 10
                nums[i] = nums[i] // 10
            ans[i] = digit_sum
        return min(ans)


solution = Solution()
print(solution.minElement([999, 19, 199]))
