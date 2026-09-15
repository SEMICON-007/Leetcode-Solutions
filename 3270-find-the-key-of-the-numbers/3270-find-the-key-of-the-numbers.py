class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans=0
        k=1
        while num1>0 or num2>0 or num3>0:
            a=min([num1%10,num2%10,num3%10])
            ans+=k*a
            k*=10
            num1=num1//10
            num2=num2//10
            num3=num3//10
        return ans
