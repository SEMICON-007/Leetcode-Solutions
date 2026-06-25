class Solution:
    def interpret(self, command: str) -> str:
        siuuu = command.replace("(al)", "al")
        return siuuu.replace("()", "o")


solution = Solution()
print(solution.interpret("G()(al)"))
