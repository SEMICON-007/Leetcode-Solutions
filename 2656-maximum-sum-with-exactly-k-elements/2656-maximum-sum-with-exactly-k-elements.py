class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sum_score=max(nums)
        score=0

        for i in range(k):
            score+=sum_score
            sum_score+=1
            

        return score