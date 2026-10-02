class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = ""
        for i in range(len(digits)):
            num += str(digits[i])
        nums = int(num)
        nums += 1
        return [int(digit) for digit in str(nums)]
