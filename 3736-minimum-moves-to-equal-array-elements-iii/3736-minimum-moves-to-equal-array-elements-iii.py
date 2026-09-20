class Solution:
    def minMoves(self, nums: List[int]) -> int:

        n=max(nums)
        count=0
        for num in nums:
            while num!=n:
                num+=1
                count+=1
        return count
        