from typing import List


def minimumOperations(self, nums: List[int]):
    for i in range(len(nums)):
        if nums[i] % 3 == 0:
            continue
        else:
            if (nums[i] + 1) % 3 == 0 or (nums[i] - 1) % 3 == 0:
                count += 1
    return count
