class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice=0
        bob=0
        for i in nums:
            if len(str(i))==2:
                alice+=i
            else:
                bob+=i

        if alice!=bob:
            return True
        else:
            return False
