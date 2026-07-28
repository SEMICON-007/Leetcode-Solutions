# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"

# solution:


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])
    
    # alternate Solution:
        # s_split = s.split()
        # rev_str = ""
        # for word in s_split:
        #     rev_str += word[::-1] + " "
        # return rev_str[0:-1]

        

