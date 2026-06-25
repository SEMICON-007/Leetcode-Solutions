class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        permu_diff = 0
        for i in range(len(s)):
            if s[i] in t:
                permu_diff += abs(i - (t.index(s[i])))
        return permu_diff
